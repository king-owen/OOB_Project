from flask import Flask, request, render_template
from OOB-Porject.assignment_demo.models.database_manager import DatabaseManager
from OOB-Porject.assignment_demo.models.score import Score
from OOB-Porject.assignment_demo.models.score_manager import ScoreManager

app = Flask(__name__)

@app.route('/api/list')
def list_all_scores():
    print("work")
    manager = DatabaseManager("scores2.db")
    scores = manager.get_all()
    manager.close()

    return {"scores": scores}

@app.route('/api/new', methods=["PUT"])
def add_new_score():
    try:
        data = request.get_json()
        manager = DatabaseManager("scores2.db")
        score = Score(data["name"], data["score"], data["date"])

        manager.add(score)

        manager.close()
        return "", 204
    except:
        return "Invalid data provided.", 400

# @app.route('/api/list', methods=["DELETE"])
# def delete_score():
#     try:
#         data = request.get_json()
#         score_manager.remove_score(data["name"])
#         return "", 204
#     except:
#         return "Error", 400

@app.route('/')
def list_all_scores_html():
    print("also")
    manager = DatabaseManager("scores2.db")
    scores = manager.get_all()
    print(scores)
    manager.close()

    return render_template("list.html", scores=scores)

if __name__ == "__main__":
    print("here")
    app.run(debug=True)

#class has function record score
#passes score into api manager
#which sends to database