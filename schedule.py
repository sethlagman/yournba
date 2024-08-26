"""NBA Schedule"""

import requests
import json

class NbaSchedule:
    """Retrieves the schedule of NBA games"""

    def __init__(self) -> None:
        """Initialize attributes"""

        self.url = 'https://cdn.nba.com/static/json/staticData/scheduleLeagueV2_1.json'
        self.response = requests.get(self.url)
        self.result = None

    def fetch_schedule(self):
        """Fetches the game schedule"""
        
        pass

    def store_schedule(self):
        """Stores the game schedule"""

        pass

    def update_schedule(self):
        """Updates the game schedule"""

        pass


def main():

    pass

if __name__ == '__main__':
    main()