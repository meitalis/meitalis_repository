class MyClass:
    #Not only can they modify object state, instance methods can also access the class itself through the self.__class__ attribute.
    def method(self):
        return 'instance method called', self

    # class methods can still modify class state that applies across all instances of the class.
    #it can’t modify object instance state
    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    #a static method can neither modify object state nor class state. Static methods are restricted in what data they can access
    @staticmethod
    def staticmethod():
        return 'static method called'


obj = MyClass()

#2 ways to call instance method
print(obj.method())
print(MyClass.method(obj))

#call classmethod
print(obj.classmethod())
MyClass.classmethod()

obj.staticmethod()
MyClass.staticmethod()
