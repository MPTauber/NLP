from pathlib import Path
from textblob import TextBlob
from textblob import Word

blob = TextBlob(Path('RomeoAndJuliet.txt').read_text())

print(blob.words.count('Joy')) ### counts how many times 'joy' is said in the play

happy = Word('happy')
print(happy.definitions) # searches through wordnet 19 (database by Princeton) and gives defintinions of words

print(happy.synsets) # gets synonyms --> all of these are lemma objects

synonyms = set() # by using a set we eliminate duplicates
for synset in happy.synsets:
    for x in synset.lemmas(): # lemma object represents all the synonyms (because theya re lemma objects)
        synonyms.add(x.name()) #lemma.name method adds specific synonyms from earlier set
print(synonyms)  ### just gives all the words without the weird stuff with them

#########################################################################################################
# pip install nltk
from nltk.corpus import stopwords

stops = stopwords.word("english") #supposed to give all the stopwords in the english language