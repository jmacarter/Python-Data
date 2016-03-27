#Use mbox-short.txt as the file name
fname = raw_input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()


hours = dict()

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    fromline = line.split()
    time = fromline[5]
    time = time.rstrip()
    timeElements = time.split(':')
    hour = timeElements[0]
    hours[hour] = hours.get(hour,0)+1


lst = list()
for hour, count in hours.items():
    lst.append( (hour, count))

lst.sort()

for key, val in lst:
    print key,val

#
# for hour,count in hours.items():
#     print hour, count
