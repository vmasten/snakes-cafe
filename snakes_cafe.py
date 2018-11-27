from textwrap import dedent
import sys

WIDTH = 60
MENU = [
  {
    'appetizer': 'Poutine',
    'number_ordered': 0,
    'type': 'appetizer',
  },
  {
    'appetizer': 'Jalapeno Poppers',
    'number_ordered': 0,
    'type': 'appetizer'
  },
  {
    'appetizer': 'Hummus Plate',
    'number_ordered': 0,
    'type': 'appetizer'
  },
]

def greeting():
  """Function to greet the user
  """
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

def display_menu():
    print('Appetizers')
    print('----------')
    for item in MENU:
        if item['appetizer']:
            print(item['appetizer'])

def order_prompt():

    prompt = 'What would you like to order?'

    print(dedent(f'''
    {'*' * WIDTH}
    {('**' + ' ' * ((WIDTH - len(prompt)) // 2 - 2)) + prompt + (' ' * ((WIDTH - len(prompt)) // 2 - 2) + '**')}
    {'*' * WIDTH}
  '''))

def order(user_order):
    if user_order.lower() == 'quit':
        exit()

    for item in MENU:
      if item['appetizer'] == user_order:
        item['number_ordered'] += 1
        if item['number_ordered'] == 1:
          print('\n', '**', item['number_ordered'], 'order of', item['appetizer'], 'has been added to your meal', '**', '\n')
          return
        print('\n', '**', item['number_ordered'], 'orders of', item['appetizer'], 'have been added to your meal', '**', '\n')

def exit():
    sys.exit()

def run():
  greeting()
  display_menu()
  order_prompt()
  while True:
    order(input())


if __name__ == '__main__':
  run()
