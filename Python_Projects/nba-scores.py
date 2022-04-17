from ast import Lambda
from urllib import response
from requests import get
from pprint import PrettyPrinter


BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()

def get_links():
    data = get(BASE_URL+ALL_JSON).json()
    links = data['links']
    return links



def get_scoreboard():
    scoreboard = get_links()['currentScoreboard']
    games = get(BASE_URL+scoreboard).json()['games']

    for game in games:
        home_team = game['hTeam']
        visitor_team = game['vTeam']
        clock = game['clock']
        period = game['period']

        print("--------------------------------")
        print(f"{home_team['triCode']} vs {visitor_team['triCode']}")
        print(
            f"{home_team['score']} - {visitor_team['score']}")
        print(f"{clock} -- {period['current']}")
       # printer.pprint(games.keys())
        
def get_statistics():
    stats = get_links()['leagueTeamStatsLeaders']
    teams = get(
        BASE_URL+stats).json()['league']['standard']['regularSeason']['teams']

    teams = list(filter(lambda x:  x['name'] != "Team", teams))
    teams.sort(key=lambda x: int(x['ppg']['rank']))

    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


    print(f"Name -- Nickname -- Avg Points per Game")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg']['avg']

        print(f"{i+1}--{name} -- {nickname}-- {ppg}")

def main():
    
    get_scoreboard()
    get_statistics()


#Main Call to main()
if __name__ == '__main__':
    main()



