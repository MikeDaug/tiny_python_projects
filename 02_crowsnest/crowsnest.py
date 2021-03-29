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
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    
    if word[0] == word[0].upper():
        if word[0] in 'AEIOU':
            article = 'An'
        else: article = 'A'
    else:
        if word[0] in 'aeiou':
            article = 'an'
        else:
            article = 'a'
    
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')
        

# --------------------------------------------------
if __name__ == '__main__':
    main()
