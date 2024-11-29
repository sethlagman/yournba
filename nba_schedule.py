"""NBA Schedule"""

import json

from filehandler import FileHandler

class NbaSchedule:
    """Retrieves the schedule of NBA games"""

    def __init__(self):
        """Initialize attributes"""

        self.schedule = FileHandler('schedule').read()

    def fetch_shedule(self) -> dict:
        """
        Fetches the game schedules for the whole season
        
        Returns:
            dict: - Full schedule for the current NBA season
        """
        
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

    def fetch_id_schedule(self, gameid: str) -> dict:
        """
        Fetches the game schedule using game id

        Args:
            gameid (string): - 10 Digits game id

        Returns:
            dict: - Game associated with the id
        """

        for dates, games in self.fetch_shedule().items():
            for game in games:
                if game['gameId'] == gameid:
                    return {
                        dates: game
                    }

    def fetch_date_schedule(self, date: str) -> dict:
        """
        Fetches the game schedules for the given date

        Args:
            date (string): - MM/DD/YYYY

        Returns:
            dict: - Game matchups for the date 
        """

        for dates, games in self.fetch_shedule().items():
            if dates == date:
                return {date: games}


def main():

    pass

if __name__ == '__main__':
    main()