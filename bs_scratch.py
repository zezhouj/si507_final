html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
import re
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
# <html>
#  <head>
#   <title>
#    The Dormouse's story
#   </title>
#  </head>
#  <body>
#   <p class="title">
#    <b>
#     The Dormouse's story
#    </b>
#   </p>
#   <p class="story">
#    Once upon a time there were three little sisters; and their names were
#    <a class="sister" href="http://example.com/elsie" id="link1">
#     Elsie
#    </a>
#    ,
#    <a class="sister" href="http://example.com/lacie" id="link2">
#     Lacie
#    </a>
#    and
#    <a class="sister" href="http://example.com/tillie" id="link3">
#     Tillie
#    </a>
#    ; and they lived at the bottom of a well.
#   </p>
#   <p class="story">
#    ...
#   </p>
#  </body>
# </html>
with open("120_pen.txt", 'r') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
print(soup.prettify())
# with open("temp2.txt",'w') as fp:
#     fp.write(soup.prettify())

# print(soup.find_all('div'))
div_list = []
for div in soup.find_all(['div', 'meta', 'span']):
    if len(div.find_all(['div', 'meta', 'span'])) == 0:
        print(div)
        print("++++")
        div_list.append(str(div))
#     if re.search(r"class=\"competition-matches\"", div):
#         print(div)
# print(div_list)
competition_dict = {}
for div in div_list:
    if re.search(r"class=\"competition-name\"", div):
        print("*************")
        print(div)
    if re.search(r"content=\"\w+ vs \w+\"", div):
        print("*************")
        print(div)
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
print(match_list)
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
print(match_shaped)
print("Finished matches:")
for match in match_shaped:
    if match[0] in ['FT', 'PEN']:
        print(' '.join(match[1:]))
print("Ongoing matches:")
for match in match_shaped:
    if re.search(r"\d+\'$",match[0]):
        print(' '.join(match))
    elif match[0] == "ATE":
        print(' '.join(match[1:]))
print("future matches:")
for match in match_shaped:
    if len(match) == 5:
        print(f"{match[1]} vs {match[-1]}")
for match in match_shaped:
    if len(match) == 7:
        print(match)
        print(soup.find_all(href=re.compile(f"{match[-5].lower().replace(' ', '-')}-v-{match[-2].lower().replace(' ', '-')}"))[0]["href"])
    else:
        print(match)
        print(soup.find_all(href=re.compile(f"{match[-4].lower().replace(' ', '-')}-v-{match[-1].lower().replace(' ', '-')}"))[0]["href"])
for item in soup.find_all(href=re.compile("brazil")):
    print(item['href'])

