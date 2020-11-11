import sqlite3


class ScoreboardData:
    def __init__(self, data:dict):
        self.score_1:int, self.score_2:int = data.values()
        self.name_1:str, self.name_2:str = data.keys()
        self.winner:tuple = (self.name_1, self.score_1) if self.score_1 >= self.score_2 else (self.name_2, self.score_2)
    
    def connect(self):
        try:
            conn = sqlite3.connect('scores.db')
            c=conn.cursor()
            conn.execute("CREATE TABLE scores (id INTEGER PRIMARY KEY, name TEXT NOT NULL, wins INTEGER);")
            conn.commit()
            conn.close()
            print("Done.")
        
        except:
            print("Database has already been created.")

    def updateTable(self):
        conn = sqlite3.connect("scores.db")
        c = conn.cursor()
        query = "INSERT INTO scores (name, wins) VALUES (?,?), (?,?);"
        data = (self.name_1,0,self.name_2,0)
        conn.execute(query, data)
        conn.commit()
        conn.close()
        print("Done.")
    
    def winnerUpdate(self):
        conn = sqlite3.connect("scores.db")
        c = conn.cursor()
        query = f"UPDATE scores SET wins = wins + 1 WHERE name = '{self.winner[0]}';"
        conn.execute(query)
        conn.commit()
        conn.close()
        print("Done.")


data = {
    "Roberto":0,
    "Arnaldo":1,
}
a = ScoreboardData(data)

#a.connect()
#a.updateTable()

a.winnerUpdate()
    









# import pandas as pd

# class ScoreCSV:
#     def __init__(self, data):
#         self.score_1 = data[0]
#         self.name_1 = data[1]
#         self.score_2 = data[2]
#         self.name_2 = data[3]
    
#     def exportCSV(self):
        
#         pd.DataFrame([[self.name_1,self.score_1],[self.name_2,self.score_2]],columns=["Player", "Wins"])



# data = [5,"Pedro",10,"Rodrigo"]

# obj = ScoreCSV(data)


# obj.exportCSV()





















# import psycopg2

# #establishing the connection
# conn = psycopg2.connect(
#    database="postgres", user='postgres', password='djbc!2001HQ', host='127.0.0.1', port= '5432'
# )
# conn.autocommit = True

# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()

# #Preparing query to create a database
# sql = '''CREATE database mydb;'''

# #Creating a database
# cursor.execute(sql)
# print("Database created successfully........")

# #Closing the connection
# conn.close()