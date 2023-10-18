from dbcontext1 import DbContext1
context = DbContext1('temperature.sl3', 5.0)
# 1 Creating Table

context.Query("CREATE TABLE temperature(id INTEGER PRIMARY KEY AUTOINCREMENT, )")
