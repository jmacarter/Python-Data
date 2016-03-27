# x = ('Glenn','Sally','Joseph')
# print x[2]
#
#
# x = [9,8,7]
# print x
# x[2] = 6
# print x
#
# (x,y) = (4,'fred')
# print y
# (a,b) = (99,98)
# print a
#
# d = dict()
# d['csev'] = 2
# d['cwen'] = 4
#
# for (k,v) in d.items():
#     print k,v
#
# tups = d.items()
# print tups
#
#
# print (0,1,2) < (5,1,2)
# print (0,1,2000000) < (0,3,4)
# print ('Jones', 'Sally') < ('Jones','Fred')
# print ('Jones', 'Sally') < ('Adams', 'Sam')

# d = {'a':10, 'b':1, 'c':22}
# t = d.items()
# print t
# s = t.sort()
# print s

# d = {'a':10, 'b':1, 'c':22}
# t = d.items()
# print t1
# t = sorted(d.items())
# print t
#
# for k,v in t:
#     print k,v


# c = {'a':10, 'b':1, 'c':22}
# tmp = list()
# for k,v in c.items():
#     tmp.append( (v,k) )
#
# print tmp
# tmp.sort(reverse=True)
# print tmp


fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1

lst = list()
for key, val in counts.items():
    lst.append( (val, key))

lst.sort(reverse=True)

for val, key in lst[:10]:
    print key,val


c = {'a':10, 'b':1, 'c':22}
print sorted( [(v,k) for k,v in c.items()])
