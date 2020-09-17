
from userInput import createGrid, getStartEnd

class Grid:

    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)] #  rdlu
    visited = []

    def __init__(self):
        self.grid, self.dims = createGrid()
        self.start, self.end = getStartEnd(self.dims)

    def __init__(self, grid, start, end, dims):
        self.grid = grid
        self.dims = dims
        self.start = start
        self.end = end

    def getChildren(self,currentPos):
        children = []

        for move in self.moves:
            x = move[0] + currentPos[0]
            y = move[1] + currentPos[1]
            if x < 0 or y < 0 or x >= self.dims[0] or y >= self.dims[1]:
                continue
            if (x, y) in self.visited:
                continue
            if self.grid[x][y] == 1:
                continue
            else:
                children.append((x, y))
        # print('Children of : ',currPos, ':', children)
        return children

    def getEnd(self):
        self.final_path = self.findEnd(self.start)
        print(self.final_path)
        return self.final_path

    def findEnd(self, currentPos):

        if currentPos == self.end:
            return [self.end]

        children = self.getChildren(currentPos)
        self.visited.append(currentPos)

        for ch in children:
            path = self.findEnd(ch)

            if path is not None:
                path.insert(0, currentPos)
                return path
