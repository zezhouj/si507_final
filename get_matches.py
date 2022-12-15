import re
import json
from bs4 import BeautifulSoup
import requests

def get_matches(url):
    base_url = "https://www.goal.com"

    temp = url.split('/')
    temp.insert(-1, "fixtures-results/world-cup/70excpe1synn9kadnbppahdn7")
    url_ext = '/'.join(temp)
    # print(base_url+url_ext)
    response = requests.get(url=base_url+url_ext)

    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    m_list = []
    for item in soup.find_all(["span", "div"]):
        if item.string:
            if item.string.strip():
                m_list.append(item.string.strip())
    return m_list[2:-3]
# with open("./team_url.json", 'r') as file_obj:
#     team_url = json.load(file_obj)
# temp = []
# for team in team_url.items():
#     temp.append(get_matches(team[1]))
# # print(temp)
# matches = []
# for item in temp:
#     while (len(item) > 5):
#         if item[0] == "FT":
#             matches.append(item[0:6])
#             item = item[6:]
#         elif item[0] == "PEN":
#             matches.append(item[0:7])
#             item = item[7:]

# # print(matches)
# for match in matches:
#     match.append({match[2], match[5]})

# i = 0
# while i < len(matches)-1:
#     print(i)
#     j = 0
#     while j != len(matches[i+1:]):
#         if matches[i+j+1][-1] == matches[i][-1]:
#             matches.pop(i+j+1)
#         else:
#             j += 1
#     i += 1
# for match in matches:
#     match.pop(-1)
# print(len(matches))
# with open("./matches.json", 'w') as fp:
#     json.dump(matches, fp)
