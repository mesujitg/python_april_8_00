class Cat:
    color = ''
    height = ''

    def moves(self):
        print('Cat Walks')

    def sound(self):
        print('Cat Meow')


# c = Cat()
# c.moves()
# c.sound()

class EnrolledStudent:
    name = ''
    address = ''
    phone = ''
    email = ''
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



class Triangle:
    base = 0
    height = 0

    def area(self):
        return (1/2 * self.base * self.height)


# t = Triangle()

# b = int(input('Enter base of triangle'))
# h = int(input('Enter height of triangle'))

# t.base = b
# t.height = h
# print('Area of given Triangle is ', t.area())


class Rectangle:
    __length = ''
    __breadth = ''

    # def __init__(self, l, b):
    #     self.__length = l
    #     self.__breadth = b

    # setter functions
    def setLength(self, l):
        self.__length = l

    def setBreadth(self, b):
        self.__breadth = b

    # getter functions
    # def getLength(self):
    #     return self.__length

    # def getBreadth(self):
    #     return self.__breadth

    def area(self):
        return (self.__length * self.__breadth)


l = int(input('Enter length of Rectangle'))
b = int(input('Enter breadth of Rectangle'))

r = Rectangle()
r.setLength(l)
r.setBreadth(b)


print('Area of given Rectangle is ', r.area())

