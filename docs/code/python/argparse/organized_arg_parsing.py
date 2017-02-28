"""
organized_arg_parsing.py


Same as more_arg_parsing.py, but refactored and organized in more of a
  "best practices" way

This includes the use of the `if __name__ == '__main__'`` convention,
  which allows us to specify how the script should behave when
  it is called from the command line, and when it is imported into
  another script as a module (or interactive Python shell)

The extra organization allows for more flexibility.

Example usage from command-line:

  $ python organized_arg_parsing.py 'Sally smith'
  Hello, Sally smith!

Example usage in ipython:

  >>> import organized_arg_parsing
  >>> better_arg_parsing.foo_greetings('John Doe')
  Hello, John Doe!
"""


import argparse


def foo_greetings(recipient_name):
  """
  `recipient_name` is a string

  Return value:
    a string
  """
  greeting_str = 'Hello, {}!'.format(recipient_name)
  return greeting_str



if __name__ == '__main__':
  # this only runs if this script is invoked from the command line:
  parser = argparse.ArgumentParser(description='More fun with optional args!')
  parser.add_argument('name', type=str,
                          help='A name to deliver greetings to.')
  parser.add_argument('--number', type=int,
                          default=1,
                          help='The number of times to deliver greetings.')

  args = parser.parse_args()
  # make the greeting string
  gtext = foo_greetings(args.name)

  for i in range(args.number):
      print(gtext)

