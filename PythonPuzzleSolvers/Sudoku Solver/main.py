#Program that can solve Sudoku Boards using backtracking / recursion

#The layout of the board
board = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]  

#Function that will display the board
def print_board(board):
  if board is None:
    print("No Solution")
  for row in board:
    row_print = ""
    for value in row:
      row_print += str(value) + " "
    print(row_print)

#Function to find the next Zero in the puzzle
def find_zero(board):
  empty_cell = [] 
  for i in range(len(board)):
    for j in range(len(board[0])):
      
      if board[i][j] == 0:
       empty_cell.append(i)
       empty_cell.append(j)
       return empty_cell

#Function to check if the current value entered is valid by seeing if it's already
#In the corresponding row or column
def is_valid(board, row, col, value):

    for i in range(len(board)):
      if board[row][i] == value:
        return False
    
    for i in range(len(board)):
      if board[i][col] == value:
        return False
    
    x = (row//3)*3
    y = (col//3)*3
    for i in range(3):
      for j in range(3):
        if board[x+i][y+j] == value:
          return False
    return True     

def solve(board):
  #Find the Empty Cell
  empty_cell = find_zero(board)

  #If there is no empty cell you return the board, it is complete
  if empty_cell is None:
    return print_board(board)
    
  #Keep Track of the row and column of your empty cell
  row = empty_cell[0]
  col = empty_cell[1]
  
  #Try filling those with numbers from 1 to 9
  for value in range(1,10):
    if is_valid(board, row, col, value):
      board[row][col] = value
      solution = solve(board)
      if solution is not None:
        return solution
      board[row][col] = 0
  return None                                           



#Test case print outs
print(find_zero(board))
print(is_valid(board, 0 , 2 , 1 ))
print(is_valid(board, 0 , 2 , 7 ))
print(is_valid(board, 0 , 2 , 6 ))
print(is_valid(board, 3 , 5 , 2 ))

print("======================== Board Before Solve =====================")
print_board(board)
print("=================================================================")

print("======================== Board After Solve ======================")
solve(board)
print("=================================================================")