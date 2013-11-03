def print_grid(grid):
  """Print tic tac toe grid."""
  print " ",grid[0][0]," | ",grid[0][1]," | ",grid[0][2]
  print "-----------------"
  print " ",grid[1][0]," | ",grid[1][1]," | ",grid[1][2]
  print "-----------------"
  print " ",grid[2][0]," | ",grid[2][1]," | ",grid[2][2]

def has_win(grid):
  """Return the char of the winning player o ' ' otherwise."""
  #cols
  if grid[0][0] == grid[0][1] == grid[0][2] != ' ':
    return grid[0][0]
  if grid[1][0] == grid[1][1] == grid[1][2] != ' ':
    return grid[1][0]
  if grid[2][0] == grid[2][1] == grid[2][2] != ' ':
    return grid[2][0]
  #rows
  if grid[0][0] == grid[1][0] == grid[2][0] != ' ':
    return grid[0][0]
  if grid[0][1] == grid[1][1] == grid[2][1] != ' ':
    return grid[0][1]
  if grid[0][2] == grid[1][2] == grid[2][2] != ' ':
    return grid[0][2]
  #diags
  if grid[0][0] == grid[1][1] == grid[2][2] != ' ':
    return grid[0][0]
  if grid[0][2] == grid[1][1] == grid[2][0] != ' ':
    return grid[0][2]
  return ' '

def valid_move(grid,j,i):
  """Return true if [j,i] is a valid move"""
  if j > 2 or i > 2 or j < 0 or i < 0:
    return False
  if grid[j][i] == ' ':
    return True
  return False

def game_over(grid):
  """Return true if game is over"""
  for j in range(0,3):
    for i in range(0,3):
      if grid[j][i] == ' ':
        return False
  return True

def valid_input(i):
  """Return true if i is a valid input"""
  if i >= 0 and i <= 2:
    return True
  return False

def user_input():
  """Ask user for a move"""
  j = ord(raw_input("Row: "))-48
  while not valid_input(j):
    j = ord(raw_input("Row: "))-48
  i = ord(raw_input("Col: "))-48
  while not valid_input(i):
    i = ord(raw_input("Col: "))-48
  return j,i

def AI(grid,computer,player):
  return 1,1 
  #TODO


grid = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
player = 'x'
computer = 'o'
while not game_over(grid):
  move = user_input()
  while not valid_move(grid,move[0],move[1]):
    move = user_input()
  grid[move[0]][move[1]] = player
  print_grid(grid)
  compMove = AI(grid,computer,player)
  grid[compMove[0]][compMove[1]] = computer
  print_grid(grid)



