#!/usr/bin/env python3
"""tests for article.py"""

import os
import re
import string
from subprocess import getstatusoutput
import secrets

prg = './article.py'


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
def test_masculine_lower():
    """masculine_lower"""

    word = secrets.choice('chico teatro cartero'.split())
    rv, out = getstatusoutput(f'{prg} {word}')
    assert rv == 0
    assert out == f'Me gusto el {word}.'


# --------------------------------------------------
def test_masculine_upper():
    """masculine_upper"""

    word = secrets.choice('CHICO TEATRO CARTERO'.split())
    rv, out = getstatusoutput(f'{prg} {word}')
    assert rv == 0
    assert out == f'Me gusto el {word}.'


# --------------------------------------------------
def test_feminine_lower():
    """feminine_lower"""

    word = secrets.choice('chica gata abuela'.split())
    rv, out = getstatusoutput(f'{prg} {word}')
    assert rv == 0
    assert out == f'Me gusto la {word}.'


# --------------------------------------------------
def test_feminine_upper():
    """feminine_upper"""

    word = secrets.choice('CHICA GATA ABUELA'.split())
    rv, out = getstatusoutput(f'{prg} {word}')
    assert rv == 0
    assert out == f'Me gusto la {word}.'
