class Grid:

    def __init__(self, size):
        self.size = size
        self.contents = [[[] for row in range(size)] for column in range(size)]

    def get(self):
        for block in self.contents: print(block)



