with open("data.txt", "r") as file:
  seats = [(line.split('\n')[0]) for line in file]

# Part 1:
# I got this one pretty quickly by observing the data. 
# I found a few likely candidates and then calculated their ids.
# None started with "BBBBB", so I calculated the ids of the 4 that started with "BBBB"
# BBBBFFFLRR (120 * 8) + 3 = 963
# BBBBFFFLRL 
# BBBBFFFLLL
# BBBBFFFLLR

# ...but to solve part 2, I had to go back and do part 1 properly. :)

def split_characters(text): 
  return [char for char in text]  

seat_ledger = []
for seat in seats:
  row = 128
  column = 8
  for i, letter in enumerate(split_characters(seat)):
    if letter == "F":
      row = row - (2**(6 - i))
    elif letter == "L":
      if i == 7:
        column -= 4
      elif i == 8:
        column -= 2
      elif i == 9:
        column -= 1
  row -= 1
  column -=1
  id = (row * 8) + column
  seat_ledger.append(id)
  
print(f"The highest seat id is: {max(seat_ledger)}")

sorted_seats = sorted(seat_ledger)
for i, seat in enumerate(sorted_seats):
  if seat + 1 != sorted_seats[i + 1]:
    print(f"Your seat id is: {seat + 1}")
    break

