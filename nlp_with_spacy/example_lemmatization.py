import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("I was reading the paper.")

for token in doc:
    print(f"{token.text}  -->  {token.lemma_}")