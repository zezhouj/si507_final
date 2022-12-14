import requests
import json
import re
from bs4 import BeautifulSoup
def get_team():
    url_team_all = "https://www.goal.com/en-us/world-cup/70excpe1synn9kadnbppahdn7"
    response = requests.get(url=url_team_all)

    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    team = []
    url_team = []
    flag = 0
    for item in soup.find_all(["span", "div", "a"]):
        if item.string == " ":
            flag = 0
        if item.name == 'a':
            try:
                # print(item['href'])
                url_team.append(item['href'])
            except:
                pass
        if item.string and flag:
            # print(item.string)
            team.append(item.string)
        if item.string == "Teams":
            flag = 1
    # print(team)
    # print(url_team)
    team_url_dict = {}
    for item in team:
        for url in url_team:
            try:
                # print(url.split('/')[3])
                
                if url.split('/')[3].replace('-', ' ') == item.lower():
                    # print(url)
                    team_url_dict[item] = url
                    break
            except:
                pass
    # for item in team_url_dict.items():
    #     print(item)
    return team_url_dict

# def get_team():
#     pass
# team_url_dict = get_team()
# with open("./team_url.json", 'w') as file_obj:
#     json.dump(team_url_dict, file_obj)
