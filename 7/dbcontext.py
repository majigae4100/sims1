import sqlite3
class DbContext:
    def __init__(self, database:str, timeout:float):
        self.Database = database
        self.Timeout = timeout
    def Query(self, sqlQuery:str):
        try:
            connection = sqlite3.connect(self.Database, self.Timeout)
            cursor = connection.cursor()
            cursor.execute(sqlQuery)
            connection.commit()
        except Exception as ex:
            print(ex)
        finally:
            connection.close()
    def Execute(self, sqlQuery:str):
        try:
            connection = sqlite3.connect(self.Database, self.Timeout)
            cursor = connection.cursor()
            cursor.execute(sqlQuery)
            connection.commit()
            return cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            connection.close()