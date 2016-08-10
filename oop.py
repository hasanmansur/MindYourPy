
'''
-------------------------------------Class object/Instance object--------------------------
# Class objects support two kinds of operations: attribute references and instantiation.
# Only operations understood by instance objects are attribute references.
# Special thing about methods is that the object is passed as the first argument of the function.

'''


print('---------------------example1----------------------------')
class MyClass:
    x = 100
    def hello(self):
        print('hello duniya')

print(MyClass.x)
# instantiation
myClassObject = MyClass() 
# Following two statements are exactly equivalent
MyClass.hello(myClassObject)
myClassObject.hello()

print('---------------------example2----------------------------')
class Fun:
    x = 0
    def square(self):
        return self.x * self.x

print(Fun.x)
funObject = Fun()
print(funObject.x)
print(funObject.square())
funObject.x = 2
print(funObject.x)
print(funObject.square())
print(Fun.x)
print(Fun.square(funObject))

print('---------------------example3----------------------------')
class Wow:
    x = 2
    def __init__(self, val):
        self.x = val
    def square(self, val):
        self.x = val
        return self.x * self.x

print(Wow.x)
wowObject = Wow(3)
print(wowObject.x)
print(wowObject.square(4))
wowObject.x = 2
print(wowObject.x)
print(wowObject.square(5))
print(Wow.x)
print(Wow.square(wowObject,6))

'''
----------------------------------class & instance variables-------------------------------------
# class variable shared by all instances
# instance variable unique to each instance
'''

print('---------------------example4----------------------------')
class Dog:
    
    kind = 'canine'
    def __init__(self, name):
        self.name = name

d = Dog('fido')
e = Dog('buddy')
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)

'''
---------------------------------------------Inheritance-----------------------------------------
'''

print('---------------------example5----------------------------')
class Vehicle:
    info = 'this is a vehicle'
    def __init__(self):
        self.type = '4 wheeler'
    def setName(self):
        self.name = 'test'

class Car(Vehicle):
    def setName(self):
        self.name = 'car'

print(':::::::: base class :::::::')
vehicleObj = Vehicle()
print(Vehicle.info)
print(vehicleObj.info)
print(vehicleObj.type)
vehicleObj.setName()
print(vehicleObj.name)

print(':::::::: sub class :::::::')
toyota = Car()
print(Car.info)
print(toyota.info)
print(toyota.type)
toyota.setName()
print(toyota.name)

print('---------------------example6----------------------------')

class Base1:
    def __init__(self):
        self.x = 99;

class Base2:
    def setY(self):
        self.y = 100

class Derived(Base1, Base2):
    pass

foo = Derived()
foo.setY()
print(foo.x)
print(foo.y)
