a = 'Iam Milad'
for x in a:
    print(x)

print('--------')
print(a[5:7])

print(len(a)) # 9

print("Milad" in a) # True

if "Milad" not in a:
    print("Milad is in the text.")
else:
    print("Milad isn't in the text.")


# Slicing String 
x = "Hello, Wrold!!"
print(x[1:-3])
#Upper Case
print(x.upper())
#lower Case
print(x.lower())
#Replace
print(x.replace('l','1'))
#Sclice
y = x.split(',') # ['Hello', ' Wrold!!']
print(y[0])

#Multi line
txt = """this is a long text
in multi line.
it's so cool.
try it!"""
print(txt)
#String Concatenation
d = "this is"
l = 'begun'
p = d + ' ' + l 
print(p)

#Format
print('----Format in Python----')
name = 'Milad'
age = 25
height = 180
phone_number = '0915444120'
info = '''my name is {0}, 
I am {3}. I Height is {1},
my phone number is {2}'''
print(info.format(name,height,phone_number,age))
#Strip
xx = " Hello world "
print(xx.strip())




