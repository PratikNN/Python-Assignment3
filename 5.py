#5.write a program to read a tuple with  months,and days convert tuple into dictionary.
#list of tuples
tup=[('jan',31),('feb',28),('mar',31)]
d={}
for i in tup:
    key=i[0]
    val=i[1]
    d[key]=val
print(d)

#tuple of tuples
tuple=(("jan",31),("feb",28),("mar",31),("apr",30))
print(dict(tuple))
