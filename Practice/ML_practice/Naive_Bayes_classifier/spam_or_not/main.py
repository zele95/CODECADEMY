# %%
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from preprocessing import preprocess_text

labels = []
messages = []

#load data into list 
with open('SMSSpamCollection') as f:
    for line in f:
        splitted = line.split('\t')
        labels.append( splitted[0])
        messages.append( splitted[1])

# print(len(messages))
# print(len(labels))

# process messages and labels
training_docs = [preprocess_text(message) for message in messages]
training_labels = [0  if x == 'ham' else 1 for x in labels]


test_text = """
Dear Mr. Haber-Zelanto,


thank you for the information but it would not have been necessary. But it’s fine, so we’ll talk to you tomorrow!

Have a great afternoon

Best wishes
"""

# bag of words
bow_vectorizer = CountVectorizer()

training_vectors = bow_vectorizer.fit_transform(training_docs)
test_vectors = bow_vectorizer.transform([test_text])

# Naive Bayes Classifier
spam_classifier = MultinomialNB()
spam_classifier.fit(training_vectors, training_labels)

predictions = spam_classifier.predict(test_vectors)
# print(predictions)
print("Looks like a normal email!" if predictions[0] == 0 else "You've got spam!")
