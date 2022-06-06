# %%
# import necessary libraries 
from cgi import test
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras import layers

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import matplotlib.pyplot as plt
import numpy as np


# load data

#Construct an ImageDataGenerator object:
DIRECTORY_TRAIN = "Covid19-dataset/train"
DIRECTORY_TEST = "Covid19-dataset/test"
CLASS_MODE = "categorical"
COLOR_MODE = "grayscale"
TARGET_SIZE = (256,256)
BATCH_SIZE = 32

data_generator = ImageDataGenerator(rescale = 1./255) 
 

training_iterator = data_generator.flow_from_directory(DIRECTORY_TRAIN,
                                                        class_mode=CLASS_MODE,
                                                        color_mode=COLOR_MODE,
                                                        target_size=TARGET_SIZE,
                                                        batch_size=BATCH_SIZE)

validation_iterator = data_generator.flow_from_directory(DIRECTORY_TEST,
                                                    class_mode=CLASS_MODE,
                                                    color_mode=COLOR_MODE,
                                                    target_size=TARGET_SIZE,
                                                    batch_size=BATCH_SIZE)




def build_model():
    model = Sequential()
    model.add(layers.Input(shape = (256,256,1)))
    model.add(layers.Conv2D(4, 5, strides=2, activation="relu")) 
    model.add(layers.Flatten())
    model.add(layers.Dense(3,activation = 'softmax'))

    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
                    loss=tf.keras.losses.CategoricalCrossentropy(), # sparse
                    metrics=[tf.keras.metrics.CategoricalAccuracy(),tf.keras.metrics.AUC()])

    model.summary()
    return model

model = build_model()

history = model.fit(training_iterator,
                    steps_per_epoch=training_iterator.samples/BATCH_SIZE,
                    epochs=5,
                    validation_data=validation_iterator ,
                    validation_steps=validation_iterator.samples/BATCH_SIZE)

# loss, acc = model.evaluate(X_test, y_test)
# print(loss, acc)


# y_estimate = np.argmax(model.predict(X_test), axis = 1)
# y_true = np.argmax(y_test, axis = 1)
# print(classification_report(y_true,y_estimate))
print(history.history)


fig = plt.figure()

axes1 = fig.add_subplot(2,1,1) #,figsize=(25,10)

axes1.plot(history.history['categorical_accuracy'])
axes1.plot(history.history['val_categorical_accuracy'])
plt.grid()
axes1.set_title('model accuracy')
axes1.set_xlabel('epoch')
axes1.set_ylabel('accuracy')
axes1.legend(['train', 'validation'], loc='upper left')

axes2 = fig.add_subplot(2,1,2)

axes2.plot(history.history['auc'])
axes2.plot(history.history['val_auc'])
plt.grid()
axes2.set_title('model auc')
axes2.set_xlabel('epoch')
axes2.set_ylabel('auc')
axes2.legend(['train', 'validation'], loc='upper left')

fig.tight_layout()
plt.show()
