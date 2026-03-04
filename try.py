import nltk

def fetch():
    text = input("Enter text: ")
    sentences = nltk.sent_tokenize(text)
    return sentences

t = fetch()
print(t)
print(t)
