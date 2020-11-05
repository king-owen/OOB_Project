
class MazeView:

    def __init__(self, maze):
        self.maze = maze

    def display_maze(self):
        for i in self.maze.content:
            print(i)