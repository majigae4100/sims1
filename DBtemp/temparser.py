import requests as r
from bs4 import BeautifulSoup as bs

class HTMLParser:
    def __init__(self, url:str):
        self.Url = url
        self.Counter = 0
        self.Result = {}

    def TempParser(self, separator:1, separator2:str):
        responce = r.get(self.Url)
        responce_content = responce.content
        html = bs(responce_content, features="html.parser")
        tags = html.find_all('div', attrs={'class'})