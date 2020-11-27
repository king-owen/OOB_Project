import sqlite3
from .score import Score

class DatabaseManager:

    def __init__(self, filename):
        self._db = sqlite3.connect(filename)
        self._cursor = self._db.cursor()
        
        self._cursor.execute('SELECT name from sqlite_master where type="table"')
        res = self._cursor.fetchone()
        if not res or "scores" not in res:
            print("creating table")
            self._cursor.execute("CREATE TABLE scores (name TEXT NOT NULL,score INTEGER NOT NULL,date TEXT NOT NULL)")
            self._db.commit()

    def add(self, score):
        self._cursor.execute("INSERT INTO scores (name, score, date) VALUES (?, ?, ?)", (score.name, (int)(score.score), score.date))
        self._db.commit()
            
    def close(self):
        self._db.close()

    def get_all(self):
        scores_list = []
        self._cursor.execute("SELECT name, score, date FROM scores ORDER BY score DESC")
        for data in self._cursor.fetchall():
            score = Score(data[0], data[1], data[2])
            dict_score = score.to_dict()
            scores_list.append(dict_score)
        return scores_list

    def remove_by_name(self, name):
        self._cursor.execute("DELETE FROM scores WHERE name='{}'".format(name.get("name")))
        self._db.commit()
