import datetime, json

class Score:

    def __init__(self, _name="", _score=0, _date=""):
        self._player_name = name
        self._score = score
        current = datetime.datetime.now()
        self._date = "Date: {}, Time: {}".format(current.date(), current.time())

    @property
    def change_name(self, name):
        self.player_name = name

    @property
    def change_score(self, score):
        self.score = score

    @property
    def change_date(self, date):
        self.date = date

    @property
    def name(self):
        return self._name

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
        pass

    def to_dict(self):
        serial = {}
        serial["name"] = self.player_name
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

score.from_json("scores.json")
