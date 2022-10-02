import requests
from bs4 import BeautifulSoup as bs
import csv

def get_html(url):
    response = requests.get(url)
    soup = bs(response.text, 'lxml')
    return soup
url = "https://www.hltv.org/results"

def get_content(html):
    games = html.find_all('div', class_ = 'result-con')
    for game in games:
        teams = game.find_all('td', class_ = 'team-cell')
        team1 = teams[0].find('div', class_ = 'team').text
        team2 = teams[1].find('div', class_ = 'team').text
        result = game.find('td', class_ = 'result-score').text.strip().split()
        score1 = result[0]
        score2 = result[2]
        event = game.find('span', class_ = 'event-name').text
        data = {}
        data['team1'] = team1
        data['team2'] = team2
        data['score1'] = score1
        data['score2'] = score2
        data['event'] = event
        csv_writer(data)
def csv_writer(data):
    with open('hltv_games.csv', mode = 'a', encoding = 'utf-8') as file:
        headers = ['team1', 'score1', 'score2', 'team2', 'event']
        file_writer = csv.DictWriter(file, delimiter=',', fieldnames=headers)
        file_writer.writerow({'team1': data['team1'], 'score1' : data['score1'], 'score2' : data['score2'], 'team2' : data['team2'], 'event' : data['event']})


get_content(get_html(url))