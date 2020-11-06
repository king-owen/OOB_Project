# Maze Game
## Developed by Brent Lee, Owen Andercheck, Rony Tran
  
# Description:
A Maze game created for ACIT 2515.
This game is implemented in OOP using Pygame and a MVC model.

# Project Structure:
 ```
OOB-Porject
 ┣ .git
 ┃ ┣ hooks
 ┃ ┃ ┣ applypatch-msg.sample
 ┃ ┃ ┣ commit-msg.sample
 ┃ ┃ ┣ fsmonitor-watchman.sample
 ┃ ┃ ┣ post-update.sample
 ┃ ┃ ┣ pre-applypatch.sample
 ┃ ┃ ┣ pre-commit.sample
 ┃ ┃ ┣ pre-push.sample
 ┃ ┃ ┣ pre-rebase.sample
 ┃ ┃ ┣ pre-receive.sample
 ┃ ┃ ┣ prepare-commit-msg.sample
 ┃ ┃ ┗ update.sample
 ┃ ┣ info
 ┃ ┃ ┗ exclude
 ┃ ┣ logs
 ┃ ┃ ┣ refs
 ┃ ┃ ┃ ┣ heads
 ┃ ┃ ┃ ┃ ┗ master
 ┃ ┃ ┃ ┗ remotes
 ┃ ┃ ┃ ┃ ┗ origin
 ┃ ┃ ┃ ┃ ┃ ┗ HEAD
 ┃ ┃ ┗ HEAD
 ┃ ┣ objects
 ┃ ┃ ┣ info
 ┃ ┃ ┗ pack
 ┃ ┃ ┃ ┣ pack-d7de05f570fc4f7c7064102583d2902af1a1ca4b.idx
 ┃ ┃ ┃ ┗ pack-d7de05f570fc4f7c7064102583d2902af1a1ca4b.pack
 ┃ ┣ refs
 ┃ ┃ ┣ heads
 ┃ ┃ ┃ ┗ master
 ┃ ┃ ┣ remotes
 ┃ ┃ ┃ ┗ origin
 ┃ ┃ ┃ ┃ ┗ HEAD
 ┃ ┃ ┗ tags
 ┃ ┣ config
 ┃ ┣ description
 ┃ ┣ HEAD
 ┃ ┣ index
 ┃ ┗ packed-refs
 ┣ .vscode
 ┃ ┗ .ropeproject
 ┃ ┃ ┗ config.py
 ┣ controllers
 ┃ ┣ game_move.py
 ┃ ┣ game_start.py
 ┃ ┗ __init__.py
 ┣ models
 ┃ ┣ maze.py
 ┃ ┣ player.py
 ┃ ┗ __init__.py
 ┣ sprites
 ┃ ┣ door.png
 ┃ ┣ key.png
 ┃ ┗ player.png
 ┣ tests
 ┃ ┣ controllers
 ┃ ┃ ┗ __init__.py
 ┃ ┣ models
 ┃ ┃ ┗ __init__.py
 ┃ ┣ views
 ┃ ┃ ┗ __init__.py
 ┃ ┗ __init__.py
 ┣ views
 ┃ ┣ maze_view.py
 ┃ ┗ __init__.py
 ┣ .gitattributes
 ┣ main.py
 ┣ maze.txt
 ┣ test_maze.py
 ┗ test_player.py
 ```
 
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
 
  
