# class Node():
#     def __init__(self,value):
#         self._left = None
#         self._value = value
#         self._right = None
#
#     @property
#     def value(self):
#         return self._value
#
#     @value.setter
#     def value(self, value):
#         self._value = value
#
#     @property
#     def left(self):
#         return self._left
#
#     @left.setter
#     def left(self, left):
#         self._left = left
#
#     @property
#     def right(self):
#         return self._right
#
#     @right.setter
#     def right(self, right):
#         self._right = right



class Node():

    def __init__(self, number):

        self.left = None
        self.right = None
        self.number = number


    def add(self,number):
        # Compare the new value with the parent node
        if self.number:
            if number < self.number:
                if self.left is None:
                    self.left = Node(number)
                else:
                    self.left.add(number)
            elif number > self.number:
                if self.right is None:
                    self.right = Node(number)
                else:
                    self.right.add(number)
        else:
            self.number = number


    def print(self):
        if self.left:
            self.left.print()
        print(self.number),
        if self.right:
            self.right.print()

#numbers = [42,13,64,7,15,100,105,104]

root = Node(42)
root.add(13)
root.add(64)
root.add(7)
root.add(15)
root.add(100)
root.add(105)
root.add(104)

root.print()
