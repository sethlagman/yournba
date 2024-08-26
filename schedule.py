import requests
import json

class NbaSchedule:
    """Retrieves the schedule of NBA games"""

    def __init__(self) -> None:
        """Initialize attributes"""

        self.url = 'https://cdn.nba.com/static/json/staticData/scheduleLeagueV2_1.json'
        self.result = None

    def fetch_schedule(self):
        """Fetches the game schedule"""
        
        pass
