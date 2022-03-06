import re

class Inputs:
  def input_number(prompt, function):
    while True:
      user_input = input(prompt)
      try:
        user_input = function(user_input)
        break
      except ValueError:
        print('Please enter a number')
      
    return user_input
    
  def input_number_range(prompt, function, min_value, max_value):
    while True:
      user_input = Inputs.input_number(prompt,function)
      if user_input < min_value or user_input > max_value:
        print('Invalid option')
        continue
      break
    return user_input
    
  def input_string(prompt, min_lenght, max_length):
    while True:
      user_input = input(prompt)
      if len(user_input) < min_lenght or len(user_input) > max_length:
        print(f"Your value must be within {min_lenght} to {max_length} characters")
        continue
      break
    return user_input
  
  def input_string_alphabets(prompt, min_lenght, max_length):
    while True:
      user_input = input(prompt)
      if re.search("[0-9]", user_input):
        print('Your value must only contain alphabets')
      if len(user_input) < min_lenght or len(user_input) > max_length:
        print(f"Your value must be within {min_lenght} to {max_length} characters")
        continue
      break
    return user_input
  
  def input_bool(prompt):
    while True:
      user_input = input(prompt)
      user_input = user_input.lower()
      if user_input != 'y' and user_input != 'n' :
        print('Please choose a valid option')
        continue
      break
    return user_input == 'y'
    