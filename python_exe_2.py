# -*- coding: utf-8 -*-
# Author: Kayi
# create time: 2021/4/2
def test_2(value):
    '''
    >>> test_2(123)
    911
    >>> test_2(23)
    12300
    '''
    if value == 23:
        return 12300
    else:
        return 911

if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    pass