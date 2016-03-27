#Use mbox-short.txt as the file name
fname = raw_input("Enter file: ")
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()

senders = dict()

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    fromline = line.split()
    sender = fromline[1]
    senders[sender] = senders.get(sender,0)+1



bigcount = None
bigword = None
for sender,count in senders.items():
    if bigcount is None or count > bigcount:
        bigword = sender
        bigcount = count
print bigword, bigcount
