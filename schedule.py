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

        return {
            games['gameDate'][:10]: [
                {
                    'gameId': game['gameId'],
                    'gameCode': game['gameCode'],
                    'gameTime': game['gameStatusText'],
                    'Home': f"{game['homeTeam']['teamCity']} {game['homeTeam']['teamName']}",
                    'Away': f"{game['awayTeam']['teamCity']} {game['awayTeam']['teamName']}",
                }
                for game in games['games']
            ]
            for games in self.schedule['leagueSchedule']['gameDates']
        }

    def fetch_id_schedule(self, gameid=None):
        """Fetches the game schedule using game id"""

        pass

    def fetch_date_schedule(self, date=None):
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
    print(json.dumps(nbaschedule.fetch_shedule(), indent=2))

if __name__ == '__main__':
    main()