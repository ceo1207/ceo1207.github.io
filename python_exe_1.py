# -*- coding: utf-8 -*-
# Author: Kayi
# create time: 2021/4/2

def test_doc(value):
    '''
    >>> test_doc(123)
    123
    >>> test_doc(23)
    908
    '''
    if value == 123:
        return 123
    else:
        return 908

class Test(object):
    def print_a(self):
        '''
        需要创建对象 自己编写测试用例
        '''
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    from python_exe_2 import main
    main()