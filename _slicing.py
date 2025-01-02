from operator import index

s = "Welcome to Rajesh Academy"

print(s[0:2]) # We
print(s[2:6])

print(s[2:6:2]) #lo

print(s[:]) # Welcome to Rajesh Academy

print(s[0:]) # Welcome to Rajesh Academy


#negative index
print(s[-7:-1])

print(s[::-1])

y = "name, age, city"
print(y.index(','))
print(y[0:y.index(',')])
