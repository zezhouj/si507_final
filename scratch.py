import requests
import re
from html.parser import HTMLParser

# url = "https://football98.p.rapidapi.com/fifaworldcup/table"

# headers = {
# 	"X-RapidAPI-Key": "54d3a8ed22msh95eea4ff4163d71p1208f0jsn153171fa4f8f",
# 	"X-RapidAPI-Host": "football98.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers)

# print(response.text)

url_matches = "https://www.goal.com/en-us/live-scores"

headers = {
	"X-RapidAPI-Key": "54d3a8ed22msh95eea4ff4163d71p1208f0jsn153171fa4f8f",
	"X-RapidAPI-Host": "football98.p.rapidapi.com"
}

text_matches = requests.get(url=url_matches).text

# print(text_matches)
# m = re.search(r"competition-matches", text_matches)
# print(m)

with open(file="./1205_post_match.txt", mode='w') as file:
    file.write(text_matches)
find_all = re.findall(r"class=\"competition-name\">([\w\s]+)<", text_matches)
print(f"Debugging: {find_all}\nSize = {len(find_all)}")
listed_text = re.split(r">[\s\t]*<", text_matches)
# print(listed_text)
# with open(file="./temp1.txt", mode='w') as file:
#     for item in listed_text:
#         file.write(item+"\n")
flag = 0
for line in listed_text:
    if re.search(r"competition-name",line):
        flag = 1
        c_name = re.search(r">([\w\s]+)<",line).group(1)
        print(c_name)
    if flag and re.search(r" vs ",line):
        print(line)
