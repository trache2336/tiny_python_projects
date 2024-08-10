#!/usr/bin/env python3
"""tests for classify.py"""

import os
import re
import string
from subprocess import getstatusoutput
import secrets

prg = './classify.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_upper():
    """upper"""

    word = secrets.choice('APPLE BANANA CHERRY'.split())
    rv, out = getstatusoutput(f'{prg} {word}')
    assert rv == 0
    assert out == f'{word} is uppercase.'


# --------------------------------------------------
def test_lower():
    """lower"""

    word = secrets.choice('apple banana cherry'.split())
    rv, out = getstatusoutput(f'{prg} {word}')
    assert rv == 0
    assert out == f'{word} is lowercase.'


# --------------------------------------------------
def test_title():
    """title"""

    word = secrets.choice('Apple Banana Cherry'.split())
    rv, out = getstatusoutput(f'{prg} {word}')
    assert rv == 0
    assert out == f'{word} is title case.'


# --------------------------------------------------
def test_digit():
    """digit"""

    word = secrets.choice('1 2 3'.split())
    rv, out = getstatusoutput(f'{prg} {word}')
    assert rv == 0
    assert out == f'{word} is a digit.'


# --------------------------------------------------
def test_space():
    """space"""

    word = secrets.choice([' ', '\t'])
    rv, out = getstatusoutput(f'{prg} "{word}"')
    assert rv == 0
    assert out == f'input is space.'


# --------------------------------------------------
def test_unclassified():
    """unclassified"""

    word = secrets.choice('1.2 3.04 40.5'.split())
    rv, out = getstatusoutput(f'{prg} "{word}"')
    assert rv == 0
    assert out == f'{word} is unclassified.'
