#!/usr/bin/env python3
"""
Author : Mike Daugherty <mikedaug@yahoo.com>
Date   : 2021-03-29
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args       = get_args()
    sort_list  = args.sorted
    items_list = args.positional
    
    if sort_list:
        items_list.sort()
        
    num_items = len(items_list)
    
    # ~ print(f'flag_arg = "{sort_list}"')
    # ~ print(f'positional = "{items_list}"')
    
    output = ''
    if num_items == 1:
        output = items_list[0]
    elif num_items == 2:
        output = ' and '.join(items_list)
    else:
        items_list[-1] = 'and ' + items_list[-1]
        output = ', '.join(items_list)
    
    print(f"You are bringing {output}.")
    
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
