import spacy
nlp = spacy.load("en_core_web_sm")

text = "This is an example sentence with some stop words."

for word in text.split(" "):
    if word in  nlp.Defaults.stop_words:
        print(word ," is stop word")
