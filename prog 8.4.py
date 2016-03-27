#Use romeo.txt as the file name
fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()

lst = list()
for line in fh:
    thisLine = line.rstrip()
    words = thisLine.split()
    for word in words:
        if word in lst: continue
        lst.append(word)

lst.sort()
print lst
