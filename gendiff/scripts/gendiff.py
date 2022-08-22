#!/usr/bin/env/python3

from gendiff.gen_diff import generate_diff
import argparse


DESCRIPTION = "Compares two configuration files and shows the difference"


parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument('first_file',
                    type=str, metavar='first_file')
parser.add_argument('second_file',
                    type=str, metavar='second_file')
parser.add_argument('-f', '--format',
                    metavar='FORMAT',
                    default='json',
                    help='set format of output')


def main():
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
