# Backtracking

maze = [["S", ".", ".","."],
        [".","x","x","."],
        [".",".",".","x"],
        ["x","x",".","E"]]


def print_maze(maze):
  for row in maze:
    row_print = ""
    for value in row:
      row_print += value + " "
    print(row_print)



def solve_maze(maze):
  if len(maze) < 1:
    return None
  if len(maze[0]) < 1:
    return None
  
  return solve_maze_helper(maze, [], 0, 0)


def solve_maze_helper(maze, solution, pos_row, pos_col):
  # Get the Size of the maze both rows and columns
  num_row = len(maze)
  num_col = len(maze[0])

  # Base cases   

  # Robot is already home  
  if pos_row == num_row - 1 and pos_col == num_col -1:
    return solution
  
  # Is the robot out of bounds?
  if pos_row >= num_row or pos_col >= num_col:
    return None
  
  # Is robuddy on an obstacle?
  if maze[pos_row][pos_col] == 'x':
    return None

  # Recursive case

  #Try going right
  solution.append("r")
  solution_going_right = solve_maze_helper(maze,solution,pos_row, pos_col +1)
  if solution_going_right is not None:
    return solution_going_right
  
  # Going Right Doesn't Work, Backtrack
  solution.pop()
  solution.append("d")
  solution_going_down = solve_maze_helper(maze,solution,pos_row +1, pos_col)
  if solution_going_down is not None:
    return solution_going_down
  
  # No solution, impossible, Backtrack
  solution.pop()
  return None

print_maze(maze)
print(solve_maze(maze))