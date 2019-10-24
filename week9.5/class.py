

print("Hello, World!")

name = "World"

print(name)
print(f"Hello, {name}!")
print("Hello, {}!".format(name))

x = 1
y =  1
x = 1
y = 1
if x == 1:
    print("I'm indented.")
    if y == 1:
        print("Double indented.")
        print(" same as double level.")
    else:
        print("This is second else.")
else:
    print("From the first if statement.")

x = 1
x += 1
# This is a comment.
if x < 3:
    pass
    print("X < 3")
    pass
    pass
elif x < 10:
    print("X  < 10 ")
else:
    print("X isn't 1 or 2.")

x = 'Dog'
y = "Cat\"s"

z = 1
a = 1.0

b = [ "a", "b", 1, 1.0 ]
c  = (1, 2,3,4 )
d = {"name":"value", "anotherName":3}

print(type(a))
print(type(b))
print(type(c))

a = 1
b = 2
b, a = a, b
mylist  = []
mylist.append(1)
mylist.append("2")
print(mylist[0])
print(mylist[1])
# print(mylist[2])

print("My for loop: ")

for x in range(3):
    print(x)

for x  in [1,2,3,4,5,6,7]:
    print("x: ", x)

print("While loop")
x = 0
while x < 10:
    pass
    print(x)
    x += 1
    # No ++   -    x++ 

for x in range(5,11,2): # start, stop , [step]
    print("Next X: ", x)







