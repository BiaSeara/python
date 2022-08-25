from xmlrpc.client import Boolean


print("Hello, World!")
if 5 >  2:
    print("five is greater than two") #indentation is very important in Python.
x = 10 #int
y = 12 #int

"""
comments written in more than just one line
we can use the triple quotes instead of a # in each line 
"""

x = "dez" #str
print(x)
print(y)

a = str(4)
b = int(4)
c = float(4)

"""
Solo se accepta valores alfanumericos 
A-Z | a-z | 0-9 | _
"""

print(a)
print(b)
print(c)

#type() to get the Type
print(type(a))
print(type(b))
print(type(c))

print('We can use single quotes, it is the same')

#Python = Case-Sensitive || a != A

myVariableName = 'View' #Camel Case
MyVariableName = 'Replay' #Pascal Case
my_variable_name = 'Tell me what to do' #Snake Case

#Many values to multiple variables 
a, b, c = 'ATEEZ', 'BTS', 'Calum' 

print(a)
print(b)
print(c)

#One value to multiple variables
a = b = c = 'singers'

print(a)
print(b)
print(c)

#Unpack a collection
actors = ['Atthaphan ', 'Seung Gi ', 'Fluke']
a, b, c = actors

print(a)
print(b)
print(c)

#Output multiple variables
print(a, b, c) #comma
print(a + b + c) #addition operator 

#Addition operator with number = math
x = 8 
y = 7
z = 5
print(x + y + z)

#Output variables
x = "Justin Bieber"
print(len(x)) #nos muestra el tamaño del string

#Boolean --> keyword
verdad = True
print(verdad)

#Indexación 
#Rebanada(porción) cadena de caracteres --> <cadena>[inicio:fin]