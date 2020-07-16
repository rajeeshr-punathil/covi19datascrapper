# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Patient(scrapy.Item):

    """Patient model with relevant fields."""

    patient_number = scrapy.Field()
    date_announced = scrapy.Field()
    date_added = scrapy.Field()
    age = scrapy.Field()
    gender = scrapy.Field()
    residence_district = scrapy.Field()
    detected_city = scrapy.Field()
    detected_district = scrapy.Field()
    status = scrapy.Field()
    transmission_type = scrapy.Field()
    notes = scrapy.Field()
    related_patients = scrapy.Field()
    known_cluster = scrapy.Field()
    dhs_orig_patient_number = scrapy.Field()
    origin_state = scrapy.Field()
    origin_country = scrapy.Field()
    district_patient_number = scrapy.Field()
    city_patient_number = scrapy.Field()
    released = scrapy.Field()
    recovery_time = scrapy.Field()
    deceased = scrapy.Field()
    sources = scrapy.Field()


class SummaryItem(scrapy.Item):

    summary_date = scrapy.Field()
    confirmed_cases = scrapy.Field()
    recovered_cases = scrapy.Field()
    deceased_cases = scrapy.Field()
    transferred_cases = scrapy.Field()
    critical_cases = scrapy.Field()
    active_cases = scrapy.Field()
    total_tests = scrapy.Field()
    total_under_observation = scrapy.Field()
    quarantined = scrapy.Field()
    hospitalized = scrapy.Field()
    status = scrapy.Field()
