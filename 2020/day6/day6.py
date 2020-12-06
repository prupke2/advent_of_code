import time
start_time = time.time()

with open("data.txt", "r") as file:
  data = file.read().split('\n\n')

# part 1
def split_characters(text): 
  return [char for char in text]  

def sum_of_yes_answers_in_groups(data):
  sum_of_yes_answers = 0
  for line in data:
    char_list, count = [], 0
    for char in split_characters(line):
      if char != '\n' and char not in char_list:
        char_list.append(char)
        count += 1
    sum_of_yes_answers += count
  print(f"Sum of unique yes answers in all groups: {sum_of_yes_answers}")

sum_of_yes_answers_in_groups(data)

# part 2
def sum_of_unanimous_yes_answers_in_groups(data):
  sum_of_unanimous_yes_answers = 0
  combined_char_set = set()
  for i, group in enumerate(data):
    forms = group.split('\n')
    combined_char_set.clear() # create a new set for each group of forms.
    for char in split_characters(forms[0]):
      combined_char_set.add(char) # Get the characters of the first form (to compare with the rest)
    forms.pop(0) # Remove the first form from the array
    char_list = compare_char_list(combined_char_set, forms) # Compare the first form to the rest
    sum_of_unanimous_yes_answers += char_list

  print(f"Sum of unanimous yes answers in all groups: {sum_of_unanimous_yes_answers}")

def compare_char_list(combined_char_set, forms):
  for i, form in enumerate(forms):
    if form == '':
      return len(combined_char_set)
    char_set = set()
    for char in split_characters(forms[i]):
      char_set.add(char)
    combined_char_set = combined_char_set.intersection(char_set)
  return len(combined_char_set)

sum_of_unanimous_yes_answers_in_groups(data)

seconds_elapsed = time.time() - start_time
print(f"{seconds_elapsed} s to compute.")
