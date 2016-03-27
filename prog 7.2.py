# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()

dspamTotal = 0
lineCounter = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    cleanLine = line.rstrip()
    lineCounter = lineCounter + 1
    #print cleanLine
    dspamStr = cleanLine.lstrip('X-DSPAM-Confidence:    ')
    try:
        dspamVal = float(dspamStr)
    except:
        print 'DSPAM-Confidence is non-numeric'
        exit()
    dspamTotal = dspamTotal + dspamVal

print "Average spam confidence:",dspamTotal/lineCounter
