import argparse

# python3 fromfile.py @args.txt

my_parser = argparse.ArgumentParser(fromfile_prefix_chars='@')

my_parser.add_argument('a',
                       help='a first argument')

my_parser.add_argument('b',
                       help='a second argument')

my_parser.add_argument('c',
                       help='a third argument')

my_parser.add_argument('d',
                       help='a fourth argument')

my_parser.add_argument('e',
                       type=int,
                       help='a fifth argument')

my_parser.add_argument('-v',
                       '--verbose',
                       action='store_true', # there is also 'store_false'
                       help='an optional argument')

# access by args.number
my_parser.add_argument('-n',
                       '--number',
                       metavar='MYNUM',
                       type=int,
                       action='store',
                       required=False,
                       default=42,
                       choices=range(1, 5),
                       help='an optional integer')

# Execute parse_args()
args = my_parser.parse_args()
print(args)
print('If you read this line it means that you have provided '
      'all the parameters')
