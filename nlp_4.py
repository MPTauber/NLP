# pip install StaCy
# py -m spacy download en  (## will give a warning)

import spacy
########################################################################
## This basically gives the categories of the objects in our tetdx. So 1994 --> date, Tim --> person, etc.

nlp = spacy.load("en_core_web_sm")

document = nlp("In 1994, Tim Bernes-Lee founded the World Wide WebConsortium" +
" (W3C), devoted to developing web technologies")

for entity in document.ents: #ents is short for entities
    print(entity.text, ":", entity.label_)

#####################################################
### Finds how similar two texts are:
#####################################################

from pathlib import Path

document1 = nlp(Path('RomeoAndJuliet.txt').read_text())
document2 = nlp(Path('EdwardTheSecond.txt').read_text())

print(document1.similarity(document2))