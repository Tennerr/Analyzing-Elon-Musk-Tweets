from collections import Counter
import csv
from operator import itemgetter
import matplotlib.pyplot as plt
ignoreWords = ["the", "that", "an", "a", "for", "in", "be", "by", "or", "and", "with"]
freq = None
counter = {}
with open ("TweetsElonMusk.csv", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for col in reader:
        for tweet in col:
            words = [x.lower() for x in tweet.split()] 
            for word in [s for s in words if not (s in ignoreWords)]:
                if word not in counter:
                    counter[word] = 0
                counter[word]+=1
res = dict(sorted(counter.items(), key = itemgetter(1), reverse = True)[:10])
print("The top 10 values pairs are " + str(res))
names = list(res.keys())
values = list(res.values())
plt.bar(range(len(res)), values, tick_label=names)
plt.savefig('fig.png')