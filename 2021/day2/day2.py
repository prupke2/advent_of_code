with open("data.txt", "r") as file:
  data = [(line.split('\n')[0]) for line in file]

def extract_command(row):
  if row[:7] == "forward":
    return "forward", int(row[8:])
  if row[:2] == "up":
    return "up", int(row[3:])
  if row[:4] == "down":
    return "down", int(row[5:])

horizontal = 0
depth = 0
for row in data:
  command, value = extract_command(row)
  if command == "forward":
    horizontal += value
  elif command == "up":
    depth -= value
  elif command == "down":
    depth += value

print(f"horizontal: {horizontal}, depth: {depth}")
print(f"multiplied: {horizontal * depth}")

horizontal = 0
depth = 0
aim = 0
for row in data:
  command, value = extract_command(row)
  if command == "forward":
    horizontal += value
    depth += (value * aim)
  elif command == "up":
    aim -= value
  elif command == "down":
    aim += value

print(f"horizontal: {horizontal}, depth: {depth}")
print(f"multiplied: {horizontal * depth}")
