newslist = ['trade-wars-news1.txt',
'trade-wars-news2.txt',
'trade-wars-news3.txt',
'trade-wars-news4.txt',
'trade-wars-news5.txt']

def WordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(w) for w in wordlist]
    final0 = zip(wordlist, wordfreq)
    final = list(final0)
    return dict(final)

def sortFreqDict(frequency):
    fre = [(frequency[x], x) for x in frequency]
    fre.sort()
    fre.reverse()
    return fre

wordlist0 =[]

for i in range (0,5):
 news = open(newslist[i])
 wordlist0 += news.read().lower().split()

stop_words = ["the", "and", "of", "a", "in"]
stop_words += ["to","this","that","are","my","i" ] 
#I find those words when I run this program
stop_words += ['able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','but','by','can','cannot','could','dear','did','do','does','either','else','ever','every','for','from','get','got','had','has','have','he','her','hers','him','his','how','however','i','if','in','into','is','it','its','just','least','let','like','likely','may','me','might','most','must','my','neither','no','nor','not','of','off','often','on','only','or','other','our','own','rather','said','say','says','she','should','since','so','some','than','that','the','their','them','then','there','these','they','this','tis','to','too','twas','us','wants','was','we','were','what','when','where','which','while','who','whom','why','will','with','would','yet','you','your']
#I find this at https://www.textfixer.com/tutorials/common-english-words.txt

def to_be_removed(wordlist, stop_words):
    return [w for w in wordlist if w not in stop_words]

wordlist = to_be_removed(wordlist0, stop_words)

dictionary = WordListToFreqDict(wordlist)
sorteddict = sortFreqDict(dictionary)
 
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
b = zip(a,sorteddict)
c = list(b)
print(c)

#refer to: https://programminghistorian.org/en/lessons/counting-frequencies

import csv

with open('output.csv','w',) as f:
    mywriter=csv.writer(f)
    mywriter.writerow(['rank','frequency/keyword'])
    for i in range(0,14):
        mywriter.writerow(c[i])
