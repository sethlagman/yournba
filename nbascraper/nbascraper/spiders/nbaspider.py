import scrapy

class NbaspiderSpider(scrapy.Spider):
    name = 'nbaspider'
    start_urls = ['https://www.espn.ph/nba/schedule']

    