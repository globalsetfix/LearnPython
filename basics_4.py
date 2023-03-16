#14 Strings
x = "hello" + " " \
    + " programmer"
y = 'I\'m progger'
print(y)

z = "Hello \n YouRa"
z = "Hello \n     \rYouRa"
print(z)

m = "12\t34567"
print(m)

t = "\t Hello! \n\tI'm very glad to see you!"
print(t)

s = """This is text with "triple code" """
print(s)

s = """This is text 
with "triple code" """

print(s)

#15 Indexing & Slicing

greeting = "Hello python!"
greeting_len = len(greeting)
#Length
print(greeting_len)
#First
print(greeting[0])
#Last
print(greeting[-1])

#Slicing ( кусочки )
#from - to
print(greeting[1:5])
print(greeting[-5:-2])

print(greeting[2:])
print(greeting[:2])

print(greeting[:])

#Step
print(greeting[::2])
print(greeting[1::3])
print(greeting[1:9:2])

#revers
print(greeting[::-1])



