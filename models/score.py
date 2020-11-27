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

    @classmethod
    def from_json(self, json_file):
        with open(json_file, "r") as loadfile:
            data = json.load(loadfile)
            print(data)
            # self.player_name = 
            # for item in data.get("scores"):
            #     print(item)
            #     new_score = Score(item.get("name"), item.get("score"))
            #     self.add_score(new_score)

    @classmethod
    def from_dict(self, score_dict):
        self.change_name = score_dict.get("name")
        self.change_score = score_dict.get("score")
        self.change_date = score_dict.get("date")
        

    def to_dict(self):
        serial = {}
        serial["name"] = self.name
        serial["score"] = self.score
        serial["date"] = self.date
        return serial
        #change to work with from_json so that it doesn't use score

    def to_json(self):
        with open("scores.json", "w") as outfile:
            json.dump(self.to_dict(), outfile)

score = Score()

print(score.date)

print(score.to_dict())

score.to_json()

test_dic = score.to_dict()

print(test_dic)

score2 = Score("tom", 100, "never")

print(score2.to_dict())

score2.from_dict(test_dic)

print(score2.to_dict())