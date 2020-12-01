with open("data.txt", "r") as file:
  numbers = [int(line.split('\n')[0]) for line in file] 

def print_answer_part_1(number, second_number):
  print("\nPART 1 ANSWER:\n" + str(number) + " and " + str(second_number) + " have a sum of 2020.")
  print("The product of these two numbers is " + str(number * second_number))

def print_answer_part_2(number, second_number, third_number):
  print("\nPART 2 ANSWER:\n" + str(number) + ", " + str(second_number) + ", and " + str(third_number) + " have a sum of 2020.")
  print("The product of these three numbers is " + str(number * second_number * third_number) + "\n")

def find_two_numbers(numbers):
  for index, number in enumerate(numbers):
    while index < (len(numbers) - 1):
      second_number = numbers[index + 1]
      if (number + second_number) == 2020:
        print_answer_part_1(number, second_number)
        return
      index += 1

def find_three_numbers(numbers):
  for index, number in enumerate(numbers):
    while index < (len(numbers) - 1):
      second_number = numbers[index + 1]
      inner_index = index
      # Since all the numbers are positive, don't bother checking 
      # if the first two already sum to >= 2020
      if (number + second_number) < 2020:
        while inner_index < (len(numbers) - 1):
          third_number = numbers[inner_index + 1] 
          if (number + second_number + third_number) == 2020:
            print_answer_part_2(number, second_number, third_number)
            return
          inner_index += 1
      index += 1

find_two_numbers(numbers)
find_three_numbers(numbers)
