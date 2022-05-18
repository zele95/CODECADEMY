# %%
# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow	import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras import layers
from tensorflow.keras.layers import InputLayer
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from scikeras.wrappers import KerasRegressor

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.compose import ColumnTransformer
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.metrics import make_scorer

# %% 
# inspect data
admissions = pd.read_csv('admissions_data.csv')
print(admissions.head())
print(admissions.info())

# %%
# clean column names
admissions.columns = admissions.columns.str.strip()
print(admissions.columns)

# %%
# select features and labels
features = admissions.iloc[:,1:-1]
labels = admissions['Chance of Admit']

# %%
# split test train data, standardize

# split
X_train, X_test, y_train, y_test = train_test_split(features,labels)

# select numerical features
numerical_features = features.select_dtypes(['float64','int64'])
numerical_columns = numerical_features.columns

ct = ColumnTransformer([("only numeric", StandardScaler(), numerical_columns)], remainder='passthrough')

# standardize using ColumnTransformer
X_train_std = ct.fit_transform(X_train)
X_test_std = ct.transform(X_test)

# back to dataframe
X_train_std = pd.DataFrame(X_train_std, columns = features.columns)
X_test_std = pd.DataFrame(X_test_std, columns = features.columns)

# %%
# create model

# set the model
def design_model(X = X_train_std,learning_rate = 0.01):
    model = Sequential()
    input = InputLayer(input_shape = (X.shape[1],))
    model.add(input)
    model.add(Dense(64, activation = "relu"))
    model.add(layers.Dropout(0.2)) # regularization method
    model.add(Dense(1))
    # print(model.summary())

    # set optimizer
    opt = Adam(learning_rate = learning_rate)
    model.compile(loss = 'mse', metrics = ['mae'], optimizer = opt)
    return model

learning_rate = 0.01
model = design_model(X_train_std,learning_rate)
# %%
# train the model

# fit and evaluate
def fit_model(model, features_train, labels_train, num_epochs, batch_size):

    es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience = 10)
    history = model.fit(features_train, labels_train, epochs=num_epochs, batch_size= batch_size, verbose=1, validation_split = 0.2, callbacks = [es])
    return history

num_epochs = 40
batch_size = 2
history = fit_model(model, X_train_std, y_train, num_epochs, batch_size)

# %%
# evaluate the model
res_mse,res_mae = model.evaluate(X_test_std,y_test, verbose = 0)
print()
print('RMSE:',res_mse)
print('MAE:',res_mae)

predicted_values = model.predict(X_test_std, verbose = 0) 
print('R2:', r2_score(y_test, predicted_values))
# %%

def plot(history):
  #plotting
  fig, axs = plt.subplots(1, 2, gridspec_kw={'hspace': 1, 'wspace': 0.5}) 
  (ax1, ax2) = axs
  ax1.plot(history.history['loss'], label='train')
  ax1.plot(history.history['val_loss'], label='validation')
  ax1.legend(loc="upper right")
  ax1.set_xlabel("# of epochs")
  ax1.set_ylabel("loss (mse)")

  ax2.plot(history.history['mae'], label='train')
  ax2.plot(history.history['val_mae'], label='validation')
  ax2.legend(loc="upper right")
  ax2.set_xlabel("# of epochs")
  ax2.set_ylabel("MAE")

plot(history)

# %%
# tunning the learning_rates manually
learning_rates = [1E-3, 0.01, 0.1, 1, 10]
num_epochs = 30
batch_size = 2 

plt.figure(figsize=(12,8))
for i in range(len(learning_rates)):
  plot_no = 420 + (i+1)
  plt.subplot(plot_no)
  model = design_model(X_train_std, learning_rates[i])
  history = fit_model(model,X_train_std, y_train, num_epochs, batch_size)

  plt.plot(history.history['loss'], label='train')
  plt.plot(history.history['val_loss'], label='validation')
  plt.legend(loc="upper right")
  plt.grid()
  plt.title('lrate=' + str(learning_rates[i]))
  plt.xlabel("# of epochs")
  plt.ylabel("loss (mse)")

plt.tight_layout()
plt.show()

# %%
# tunning the batch_size manually

#fixed learning rate 
learning_rate = 0.1 
#fixed number of epochs
num_epochs = 30
#we choose a number of batch sizes to try out
batches = [2,4,16,32] 

#plotting code
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize = (5,8), sharex='col', sharey='row',
                        gridspec_kw={'hspace': 0.7, 'wspace': 0.4}) #preparing axes for plotting
axes = [ax1, ax2, ax3, ax4]

#iterate through all the batch values
for i in range(len(batches)):
    model = design_model(X_train_std, learning_rates[i])
    history = fit_model(model,X_train_std, y_train, num_epochs, batch_size)
    axes[i].plot(history.history['mae'], label='train')
    axes[i].plot(history.history['val_mae'], label='validation')
    axes[i].set_title('batch = ' + str(batches[i]), fontdict={'fontsize': 8, 'fontweight': 'medium'})
    axes[i].set_xlabel('# epochs')
    axes[i].set_ylabel('mae')
    axes[i].grid()
    axes[i].legend()

# %%
# tunning with grid search

def do_grid_search():
    batch_size = [2,6]
    epochs = [40,50]
    model = KerasRegressor(model=design_model,verbose = 0)
    param_grid = dict(batch_size=batch_size, epochs=epochs)
    grid = GridSearchCV(estimator = model, param_grid=param_grid, scoring = make_scorer(mean_squared_error, greater_is_better=False),return_train_score = True)
    grid_result = grid.fit(X_train_std, y_train, verbose = 0)
    print(grid_result)
    print()
    print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
    print()
    means = grid_result.cv_results_['mean_test_score']
    stds = grid_result.cv_results_['std_test_score']
    params = grid_result.cv_results_['params']
    for mean, stdev, param in zip(means, stds, params):
        print("%f (%f) with: %r" % (mean, stdev, param))
    print()

print("-------------- GRID SEARCH --------------------")
do_grid_search()
