import sqlite3


class ScoreboardData:
    def __init__(self, data: dict):
        self.score_1, self.score_2 = data.values()
        self.name_1, self.name_2 = data.keys()
        self.winner: tuple = (
            (self.name_1, self.score_1)
            if self.score_1 >= self.score_2
            else (self.name_2, self.score_2)
        )
        self.connect()

    def connect(self):
        try:
            conn = sqlite3.connect("scores.db")

            conn.execute(
                "CREATE TABLE scores (name VARCHAR PRIMARY KEY, wins INTEGER);"
            )
            conn.commit()
            conn.close()

        except sqlite3.DatabaseError:
            print("Database has already been created.")

    def updateTable(self):
        try:
            conn = sqlite3.connect("scores.db")

            if self.name_2 == "AI":
                query = "INSERT INTO scores (name, wins) VALUES (?,?);"
                data = (self.name_1, 0)

            else:
                query = "INSERT INTO scores (name, wins) VALUES (?,?), (?,?);"
                data = (self.name_1, 0, self.name_2, 0)

            conn.execute(query, data)
            conn.commit()
            conn.close()

        except sqlite3.IntegrityError:
            print("Player names has already been created.")

    def winnerUpdate(self):
        conn = sqlite3.connect("scores.db")

        query = f"UPDATE scores SET wins = wins + 1 WHERE name = '{self.winner[0]}';"

        conn.execute(query)
        conn.commit()
        conn.close()

    def getData(self, amount=0):
        conn = sqlite3.connect("scores.db")

        cursor = conn.cursor()

        query = "SELECT * FROM scores ORDER BY wins DESC, name ASC;"

        cursor.execute(query)
        rows = cursor.fetchall()

        leader_board = []
        for i in range(amount):
            leader_board.append(rows[i])

        return leader_board
