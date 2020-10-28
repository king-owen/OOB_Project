class Maze:
        def __init__(self,filename):
        with open(filename, 'r') as inputfile:
            self.content = inputfile.readlines()
