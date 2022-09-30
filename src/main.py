import argparse
import logging

from .api import max_profit

logging.basicConfig(level=logging.DEBUG, filemode='a', format='%(levelname)s:%(asctime)s:  %(message)s'
                    , datefmt='%Y-%d-%m %H:%M:%S')

def run_max_profit(args):
    args.name_list = tuple(args.name_list.split(','))
    max_profit(args)


parser = argparse.ArgumentParser(description='Process some algorithms')
subparsers = parser.add_subparsers(help='input function name for detail help')

max_profit_parser = subparsers.add_parser('max_profit', help='This is for max_profit algorithm')
max_profit_parser.add_argument('-input', help='The file path of input data file')
max_profit_parser.add_argument('-output', help='The file path of output data file.', default='output.txt')
max_profit_parser.add_argument('-name_list', help='The name of currencies. You can use "GBP,USD,EUR,JPY"', default='')
max_profit_parser.add_argument('-start', type=int, help='The index of starting currency', default=0)
max_profit_parser.add_argument('-end', type=int, help='The index of ending currency', default=0)
max_profit_parser.set_defaults(func=run_max_profit)

args = parser.parse_args()
args.func(args)
