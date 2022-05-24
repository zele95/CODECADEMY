# %%
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn.compose import ColumnTransformer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, InputLayer
from sklearn.metrics import classification_report
from tensorflow.keras.utils import to_categorical
import numpy as np

# load data
data = pd.read_csv('heart_failure_clinical_records_dataset.csv')
# create strings
data['death_event'] = data.DEATH_EVENT.replace({1:'yes',0:'no'})
data.info()

# get classes
print(Counter(data.death_event))

# separate labels and features
y = data.death_event
x = data[['age','anaemia','creatinine_phosphokinase','diabetes','ejection_fraction','high_blood_pressure','platelets','serum_creatinine','serum_sodium','sex','smoking','time']]

# hot encode numerical data and split
x = pd.get_dummies(x)
X_train, X_test, y_train, y_test  = train_test_split(x,y)

# standardize data
ct = ColumnTransformer([('scale', StandardScaler(),['age','creatinine_phosphokinase','ejection_fraction','platelets','serum_creatinine','serum_sodium','time'])])

X_train = ct.fit_transform(X_train)
X_test = ct.transform(X_test)

# encode labels
le = LabelEncoder()
y_train = le.fit_transform(y_train)
y_test = le.transform(y_test)
# convert them to categorical vectors
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# crete a model
model = Sequential()
model.add(InputLayer(input_shape = (X_train.shape[1],)))
model.add(Dense(2,activation = 'softmax'))
model.compile(loss = 'categorical_crossentropy', optimizer = 'Adam', metrics = ['accuracy'])

# fit and evaluate model
model.fit(X_train,y_train, epochs = 100, batch_size = 16, verbose = 1)
loss, acc = model.evaluate(X_test, y_test)
print(loss, acc)

# check the accuracy, f1-score
y_estimate = np.argmax(model.predict(X_test), axis = 1)
y_true = np.argmax(y_test, axis = 1)
print(classification_report(y_true,y_estimate))