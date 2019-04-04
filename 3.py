fhand=open("mail.txt")
count=dict()
for line in fhand:
    line=line.strip()
    if(line.startswith("From")):
        words=line.split()
        day=words[0]
        count[day]=count.get(day,0)
        if day in count:
            count[day]=count[day]+1
print(count)
fhand=open("mail.txt")
count={"mon":0,"Tue":0,"wed":0,"thu":0}
for line in fhand:
    line=line.strip()
    if(line.startswith("From")):
        words=line.split()
        print(words)
        for word in words:
            if word in count:
                count[word]=count[word]+1
print(count)

