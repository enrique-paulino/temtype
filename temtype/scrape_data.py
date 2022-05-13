import fandom
import json
import requests
from bs4 import BeautifulSoup

fandom.set_wiki("temtem")

types = [ "Neutral", "Fire", "Water", "Nature", "Electric", "Earth",
                "Mental", "Wind", "Digital", "Melee", "Crystal", "Toxic"];

weaknesses = json.load(open("temtype/static/data/weaknesses.json"), encoding="utf8")

def FindTem(temtem):
    if fandom.page(title = temtem).section("Type Matchup") != None:
        return "FOUND"
    else:
        return "NOT FOUND"

def ScrapeSummary(temtem):
    return fandom.page(title = temtem).summary

def ScrapePicture(temtem):
    link = requests.get('https://temtem.fandom.com/wiki/' + temtem).text
    page = BeautifulSoup(link, 'lxml')
    status = page.find('table', class_= "infobox-table")
    images = [i['data-src'].split("/revision", 1)[0] for i in status.find_all('img')]

    return [images[0], images[1]]

def ScrapeType(temtem):
    summary = fandom.page(title = temtem).summary
    res = int(summary[summary.index("#") + len("") + 1: summary.index(")")])-1
    temtem_data = open('temtype/static/data/temtem.json', encoding="utf8")
    data = json.load(temtem_data)
    types = data[res]['types']
    return types

def ScrapeMatchup(temtem):
    ttypes = ScrapeType(temtem)
    total = {"Neutral": None, "Fire": None, "Water": None, "Nature": None, "Electric": None, "Earth": None,
              "Mental": None, "Wind": None, "Digital": None, "Melee": None, "Crystal": None, "Toxic": None}
    for i in types:
        if (len(ttypes) > 1):
            total[i] = weaknesses[ttypes[0]][i] * weaknesses[ttypes[1]][i]
        else:
            total[i] = weaknesses[ttypes[0]][i]

    new_total = {}

    for key, value in sorted(total.items(), reverse=False):
        new_total.setdefault(value, []).append(key.lower())

    sorted_total = {}
    for key in sorted(list(new_total.keys()), reverse=True):
        sorted_total[key] = new_total[key]

    return sorted_total
