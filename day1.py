def parse_text_file():
  with open("day1input.txt", "r") as inputfile:
    line_nums = [line.strip().split('   ') for line in inputfile]
    left_list = [int(pairs[0]) for pairs in line_nums]
    right_list = [int(pairs[1]) for pairs in line_nums]
  return [left_list, right_list]

def calc_distance(sorted_left, sorted_right):
  # calc differences and sum
  if len(sorted_left) != len(sorted_right):
    print("PROBLEM! LIST LENGTHS DON'T MATCH")

  total_dif = 0
  for left_num, right_num in zip(sorted_left, sorted_right):
    total_dif += abs(left_num-right_num)
  return total_dif

def get_right_frequencies(right_list):
  frequencies = {}
  for num in right_list:
    if num in frequencies:
      frequencies[num] += 1
    else:
      frequencies[num] = 1
  return frequencies

def calc_similarity(sorted_left, right_frequencies):
  similarity = 0
  for num in sorted_left:
    if num not in right_frequencies:
      continue # essentially adding 0 by skipping operation
    similarity = similarity + (num * right_frequencies[num])
  return similarity

def day1_runner():
  lists = parse_text_file()

  sorted_left = sorted(lists[0])
  sorted_right = sorted(lists[1])

  total_distance = calc_distance(sorted_left, sorted_right)
  print(f'Total Distance = {total_distance}')

  right_frequencies = get_right_frequencies(sorted_right)
  similarity_score = calc_similarity(sorted_left, right_frequencies)
  print(f'Similarity = {similarity_score}')


if __name__ == "__main__":
  day1_runner()