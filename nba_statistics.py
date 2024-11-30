"""NBA Statistics"""

from filehandler import FileHandler

class NbaStatistics:
    """
    Retrieves NBA players' statistics
    """

    def __init__(self) -> None:
        """Initialize attributes"""
        
        self.statistics = FileHandler('statistics').read()

    def fetch_statistics(self) -> dict:
        """
        Retrieves all the players' statistics for the current season

        Returns:
            dict: - Statistics of the players
        """

        return {
            player['playerProfile']['code']: player['statAverage']
            for player in self.statistics['payload']['players']
        }
    
    def fetch_player_statistics(self, first_name: str, last_name: str) -> dict:
        """
        Retrieves the given player's statistics

        Args:
            first_name (string): - First name of the player
            last_name (string): - Last name of the player
        """

        formatted_name = f'{first_name}_{last_name}'.lower()
        for name, statistics in self.fetch_statistics().items():
            if name == formatted_name:
                return {name: statistics}


def main():

    pass

if __name__ == '__main__':
    main()