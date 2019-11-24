def make_node(left,num,right):
    return [left,num,right]

def make_tree():
    n1 = make_node(None,4,None)
    n2 = make_node(None,10,None)
    n3 = make_node(None,14,None)
    n4 = make_node(None,17,None)
    n5 = make_node(None,29,None)

    n6 = make_node(n1,8,n2)
    n7 = make_node(n6,12,n3)
    n8 = make_node(n4,23,n5)
    n9 = make_node(n7,15,n8)

    return n9


def do_all():
    tree = make_tree()
    print(tree)
    print(sum_tree(tree))


def sum_tree(tree):
    if tree is None:
        return 0
    sum_left = sum_tree(tree[0])
    sum_right = sum_tree(tree[2])
    return sum_left + tree[1] + sum_right

do_all()




# def rec_sum(n):
#     if n == 1:
#         return 1
#
#     return rec_sum(n-1) + n
#
# print(rec_sum(5)) #15