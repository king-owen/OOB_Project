from flask import Flask, request, render_template
from models.score import Score
from models.score_manager import ScoreManager
import os

app = Flask(__name__)
score_manager = ScoreManager()
score_manager.from_json("../scores.json")

@app.route('/api/list')
def list_all_scores():
    return {"scores": score_manager.get_scores()}

@app.route('/api/new', methods=["PUT"])
def add_new_score():
    try:
    #-- get the JSON data of the request, containing a new object to add        
        data = request.get_json()
        if ("name" in data) and ("score" in data):
            new_score = Score(data.get("name"), data.get("score"), data.get("date"))
            score_manager.add_score(new_score)
            return"", 204 
        else:
            return"Invalid data provided.", 400
    except:
        return"Invalid data provided.", 400

@app.route('/api/list', methods=["DELETE"])
def delete_score():
    try:
        #-- get the JSON data of the request, containing an object to remove       
        data = request.get_json()
        name = "name"
        delete = []

        if name in data:
            for key in score_manager._scores.keys():

                if key == data.get("name"):
                    delete.append(key)

            for i in delete:
                del score_manager._scores[i]

        return"", 204 

    except:
        return"Invalid data provided.", 400


@app.route('/')
def list_all_scores_html():
    scores = score_manager.get_scores()
    sorted_scores = []
    for count, item in enumerate(scores):
        next_score = item
        for count2, item2 in enumerate(scores):
            if (item2.get("score")) > (next_score.get("score")):
                next_score = item2
                count = count2
        scores.pop(count)
        sorted_scores.append(next_score)
    full_sort = sorted_scores + scores

    return render_template("list.html", scores=full_sort)

if __name__ == "__main__":
    print("main")
    app.run(debug=True)

#class has function record score
#passes score into api manager
#which sends to database