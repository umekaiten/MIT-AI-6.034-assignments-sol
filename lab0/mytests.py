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
    #tst_sum()
    #tst_product()
    tst_do_mult()


def tst_sum():

    cur_sum = Sum([1, Sum([2, Sum([Sum([3, 4]), Sum([5, 6])])])])
    print("cur_sum: \t\t\t\t" + str(cur_sum))

    flat_sum = cur_sum.flatten()
    print("flat_sum: \t\t\t\t" + str(flat_sum))

    print("simplified orig sum: \t" + str(cur_sum.simplify()))
    print("simplified flat sum: \t" + str(flat_sum.simplify()))


def tst_product():

    cur_prdct = Product([1, Product([Product([2, 3]), Product([Product([4, 5]), 6])]), 7]) # 1*()*7
    print("cur: \t" + str(cur_prdct))
    print("cur: \t" + str(prod2str(cur_prdct)))
    print("")

    flat_prod = cur_prdct.flatten()
    print("flat: \t" + str(flat_prod))
    print("flat: \t" + prod2str(flat_prod))

    simple_prod = cur_prdct.simplify()
    print("simple: \t" + str(simple_prod))
    print("simple: \t" + prod2str(simple_prod))

def prod2str(product):

    expr_str = ""

    for i, factor in enumerate(product):

        if isinstance(factor, Expression):
            expr_str += "(" + str(prod2str(factor)) + ")"
        else:
            expr_str += str(factor)

        if i != len(product)-1:  # if it's NOT the last item, add '*' symbol
            if isinstance(product, Product):
                expr_str += "*"
            else:
                expr_str += "+"

    return expr_str


def tst_do_mult():

    #expr1 = Sum([1])
    #expr2 = Sum([Sum([3, 4]), 5])

    #print(do_multiply(expr1, expr2))

    cur_prod = Product([1])
    print("cur: \t" + str(cur_prod))
    print("cur: \t" + prod2str(cur_prod))
    print("")
    simp_prod = cur_prod.simplify()
    print("simp: \t" + str(simp_prod))
    print("simp: \t" + prod2str(simp_prod))


if __name__ == "__main__":
    #tst_count_pattern()
    #tst_depth()
    #tst_tree_ref()
    tst_algebra()