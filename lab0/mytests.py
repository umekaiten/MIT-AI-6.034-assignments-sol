from lab0 import *
from algebra import *


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


def tst_tree_ref():

    tree =      [1,     [2, [ 3,4,5, [6,7] ],   8]]
    index =     [1,1,3,1]

    print (tree_ref(tree, index))


def tst_algebra():

    # check Sums:
    cur_sum = Sum([1, Sum([2, Sum([Sum([3, 4]), Sum([5, 6])])])])
    print( "cur_sum: \t\t\t\t" + str(cur_sum) )

    flat_sum = cur_sum.flatten()
    print( "flat_sum: \t\t\t\t" + str(flat_sum))

    print("simplified orig sum: \t" + str(cur_sum.simplify()))
    print("simplified flat sum: \t" + str(flat_sum.simplify()))

    # check Products:
    

if __name__ == "__main__":
    #tst_count_pattern()
    #tst_depth()
    #tst_tree_ref()
    tst_algebra()