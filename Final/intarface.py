from dbcontext1 import DbContext as dc
from htmlparser1 import HtmlParser
base = 'database1.sl3'
context = dc(base, 5.0)

# 1 Creating Table

#context.Query("CREATE TABLE LINKS(id INTEGER PRIMARY KEY AUTOINCREMENT, link VARCHAR(50), name VARCHAR(20))")
#context.Query("CREATE TABLE RESULT(id INTEGER PRIMARY KEY AUTOINCREMENT, result VARCHAR(50)")

# INSERT INTO

recoreds = [
      ('https://bank.gov.ua/', 'nbu'),
      ('https://meteo.ua/ua/34/kiev', 'weather')
]
query = "INSERT INTO LINKS(link, name) VALUES(?, ?)"
context.QueryMany(query, recoreds)


