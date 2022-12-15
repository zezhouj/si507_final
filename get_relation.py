import json

# with open("./matches.json", 'r') as fp:
#     matches = json.load(fp)

# with open("./team_url.json", 'r') as fp:
#     team_url = json.load(fp)

def get_relation(team1, team2, team_match, match_team):
    bfs = [team1]
    visited = {team1: (None, None)}
    while bfs:
        curr_team = bfs.pop(0)
        for match in team_match[curr_team]:
            for team in match_team[match]:
                if team not in visited.keys():
                    bfs.append(team)
                    visited[team] = (match, curr_team)
        if curr_team == team2:
            chain = [team2]
            while visited[curr_team][0]:
                # print(visited[curr_team][0])
                chain.insert(0,visited[curr_team][0])
                curr_team = visited[curr_team][1]
                chain.insert(0, curr_team)
            for i in range(len(chain)):
                temp2 = chain[i].split(',')
                if len(temp2) > 1:
                    if temp2[2] == chain[i-1]:
                        pass
                    else:
                        a1 = temp2.pop(3)
                        temp2.insert(5, a1)
                        a1 = temp2.pop(2)
                        temp2.insert(5, a1)
                        a1 = temp2.pop(1)
                        temp2.insert(5, a1)
                        # print(temp2)
                    chain[i] = ' '.join(temp2[1:])
            # print(chain)
            return chain
    return None


# team_match = {}
# match_team = {}
# for team in team_url.keys():
#     for match in matches:
#         if team in match:
#             if team in team_match.keys():
#                 team_match[team].append(','.join(match))
#             else:
#                 team_match[team] = [','.join(match)]
# for match in matches:
#     match_team[','.join(match)] = [match[2], match[5]]

# for item in team_match.items():
#     print(item)
# for item in match_team.items():
#     print(item)
# print(len(match_team))

# get_relation('Germany','Croatia')
# print(get_relation('South Korea','Netherlands'))
# temp = get_relation('South Korea','Netherlands')
# for i in range(len(temp)):
#     temp2 = temp[i].split(',')
#     if len(temp2) > 1:
#         if temp2[2] == temp[i-1]:
#             pass
#         else:
#             a1 = temp2.pop(3)
#             temp2.insert(5, a1)
#             a1 = temp2.pop(2)
#             temp2.insert(5, a1)
#             a1 = temp2.pop(1)
#             temp2.insert(5, a1)
#             print(temp2)
#         temp[i] = ' '.join(temp2[1:])
# print(temp)
