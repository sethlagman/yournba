import scrapy

class NbaScraperSpider(scrapy.Spider):
    name = 'nbascraper'
    custom_settings = {
        "FEEDS": {
            "nba_data/statistics.json": {
                "format": "json",
                "overwrite": True,
            },
        },
    }
    start_urls = ['https://www.nbastuffer.com/2024-2025-nba-player-stats/']

    def parse(self, response):
        rows = response.css('tbody.row-hover tr')
        for row in rows:
            data = {
                'name': row.css('.column-2::text').get(),  # Get the player's name
                'team': row.css('.column-3::text').get(),  # Get the player's team
                'position': row.css('.column-4::text').get(),  # Get the player's position
                'age': row.css('.column-5::text').get(),  # Get the player's age
                'gp': row.css('.column-6::text').get(),  # Get the player's games played
                'mpg': row.css('.column-7::text').get(),  # Get the player's minutes per game
                'usg': row.css('.column-8::text').get(),  # Get the player's usage rate
                'to': row.css('.column-9::text').get(),  # Get the player's turnovers
                'fta': row.css('.column-10::text').get(),  # Get the player's free throw attempts
                'ft': row.css('.column-11::text').get(),  # Get the player's free throw percentage
                'twopa': row.css('.column-12::text').get(),  # Get the player's 2P%
                'twop': row.css('.column-13::text').get(),  # Get the player's 2P made
                'threepa': row.css('.column-14::text').get(),  # Get the player's 3P attempts
                'threep': row.css('.column-15::text').get(),  # Get the player's 3P made
                'efg': row.css('.column-16::text').get(),  # Get the player's effective field goal percentage
                'ts': row.css('.column-17::text').get(),  # Get the player's true shooting percentage
                'ppg': row.css('.column-18::text').get(),  # Get the player's points per game
                'apg': row.css('.column-19::text').get(),  # Get the player's assists per game
                'spg': row.css('.column-20::text').get(),  # Get the player's steals per game
                'bpg': row.css('.column-21::text').get(),  # Get the player's blocks per game
                'tpg': row.css('.column-22::text').get(),  # Get the player's turnovers per game
                'pplusr': row.css('.column-23::text').get(),  # Get the player's points per rebound
                'pplusa': row.css('.column-24::text').get(),  # Get the player's points per assist
                'pplusrplusa': row.css('.column-25::text').get(),  # Get the player's points per rebound + assist
                'vi': row.css('.column-26::text').get(),  # Get the player's value index
                'ortg': row.css('.column-27::text').get(),  # Get the player's offensive rating
            }
            yield data


class NbaTeamScraperSpider(scrapy.Spider):
    name = 'nbateamscraper'
    custom_settings = {
        "FEEDS": {
            "nba_data/teams.json": {
                "format": "json",
                "overwrite": True,
            },
        },
    }
    start_urls = ['https://www.nbastuffer.com/2024-2025-nba-team-stats/']

    def parse(self, response):
        rows = response.css('#tablepress-122 tbody tr')
        for row in rows:
            data = {
                'team': row.css('a::text').get(),
                'conference': row.css('.column-3::text').get(),
                'wins': row.css('.column-18::text').get(),
                'losses': row.css('.column-19::text').get(),
                'winrate': row.css('.column-20::text').get(),
                'streak': row.css('.column-24::text').get(),
                'games_played': row.css('.column-5::text').get(),
            }
            yield data