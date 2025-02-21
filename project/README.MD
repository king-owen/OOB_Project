# Maze Game
## Developed by Brent Lee, Owen Andercheck, Rony Tran
  
# Description:
A Maze game created for ACIT 2515.
This game is implemented in OOP using Pygame and a MVC model.

# Project Structure:
 ```
OOB_Project
 ┣ project
 ┃ ┣ documentation
 ┃ ┃ ┗ Report.pdf
 ┃ ┣ maze
 ┃ ┃ ┣ controllers
 ┃ ┃ ┃ ┣ game_move.py
 ┃ ┃ ┃ ┣ game_start.py
 ┃ ┃ ┃ ┗ __init__.py
 ┃ ┃ ┣ documentation
 ┃ ┃ ┃ ┗ uml.pdf
 ┃ ┃ ┣ models
 ┃ ┃ ┃ ┣ maze.py
 ┃ ┃ ┃ ┣ player.py
 ┃ ┃ ┃ ┣ score.py
 ┃ ┃ ┃ ┣ score_manager.py
 ┃ ┃ ┃ ┗ __init__.py
 ┃ ┃ ┣ sprites
 ┃ ┃ ┃ ┣ door.png
 ┃ ┃ ┃ ┣ key.png
 ┃ ┃ ┃ ┣ player.png
 ┃ ┃ ┃ ┣ wall.png
 ┃ ┃ ┃ ┗ __init__.py
 ┃ ┃ ┣ tests
 ┃ ┃ ┃ ┣ controllers
 ┃ ┃ ┃ ┃ ┣ maze.txt
 ┃ ┃ ┃ ┃ ┣ test_game_move.py
 ┃ ┃ ┃ ┃ ┣ test_game_start.py
 ┃ ┃ ┃ ┃ ┗ __init__.py
 ┃ ┃ ┃ ┣ models
 ┃ ┃ ┃ ┃ ┣ maze.txt
 ┃ ┃ ┃ ┃ ┣ test_maze.py
 ┃ ┃ ┃ ┃ ┣ test_player.py
 ┃ ┃ ┃ ┃ ┣ test_score.py
 ┃ ┃ ┃ ┃ ┣ test_score_manager.py
 ┃ ┃ ┃ ┃ ┗ __init__.py
 ┃ ┃ ┃ ┣ views
 ┃ ┃ ┃ ┃ ┣ test_maze_view.py
 ┃ ┃ ┃ ┃ ┗ __init__.py
 ┃ ┃ ┃ ┗ __init__.py
 ┃ ┃ ┣ views
 ┃ ┃ ┃ ┣ maze_view.py
 ┃ ┃ ┃ ┗ __init__.py
 ┃ ┃ ┣ main.py
 ┃ ┃ ┣ maze.txt
 ┃ ┃ ┣ README.MD
 ┃ ┃ ┗ __init__.py
 ┃ ┣ web
 ┃ ┃ ┣ models
 ┃ ┃ ┃ ┣ score.py
 ┃ ┃ ┃ ┗ score_manager.py
 ┃ ┃ ┣ templates
 ┃ ┃ ┃ ┣ base.html
 ┃ ┃ ┃ ┗ list.html
 ┃ ┃ ┣ app.py
 ┃ ┃ ┣ test_app.py
 ┃ ┃ ┗ __init__.py
 ┃ ┣ scores.json
 ┃ ┗ __init__.py
 ```
 # How to test the Code:
 Python and Pytest(pip install pytest in the terminal) are required to test the code
 1. Open Command Prompt/Terminal
 2. Change directory to the downloaded folder
 3. Change directory to the test folder
 4. Type Pytest *filename* to test the file.
 
 # How to run the Code:
  - [Python](https://www.python.org/) and Pygame(pip install pygame in the terminal) and a Virtual Enviroment is required to run this code.

 1. Download all the content to a folder.
 2. Open Command Prompt (CMD)
 3. Change Directory to the downloaded folder.
 4. Input python main.py
 5. Pygame now runs the code.
 
 # How to Control the game:
 1. Use WASD to move:
    - W to move the Player Up.
    - A to move the Player Left.
    - S to move the Player Down.
    - D to move the Player Right.
 2. Collect all 4 of the items by moving over them.
 3. Head towards the exit with all 4 items to win the game.
 
  
