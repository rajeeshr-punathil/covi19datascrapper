import scrapy

from covid19datascrapper.items import SummaryItem 

SUMMARY_FIELDS = [
        'summary_date', 'confirmed_cases', 'recovered_cases', 'deceased_cases',
        'transferred_cases', 'critical_cases', 'active_cases', 'total_tests',
        'total_under_observation', 'quarantined', 'hospitalized', 'status'
]


class SummarySpider(scrapy.Spider):

    """This spider crawls through the Google docs spreadsheet at given URL and
    collects necessary information regarding covid 19 patients of Kerala during
    the 2020 epidemic."""

    name = 'kerala_summary'
    allowed_domains = ['https://docs.google.com']
    start_urls = ['https://docs.google.com/spreadsheets/d/e/2PACX-1vQU9eLCMT0XwWnoxV_LkyCkxMcPYO7z7ULdODoUFgcdzp48pgGpGrVZFXvraXYvUioVRsQgQDU_pQyI/pubhtml']
    custom_settings = {
        'FEED_EXPORT_FIELDS' : SUMMARY_FIELDS 
    }

    def __init__(self, sr_start=1, sr_end=0, **kwargs):
        """
        sr_start: Number of summary row where to begin with.
        sr_end: Number of the row where to end scrapping.

        For both numbers, start counting rows with first row as 1 (not 0).
        """
        self.sr_start = int(sr_start)
        self.sr_end = int(sr_end)
        super().__init__(**kwargs)

    def parse(self, response):
        """Parse the spreadsheet and yield all requested summary rows."""
        # All rows in the first tab, "Patient Data".
        rows = response.xpath('//div[@id="211530313"] //tr[@style="height:20px;"]')
        start = max(self.sr_start - 1, 0)
        end = self.sr_end or len(rows)
        summaries = rows[start : end]
        for summary in summaries:
            item = SummaryItem()
            cols = summary.css('td')
            # If col 0, summary_date is empty, we have at the end. Break the loop.
            if not (cols and cols[0].css('::text').get()):
                break
            for index, field in enumerate(SUMMARY_FIELDS):
                if index >= len(cols):
                    break
                item[field] = cols[index].css('::text').get(default='')
            yield item
        else:
            print("Scrapped", len(patients), "/", len(rows), "summary rows.")
