for i in [5,4,3,2,1]:
    print i
print "Blastoff!"



friends = ['Joseph','Jeremy','Jimmy Jackhammer','Tyrone', 'Jamal', 'Terrance']

for i in friends:
    print i+' is a friend'

print range(len(friends))

for i in range(len(friends)):
    friend = friends[i]
    print friend+' is a good friend'

a = [1,2,3]
b = [4,5,6]
c = a + b
d = a + friends


print c[1:4]
print c[:5]
print c[:]
print d


stuff = list()
stuff.append('book')
stuff.append(99)
print stuff
stuff.append('cookie')
print stuff
friends.append('Antonio')
friends.sort()
print friends
print max(friends)
print min(friends)
print len(friends)



# total = 0
# count = 0
# while True:
#     inp = raw_input("Enter a number:")
#     if inp == 'done':break
#     value = float(inp)
#     total = total + value
#     count = count + 1
#
# average = total/count
# print 'Average:',average
#
# numlist = list()
# while True:
#         inp = raw_input('Enter a number:')
#         if inp == 'done':break
#         value=float(inp)
#         numlist.append(value)
#
# average = sum(numlist)/len(numlist)
# print 'Average:',average




abc = 'With three words'
stuff = abc.split()
print stuff
print len(stuff)
print stuff[0]

for w in stuff:
    print w


line = 'A lot               of spaces'
etc = line.split()
print etc

line = 'first;second;third'
thing = line.split()
print thing
print len(thing)

thing = line.split(';')
print thing
print len(thing)



fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    # print words[2]
    email = words[1]
    print email
    pieces = email.split('@')
    print pieces[1]
