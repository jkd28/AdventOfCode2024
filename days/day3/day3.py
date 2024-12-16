import re

def parse_instructions():
  regex = r"(don?'?t?\(\))|(mul\(\d{1,3},\d{1,3}\))"
  corrupted_mem = ""
  with open("days/day3/day3input.txt", "r", encoding="UTF-8") as infile:
    corrupted_mem = infile.read()

  # using capture groups creates a tuple, so 'do/don't' instructions are in group 0 
  # and 'mul' instructions are in group 1
  instructions = re.findall(regex, corrupted_mem)
  return instructions

def perform_instructions(instructions):
  sum = 0
  enabled = True
  for instruction in instructions:
    if instruction[0]:
      if instruction[0] == "don't()":
        enabled = False
      if instruction[0] == "do()":
        enabled = True
        
    elif instruction[1]:
      if enabled:
        nums = re.findall(r'\d{1,3}', instruction[1])
        sum += int(nums[0]) * int(nums[1])
  return sum

if __name__ == "__main__":
  instructions = parse_instructions()
  sum = perform_instructions(instructions)
  print(f"Sum: {sum}")