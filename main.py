from library import Library
from inputs import Inputs

program = Library()
print('Welcome to School Library App')

while True:
  program.display_menu()
  option = Inputs.input_number_range('Input choice ',int, 1, 7)
  print(option)
  if option == 7:
    break
  program.display_sub_menu(option)
  input('Press enter to continue')