a = 30
b = "this is a string."
print(b , a)
a = "now this a text."
b = 10
print(b , a)

"""casting"""
number = int() # float(), string()
print("number is " , number)

varient = 5
varient = ['abc',"xyz"] # It's a list
print(type(varient))

Number = float(3.2)
print("Number is ",Number,", number is ", number)

x, y, z = 1.2, 'salam', 44
print(x, y, z)

x = y = z = 'a simpe text.'
print(x, y, z)

lst = ['apple', 'orange', 'avacado']#, 'banana']

x, y, z = lst
print(x, y, z)


i, o, p = 'I', 'am', 'Milad'
print("first way for ptint sth.")
print(i+o+p)
print("second way for ptint sth.")
print(i,o,p)
"""first way for ptint sth.
IamMilad
second way for ptint sth.
I am Milad"""

gv = 'good'
def testFunction():
    #global gv = 'bad' # it occors an error
    # global ig = 'inside function' # it's not true
    global ig 
    ig = 'inside function' 
    gv = 'not too bad'
    print(gv)
# print(gv,ig) # it couses an error
testFunction()
print(gv,ig)

