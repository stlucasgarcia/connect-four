import sqlite3


class ScoreboardData:
    """Class to manage Database features"""

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
        """Creates the connetion with the database"""
        
        try:
            conn = sqlite3.connect("scores.db")

            conn.execute(
                "CREATE TABLE scores (name VARCHAR PRIMARY KEY, wins INTEGER);"
            )
            conn.commit()
            conn.close()

        except sqlite3.DatabaseError:
            pass

    def updateTable(self):
        """Updates the database table"""

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
            pass

    def winnerUpdate(self):
        """"Exports the winner of the match to the database"""

        conn = sqlite3.connect("scores.db")

        query = f"UPDATE scores SET wins = wins + 1 WHERE name = '{self.winner[0]}';"

        conn.execute(query)
        conn.commit()
        conn.close()

    def getData(self, amount=0):
        """Import the data from the databse"""

        conn = sqlite3.connect("scores.db")

        cursor = conn.cursor()

        query = "SELECT * FROM scores ORDER BY wins DESC, name ASC;"

        cursor.execute(query)
        rows = cursor.fetchall()

        amount = len(rows) if len(rows) < amount else amount

        leader_board = []
        for i in range(amount):
            leader_board.append(rows[i])

        return leader_board
