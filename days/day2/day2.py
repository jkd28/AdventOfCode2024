def parse_input():
  with open("days/day2/day2input.txt") as inputfile:
    reports = [list(map(int, line.strip().split(' '))) for line in inputfile] # read line and convert all vals to int
  return reports

def report_is_safe(report):
  increasing = True
  for index, level in enumerate(report[:-1]):
    next_level = report[index + 1]
    difference = level - next_level

    # print (f'{level} and {next_level}')
    if index == 0:
      # initialize state for report (determine trending)
      if difference < 0:
        increasing = True
      elif difference > 0:
        increasing = False
      else:
        # no change is unsafe
        return False      
  
    if increasing and difference > 0:
      # should be increasing, but found a decrease
      return False
    if (not increasing) and difference < 0:
      # should be decreasing, but found an increase
      return False
    difference = abs(difference)
    if difference > 3 or difference < 1:
      # difference outside bounds
      return False
    
  # if we get here, we've got a safe report
  return True

def implement_problem_dampener(report):
  for index in range(len(report)):
    if report_is_safe(report[:index] + report[index+1:]):
      return True
  return False

def get_num_safe_reports(reports):
  num_safe_reports = 0
  for report in reports:
    if report_is_safe(report):
      num_safe_reports += 1
    else:
      if implement_problem_dampener(report):
        num_safe_reports += 1
  return num_safe_reports

if __name__ == "__main__":
  reports = parse_input()

  num_safe_reports = get_num_safe_reports(reports)
  print(f"Safe Reports: {num_safe_reports}")