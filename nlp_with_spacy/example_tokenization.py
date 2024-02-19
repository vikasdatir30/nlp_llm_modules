import spacy

nlp = spacy.load("en_core_web_sm")

text ="Tokenization is a crucial step in natural language processing."

doc = nlp(text)

for token in doc:
    print(token)