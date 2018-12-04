from textwrap import dedent
import sys

WIDTH = 60
MENU = {
  'Appetizers': ['Poutine', 0, 'Jalapeno Poppers', 0, 'Hummus', 0],
  'Entrees': ['Salmon', 0, 'Steak', 0, 'Hamburger', 0],
  'Desserts': ['Cheesecake', 0, 'Chocolate Cake', 0, 'Peanut Butter Ice Cream', 0],
  'Drinks': ['Coffee', 0, 'Tea', 0, 'Beer', 0]
}
# I originally had a list of dictionaries, as in today's demo, but Scott advised me that a dictionary of lists
# (among other options) would be more iterable

def greeting():
  """Greets the user and provides instructions"""
  line_one = 'Welcome to the Snakes Cafe!'
  line_two = 'Please see our menu below.'
  line_three = ''
  line_four = 'To quit at any time, type "quit"'

  print(dedent(f'''
    {'*' * WIDTH}
    {('**' + ' ' * ((WIDTH - len(line_one)) // 2 - 2)) + line_one + (' ' * ((WIDTH - len(line_one)) // 2 - 2) + '**')}
    {('**' + ' ' * ((WIDTH - len(line_two)) // 2 - 2)) + line_two + (' ' * ((WIDTH - len(line_two)) // 2 - 2) + '**')}
    {('**' + ' ' * ((WIDTH - len(line_three)) // 2 - 2)) + line_three + (' ' * ((WIDTH - len(line_three)) // 2 - 2) + '**')}
    {('**' + ' ' * ((WIDTH - len(line_four)) // 2 - 2)) + line_four + (' ' * ((WIDTH - len(line_four)) // 2 - 2) + '**')}
    {'*' * WIDTH}
  '''))
  #Dedenting blatantly copied from the demo code

def display_menu():
  """Displays the menu of options by parsing the keys and lists of values within."""

  for item in MENU:
      print(item)
      print('-' * len(item))
      for j in range(len(MENU[item])):
        if j % 2 == 0:
          print(MENU[item][j])
      print('\n')
    # Because of the list structure, iterating by every other element grabs the named items

def order_prompt():
  """A simple display to prompt the user to order from the above menu."""

  prompt = 'What would you like to order?'

  print(dedent(f'''
  {'*' * WIDTH}
  {('**' + ' ' * ((WIDTH - len(prompt)) // 2 - 2)) + prompt + (' ' * ((WIDTH - len(prompt)) // 2 - 2) + '**')}
  {'*' * WIDTH}
  '''))

def order(user_order):
  """The user can input any item on the menu, which is then
  appropriately added to the dictionary so that the total of any
  individual item is tracked and output to the CLI"""

  if user_order.lower() == 'quit':
      exit()



  for item in MENU:
    for j in range(len(MENU[item])):
      if j % 2 == 0 and user_order == MENU[item][j].lower():
        MENU[item][j + 1] += 1
        if MENU[item][j + 1] == 1:
          print('\n', '**', MENU[item][j + 1], 'order of', MENU[item][j], 'has been added to your meal', '**', '\n')
        else:
          print('\n', '**', MENU[item][j + 1], 'orders of', MENU[item][j], 'have been added to your meal', '**', '\n')
        # Depending on whether the item has been ordered previously, the response looks a little different

def exit():
  """Calls the system exit function to break out of the loop when 'quit' is input into the CLI"""
  sys.exit()

def run():
  """A wrapper to contain the rest of the functions, called when the module is passed
  into the Python interpreter"""

  try:
    greeting()
    display_menu()
    order_prompt()
    while True: #probably dangerous, but it works
      order(input().lower())

  except KeyboardInterrupt:
      exit()


if __name__ == '__main__':
  run()
