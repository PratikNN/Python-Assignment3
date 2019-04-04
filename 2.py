# write a program to read through a mail log build a histogram using dictionary to count how many messages have come from each email address
fhand=open("mail.txt")
count=dict()
for line in fhand:
    if line.startswith("From:"):
        line=line.split()
        email=line[0]
        count[email]=count.get(email,0)+1
print(count)

