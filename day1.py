def parse_text_file():
  with open("day1input.txt", "r") as inputfile:
    line_nums = [line.strip().split('   ') for line in inputfile]
    left_list = [int(pairs[0]) for pairs in line_nums]
    right_list = [int(pairs[1]) for pairs in line_nums]
  return [left_list, right_list]

def day1_runner():
  # intake list
  lists = parse_text_file()

  # sort both lists
  sorted_left = sorted(lists[0])
  sorted_right = sorted(lists[1])

  # calc differences and sum
  if len(sorted_left) != len(sorted_right):
    print("PROBLEM! LIST LENGTHS DON'T MATCH")

  total_dif = 0
  for left_num, right_num in zip(sorted_left, sorted_right):
    total_dif = total_dif + abs(left_num-right_num)

  print(total_dif)

if __name__ == "__main__":
  day1_runner()