#4 find who has the most message in the file
fhand=open("mail.txt")
count=dict()
for line in fhand:
    if line.startswith("From:"):
        line=line.split()
        email=line[0]
        count[email]=count.get(email,0)+1
print(count)

larg=0
for i in count:
    ev=count.get(i)
    if larg<ev:
        larg=ev

max=None
for i in count:
    if count.get(i)==larg:
        max=i

for a,b in count.items():
    if b==larg:
        print(a)



