import pygame
import sys
from maze import Maze
from solver import Solver

pygame.init()

WIDTH = 800
HEIGHT = 600
ROWS = 20
COLS = 20
CELL_SIZE = 25

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

maze = Maze(ROWS, COLS)
maze.generate_maze()

# entrance & exit openings
maze.grid[0][0].walls["left"] = False
maze.grid[ROWS - 1][COLS - 1].walls["right"] = False

solver = Solver(maze)
solved = False


def draw_maze():
    for row in maze.grid:
        for cell in row:
            x = cell.col * CELL_SIZE
            y = cell.row * CELL_SIZE

            if cell.walls["top"]:
                pygame.draw.line(screen, BLACK, (x, y), (x + CELL_SIZE, y))
            if cell.walls["right"]:
                pygame.draw.line(screen, BLACK, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE))
            if cell.walls["bottom"]:
                pygame.draw.line(screen, BLACK, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE))
            if cell.walls["left"]:
                pygame.draw.line(screen, BLACK, (x, y), (x, y + CELL_SIZE))


def draw_solver():
    for cell in solver.dead_ends:
        x = cell.col * CELL_SIZE + CELL_SIZE // 2
        y = cell.row * CELL_SIZE + CELL_SIZE // 2
        pygame.draw.circle(screen, (0, 0, 255), (x, y), 5)

    for cell in solver.path:
        x = cell.col * CELL_SIZE + CELL_SIZE // 2
        y = cell.row * CELL_SIZE + CELL_SIZE // 2
        pygame.draw.circle(screen, (0, 255, 0), (x, y), 4)

    x = solver.current.col * CELL_SIZE + CELL_SIZE // 2
    y = solver.current.row * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 7)


running = True
while running:
    screen.fill(WHITE)

    draw_maze()
    draw_solver()

    if not solved:
        solved = solver.step()
        pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
sys.exit()