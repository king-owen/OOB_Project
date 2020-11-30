import datetime, json

class Score:

    current = datetime.datetime.now()

    def __init__(self, _name="", _score=0, _date="Date: {}, Time: {}".format(current.date(), current.time())):
        self._player_name = _name
        self._score = _score
        self._date = _date

    @property
    def change_name(self, name):
        self._player_name = name

    @property
    def change_score(self, score):
        self._score = score

    @property
    def change_date(self, date):
        self._date = date

    @property
    def name(self):
        return self._player_name

    @property
    def score(self):
        return self._score

    @property
    def date(self):
        return self._date

    def to_dict(self):
        score_dict = {}
        score_dict["name"] = self.name
        score_dict["score"] = self.score
        score_dict["date"] = self.date
        return score_dict