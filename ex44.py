class Parent(object):

    def implicit(self):
        print("PARENT implicit()")
    def explicit(self):
        print("PARENT explicit")

class Child(Parent):
    def implicit(self):
        print("Child implicit()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
son.explicit()
dad.explicit()
