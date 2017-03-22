# Create needed variables here.

alist = ['Hello', 'world']
atuple = ('Hello', 'world')
adict = {'a': 1, 'b': 2}
aset = {1, 2, 3, 4, 5}


def test_list():
    assert alist == ['Hello', 'world']
    assert alist[0] == 'Hello'
    assert alist[1] == 'world'
    assert alist[-1] == 'world'
    assert alist[:1] == ['Hello']
    assert alist[1:] == ['world']
    assert 'Hello' in alist
    assert 'He' not in alist
    assert 'He' in alist[0]


def test_list_is_mutable():
    blist = alist
    clist = alist[:]
    assert alist == blist == clist
    assert alist is blist
    assert alist is not clist
    alist.append('!!')
    blist[0] = 'Hillo'
    assert alist == ['Hillo', 'world', '!!']
    assert alist == blist
    assert alist != clist
    assert clist == ['Hello', 'world']
    blist = 'Not even a list'
    assert alist != blist
    assert alist is not blist


def test_scopes():
    assert alist == ['Hillo', 'world', '!!']
    try:
        blist
    except NameError:
        pass
    else:
        raise AssertionError('Expected NameError')


def test_scopes2():
    alist = [1, 2, 3]
    assert alist == [1, 2, 3]


def test_scopes3():
    assert alist == ['Hillo', 'world', '!!']


def test_scopes4():
    global alist
    alist = 'Not even a list!!!'
    assert alist == 'Not even a list!!!'


def test_scopes5():
    assert alist == 'Not even a list!!!'


def test_tuple():
    assert atuple == ('Hello', 'world')
    assert atuple != ['Hello', 'world']
    assert list(atuple) == ['Hello', 'world']
    assert atuple == tuple(['Hello', 'world'])
    assert atuple[0] == 'Hello'
    assert atuple[-1] == 'world'
    assert atuple[:1] == ('Hello',)  # trailing comma needed with one item tuple
    assert atuple[1:] == ('world',)
    assert 'Hello' in atuple


def test_tuple_is_not_mutable():
    try:
        atuple[0] = 'tuples are not mutable'
    except TypeError:
        pass
    else:
        raise AssertionError('Expected TypeError')


def test_dict():
    assert adict == {'a': 1, 'b': 2}
    assert adict == {'b': 2, 'a': 1}
    assert adict['a'] == 1
    assert 'a' in adict
    assert 1 not in adict
    assert 1 in adict.values()


def test_iterating_dict_returns_keys():
    assert sorted(adict) == ['a', 'b']
    assert list(adict) in (['a', 'b'], ['b', 'a'])


def test_dict_is_mutable():
    bdict = adict
    cdict = adict.copy()
    assert adict == bdict == cdict
    assert adict is bdict
    assert adict is not cdict
    adict['b'] = 3
    bdict['c'] = 42
    assert adict == {'a': 1, 'b': 3, 'c': 42}
    assert adict == bdict
    assert adict is bdict
    assert adict != cdict


def test_set():
    assert aset == {1, 2, 3, 4, 5}
    assert aset == {5, 2, 1, 4, 3}
    assert aset == {1, 2, 3, 4, 5, 1, 2, 3, 4, 4, 4, 4}
    assert 1 in aset
    assert 0 not in aset


def test_set_is_iterable_but_not_indexable():
    assert sorted(aset) == [1, 2, 3, 4, 5]
    try:
        aset[0]
    except TypeError:
        pass
    else:
        raise AssertionError('Expected TypeError')


def test_set_is_mutable():
    bset = aset
    cset = aset.copy()
    assert aset == bset == cset
    aset.add(0)
    assert aset == {0, 1, 2, 3, 4, 5}
    assert aset == bset
    assert aset != cset
