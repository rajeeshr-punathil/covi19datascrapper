from datetime import date, timedelta

import os
import scrapy


class GetBulletinsSpider(scrapy.Spider):

    """
    Spider to download and save covid-specific daily medical bulletins 
    published by the health department of the state of Kerala, India.
    """

    name = 'kerala_bulletins'
    allowed_domains = ['dhs.kerala.gov.in']
    start_urls = ['http://dhs.kerala.gov.in/%e0%b4%a1%e0%b5%86%e0%b4%af%e0%b4%bf%e0%b4%b2%e0%b4%bf-%e0%b4%ac%e0%b5%81%e0%b4%b3%e0%b5%8d%e0%b4%b3%e0%b4%b1%e0%b5%8d%e0%b4%b1%e0%b4%bf%e0%b4%a8%e0%b5%8d%e2%80%8d']

    def __init__(self, pdf_dir='', day_count=1, **kwargs):
        """pdf_dir: Provide a path where all PDFs must be saved to."""
        self.pdf_dir = pdf_dir
        self.day_count = int(day_count)
        super().__init__(**kwargs)

    def parse(self, response):
        """Collect link to all day pages and yield them one by one."""
        latest_dates = []
        day = date.today()
        for count in range(self.day_count):
            latest_dates.append(day.strftime('%Y-%m-%d'))
            day = day - timedelta(days=1)

        for link in response.css("h3.entry-title a"):
            href = link.css("::attr(href)").get()
            title = link.css('::text').get()
            # Change title from dd/mm/YYYY to YYYY-mm-dd format.
            title = '-'.join(title.split('/')[::-1]) if title else ''
            if title not in latest_dates:
                continue
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse_day_page, 
                                 cb_kwargs=dict(title=title))

    def parse_day_page(self, response, title):
        """Collect link to daily bulletin (English) and yield it."""
        link = response.css("div.entry-content a::attr(href)").get()
        yield scrapy.Request(url=response.urljoin(link), 
                             callback=self.save_pdf, 
                             cb_kwargs=dict(title=title))

    def save_pdf(self, response, title):
        """Save response body as PDF."""
        if self.pdf_dir:
            path = os.path.join(self.pdf_dir, title + '.pdf')
        else:
            path = title + '.pdf'
        with open(path, 'wb') as pdf_file:
            pdf_file.write(response.body)
