import random

class Solver:
    def __init__(self, maze):
        self.maze = maze
        self.stack = []
        self.visited = set()

        self.current = maze.grid[0][0]
        self.end = maze.grid[maze.rows - 1][maze.cols - 1]

        self.visited.add((self.current.row, self.current.col))

        self.path = []
        self.dead_ends = []

    def get_moves(self, cell):
        moves = []

        row = cell.row
        col = cell.col

        if not cell.walls["top"] and (row - 1, col) not in self.visited:
            moves.append(self.maze.grid[row - 1][col])

        if not cell.walls["bottom"] and (row + 1, col) not in self.visited:
            moves.append(self.maze.grid[row + 1][col])

        if not cell.walls["left"] and (row, col - 1) not in self.visited:
            moves.append(self.maze.grid[row][col - 1])

        if not cell.walls["right"] and (row, col + 1) not in self.visited:
            moves.append(self.maze.grid[row][col + 1])

        return moves

    def step(self):
        if self.current == self.end:
            self.path = self.stack.copy()
            self.path.append(self.end)
            return True

        moves = self.get_moves(self.current)

        if moves:
            self.stack.append(self.current)

            next_cell = random.choice(moves)
            self.current = next_cell
            self.visited.add((self.current.row, self.current.col))

        elif self.stack:
            self.dead_ends.append(self.current)
            self.current = self.stack.pop()

        return False