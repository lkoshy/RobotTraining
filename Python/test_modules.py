# Import needed modules here.

import os
import os.path
from os.path import abspath, dirname
import time

import pytest
import robot

import test_basetypes
from test_containers import aset


def test_standard_modules():
    assert time.time() > 10**9
    curdir = os.path.dirname(os.path.abspath(__file__))
    assert 'test_modules.py' in os.listdir(curdir)


def test_from_import():
    curdir1 = os.path.dirname(os.path.abspath(__file__))
    curdir2 = dirname(abspath(__file__))
    assert curdir1 == curdir2


def test_third_party_modules():
    assert pytest.__name__ == 'pytest'
    assert robot.__version__.startswith('3')


def test_own_modules():
    assert test_basetypes.string == 'Hello, world!'
    assert 1 in aset
