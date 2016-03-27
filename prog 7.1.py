#Use words.txt as the file name
fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()

data = fh.read()
data = data.upper()
print data.rstrip()
