"""NBA Schedule"""

import requests
import json

URL = 'https://cdn.nba.com/static/json/staticData/scheduleLeagueV2_1.json'

class NbaSchedule:
    """Retrieves the schedule of NBA games"""

    def __init__(self, filename='nbaschedule.json', url=URL) -> None:
        """Initialize attributes"""

        self.url = url
        self.response = requests.get(self.url)
        self.filename = filename
        self.schedule = self.read_schedule()

    def fetch_shedule(self):
        """Fetches the game schedules for the whole season"""

        season_year = self.schedule['leagueSchedule']['seasonYear']
        games = self.schedule['leagueSchedule']['gameDates']
        for game in games[:2]:
            print(f'Date: {game['gameDate'][:10]}')
            for sched in game['games']:
                print(f'Game: {sched['gameCode']}')
                print(f'Home: {sched['homeTeam']['teamCity']} {sched['homeTeam']['teamName']}')
                print(f'Away: {sched['awayTeam']['teamCity']} {sched['awayTeam']['teamName']}')
                print()
            print('------')

    def fetch_date_schedule(self):
        """Fetches the game schedules for the given date"""

        pass

    def read_schedule(self):
        """Reads the game schedules from the stored json file"""
        
        with open(self.filename, 'r') as file:
            return json.load(file)

    def store_schedule(self):
        """Stores the game schedules as a json file"""

        with open(self.filename, 'w') as file:
            file.write(json.dumps(self.response.json(), indent=2))

    def update_schedule(self):
        """Updates the game schedule"""

        pass


def main():

    nbaschedule = NbaSchedule()
    nbaschedule.fetch_shedule()

if __name__ == '__main__':
    main()