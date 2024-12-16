from math import floor 


def process_input():
  dependency_map = {}
  updates = []
  with open("days/day5/day5input.txt", "r") as infile:
    for line in infile: 
      line = line.strip()
      if line == '':
        continue
      if "|" in line:
        # add to dependency map
        pages = line.split('|')
        page = pages[1]
        dependency = pages[0]
        
        if page not in dependency_map:
          dependency_map[page] = [dependency]
        else:
          dependency_map[page].append(dependency)
      else:
        # add to updates list
        updates.append(line.split(','))
  return dependency_map, updates

def is_valid_update(dependency_map, update):
  queued_pages = set()
  for page in update:
    if len(queued_pages) == 0:
      # first page will always be added 
      queued_pages.add(page)
      continue

    for dependency in dependency_map[page]:
      if dependency in update and dependency not in queued_pages:
        return False
    queued_pages.add(page)
  return True

def sum_middle_valid_updates(dependency_map, updates):
  sum = 0
  for update in updates:
    # check if update is valid
    if is_valid_update(dependency_map, update):
      middle_num = update[floor(len(update)/2)]
      sum += int(middle_num)
  return sum

        
        
      
      

if __name__ == "__main__":
  dependency_map, updates = process_input()
  sum = sum_middle_valid_updates(dependency_map, updates)
  print(f"Sum of middle nums is {sum}")
