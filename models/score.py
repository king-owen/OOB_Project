import datetime, json

class Score:

    def __init__(self):
        self.player_name = ""
        self.score = 0
        self.date = datetime.datetime.now()

    @classmethod
    def from_json(self, json_file):
        with open(json_file, "r") as loadfile:
            data = json.load(loadfile)
            for item in data.get("scores"):
                new_score = Score(item.get("name"), item.get("score"))
                self.add_score(new_score)

    @classmethod
    def from_dict(self):
        pass

    def to_dict(self):
        serial = {}
        serial["scores"] = self.get_scores()
        return serial
        #change to work with from_json so that it doesn't use score

    def to_json(self, json_file):
        with open(json_file, "w") as outfile:
            json.dump(self.serialize(), outfile)

score = Score()

print(score.date)
