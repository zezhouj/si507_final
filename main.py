## Final project of SI507
# name: Zezhou Jin
# unique name: zezhouj
import re
import json
import requests
from bs4 import BeautifulSoup
import get_team
import get_player
# from get_matches import get_matches
# from get_info import get_info
def show_matches():
    url_live_score = "https://www.goal.com/en-us/live-scores"
    response = requests.get(url=url_live_score)
    soup = BeautifulSoup(response.text, 'html.parser')
    div_list = []
    for div in soup.find_all(['div', 'meta', 'span']):
        if len(div.find_all(['div', 'meta', 'span'])) == 0:
            # print(div)
            # print("++++")
            div_list.append(str(div))
    #     if re.search(r"class=\"competition-matches\"", div):
    #         print(div)
    # print(div_list)
    competition_dict = {}
    # for div in div_list:
        # if re.search(r"class=\"competition-name\"", div):
            # print("*************")
            # print(div)
        # if re.search(r"content=\"\w+ vs \w+\"", div):
            # print("*************")
            # print(div)
    flag = 0
    match_id = 0
    match_dict = {}
    match_list = []
    # l_limit = 3
    for item in soup.find_all(name=['div', 'meta', 'span']):
        if item.string == "UEFA Champions League":
            flag = 0
        # if flag and item.string and item.string != ' ':
        if flag and item.string and item.string != ' ' and re.search(r"^[\w\s-]+\'?$|\(.*\)", item.string):
            match_list.append(item.string.strip())
            # print(">"+item.string+"<")
            # if item.string == "FT":
            #     l_limit = 4
            # if str(match_id) not in match_dict.keys():
            #     match_dict[str(match_id)] = [item.string.strip()]
            # else:
            #     match_dict[str(match_id)].append(item.string.strip())
            # if len(match_dict[str(match_id)]) > l_limit:
            #     match_id += 1
            #     l_limit = 3
        if item.string == "World Cup":
            flag = 1
    # print(match_list)
    index_l = []
    for i in range(len(match_list)):
        if match_list[i] == '-':
            # print(i)
            index_l.append(i)
    match_shaped = []
    slice_ind = 0
    for index in index_l:
        if match_list[slice_ind] == 'PEN':
            match_shaped.append(match_list[slice_ind:index+4])
            slice_ind = index+4
        else:
            match_shaped.append(match_list[slice_ind:index+3])
            slice_ind = index+3
    # print(match_shaped)
    # print("Finished matches:")
    for match in match_shaped:
        if match[0] in ['FT', 'PEN']:
            print("Finished:",' '.join(match[1:]))
    # print("Ongoing matches:")
    for match in match_shaped:
        if re.search(r"\d+\'$",match[0]):
            print('Ongoing:',' '.join(match))
        elif match[0] == "ATE":
            print(' '.join(match[1:]))
    # print("future matches:")
    for match in match_shaped:
        if len(match) == 5:
            print(f"Future: {match[1]} vs {match[-1]}")
def main():
    print("Welcome to The Dashboard of 2022 Qatar World Cup")
    print("Here are recently played match(es):")
    show_matches()
    print("There 2 options in this project.")
    print("1: get the players' info of your favorite team")
    print("2: show relation of two players through teams and matches")
    option = input("Please enter an option(1 or 2): ")
    while True:
        if option == "1":
            break
        elif option == "2":
            break
        else:
            print("unknown input detected")
            option = input("Please enter again(1 or 2):")
    if option == '1':
        print("There 32 teams in 2022 Qatar World Cup, shown below")
        try:
            with open('./team_url.json', 'r') as file_obj:
                team_url = json.load(file_obj)
        except:
            team_url = get_team.get_team()
        i = 0
        for item in team_url.keys():
            if (i+1)%8:
                print(item, end=' | ')
            else:
                print(item)
            i += 1
        in_team = input("Please enter the team interested in: ")
        while True:
            if in_team in team_url.keys():
                print(f"Loading data for team {in_team} ... ...")
                break
            else:
                in_team = input("Unknown input found, please enter a team in the list above: ")
        try:
            with open("teams_players_temp.json") as file_obj:
                team_player_dict = json.load(file_obj)
        except:
            team_player_dict = get_player.get_players(team_url[in_team])
        print(f"Data for {in_team} has been loaded successfully.")
        print(f"Team {in_team} | Coach: {team_player_dict[in_team]['Coach']}")
        print(f"Players in team {in_team} are divide into 3 parts: Attackers, Midfielders and Defenders")
        t_player = input("Please enter player in which position you are interested in(Midfielders, Attackers or Defenders): ")
        while True:
            if t_player.lower() in ["attackers", "attacker", "att"]:
                print(f"Attackers in team {in_team} shown below")
                for item in team_player_dict[in_team].items():
                    if item[1][0] == "Attackers":
                        print(f"Name: {item[1][2]} |Number: {item[0]}")
                break
            elif t_player.lower() in ["defenders", "defender", 'def']:
                print(f"Defenders in team {in_team} shown below")
                for item in team_player_dict[in_team].items():
                    if item[1][0] == "Defenders":
                        print(f"Name: {item[1][2]} |Number: {item[0]}")
                break
            elif t_player.lower() in ["midfielders", "midfielder", "mid"]:
                print(f"Defenders in team {in_team} shown below")
                for item in team_player_dict[in_team].items():
                    if item[1][0] == "Defenders":
                        print(f"Name: {item[1][2]} |Number: {item[0]}")
                break
            else:
                t_player = input("Unknown input found, please enter again(Midfielders, Attackers or Defenders): ")
        in_player = input("Enter the Number of player for more info:")
        while True:
            if in_player in team_player_dict[in_team].keys():
                # TODO
                print(team_player_dict[in_team][in_player])
                break
            else:
                in_player = input("No player is found, please enter the Number again:")
if __name__=="__main__":
    main()
