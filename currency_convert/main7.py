import requests
from htmlparser1 import HtmlParser

parser = HtmlParser("https://bank.gov.ua/")
parser.NbuParse('index-page', 'small')

print(f"Current dollar currency is {parser.Result} hryvnas")

number = (int(input("Enter how many dollars do you want to convert: ")))

print(f"{number} dollars = {number * 36} hryvnas")