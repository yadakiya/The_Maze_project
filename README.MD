# Maze Generator and Solver using Python and Pygame

## Project Description

This project is a graphical maze generator and maze solver built using Python and the Pygame library.

The program performs two major tasks:

1. Generate a random rectangular maze
2. Automatically solve the maze

The maze is generated dynamically using a Depth-First Search (DFS) algorithm with a stack. A virtual “mouse” moves through the maze and removes walls between cells to create valid paths.

The solver then traverses the maze from the start cell to the end cell using another stack-based backtracking algorithm.

---

## Features

- Random maze generation
- Real-time maze drawing using Pygame
- Automatic maze solving
- Dead-end visualization
- Stack-based DFS traversal
- Backtracking algorithm
- Dynamic animation of maze creation and solving

---

## Project Structure

```text
project_folder/
│
├── main.py
├── maze.py
├── solver.py
├── README.md
```

---

## How the Maze Works

Each maze cell contains four walls:

- Top wall
- Right wall
- Bottom wall
- Left wall

Initially, every wall is intact.

The program removes walls between neighboring cells to create paths.

Because of the DFS algorithm, every cell becomes connected with exactly one valid path between any two cells, making it a proper maze.

---

## Data Structure

Each cell is represented using a class.

This project uses a Python dictionary-based wall system instead of separate `northWall` and `eastWall` arrays. Each cell stores its top, right, bottom, and left wall states using Boolean values.

```python
self.walls = {
    "top": True,
    "right": True,
    "bottom": True,
    "left": True
}
```

- `True` means the wall exists
- `False` means the wall has been removed

The maze itself is stored as a 2D grid:

```python
self.grid = [[Cell(r, c) for c in range(cols)] for r in range(rows)]
```

---

## Maze Generation Algorithm

The maze is generated using:

### Depth-First Search (DFS) with Stack

#### Steps

1. Start from the first cell
2. Mark it as visited
3. Check all neighboring cells
4. Choose one unvisited neighbor randomly
5. Remove the wall between the current cell and chosen neighbor
6. Push the current cell onto the stack
7. Move to the chosen neighbor
8. Repeat the process
9. If trapped in a dead end:
   - Pop a cell from the stack
   - Backtrack
10. Continue until all cells are visited

---

## Why Use a Stack?

A stack follows Last In First Out (LIFO) behavior.

This creates long winding paths and natural-looking mazes because the algorithm keeps exploring deeply before backtracking.

---

## Would a Queue Be Better?

No.

Using a queue would produce a very different maze.

### Stack (DFS)

- Creates long corridors
- Produces deep paths
- Generates complex mazes
- Better for maze appearance

### Queue (BFS)

- Expands evenly
- Produces short paths
- Maze looks less interesting
- More grid-like

That is why a stack is preferred.

---

## Maze Solving Algorithm

The maze is solved using another stack-based backtracking algorithm.

### Solver Steps

1. Start at the maze entrance
2. Move randomly to a valid neighboring cell
3. Push visited cells onto a stack
4. If a dead end is reached:
   - Mark the cell blue
   - Pop from the stack
   - Backtrack
5. Continue until reaching the destination

---

## Color Representation

| Color | Meaning |
|---|---|
| Black | Maze walls |
| Red | Current mouse position |
| Green | Correct path |
| Blue | Dead-end cells |
| White | Background |

---

## main.py Explanation

`main.py` controls:

- Pygame window
- Drawing the maze
- Drawing the solver
- Animation loop
- Event handling

It connects the maze generator and solver together.

---

## maze.py Explanation

`maze.py` contains:

### Cell Class

Represents each maze cell.

Stores:
- Position
- Walls
- Visited state

### Maze Class

Handles:
- Grid creation
- Neighbor checking
- Wall removal
- DFS maze generation

---

## solver.py Explanation

`solver.py` contains the solving algorithm.

It handles:
- Valid movement checking
- Stack-based traversal
- Backtracking
- Path storage
- Dead-end tracking

---

## Installation

### Install Python

Download Python from the official website:

https://www.python.org

---

### Install Pygame

Run:

```bash
pip install pygame
```

---

## How to Run

Open terminal in the project folder and run:

```bash
python main.py
```

---

## Output

The program will:

1. Generate a random maze
2. Display it graphically
3. Start solving automatically
4. Show:
   - Red moving solver
   - Blue dead ends
   - Green successful path

---

## Algorithms Used

| Part | Algorithm |
|---|---|
| Maze Generation | DFS + Stack |
| Maze Solving | Backtracking + Stack |

---

## Bonus Challenge (Cycles)

The assignment suggests adding extra random wall removals.

Example:

```python
if random.randint(1, 20) == 1:
```

This can create cycles inside the maze.

### Effect

- The maze is no longer a perfect tree
- Multiple paths may exist
- The “shoulder-to-the-wall” method may fail
- The maze becomes more challenging

---

## Complexity Analysis

### Maze Generation

Time Complexity:

```text
O(R × C)
```

Every cell is visited once.

### Maze Solving

Time Complexity:

```text
O(R × C)
```

The solver may visit every cell once.

---

## Learning Outcomes

This project helps understand:

- Depth-First Search (DFS)
- Backtracking
- Stack data structures
- Graph traversal
- Maze algorithms
- Pygame graphics
- Object-Oriented Programming
- Randomized algorithms

---

## Sample Commit History

Example GitHub commits:

```text
Initial project setup
Created Cell class
Implemented maze grid
Added DFS maze generation
Implemented wall removal
Implemented solver algorithm
Added backtracking
Added Pygame visualization
Added dead-end coloring
Final README update
```

---

## Loom Demonstration Checklist

### In the recording show:

#### Maze Generation

- Mouse removing walls dynamically
- Maze forming step-by-step

#### Maze Solver

- Red dot movement
- Blue dead ends
- Green final path

#### Bonus

- Extra wall removals
- Cycles inside maze
- Shoulder-rule discussion

---

## Conclusion

This project demonstrates how stacks and backtracking algorithms can be used to create and solve mazes dynamically.

The maze generation algorithm guarantees that every cell is reachable, while the solver efficiently explores paths and backtracks from dead ends until the correct route is found.

The project combines algorithms, data structures, and graphical visualization into an interactive application.