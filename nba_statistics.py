"""NBA Statistics"""

import json

from filehandler import FileHandler

class NbaStatistics:
    """
    Retrieves NBA players' statistics
    """

    def __init__(self) -> None:
        
        self.statistics = FileHandler('statistics').read()

    def fetch_statistics(self) -> dict:
        """
        Retrieves all the players' statistics for the current season

        Returns:
            dict: - Statistics of the players
        """

        for player in self.statistics['payload']['players']:
            print(json.dumps(player, indent=2))


def main():

    pass

if __name__ == '__main__':
    main()