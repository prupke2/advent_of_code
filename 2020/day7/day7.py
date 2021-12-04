with open("data.txt", "r") as file:
  data = file.read().split('\n')

colors_holding_gold_bags = set()
def find_color(data, color):
  for line in data:
    if color in line:
      first_bag = line.find("bags")
      colors_holding_gold_bags.add(line[0:(first_bag - 1)])

find_color(data, "shiny gold") # start by finding the bags that can hold shiny gold bags directly

colors = set() # create a new set since you can't modify a set while iterating
def find_bags(colors):
  for color in colors_holding_gold_bags:
    colors.add(color)
  count = len(colors)
  for color in colors:
    find_color(data, color)
  if len(colors_holding_gold_bags) == count: # when these are equal, there are no more new colors to check
    print(f"Total bags: {len(colors_holding_gold_bags) - 1}") # subtract one for shiny gold bags themselves
    return
  find_bags(colors)

find_bags(colors) # call this recursive function to find all bags

# part 2

shiny_gold_bags_set = {"light chartreuse": 2, "drab black": 2, "bright orange": 1, "shiny teal": 1}

def get_containing_bags_part_2(color):
  for line in data:
    new_colors = {}
    if line[0:len(color)] == color:
      number = line.find("contain") + 8
      color_start = number + 2
      color_end = line.find("bag", number)
      color = line[color_start:color_end - 1]
      new_colors[color] = line[number]
      print(f"new_colors: {new_colors}")
      return new_colors
  return line

colors = {}
def find_bags_part_2(colors):
  for color, value in colors.items():
    if color not in shiny_gold_bags_set:
      shiny_gold_bags_set[color] = value
    else:
      shiny_gold_bags_set[color] += value
      new_colors = get_containing_bags_part_2(color)
      find_bags_part_2(new_colors)
  print(f"colors: {shiny_gold_bags_set}")

find_bags_part_2(colors)
