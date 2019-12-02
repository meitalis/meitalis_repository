
class BinaryTree:
    class __Node:
        def __init__(self, datum):
            self.left = self.right = None
            self.datum = datum

    def __init__(self):
        self.__root = None

    def add(self, datum):
        self.__root = self.__insert(self.__root, datum)

    def traverse(self, startegy):
        self.__traverse(self.__root, startegy)

    def __traverse(self, node, strategy):
        """
        in-order traversal of the tree
        """
        if node is not None:
            self.__traverse(node.left, strategy)
            strategy(node.datum)
            self.__traverse(node.right, strategy)


    def print(self):
        self.__traverseInorder(self.__root)

    def __insert(self, node, datum):
        """
        Insert function will insert a node into tree.
        """
        if node is None:
            return BinaryTree.__Node(datum)
        elif datum < node.datum:
            node.left = self.__insert(node.left, datum)
        elif datum > node.datum:
            node.right = self.__insert(node.right, datum)

        return node

    def __traverseInorder(self, node):
        """
        in-order traversal of the tree
        """
        if node is not None:
            self.__traverseInorder(node.left)
            print(node.datum)
            self.__traverseInorder(node.right)



"""
         10
    5          20
      8     16
   1
"""
t = BinaryTree()
t.add(10)
t.add(5)
t.add(20)
t.add(16)
t.add(8)
t.add(1)

# t.print()

class Printer:
    def __init__(self, delim):
        self.__delim = delim

    def __call__(self, value):
        self.execute(value)

    def execute(self, value):
        print(value)
        print(self.__delim)


t.traverse(Printer("///"))


def printer(v):
    print(v)

list =[]
def add2list(v):
    list.append(v)

t.traverse(add2list)

print(list)



#############################################3


from abc import ABC, abstractclassmethod

class BinaryTree:
    class Visitor(ABC):
        @abstractclassmethod
        def __call__(self, datum):
            self.visit(datum)

    class __Node:
        def __init__(self, datum):
            self.left = self.right = None
            self.datum = datum

    def __init__(self):
        self.__root = None

    def add(self, datum):
        self.__root = self.__insert(self.__root, datum)

    def traverse(self, startegy):
        if isinstance(startegy, BinaryTree.Visitor):
            self.__traverse(self.__root, startegy)
        return startegy

    def __traverse(self, node, strategy):
        """
        in-order traversal of the tree
        """
        if node is not None:
            self.__traverse(node.left, strategy)
            strategy(node.datum)
            self.__traverse(node.right, strategy)


    def print(self):
        self.__traverseInorder(self.__root)

    def __insert(self, node, datum):
        """
        Insert function will insert a node into tree.
        """
        if node is None:
            return BinaryTree.__Node(datum)
        elif datum < node.datum:
            node.left = self.__insert(node.left, datum)
        elif datum > node.datum:
            node.right = self.__insert(node.right, datum)

        return node

    def __traverseInorder(self, node):
        """
        in-order traversal of the tree
        """
        if node is not None:
            self.__traverseInorder(node.left)
            print(node.datum)
            self.__traverseInorder(node.right)



"""
         10
    5          20
      8     16
   1
"""
t = BinaryTree()
t.add(10)
t.add(5)
t.add(20)
t.add(16)
t.add(8)
t.add(1)

# t.print()

class IsEven:
    def __call__(self, val):
        return val % 2 == 0

class ListAccumelatorIf(BinaryTree.Visitor):
    def __init__(self, predicate):
        super().__init__()
        self.list = []
        self.pred = predicate

    def  __call__(self, value):
        if self.pred(value):
            self.list.append(value)



# print(t.traverse( ListAccumelatorIf(IsEven()) ).list)

def even(v):
    return v % 2 == 0

print(t.traverse( ListAccumelatorIf(even) ).list)






