import math


class Animal:
    color = ''

    def moves(self):
        print('It Walks')


class Cat(Animal):
    height = ''

    def make_sound(self):
        print('Cat Meow')


class Dog(Animal):
    height = ''

    def make_sound(self):
        print('Dog Bark')

class Crocodile(Animal):
    length = ''

    def moves(self):
        print('Crocodile Crawls')

    def make_sound(self):
        print('Cat Bark')

class Bird(Animal):
    height = ''

    def moves(self):
        print('Birds Fly')



# c = Cat()
# c.moves()
# c.sound()




class User:
    name = ''
    address = ''
    phone = ''
    email = ''
    username = ''
    password = ''

    def login():
        pass

    def logout():
        pass


class Student(User):
    course = ''
    fee = ''

    def enroll():
        pass

    def attend():
        pass

    def upgrade():
        pass

    def pay():
        pass

    def leave():
        pass


class Staff(User):
    salary = ''
    time = ''

    def add_staff():
        pass

    def update_staff():
        pass

    def delete_staff():
        pass

    def get_staff():
        pass


def add(a, b):
    return a+b

def add(a, b, c):
    return a+b+c



from abc import ABC, abstractmethod

class Shape(ABC):
    no_of_side = ''
    length = ''
    name = ''

    def __init__(self, n, name):
        self.no_of_side = n
        self.name = name

    def get_perimeter(self):
        return (self.no_of_side * self.length)

    @abstractmethod
    def get_area(self):
        pass

    def get_angle(self):
        return (((self.no_of_side-2) * 180)/self.no_of_side)



class Triangle(Shape):
    base = 0
    height = 0

    def __init__(self, b, h, n, name):
        self.base = b
        self.height = h
        super().__init__(n, name)

    def get_area(self):
        return (1/2 * self.base * self.height)

    @staticmethod
    def get_perimetert(a, b, c):
        return (a+b+c)

    @classmethod
    def get_triangle(cls, b, h, n, name):
        return cls(b, h, n, name)


ob1 = Triangle.get_triangle(10, 10, 3, 'Equilateral Triangle')
ob2 = Triangle.get_triangle(10, 10, 3, 'Isosceles Triangle')
ob3 = Triangle.get_triangle(10, 10, 3, 'Right Angled Triangle')

print(ob1.name)
print(ob2.name)
print(ob3.name)


class Rectangle(Shape):
    length = ''
    breadth = ''

    def __init__(self, l, b, n, name):
        self.length = l
        self.breadth = b
        super().__init__(n, name)

    def get_area(self):
        return (self.length * self.breadth)

    def get_perimeter(self):
        return (2 * (self.length + self.breadth))


class Circle(Shape):
    radius = ''

    def __init__(self, r, n, name):
        self.radius = r
        super().__init__(n, name)

    def get_area(self):
        return (math.pi * self.radius * self.radius)

    def get_perimeter(self):
        return (2 * math.pi * self.radius)


class Square(Shape):
    length = ''

    def __init__(self, l, n, name):
        self.length = l
        super().__init__(n, name)

    def get_area(self):
        return (self.length * self.length)


c = Circle(10, 0, 'Circle')
print(c.get_area())

t = Triangle(20, 10, 3, 'Triangle')
print(t.get_area())

r = Rectangle(20, 30, 4, 'Rectangle')
print(r.get_area())

s = Square(10, 4, 'Square')
print(s.get_perimeter())


class Math:

    @staticmethod
    def add(a, b, c=0):
        return a+b+c

m = Math()
print(m.add(5, 10))
print(m.add(5, 10, 15))



class Account:
    name = ''
    username = ''
    password = ''
    balance = 0

    def login(self):
        pass

    def transaction(self):
        pass
