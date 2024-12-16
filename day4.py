def process_input():
  crossword = []
  with open("day4input.txt", "r") as infile:
    for line in infile:
      crossword.append(list(line))
  return crossword

if __name__ == "__main__":
  crossword = process_input()
  print(crossword)