#!/usr/bin/env python3
import argparse
from gendiff.makediff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file', help='path to first file')
    parser.add_argument('second_file', help='path to second file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    compare = generate_diff(args.first_file, args.second_file)
    print(compare)


if __name__ == '__main__':
    main()

