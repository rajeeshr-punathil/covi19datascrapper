=====================
Covid19 Datascrapper
=====================

------------------------------------------------------------------------
A scrapy project to crawl and collect data regarding Covid 19 Pandemic.
------------------------------------------------------------------------

Requirements
=============

* Python >= 3.8

* Scrapy >= 2.2.0


How to Install
==============

* Download or clone this repo.

* Setup a virtual environment, if required. Example: 
  ::

    python3 -m venv env
    source env/bin/activate

* Install the dependencies using `pip` 
  ::

    pip install -r requirements.txt

How to run (scrape data)
=========================

1. To collect data of patients in Kerala
-----------------------------------------

* Run the spider, `kerala_patients`, as below: 
  ::

    scrapy crawl kerala_patients -o kerala_patients.json

* You can use any desired filename as output file.

* The above command will collect data of all patients from the spreadsheet.
  You can optionally specify the start and end row numbers, if you want rows 
  in a specific range only. Provide optional arguments `pr_start` and `pr_end` 
  for this. Example: ::

    scrapy crawl kerala_patients -a pr_start=4443 pr_end=4593 -o kerala_patients_latest.json


