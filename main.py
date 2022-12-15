## Final project of SI507
# name: Zezhou Jin
# unique name: zezhouj
import re
import json
import requests
from bs4 import BeautifulSoup
import get_team
import get_player
import get_matches
import get_relation
import get_info
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
    while True:
        print("There 2 options in this project.")
        print("1: get the players' info of your favorite team")
        print("2: show relation of two players through teams and matches")
        option = input("Please enter an option(1 or 2 or exit): ")
        while True:
            if option == "1":
                break
            elif option == "2":
                break
            elif option.lower() == "exit":
                exit("Thank you, program finished :)")
            else:
                print("unknown input detected")
                option = input("Please enter again(1 or 2):")
        if option == '1':
            print("There 32 teams in 2022 Qatar World Cup, shown below ...")
            try:
                with open('./team_url.json', 'r') as file_obj:
                    team_url = json.load(file_obj)
            except:
                team_url = get_team.get_team()
                with open('./team_url.json', 'w') as file_obj:
                    json.dump(team_url, file_obj)
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
            team_player_dict = {}
            try:
                with open("./teams_players_cached.json", 'r') as file_obj:
                    team_player_dict = json.load(file_obj)
            except:
                for item in team_url.items():
                    team_player_dict.update(get_player.get_players(item[0],item[1]))
                with open("./teams_players_cached.json", 'w') as file_obj:
                    json.dump(team_player_dict, file_obj)
            print(f"Data for {in_team} has been loaded successfully.")
            print("**********************************************")
            # print("**********************************************")
            print(f"Team {in_team} | Coach: {team_player_dict[in_team]['Coach']}")
            # print("**********************************************")
            print("**********************************************")
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
                    print(f"Midfielders in team {in_team} shown below")
                    for item in team_player_dict[in_team].items():
                        if item[1][0] == "Midfielders":
                            print(f"Name: {item[1][2]} | Number: {item[0]}")
                    break
                else:
                    t_player = input("Unknown input found, please enter again(Midfielders, Attackers or Defenders): ")
            in_player = input("Enter the Number of player for more info: ")
            while True:
                if in_player in team_player_dict[in_team].keys():
                    # TODO
                    try:
                        with open("./teams_players_info.json", 'r') as fp:
                            team_player_info = json.load(fp)
                        player_info = team_player_info[in_team][in_player][-1]
                    except:
                        player_info = get_info.get_info(team_player_dict[in_team][in_player][-1])
                    print(f"* Name: {team_player_dict[in_team][in_player][2]}")
                    print(f"* Team: {in_team}")
                    print(f"* Nationality: {player_info[1]}")
                    print(f"* Registration Club: {player_info[0]}")
                    print(f"* Date of Birth: {player_info[2]}")
                    print(f"* Height: {player_info[3]}")
                    print(f"* Weight: {player_info[4]}")
                    print(f"* Footedness: {player_info[5]}")
                elif in_player.lower() in ["back", "b"]:
                    break
                else:
                    in_player = input("No player is found, please enter the Number again:")

                in_player = input(f"Enter the Number for another player in team {in_team} or \"back\" to the main menu: ")
        elif option == "2":
            print("*************************")
            print("Here are some famous player in 2022 World Cup. If you are new to soccer, you may choose two of players in the list below")
            print("Or you may pick any two of players in the World Cup.")
            print("|L. Messi       | Cristiano Ronaldo | Neymar        | Vinícius Júnior")
            print("|R. Lewandowski | E. Hazard         | Son Heung-Min | K. Mbappé ")
            print("|G. Bale        | H. Kane           | L. Suárez     | L. de Jong")
            print("|C. Eriksen     | K. De Bruyne      | H. Maguire    | K. Mitoma")
            try:
                with open('./team_url.json', 'r') as file_obj:
                    team_url = json.load(file_obj)
            except:
                team_url = get_team.get_team()
                with open('./team_url.json', 'w') as file_obj:
                    json.dump(team_url, file_obj)
            try:
                with open("./teams_players_cached.json", 'r') as file_obj:
                    team_player_dict = json.load(file_obj)
            except:
                for item in team_url.items():
                    team_player_dict.update(get_player.get_players(item[0],item[1]))
                with open("./teams_players_cached.json", 'w') as file_obj:
                    json.dump(team_player_dict, file_obj)
            player_1 = input("Now it's time to make your choose, please enter the name of the first player: ")
            player_1_team = None
            while player_1_team == None:
                for item in team_player_dict.items():
                    for element in item[1].items():
                        if element[1][2] == player_1:
                            print("+++++++++++++++++++++++++")
                            print("Player's Name detected.")
                            print(f"{player_1} from Team {item[0]}.")
                            print(f"Number: {element[0]}")
                            print(f"Position: {element[1][0][:-1]}")
                            print("+++++++++++++++++++++++++")
                            player_1_team = item[0]
                            break
                    if player_1_team:
                        break
                if player_1_team == None:
                    player_1 = input("Unknown player in this World Cup or invalid input, please enter the name again: ")
            player_2 = input("Please enter the name of the second player: ")
            player_2_team = None
            while player_2_team == None:
                for item in team_player_dict.items():
                    for element in item[1].items():
                        if element[1][2] == player_2:
                            print("+++++++++++++++++++++++++")
                            print("Player's Name detected.")
                            print(f"{player_2} from Team {item[0]}.")
                            print(f"Number: {element[0]}")
                            print(f"Position: {element[1][0][:-1]}")
                            print("+++++++++++++++++++++++++")
                            player_2_team = item[0]
                            break
                    if player_2_team:
                        break
                if player_2_team == None:
                    player_2 = input("Unknown player in this World Cup or invalid input, please enter the name again: ")
            try:
                with open("./matches.json", 'r') as fp:
                    matches = json.load(fp)
            except:
                temp = []
                for team in team_url.items():
                    temp.append(get_matches.get_matches(team[1]))
                matches = []
                for item in temp:
                    while (len(item) > 5):
                        if item[0] == "FT":
                            matches.append(item[0:6])
                            item = item[6:]
                        elif item[0] == "PEN":
                            matches.append(item[0:7])
                            item = item[7:]

                # print(matches)
                for match in matches:
                    match.append({match[2], match[5]})

                i = 0
                while i < len(matches)-1:
                    print(i)
                    j = 0
                    while j != len(matches[i+1:]):
                        if matches[i+j+1][-1] == matches[i][-1]:
                            matches.pop(i+j+1)
                        else:
                            j += 1
                    i += 1
                for match in matches:
                    match.pop(-1)
                with open("./matches.json", 'w') as fp:
                    json.dump(matches, fp)
            team_match = {}
            match_team = {}
            for team in team_url.keys():
                for match in matches:
                    if team in match:
                        if team in team_match.keys():
                            team_match[team].append(','.join(match))
                        else:
                            team_match[team] = [','.join(match)]
            for match in matches:
                match_team[','.join(match)] = [match[2], match[5]]
            relation = get_relation.get_relation(player_1_team, player_2_team, team_match, match_team)
            if relation:
                print(player_1, end=' ')
                for i in range(len(relation)):
                    if i%2:
                        print(f"--> {relation[i]} <-", end='-')
                print(player_2)
            else:
                "None relations found between these two plyers based on currently finished matches."
            input("Press enter to continue")
if __name__=="__main__":
    main()
