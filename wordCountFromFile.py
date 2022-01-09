def wordCountFromFile():
    filename = input ('enter file name ')
    file = open(filename,'r')
    wordcount = 0
    for i in file:
        words=i.split()
        wordcount=wordcount+len(words)
    print ('number of words = ', wordcount)


wordCountFromFile()