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
        self._root = None

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, root):
        self._root = root

    def add(self,value):
        self.root = self.insert(value,self.root)

    def insert(self,value,node):

        if node is None:
            node =  Node(value)
            #print('insert val node is None',node.value)
            return node

        if value < node.value:
            node.left = self.insert(value,node.left)
        elif value > node.value:
            node.right = self.insert(value, node.right)

        #print('insert val ', node.left,node.value,node.right)
        return node



    def print(self):
        print("print")
        self.traverseInorder(self.root)

    def traverseInorder(self, node):
        if node is not None:
            self.traverseInorder(node.left)
            print(node.value)
            self.traverseInorder(node.right)

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

root.print()
# s = Strategy()
# root.inorder(s)
#s.print()


