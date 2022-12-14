import requests
import json
import re
from bs4 import BeautifulSoup

def get_players(team, url):


    base_url = "https://www.goal.com"

    response = requests.get(url=base_url+url)

    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    flag = 0
    goalkeepers = []
    defenders = []
    midfielders = []
    Attackers = []
    coach = []
    player_urls = []
    player_dict = {}
    for item in soup.find_all(["span", "div", "a", "h3"]):
        if item.string:
            if item.string.lower().strip() == "goalkeepers":
                flag = 1
            if item.string.lower().strip() == "defenders":
                flag = 2
            if item.string.lower().strip() == "midfielders":
                flag = 3
            if item.string.lower().strip() == "attackers":
                flag = 4
            if item.string.lower().strip() in ["coach", "competitions"]:
                flag = 5
                # print(item.string) Competitions
            if flag == 1:
                goalkeepers.append(item.string.strip())
            if flag == 2:
                defenders.append(item.string.strip())
            if flag == 3:
                midfielders.append(item.string.strip())
            if flag == 4:
                Attackers.append(item.string.strip())
            if flag == 5:
                coach.append(item.string.strip())
            if len(coach) == 2:
                flag = 0
        if item.name == 'a':
            if flag == 1:
                try:
                    # print(item['href'])
                    goalkeepers.append(item['href'])
                except:
                    pass
            if flag == 2:
                try:
                    # print(item['href'])
                    defenders.append(item['href'])
                except:
                    pass
            if flag == 3:
                try:
                    # print(item['href'])
                    midfielders.append(item['href'])
                except:
                    pass
            if flag == 4:
                try:
                    # print(item['href'])
                    Attackers.append(item['href'])
                except:
                    pass
    goalkeepers.reverse()
    defenders.reverse()
    midfielders.reverse()
    Attackers.reverse()
    # coach.reverse()
    # print(goalkeepers)
    # print(defenders)
    # print(midfielders)
    # print(Attackers)
    # print(coach)
    # print(url)

    def player_list2dict(player_list):
        for i in range(len(player_list)):
            if i != len(player_list)-1:
                if i%4:
                    player_dict[player_list[i-i%4]].append(player_list[i])
                else:
                    player_dict[player_list[i]] =  [player_list[-1]]
    player_list2dict(goalkeepers)
    player_list2dict(defenders)
    player_list2dict(midfielders)
    player_list2dict(Attackers)
    # player_list2dict(coach)
    if "Coach" in coach:
        player_dict[coach[0]] = coach[1]
    else:
        player_dict["Coach"] = "Unknown from website"

    # print(player_urls)
    # for item in player_dict.items():
    #     print(item)
        # for element in player_urls:
        #     if item[1][-1].split(". ")[-1]
        # print(item[1][-1].split(". ")[-1].lower())
    
    return {team: player_dict}

# with open("./team_url.json", 'r') as file_obj:
#     team_urls = json.load(file_obj)
# # print(team_urls)

# team_player_dict = {}
# for team in team_urls.keys():
#     print(team)
#     team_player_dict[team] = get_players(team, team_urls[team])
#     if team == "Spain":
#         print(team_player_dict[team])

# for item in team_player_dict.items():
#     print(item)
    # pass

# with open("./teams_players_temp.json", 'w') as file_obj:
#     json.dump(team_player_dict, file_obj)
