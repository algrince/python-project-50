#!/usr/bin/env/python3


import argparse


DESCRIPTION = "Compares two configuration files and shows the difference"


parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument('first_file', type=str, metavar='first_file')
parser.add_argument('first_file', type=str, metavar='second_file')


def main():
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()