from models.maze import Maze 
from controllers.game_start import GameStart
from flask import Flask, request, render_template
from models.database_manager import DatabaseManager
from models.score import Score
from models.score_manager import ScoreManager

# app = Flask(__name__)

# @app.route('/api/new', methods=["PUT"])
# def add_new_score():
#     try:
#         data = request.get_json()
#         manager = DatabaseManager("scores.db")
#         score = Score(data["name"], data["score"], data["date"])

#         manager.add(score)

#         manager.close()
#         return "", 204
#     except:
#         return "Invalid data provided.", 400

# # @app.route('/api/list', methods=["DELETE"])
# # def delete_score():
# #     try:
# #         data = request.get_json()
# #         score_manager.remove_score(data["name"])
# #         return "", 204
# #     except:
# #         return "Error", 400

# @app.route('/')
# def list_all_scores():
#   manager = DatabaseManager("scores.db")
#   scores = manager.get_all()
#   manager.close()

#   return render_template("list.html", scores=scores)

if __name__ == "__main__":
  """The method to run the program
  """

  game = GameStart("maze.txt")
  game.run()