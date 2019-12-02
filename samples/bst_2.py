class Node():
    def __init__(self,value):
        self._left = None
        self._value = value
        self._right = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right


class Strategy():
    def execute(self,number):
        self.lst.append = number

    def print(self):
        print('self.lst',self.lst)



class Tree():

    def __init__(self):
        print('init')
        self.root = None

    def add(self,value,node = None):
        # Compare the new value with the parent node
        print('add ',value)
        if self.root is None:
            node = Node(value)
            self.root = node
            return self.root
        elif value < node.value:
            node.left = add(value,node.left)
        else:
            node.right = add(Node(value)


        return node


    def print(self):
        if self.root.left:
            self.root.left.print()
        print(self.root.value)
        if self.root.right:
            self.root.right.print()

    def inorder(self,func):
        if self.root.left:
            func.execute(self.root.left)
        func.execute(self.root.number)
        if self.root.right:
            func.execute(self.root.right)



root = Tree()
root.add(42)
root.add(13)
root.add(64)
root.add(7)
root.add(15)
root.add(100)
root.add(105)
root.add(104)

#root.print()
# s = Strategy()
# root.inorder(s)
#s.print()


