import datetime, json

class Score:

    def __init__(self, name="", score=0, date=""):
        self.player_name = name
        self.score = 0
        current = datetime.datetime.now()
        self.date = "Date: {}, Time: {}".format(current.date(), current.time())

    @classmethod
    def from_json(self, json_file):
        with open(json_file, "r") as loadfile:
            data = json.load(loadfile)
            for item in data.get("scores"):
                print(item)
                new_score = Score(item.get("name"), item.get("score"))
                self.add_score(new_score)

    @classmethod
    def from_dict(self, score_dict):
        pass

    def to_dict(self):
        serial = {}
        serial[self.player_name] = [self.score, self.date]
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
