with open("data.txt", "r") as file:
  numbers = [int(line.split('\n')[0]) for line in file] 

def compare_numbers(number1, number2):
  return True if number2 > number1 else False

total = 0
for i, number in enumerate(numbers):
  if i >= len(numbers) - 1:
    continue
  if compare_numbers(numbers[i], numbers[i+1]) == True:
    total += 1

print(f"Part 1 total: {total}")

def compare_sums(number1, number2, number3, number4):
  return compare_numbers(number1 + number2 + number3, number2 + number3 + number4)

total = 0
for i, number in enumerate(numbers):
  if i >= (len(numbers) - 3):
    continue
  if compare_sums(numbers[i], numbers[i+1], numbers[i+2], numbers[i+3]) == True:
    total += 1

print(f"Part 2 total: {total}")
