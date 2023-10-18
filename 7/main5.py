from dbcontext import DbContext
context = DbContext('students.sl3', 5.0)
#1 CREATE TABLE ...(fields_definitions)
'''
context.Query("CREATE TABLE S2816(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(20), age INT, avg_grade FLOAT)")
'''
#2 INSERT INTO ...(name_of_fields) VALUES(set_of_values)
'''
context.Query("INSERT INTO S2816(name, age, avg_grade) VALUES('Dvornikov Kyrylo', 16, 11.0)")
context.Query("INSERT INTO S2816(name, age, avg_grade) VALUES('Solop Illya', 15, 12.0)")
context.Query("INSERT INTO S2816(name, age, avg_grade) VALUES('Oliinyk Kostyantyn', 14, 10.5)")
context.Query("INSERT INTO S2816(name, age, avg_grade) VALUES('Kochkin Dmytro', 14, 11.5)")
'''
#3 UPDATE ... SET .... WHERE....
'''
context.Query("UPDATE S2816 SET avg_grade=10.7 WHERE id=3")
'''
#4 DELETE FROM ... WHERE....
#context.Query("INSERT INTO S2816(name, age, avg_grade) VALUES('test', 14, 7)")
'''
context.Query("DELETE FROM S2816")# WHERE id=5")
'''
#5 SELECT (set_name_of_fields) FROM ..... WHERE....
#res = context.Execute("SELECT name, age FROM S2816 WHERE avg_grade > 11.0")
#res = context.Execute("SELECT name, avg_grade FROM S2816 WHERE age < 15.0")
#res = context.Execute("SELECT * FROM S2816")
#print(res)
#6 DROP TABLE .....
'''
context.Query("DROP TABLE S2816")
'''