"""NBA Statistics"""

from modules.filehandler import FileHandler

class NbaStatistics:
    """
    Retrieves NBA players' statistics
    """

    def __init__(self) -> None:
        """Initialize attributes"""

        self.statistics = FileHandler().read(filename=r'nba_data\statistics.json')

    def fetch_player_statistics(self, first_name: str, last_name: str) -> dict:
        """
        Retrieves the given player's statistics
        Args:
            first_name (string): - First name of the player
            last_name (string): - Last name of the player
        """

        formatted_name = f'{first_name} {last_name}'.lower()
        for statistic in self.statistics:
            if statistic['name'].lower() == formatted_name:
                return statistic


def main():

    pass

if __name__ == '__main__':
    main()