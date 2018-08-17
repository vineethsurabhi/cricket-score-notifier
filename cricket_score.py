import requests
from bs4 import BeautifulSoup
import threading

cricket_match = "http://www.espncricinfo.com/icc-champions-trophy-2017/engine/match/1022361.html"


def print_score():
    threading.Timer(3.0, print_score).start()
    page = requests.get(cricket_match).content
    soup = BeautifulSoup(page, 'html.parser')
    print(soup.title.string.split("|")[0])
print_score()
