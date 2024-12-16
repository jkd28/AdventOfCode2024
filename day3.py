import re

def parse_instructions():
  regex = r"mul\(\d{1,3},\d{1,3}\)"
  corrupted_mem = ""
  with open("day3input.txt", "r", encoding="UTF-8") as infile:
    corrupted_mem = infile.read()

  instructions = re.findall(regex, corrupted_mem)
  return instructions

def perform_instructions(instructions):
  sum = 0
  for instruction in instructions:
    nums = re.findall(r'\d{1,3}', instruction)
    sum += int(nums[0]) * int(nums[1])
  return sum

if __name__ == "__main__":
  instructions = parse_instructions()
  sum = perform_instructions(instructions)
  print(f"Sum: {sum}")