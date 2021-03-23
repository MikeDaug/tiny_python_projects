#!/usr/bin/env python3
"""
Author : Mike Daugherty <mikedaug@yahoo.com>
Date   : 2021-03-22
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pos_arg = args.positional

    print(f'str_arg = "{str_arg}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
