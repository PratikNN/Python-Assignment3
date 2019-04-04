#1 Read a file and count the number of words repeated in the file in the form of dictionary
count=dict()



try:
    fhand=open("a.txt","r")
    for line in fhand:
        words=line.split()
    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    print(count)
except:
    printf("file error")
    exit(0)