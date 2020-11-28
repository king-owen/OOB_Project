from flask import Flask, request, render_template
from models.database_manager import DatabaseManager
from models.score import Score
from models.score_manager import ScoreManager

app = Flask(__name__)
score_manager = ScoreManager()
score_manager.from_json("project/scores.json")
database = "scores.db"

@app.route('/api/list')
def list_all_scores():
    # print("work")
    # manager = DatabaseManager(database)
    # scores = manager.get_all()
    # manager.close()

    return {"scores": score_manager.get_scores()}

@app.route('/api/new', methods=["PUT"])
def add_new_score():
    # try:
    #     data = request.get_json("project/scores.json")
    #     print(data)
    #     manager = DatabaseManager(database)
    #     score = Score(data["name"], data["score"], data["date"])

    #     manager.add(score)

    #     manager.close()
    #     return "", 204
    # except:
    #     return "Invalid data provided.", 400
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
    # try:
    #     data = request.get_json()
    #     score_manager.remove_score(data["name"])
    #     return "", 204
    # except:
    #     return "Error", 400
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
    # print("/ route")
    # manager = DatabaseManager(database)
    # scores = manager.get_all()
    # print(scores)
    # manager.close()
    scores = score_manager.get_scores()

    return render_template("list.html", scores=scores)

if __name__ == "__main__":
    print("main")
    app.run(debug=True)

#class has function record score
#passes score into api manager
#which sends to database