# Print a Feyza Balaban on the screen
print('Feyza Balaban')


# Create a variable and assign a value to it (number/string)
x = 5
y = 'grape'
z = 'ten'
print(x)
print(y)
print(z)

p, r, s = 'bmw', 'audi', 'cooper'
print(p)
print(r)
print(s)

d = 5
v = 10
print(d + v)


# Display the type of the variable you created
a = 3
b = 'Feyza'
print(type(a))
print(type(b))

m = 1j
print(type(m))


# Write if statement (if x is bigger than a number then display something...)
w = 10
if w > 5:
    print('w is greater than 5')

t = 100
o = 55
if t > o: print('t is greater than o')


# Create a list of (fruits/cars/students....)
list1 = ['apple', 'samsung', 'huawei']
print(list1)

mylist = ['one', 'two', 'three', 'four']
print(type(mylist))


# Display each element of the list using for-loop
for q in 'banana':
    print(q)


# Create a dictionary for (student/car/animal)
car = {'brand' : 'Tesla',
       'model':'model3',
       'year':2023}
print(car)


# Create a class for Student/Animal etc.
class Student:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, I am", self.name)

student1 = Student('Feyza')
student1.say_hello()


# Phyton Booleans
print(10 > 9)
print(10 == 9)
print(10 < 9)


