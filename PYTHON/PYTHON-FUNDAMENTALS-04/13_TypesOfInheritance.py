# Types of Inheritance in Python
# Inheritance in Python is a fundamental concept in object-oriented programming that allows a class (child class) to inherit attributes and methods from another class (parent class). There are several types of inheritance in Python:

# 1. Single Inheritance: A child class inherits from a single parent class.
class Parent:
    def __init__(self):
        self.parent_attr = "I am a parent attribute"

    def parent_method(self):
        print("I am a parent method")

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_attr = "I am a child attribute"

    def child_method(self):
        print("I am a child method")

# 2. Multiple Inheritance: A child class inherits from multiple parent classes.
class A:
    def __init__(self):
        self.attr_a = "Attribute from class A"

    def method_a(self):
        print("Method from class A")

class B:
    def __init__(self):
        self.attr_b = "Attribute from class B"

    def method_b(self):
        print("Method from class B")

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.attr_c = "Attribute from class C"

    def method_c(self):
        print("Method from class C")

# 3. Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another parent class.
class GrandParent:
    def __init__(self):
        self.grandparent_attr = "I am a grandparent attribute"

    def grandparent_method(self):
        print("I am a grandparent method")

class Parent(GrandParent):
    def __init__(self):
        super().__init__()
        self.parent_attr = "I am a parent attribute"

    def parent_method(self):
        print("I am a parent method")

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_attr = "I am a child attribute"

    def child_method(self):
        print("I am a child method")

# 4. Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
class Parent:
    def __init__(self):
        self.parent_attr = "I am a parent attribute"

    def parent_method(self):
        print("I am a parent method")

class Child1(Parent):
    def __init__(self):
        super().__init__()
        self.child1_attr = "I am child 1 attribute"

    def child1_method(self):
        print("I am child 1 method")

class Child2(Parent):
    def __init__(self):
        super().__init__()
        self.child2_attr = "I am child 2 attribute"

    def child2_method(self):
        print("I am child 2 method")
