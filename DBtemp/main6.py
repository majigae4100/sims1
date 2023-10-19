from dbcontext1 import DbContext1
context = DbContext1('temperature.sl3', 5.0)


# 1 Creating Table

#context.Query("CREATE TABLE TEMP(id INTEGER PRIMARY KEY AUTOINCREMENT, date FLOAT, temperature FLOAT)")

#context.Query("INSERT INTO TEMP(date, temperature) VALUES('19.10', '+12')")
#context.Query("INSERT INTO TEMP(date, temperature) VALUES('20.10', '+13')")
#context.Query("INSERT INTO TEMP(date, temperature) VALUES('21.10', '+12')")
#context.Query("INSERT INTO TEMP(date, temperature) VALUES('22.10', '+19')")
#context.Query("INSERT INTO TEMP(date, temperature) VALUES('23.10', '+14')")

# DELETE TABLE

#context.Query("DROP TABLE TEMP")