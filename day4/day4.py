import re
import time

start_time = time.time()
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def scan_all_passports(part):
  with open("data.txt", "r") as file:
    file = file.read().strip()
  passports = file.split('\n\n')
  valid_passports = 0
  for i, passport in enumerate(passports):
    passport = passport.replace('\n', ' ')
    valid_passports += check_passport(passport, part)
  seconds_elapsed = time.time() - start_time
  print(f"\nNumber of valid passports in part {part}: {valid_passports}")
  print(f"{seconds_elapsed} s to compute.")

def check_passport(passport, part):
  if part == 1:
    return all(1 if field in passport else 0 for field in required_fields)
  for field in required_fields:
    if field not in passport:
      return 0
  for field in required_fields:
    valid = verify_field(passport, field)
    if valid == 0:
      return 0
  return 1

def verify_field(passport, field):
  field_string_start = passport.find(field)
  data_string_start = passport.find(":", field_string_start) + 1
  data_string_end = passport.find(" ", data_string_start)
  if data_string_end == -1:
    data = passport[data_string_start:]
  else:
    data = passport[data_string_start:data_string_end]
  if field == "byr":
    return 1 if 1920 <= int(data) <= 2002 else 0
  elif field == "iyr":
    return 1 if 2010 <= int(data) <= 2020 else 0
  elif field == "eyr": 
    return 1 if 2020 <= int(data) <= 2030 else 0
  elif field == "hgt":
    unit = data.find("cm")
    if unit == -1:
      unit = data.find("in")
      value = data[0:unit]
      return 1 if 59 <= int(value) <= 76 else 0
    else:   
      value = data[0:unit]
      return 1 if 150 <= int(value) <= 193 else 0
  elif field == "hcl":
    return 1 if re.search("^#(?:[0-9a-fA-F]{3}){1,2}$", data) else 0
  elif field == "ecl":
    return 1 if data in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] else 0
  elif field == "pid":
    return 1 if re.search("^[0-9]{9}$", data) else 0

scan_all_passports(1)
scan_all_passports(2)
