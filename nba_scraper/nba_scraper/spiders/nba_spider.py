import scrapy

class NbaScraperSpider(scrapy.Spider):
    name = 'nbascraper'
    starturls = ['https://www.nba.com/stats/players/traditional?PerMode=PerGame&sort=PTS&dir=-1']

    def parse(self, response):
        pass