# Sudoku-Solver
Simple sudoku solver made for my AI module in my first year of computer science at the university of bath.
This project implements a Sudoku solver using a constraint-based depth-first backtracking approach. The puzzle is modeled as a constraint satisfaction problem where each cell is a variable with a domain of values from 1 to 9, and constraints enforce uniqueness across rows, columns, and 3×3 subgrids.

The solver first validates the input grid to ensure there are no immediate rule violations. If the puzzle is invalid or unsolvable, it returns a grid filled with -1.

To improve efficiency, the algorithm uses the Minimum Remaining Values (MRV) heuristic, selecting the empty cell with the fewest legal values at each step. Valid values are tried recursively, with backtracking applied whenever a dead end is reached. Candidate values are attempted in a randomized order to reduce worst-case search behavior.

This approach guarantees a correct solution when one exists and reliably identifies unsolvable puzzles. While effective for standard Sudoku boards, performance may degrade on extremely difficult instances due to limited constraint propagation.
