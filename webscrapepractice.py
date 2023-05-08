"""extracts html content from URL"""
import requests
from bs4 import BeautifulSoup

URL = "https://www.kdnuggets.com/"
res = requests.get(URL, timeout=10)
htmlData = res.content
#print(htmlData)
parsedData = BeautifulSoup(htmlData, "html.parser")
#print(parsedData.prettify)
def title():
    print(parsedData.title.string)

def find():
    h2 = parsedData.find("h2").text
    print(h2)

def find_all():
    h2s = parsedData.find_all("h2")
    for h2 in h2s:
        print(h2)

def find_anchors():
    anchors = parsedData.find_all("a")
    for a in anchors:
        print(a["href"])

def find_elements():
    tags = parsedData.find_all("li", class_="li-has-thumb")
    for tag in tags:
        print(tag.text)

find_elements()