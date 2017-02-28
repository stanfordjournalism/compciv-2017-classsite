"""
more_arg_parsing.py

A slightly more complicated version of basic_arg_parsing.py

Besides some refactoring, the additional feature shown here is how
 to create a command-line interface that has an optional argument


Example usage from the command-line:

- Print out help message

    $ python more_arg_parsing.py --help


- Print greetings to 'world' a single time:

    $ python more_arg_parsing.py 'world'
    Hello, world


- Print greetings to 'Leland Stanford, Jr.', 3 times in a row:

    $ python more_arg_parsing.py 'Leland Stanford, Jr.' --number 3
      Hello, Leland Stanford, Jr.
      Hello, Leland Stanford, Jr.
      Hello, Leland Stanford, Jr.
"""

import argparse

parser = argparse.ArgumentParser(description='More fun with optional args!')
parser.add_argument('name', type=str,
                        help='A name to deliver greetings to.')
parser.add_argument('--number', type=int,
                        default=1,
                        help='The number of times to deliver greetings.')

args = parser.parse_args()
number_of_repetitions = range(args.number)
greeting_string = 'Hello, {}'.format(args.name)

for i in number_of_repetitions:
    print(greeting_string)

