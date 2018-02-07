import json
import math
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
sentAnalysis = []
wordData = ""
i = 0

for i in range(len(tweetData)):
    tweet = tweetData[i]["text"]
    wordData = wordData + " " + tweet
    tweet = TextBlob(tweet)
    tweetPolarity = tweet.sentiment.polarity
    sentAnalysis.append(tweetPolarity)
    i += 1

sentAnalysis.sort()

#25 tweets per bin
binAmount = math.ceil(len(sentAnalysis)/10)

#graph
plt.hist(sentAnalysis, binAmount)
plt.xlabel("Polarity")
plt.ylabel("Number of Tweets")
plt.title("Tweet Polarity")
plt.axis([sentAnalysis[0], sentAnalysis[-1], 0, len(sentAnalysis)])
plt.grid(True)
#plt.show()

wordData = TextBlob(wordData)
wordData = wordData.noun_phrases
wordcloud = WordCloud().generate(wordData)
