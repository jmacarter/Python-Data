# purse = dict()
# purse['money']=12
# purse['candy']=3
# purse['tissues']=75
# print purse
# print purse['candy']
# purse['candy']=purse['candy']+2
# print purse
#
#
# ddd=dict()
# ddd['age']=21
# ddd['course']=182
# print ddd
# ddd['age']= 23
# print ddd
#
#
# jjj = {'chuck':1,'fred':42,'jan':100}
# print jjj
#
# ooo = {}
# print ooo


# ccc=dict()
# ccc['csev']=1
# ccc['cwen']=1
# print ccc
# ccc['cwen']=ccc['cwen']+1
# print ccc
#
# print 'csev' in ccc
# print 'marquadt' in ccc
#

# counts=dict()
# names=['csev','cwen','csev','zqian','cwen']
# for name in names:
#     if name not in counts:
#         counts[name]=1
#     else:
#         counts[name]=counts[name]+1
# print counts
#
# counts=dict()
# names=['csev','cwen','csev','zqian','cwen']
# for name in names:
#     counts[name]=counts.get(name,0)+1
# print counts

# counts=dict()
# print 'Enter a line of text:'
# line=raw_input('')
#
# words = line.split()
# print 'Words:',words
# print 'Counting...'
# for word in words:
#     counts[word]=counts.get(word,0)+1
#
# print 'Counts',counts

# counts = {'chuck':1,'fred':42,'jan':100}
# for key in counts:
#     print key, counts[key]
#
# print list(counts)
# print counts.keys()
# print counts.values()
# print counts.items()
#
# for aaa,bbb in counts.items():
#     print aaa,bbb

name = raw_input("Enter file:")
handle = open(name,'r')
text = handle.read()
words = text.split()

counts = dict()
for word in words:
    counts[word] = counts.get(word,0)+1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print bigword, bigcount
