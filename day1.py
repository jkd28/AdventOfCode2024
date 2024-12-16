def parse_text_file():
  with open("day1input.txt", "r") as inputfile:
    line_nums = [line.strip().split('   ') for line in inputfile]
    # print(line_nums)
    list1 = [pairs[0] for pairs in line_nums]
    list2 = [pairs[1] for pairs in line_nums]
  return [list1, list2]

def day1_runner():
  # intake list
  lists = parse_text_file()

  # sort both lists
  sorted1 = sorted(lists[0])
  sorted2 = sorted(lists[1])
  print(sorted1)

  # calc differences and sum
  if len(sorted1) =! len(sorted2):
    print("PROBLEM! LIST LENGTHS DON'T MATCH")


if __name__ == "__main__":
  day1_runner()