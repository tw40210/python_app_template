import argparse
import logging

from .api import max_profit




logging.basicConfig(level=logging.DEBUG, filemode='a', format='%(levelname)s:%(asctime)s:  %(message)s'
                    , datefmt='%Y-%d-%m %H:%M:%S')

def run_max_profit(args):
    args.name_list = tuple(args.name_list.split(','))
    max_profit(args)


parser = argparse.ArgumentParser(description='Process some integers.')
subparsers = parser.add_subparsers(help='sub-command help')

max_profit_parser = subparsers.add_parser('max_profit', help='a help')
max_profit_parser.add_argument('-input', help='foo help')
max_profit_parser.add_argument('-output', help='foo help', default='output.txt')
max_profit_parser.add_argument('-name_list', help='foo help', default='')
max_profit_parser.add_argument('-start', type=int, help='foo help', default=0)
max_profit_parser.add_argument('-end', type=int, help='foo help', default=0)
max_profit_parser.set_defaults(func=run_max_profit)

args = parser.parse_args()
args.func(args)
