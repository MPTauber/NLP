## py -3 -m venv nlp_venv
## nlp_venv/scripts/activate
## pip install textblob
## py -m textblob.download_corpora
from textblob import TextBlob

text = 'Today is a beautiful day. Tomorrow looks like bad weather.'

blob =TextBlob(text)

#print(blob)

# print(blob.sentences) ## creates sentences object

# print(blob.words)

# print(blob.tags)  ## breaks down every word with its tag. For example: Today (NN--> noun), beautiful (JJ --> adjective)

# print(blob.noun_phrases) 

#print(blob.sentiment) # shows polarity and subjectvity

#print(round(blob.sentiment.polarity,3)) # rounds to 3 decimal places
#print(round(blob.sentiment.subjectivity,3)) 

# sent_list = blob.sentences ## puts the sentences in "blob" vairable into list

# for sentence in sent_list:  # shows scores for each sentence
#     print(round(sentence.sentiment.polarity,3))
#     print(round(sentence.sentiment.subjectivity,3))


# ##########################################################
# from textblob.sentiments import NaiveBayesAnalyzer

# blob = TextBlob(text, analyzer= NaiveBayesAnalyzer()) ## we used the default analyzer above

# print(blob.sentiment)  # whichever number is higher shows its polarity. This one is .47 positive, and .52 negative, so it's slightly negative

# sent_list = blob.sentences ## puts the sentences in "blob" vairable into list

# for sentence in sent_list:  # shows scores for each sentence
#     print(sentence.sentiment)  # took off round, sentiment, and polarity because using different analyzer thatd doesnt require it
#     ### shows first sentence is positive and second is negative

# ##########################################################
# print(blob.detect_language()) ### finds out which language this is in

# spanish = blob.translate(to='es')
# print(spanish)

# german = blob.translate(to='de')   # translates the "blob" variable to german
# print(german)

###########################################################
from textblob import Word

my_word = Word('theyr')
print(my_word.spellcheck()) ## [('they', 0.5713042216741622), ('their', 0.42869577832583783)]
### means confidence is higher that the word is supposed to be 'they'

new_word = my_word.correct()  ## corrects it to 'they' automatically because confidence is higher for this
print(new_word)

my_sentence = TextBlob('Ths sentense has missplld wrds.')

new_sentence = my_sentence.correct()
print(new_sentence)
