
# #Ex1:
# # Write a Python program to create a Balanced Binary Search Tree (BST) using an array
# # (given) elements where array elements are sorted in ascending order
# my solution
# def make_node(left,num,right):
#     return [left, num, right]
#
# numbers = [1,2,3,4,5,6,7,8,9]
# def make_tree(numbers):
#     #print(numbers)
#     if not numbers:
#         #print("numbers is None")
#         return 0
#     mid_val = len(numbers) // 2
#     middle = numbers[mid_val]
#     node_left = make_tree(numbers[:mid_val])
#     node_right = make_tree(numbers[mid_val+1:])
#     print("node",node_left, middle, node_right)
#     return make_node(node_left,middle,node_right)
#
# make_tree(numbers)

# solution:
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# def sorted_array_to_bst(nums):
#     print(nums)
#     if not nums:
#         return None
#     mid_val = len(nums) // 2
#     node = TreeNode(nums[mid_val])
#     node.left = sorted_array_to_bst(nums[:mid_val])
#     node.right = sorted_array_to_bst(nums[mid_val + 1:])
#     print(node.left,node.val,node.right)
#     return node
#
# result = sorted_array_to_bst([1, 2, 3, 4, 5, 6, 7])
#
#
# def preOrder(node):
#     if not node:
#         return
#     print(node.val)
#     preOrder(node.left)
#     preOrder(node.right)
#
#

# preOrder(result)
#
