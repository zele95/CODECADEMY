from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# get training data
train_emails = fetch_20newsgroups(categories = ['comp.sys.ibm.pc.hardware','rec.sport.hockey'],subset= 'train',shuffle = True, random_state = 108)
print(train_emails.target_names)
print(train_emails.data[5])
print(train_emails.target[5])

# get test data
test_emails = fetch_20newsgroups(categories = ['comp.sys.ibm.pc.hardware','rec.sport.hockey'],subset= 'test',shuffle = True, random_state = 108)

# create bag of words
counter = CountVectorizer()

# fit and transform data into feature vectors
counter.fit(test_emails.data+ train_emails.data) # why with both train and test data?
train_counts = counter.transform(train_emails.data)
test_counts = counter.transform(test_emails.data)

# create and fit Naive Bayes Classifier
classifier = MultinomialNB()
classifier.fit(train_counts,train_emails.target)
# see the accuracy
print(classifier.score(test_counts,test_emails.target))