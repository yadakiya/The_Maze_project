import random

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col

        self.walls = {
            "top": True,
            "right": True,
            "bottom": True,
            "left": True
        }

        self.visited = False


class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(r, c) for c in range(cols)] for r in range(rows)]

    def get_neighbors(self, cell):
        neighbors = []

        directions = [
            (-1, 0, "top"),
            (1, 0, "bottom"),
            (0, -1, "left"),
            (0, 1, "right")
        ]

        for dr, dc, direction in directions:
            nr = cell.row + dr
            nc = cell.col + dc

            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                neighbor = self.grid[nr][nc]
                if not neighbor.visited:
                    neighbors.append((neighbor, direction))

        return neighbors

    def remove_wall(self, current, next_cell, direction):
        if direction == "top":
            current.walls["top"] = False
            next_cell.walls["bottom"] = False
        elif direction == "bottom":
            current.walls["bottom"] = False
            next_cell.walls["top"] = False
        elif direction == "left":
            current.walls["left"] = False
            next_cell.walls["right"] = False
        elif direction == "right":
            current.walls["right"] = False
            next_cell.walls["left"] = False

    def generate_maze(self):
        stack = []

        current = self.grid[0][0]
        current.visited = True

        while True:
            neighbors = self.get_neighbors(current)

            if neighbors:
                next_cell, direction = random.choice(neighbors)
                stack.append(current)

                self.remove_wall(current, next_cell, direction)

                current = next_cell
                current.visited = True

                #  BONUS: create cycles sometimes (1 in 20 chance)
                extra_neighbors = self.get_neighbors(current)
                if extra_neighbors and random.randint(1, 20) == 1:
                    extra_cell, extra_direction = random.choice(extra_neighbors)
                    self.remove_wall(current, extra_cell, extra_direction)

            elif stack:
                current = stack.pop()

            else:
                break