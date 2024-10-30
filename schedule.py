"""NBA Schedule"""

import json

from filehandler import FileHandler

class NbaSchedule:
    """Retrieves the schedule of NBA games"""

    def __init__(self):
        """Initialize attributes"""

        self.schedule = FileHandler('schedule').read()

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


def main():

    pass

if __name__ == '__main__':
    main()