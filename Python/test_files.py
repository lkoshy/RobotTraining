# Implement imported functions.

import os
import io
import pytest

from files import read_file, \
    write_file,\
    read_open_file, \
    write_open_file


CURDIR = os.path.dirname(os.path.abspath(__file__))
TEST_FILE = os.path.join(CURDIR, 'test.txt')
CONTENT = '''\
Hello, world!!!
---------------
'''


def test_read_file():
    path = os.path.join(CURDIR, 'README.txt')
    readme = read_file(path, binary=False)
    assert readme.startswith('This directory contains Python training material.')


def test_write_file():
    write_file(TEST_FILE, CONTENT, binary=False)
    content = read_file(TEST_FILE)
    assert content == CONTENT


@pytest.mark.skip(reason="no way of currently testing this")
def test_read_binary():
    content = read_file(TEST_FILE, binary=True)
    assert content.startswith('Hello, world!!')
    assert 'Hello, world!!' in content
    assert os.linesep in content


@pytest.mark.skip(reason="no way of currently testing this")
def test_write_binary():
    write_file(TEST_FILE, CONTENT, binary=True)
    content = read_file(TEST_FILE, binary=True)
    assert content.startswith('Hello, world!!')
    assert '\n' in content
    assert '\r' not in content


def test_read_open_file():
    with open(TEST_FILE) as real_file:
        content = read_open_file(real_file)
    assert content == read_file(TEST_FILE)
    file_like = io.StringIO('Example')
    read_open_file(file_like) == 'Example'


def test_write_open_file():
    with open(TEST_FILE, 'w') as real_file:
        write_open_file(real_file, CONTENT)
    with open(TEST_FILE) as real_file:
        read_open_file(real_file) == CONTENT
    file_like = io.StringIO()
    write_open_file(file_like, 'Example')
    assert file_like.getvalue() == 'Example'
