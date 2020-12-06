with open("data.txt", "r") as file:
  rows = [(line.split('\n')[0]) for line in file]

def count_trees_hit(move_right, move_down, trees_hit = 0):
  current_row, current_column = 0, 0
  for i, row in enumerate(rows):
    if i % move_down != 0:
      continue
    if current_row > (len(rows) - 1):
      return trees_hit
    if row[current_column] == "#":
      trees_hit += 1
    if move_down == 1:
      current_column = (((i + 1) * move_right) % 31)
    else:
      current_column = ((current_column + move_right) % 31)
    current_row += move_down
  return trees_hit

print(f"Part 1 trees hit: {count_trees_hit(3, 1)}")

# Part 2:

# Cases to test:
# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

case1 = count_trees_hit(1, 1)
case2 = count_trees_hit(3, 1)
case3 = count_trees_hit(5, 1)
case4 = count_trees_hit(7, 1)
case5 = count_trees_hit(1, 2)

print(f"\nPart 2 trees hit: \nCase 1: {case1} \nCase 2: {case2} \nCase 3: {case3} \nCase 4: {case4} \nCase 5: {case5}")
print(f"Product of tree hit count in all 5 cases: {case1 * case2 * case3 * case4 * case5}")


