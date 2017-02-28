"""
basic_arg_parsing.py

A bare-bones example of how to use the argparse library
 to create a script that can be invoked from the command line
 with a required argument

It's a simplified version of what is shown in the official
  documentation:

https://docs.python.org/3/library/argparse.html#example


Example usage from the command-line:

- Print out help message

    $ python hello_basic_arg_parsing.py --help


- Print greetings to 'world'

    $ python hello_basic_arg_parsing.py 'world'
    Hello, world
"""

import argparse

# Initialize the parser object
parser = argparse.ArgumentParser(description='My first command-line interface with parsed args!')

# add a single, required argument named `name`
parser.add_argument('name', type=str,
                     help='A name to deliver greetings to.')

args = parser.parse_args()
# the following assignment step is meant to emphasize
# how the 'name' argument we added to the `parser` object
#  is reflected in how the `args` object has a `.name` attribute
the_name = args.name

# This is what the command-line user sees:
print('Hello, ' + the_name)

