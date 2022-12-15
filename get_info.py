import re
import json
from bs4 import BeautifulSoup
import requests

def get_info(url):
    base_url = 'https://www.goal.com'


    temp = url.split('/')
    temp.insert(-1, "matches")
    url_ext = '/'.join(temp)
    # print(url_ext)

    response = requests.get(base_url+url_ext)
    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    info_list = []
    flag = 0
    for item in soup.find_all(["span", "div", 'a', 'time']):
        if item.string:
            if item.string.strip():
                # print(item.string)
                if item.string.strip() in ["Goalkeeper", "Defender", "Attacker", "Midfielder"]:
                    flag = 1
                if item.string.strip() == "Profile":
                    flag = 0
                if flag:
                    info_list.append(item.string.strip())
    # print(info_list)
    return [info_list[1],info_list[2],info_list[4],info_list[6], info_list[8],info_list[10]]

# print(get_info("/en-us/player/isma%C3%AFla-sarr/44s112hd02w1i2ucvai9jy7e1"))
# print(get_info("/en-us/player/famara-di%C3%A9dhiou/4f9cu6k87brnodww2l1u9rob9"))

# with open("teams_players_cached.json", 'r') as file_obj:
#     teams_info = json.load(file_obj)

# for team in teams_info.keys():
#     for players_num in teams_info[team].keys():
#         if players_num != "Coach":
#             temp = get_info(teams_info[team][players_num][-1])
#             print(temp)
#             teams_info[team][players_num].append(temp)
#             # - -
# with open("teams_players_info.json", 'w') as file_obj:
#     json.dump(teams_info,file_obj)
