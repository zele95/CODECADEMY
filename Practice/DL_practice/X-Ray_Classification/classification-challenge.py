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

training_data_generator = ImageDataGenerator(rescale = 1./255,
                                            # vertical_flip = True,
                                            zoom_range = 0.1,
                                            rotation_range = 15,
                                            width_shift_range = 0.05,
                                            height_shift_range = 0.05
                                            ) 
 
# print(training_data_generator.__dict__)

print("\nLoading train data...")

training_iterator = training_data_generator.flow_from_directory(DIRECTORY_TRAIN,
                                                        class_mode=CLASS_MODE,
                                                        color_mode=COLOR_MODE,
                                                        target_size=TARGET_SIZE,
                                                        batch_size=BATCH_SIZE,
                                                        # shuffle = False
                                                        )

validation_data_generator = ImageDataGenerator(rescale = 1./255) 


print("\nLoading validation data...")

validation_iterator = validation_data_generator.flow_from_directory(DIRECTORY_TEST,
                                                    class_mode=CLASS_MODE,
                                                    color_mode=COLOR_MODE,
                                                    target_size=TARGET_SIZE,
                                                    batch_size=BATCH_SIZE,
                                                    shuffle = False
                                                    )


# build model

def build_model():
    model = Sequential()
    model.add(layers.Input(shape = (256,256,1)))
    # convolutional hidden layers with relu functions
    # maxpooling layers and dropout layers as well
    model.add(layers.Conv2D(5, 5, strides=1, activation="relu"))
    # model.add(layers.MaxPooling2D(
    #     pool_size=(2, 2), strides=(2,2)))
    # model.add(layers.Dropout(0.1))

    # model.add(layers.Conv2D(3, 3, strides=1, activation="relu")) 
    # model.add(layers.MaxPooling2D(
    #     pool_size=(2, 2), strides=(2,2)))
    # model.add(layers.Dropout(0.2))

    model.add(layers.Flatten())
    model.add(layers.Dense(3,activation = 'softmax'))

    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
                    loss=tf.keras.losses.CategoricalCrossentropy(), # sparse
                    metrics=[tf.keras.metrics.CategoricalAccuracy(),tf.keras.metrics.AUC()])

    model.summary()
    return model

print("\nBuilding model...")

model = build_model()

# early stopping implementation
es = EarlyStopping(monitor='val_auc', mode='min', verbose=1, patience=10)

# train model
print("\nTraining model...")

history = model.fit(training_iterator,
                    steps_per_epoch=training_iterator.samples/BATCH_SIZE,
                    epochs=60,
                    validation_data=validation_iterator ,
                    validation_steps=validation_iterator.samples/BATCH_SIZE,
                    callbacks = [es],
                    )

# print(history.history)
print(history.params)

# plot accuracy and auc
fig = plt.figure()

axes1 = fig.add_subplot(2,1,1) #,figsize=(25,10)
axes1.plot(history.history['categorical_accuracy'])
axes1.plot(history.history['val_categorical_accuracy'])
plt.grid()
axes1.set_title('model accuracy')
axes1.set_xlabel('epoch')
axes1.set_ylabel('accuracy')
axes1.set_xticks(range(len(history.history['auc'])),labels = map(str,range(1,len(history.history['auc'])+1)))
axes1.legend(['train', 'validation'], loc='upper left')

axes2 = fig.add_subplot(2,1,2)
axes2.plot(history.history['auc'])
axes2.plot(history.history['val_auc'])
plt.grid()
axes2.set_title('model auc')
axes2.set_xlabel('epoch')
axes2.set_ylabel('auc')
axes2.set_xticks(range(len(history.history['auc'])),labels = map(str,range(1,len(history.history['auc'])+1)))
axes2.legend(['train', 'validation'], loc='upper left')

fig.tight_layout()
plt.show()

# get classification report and confusion matrix

test_steps_per_epoch = np.math.ceil(validation_iterator.samples / validation_iterator.batch_size)
predictions = model.predict(validation_iterator, steps=test_steps_per_epoch)
predicted_classes = np.argmax(predictions, axis=1)
true_classes = validation_iterator.classes
class_labels = list(validation_iterator.class_indices.keys())
report = classification_report(true_classes, predicted_classes, target_names=class_labels)
print(report)   

cm=confusion_matrix(true_classes,predicted_classes)
print(cm)
