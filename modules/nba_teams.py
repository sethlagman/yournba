"""NBA Teams"""

from filehandler import FileHandler

class NbaTeam:
    """Retrieves the NBA teams' current standings"""

    def __init__(self):
        """Initialize attributes"""

        self.teams = FileHandler().read(r'nba_data\teams.json')

    def fetch_team_standing(self, team):

        for standing in self.teams:
            if standing['team'] == team:
                return standing
            
    def fetch_eastern_conference_teams(self):

        return [standing for standing in self.teams if standing['conference'] == 'East']
    
    def fetch_western_conference_teams(self):

        return [standing for standing in self.teams if standing['conference'] == 'West']
    
    def fetch_top_eastern_teams(self):
        
        eastern_teams = self.fetch_eastern_conference_teams()
        return self.quicksort(eastern_teams, 'wins', 'losses')
    
    def fetch_top_western_teams(self):

        western_teams = self.fetch_western_conference_teams()
        return self.quicksort(western_teams, 'wins', 'losses')
    
    def quicksort(self, teams, primary_key, secondary_key):
        if len(teams) <= 1:
            return teams
        
        for team in teams:
            team[primary_key] = int(team[primary_key])
            team[secondary_key] = int(team[secondary_key])
        
        pivot = teams[-1]

        less = []
        equal = []
        greater = []
        
        for team in teams:
            if team[primary_key] > pivot[primary_key]:
                less.append(team)
            elif team[primary_key] < pivot[primary_key]:
                greater.append(team)
            else:
                if team[secondary_key] < pivot[secondary_key]:
                    less.append(team)
                elif team[secondary_key] > pivot[secondary_key]:
                    greater.append(team)
                else:
                    equal.append(team)
        
        return self.quicksort(less, primary_key, secondary_key) + equal + self.quicksort(greater, primary_key, secondary_key)


def main():
    pass

if __name__ == '__main__':
    main()