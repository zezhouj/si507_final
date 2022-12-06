import re
from bs4 import BeautifulSoup

base_url = "https://www.goal.com"
class Match:
    def __init__(self, homeTeam, awayTeam, status, url_extension=None, homeScore=None, awayScore=None):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.status = status
        self.url = f"{base_url}{url_extension}"
        self.homeScore = homeScore
        self.awayScore = awayScore

    def display_status(self):
        if self.status == "ongoing":
            print(f"Ongoing match: {self.homeTeam} : {self.awayTeam}")
            print(f"Score: {self.homeScore} : {self.awayScore}")
        elif self.status == "past":
            print(f"finished match: {self.homeTeam} : {self.awayTeam}")
            print(f"Score: {self.homeScore} : {self.awayScore}")
        else:
            print(f"future match: {self.homeTeam} : {self.awayTeam}")
            print(f"Score: {self.homeScore} : {self.awayScore}")

class Team:
    def __init__(self, players, coach):
        self.players = players
        self.coach = coach
