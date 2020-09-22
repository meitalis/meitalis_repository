class B:
    def __init__(self):
        self.x = 4

    def hello(self):
        print("hello ")

    def bybye(self):
        print("byebye")


class D(B):
    def __init__(self):
        super().__init__()  # B.__init__(self)
        self.y = 42

    def bybye(self):
        print("byebye dddd")

d = D()
d.bybye()
d.hello()