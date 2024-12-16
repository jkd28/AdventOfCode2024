def process_input():
  crossword = []
  with open("days/day4/day4input.txt", "r") as infile:
    for line in infile:
      crossword.append(list(line))
  return crossword

def find_xmas(crossword):
  occurrences = 0
  for y, row in enumerate(crossword):
    for x, col in enumerate(row):
      if col == "X":
        #try left
        if x >= 3 and crossword[y][x-1] == "M" and crossword[y][x-2] == "A" and crossword[y][x-3] == "S":
          occurrences += 1
        #try right
        if x <= len(row)-4 and crossword[y][x+1] == "M" and crossword[y][x+2] == "A" and crossword[y][x+3] == "S":
          occurrences += 1
        #try up
        if y >=3 and crossword[y-1][x] == "M" and crossword[y-2][x] == "A" and crossword[y-3][x] == "S":
          occurrences += 1
        #try down
        if y <= len(crossword)-4 and crossword[y+1][x] == "M" and crossword[y+2][x] == "A" and crossword[y+3][x] == "S":
          occurrences += 1
        
        # left-down diagonal
        if x >= 3 and y <= len(crossword)-4 and crossword[y+1][x-1] == "M" and crossword[y+2][x-2] == "A" and crossword[y+3][x-3] == "S":
          occurrences += 1
        # left-up diagonal
        if x >= 3 and y >=3 and crossword[y-1][x-1] == "M" and crossword[y-2][x-2] == "A" and crossword[y-3][x-3] == "S":
          occurrences += 1
        # right-down diagonal
        if x <= len(row)-4 and y <= len(crossword)-4 and crossword[y+1][x+1] == "M" and crossword[y+2][x+2] == "A" and crossword[y+3][x+3] == "S":
          occurrences += 1
        # right-up diagonal
        if x <= len(row)-4 and y >=3 and crossword[y-1][x+1] == "M" and crossword[y-2][x+2] == "A" and crossword[y-3][x+3] == "S":
          occurrences += 1
      else:
        continue
  return occurrences


def find_masxs(crossword):
  occurrences = 0
  for y, row in enumerate(crossword):
    for x, col in enumerate(row):
      if col == "A":
        if x >= 1 and y >= 1 and x <= len(row)-2 and y <= len(crossword)-2:
          up_right = crossword[y-1][x+1]
          down_right = crossword[y+1][x+1]
          up_left = crossword[y-1][x-1]
          down_left = crossword[y+1][x-1]
          
          if ((up_right == "M" and down_left == "S") or (up_right == "S" and down_left == "M")) and ((up_left == "M" and down_right == "S") or (up_left == "S" and down_right == "M")):
            occurrences += 1
  return occurrences
      

if __name__ == "__main__":
  crossword = process_input()
  xmas_occurrances = find_xmas(crossword)
  print(f"XMAS occurances: {xmas_occurrances}")
  
  mas_xs = find_masxs(crossword)
  print(f"MAS in an X occures {mas_xs} times")