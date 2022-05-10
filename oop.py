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





class Shape:
    no_of_side = ''
    length = ''
    name = ''

    def __init__(self, n, name):
        self.no_of_side = n
        self.name = name

    def get_perimeter(self):
        return (self.no_of_side * self.length)

    def get_area(self):
        return 0

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


class Rectangle(Shape):
    length = ''
    breadth = ''

    def __init__(self, l, b, n, name):
        self.length = l
        self.breadth = b
        super().__init__(n, name)

    def get_area(self):
        return (self.length * self.breadth)


t = Triangle(20, 10, 3, 'Triangle')
print(t.get_area())

r = Rectangle(20, 30, 4, 'Rectangle')
print(r.get_area())


