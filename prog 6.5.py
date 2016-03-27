text = "X-DSPAM-Confidence:    0.8475";

length = len(text)
#print length

lenSpace = len("    ") #determine the length of the space string that prefaces the number
#print "the space is "+str(lenSpace)+" characters long"

spaceStart =text.find("    ") #determine the starting position of the space sequence
#print "space sequence starts at "+str(spaceStart)


print float(text[spaceStart+1:length])