## Animal is-a object
class Animal(object):
    pass

## Cass Dog is-a class that has-a Animal object
class Dog(Animal):

    def __init__(self, name):
        # has-a class named self
        self.name = name

# Cat is-a class
class Cat(Animal):

    def __init__(self, name):
        ## Cas has-a name
        self.name = name

## Person is-a object
class Person():
    def __init__(self, name):
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None


#Employee is-a class
class Employee(Person):

    def __init__(self, name,salary):
        super(Employee, self).__init__(name)
        self.salary = salary
#Fish is-a object
class Fish():
    pass
#Salmon is-a class
class Salmon(Fish):
    pass
#Haibut is-a class
class Halibut(Fish):
    pass
#rover is-a Dog
rover = Dog("Rover")

#satan is-a Cat
satan = Cat("Satan")

#Mary is a Person
mary = Person("Mary")

# Mary has a pet
mary.pet = satan

#frank is-a Employee
frank = Employee("Frank", 120000)   

#frang has-a pet that is Rover
frank.pet = rover

#flipper is-a fish (an object)
flipper = Fish()

#crouse is-a instance  of Salmon
crouse = Salmon()

#harry is-a instance of halibut
harry = Halibut
