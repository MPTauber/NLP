from textblob import TextBlob
import nltk

# nltk.download("stopwords") 
# only have to do this ^ once

from nltk.corpus import stopwords
from pathlib import Path


stops = stopwords.words("english")

blob = TextBlob("Today is a beautiful day.")

print([word for word in blob.words if word not in stops]) # list comprehension
# had to add blob.word so it cycles through words and not sentences (like in blob.sentence())

## Result is: ['Today', 'beautiful', 'day']
## Theses are the words that are NOT stopwords

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

items = blob.word_counts.items() # list of tuples with every word plus their corresponding freuqency in the text


items_not_in_stops = [item for item in items if item[0] not in stops] ## we do item[0] because it only needs the word part of ('tragedy',1), 
#and that is the first object
# print(items_not_in_stops)

####################################################################################
# Now we want the TOP 20 words:
from operator import itemgetter ## this helps sort new list (operator is native to python)

sorted_items = sorted(items_not_in_stops, key = itemgetter(1), reverse=True)  # the 1 stands for [1], so the second part of the object
# reverse reverses sorted order and shows the highest numbers first. 

top20 = sorted_items[:21]
print(top20)

#####################################################################################
# pip install pandas
# pip install wordcloud
# pip install imageio
#pip install matplotlib
import pandas as pd


df = pd.DataFrame(top20, columns = ["word","count"])
print(df)

import matplotlib.pyplot as plt

df.plot.bar(x="word", y="count", rot=0, legend=False, 
color = ["y", "c", "m", "b","g","r"])

plt.gcf().tight_layout # gcf means get current figure

##plt.show()      #DO NOT FORGET!!!

###########################################################################################
## Now we make a text cloud in a heart shape
from wordcloud import WordCloud
import imageio

text = Path("RomeoAndJuliet.txt").read_text()

mask_image = imageio.imread('mask_heart.png')

wordcloud = WordCloud(colormap = "PuRd", mask=mask_image, background_color = "white")

wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file("RomeoAndJulietHeart.png")
plt.imshow(wordcloud)

print("done")
