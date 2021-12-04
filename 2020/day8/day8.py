with open("data.txt", "r") as file:
  data = file.read().split('\n')

def parse_line(line):
  command = data[line][0:3]
  number = int(data[line][4:])
  return command, number

lines_seen = []
line, count = 0, 0

# while line not in lines_seen:
#   command, number = parse_line(line)
#   old_line = line
#   if command == "acc":
#     count += number
#     line += 1
#   elif command == "jmp":
#     print(f"jump to line {line + number}")
#     line += number
#   else:
#     line += 1
#   lines_seen.append(old_line)

# print(sorted(lines_seen))
# print(f"Count: {count}")

# 1767 is too low

while line < len(data):
  command, number = parse_line(line)
  if command == "jmp":
    print(f"jmp line: {line + 1}")
    command2, number2 = parse_line(line + 1)
    if command2 == "jmp" and (number2 + line) >= 633:
      print(f"Change line {line + 1} to nop")   
  elif command == "nop":
    print(f"nop line: {line + 1}")
    if (number + line) > len(data):
      print(f"Change line {line + 1} to jmp")
  line += 1
