from nltk.stem import PorterStemmer

porter = PorterStemmer()


# Example words to be stemmed
words = ["running", "runs", "runner", "easily", "fairly"]

# Stem each word and display the result
for word in words:
    stemmed_word = porter.stem(word)
    print(f"{word} -> {stemmed_word}")