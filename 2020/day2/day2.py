with open("data.txt", "r") as file:
  data = [(line.split('\n')[0]) for line in file]

valid_passwords = 0
for row in data:
  values = row.split(' ')
  bounds = values[0].split('-')
  min, max = int(bounds[0]), int(bounds[1])
  target = values[1][-2]
  password = values[2]
  count = password.count(target)
  if min <= count <= max:
    valid_passwords += 1

print("Valid password count for part 1: " + str(valid_passwords))

# Part 2
valid_passwords = 0
for row in data:
  values = row.split(' ')
  rows_to_check = values[0].split('-')
  first_row_to_check, second_row_to_check = int(rows_to_check[0]) - 1, int(rows_to_check[1]) - 1
  target = values[1][-2]
  password = values[2]
  first_match = password[first_row_to_check] == target
  second_match = password[second_row_to_check] == target
  if ((first_match or second_match) and not (first_match and second_match)):
    valid_passwords += 1

print("Valid password count for part 2: " + str(valid_passwords))

