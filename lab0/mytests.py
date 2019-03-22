from lab0 import *


def tst_count_pattern():
    pattern =   ['a','b','a']
    lst =       ['a','b','c','a','b','a','b','a']

    print( count_pattern(pattern, lst) )


def tst_depth():

    expr_lst = [
                'x',
                ('expt', 'x', 2),
                ('+', ('expt', 'x', 2), ('expt', 'y', 2)),
                ('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2), 1), ('/', 5, 2))),
                ]

    for expr in expr_lst:
        print(depth(expr))


if __name__ == "__main__":
    #tst_count_pattern()
    tst_depth()