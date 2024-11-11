#!/usr/bin/env python3
"""Ransom note"""

import argparse
import os
import secrets


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    secrets.SystemRandom().seed(args.seed)

    # Method 2: Iterate each character, add to a list
    ransom = []
    for char in args.text:
        ransom += choose(char)

    print(''.join(ransom))


# --------------------------------------------------
def choose(char):
    """Randomly choose an upper or lowercase letter to return"""

    return char.upper() if secrets.choice([0, 1]) else char.lower()


# --------------------------------------------------
def test_choose():
    """Test choose"""

    state = secrets.SystemRandom().getstate()
    secrets.SystemRandom().seed(1)
    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'C'
    assert choose('d') == 'd'
    secrets.SystemRandom().setstate(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()
