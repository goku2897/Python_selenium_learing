x = "rcv academy rcv academy rcv academy"
y = 9938602399
print(len(x))
print(str(y))
z= str(y)
print(z.find("38"))

#Upper
a = print(x.upper())
a = x.upper()

#count
print(x.count("rcv",10,30))


#isupper
print(a.isupper())

#islower
print(a.islower())


#split
print(x.split()) #['rcv', 'academy', 'rcv', 'academy', 'rcv', 'academy'] based on space is we doesnt provide ant value in the function

#strip
u = "     ;;;;;;rcv academy rcv academy rcv academy   "
print(u.strip(';7 \''))

#lstrip
u = "     ;;;;;;rcv academy rcv academy rcv academy   "
print(u.lstrip(';7 \''))


#rstrip
u = "     ;;;;;;rcv academy rcv academy rcv academy   "
print(u.rstrip(';7 \''))

#replace
print(u.replace("rcv","stm",2))

#find
print(u.find("rcv"))

#index
print(u.index("rcv"))





