#Use mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()

count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print words[1]
    count = count + 1

print "There were", count, "lines in the file with From as the first word"
