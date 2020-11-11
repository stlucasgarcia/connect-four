import sqlite3


class ScoreboardData:
    def __init__(self, data:dict):
        self.score_1, self.score_2 = data.values()
        self.name_1 , self.name_2 = data.keys()
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
    
    def getData(self, amount=0):
        conn = sqlite3.connect("scores.db")
        c = conn.cursor()
        query = "SELECT * FROM scores ORDER BY wins DESC, name ASC;"
        c.execute(query)
        rows = c.fetchall()

        leader_board_full = []
        for row in rows:
            leader_board_full.append((row[1],row[2]))

        leader_board = []
        for i in range(amount):
            leader_board.append(leader_board_full[i])
        
        return leader_board


# data = {
#     "Nick":0,
#     "John":1,
# }
# data = {
#     "George":1,
#     "Michael":0,
# }
data = {
    "Fred":1,
    "Peter":0,
}
a = ScoreboardData(data)

a.connect()
#a.updateTable()

a.winnerUpdate()

x = a.getData(3)
print(x)