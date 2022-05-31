# %%
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from sklearn.model_selection import train_test_split
from utils import load_galaxy_data

# import app

# load data
input_data, labels = load_galaxy_data()
print(input_data.shape)
print(labels.shape)

# split data
x_train, x_valid, y_train, y_valid = train_test_split(input_data, labels, test_size=0.20, stratify=labels, shuffle=True, random_state=222)

# create data iterators
data_generator = ImageDataGenerator(rescale=1./255,
                                    # vertical_flip = True,
                                    # zoom_range = 0.2,
                                    # rotation_range = 15,
                                    # width_shift_range = 0.05,
                                    # height_shift_range = 0.05
                                    )

training_iterator = data_generator.flow(x_train, y_train,batch_size=5)
validation_iterator = data_generator.flow(x_valid, y_valid, batch_size=5)

# or before the split (from directory) for example
# DIRECTORY = "data/train"
# CLASS_MODE = "categorical"
# COLOR_MODE = "grayscale"
# TARGET_SIZE = (256,256)
# BATCH_SIZE = 32

# training_iterator = training_data_generator.flow_from_directory(DIRECTORY,
#                                                               class_mode=CLASS_MODE,
#                                                               color_mode=COLOR_MODE,
#                                                               target_size=TARGET_SIZE,
#                                                               batch_size=BATCH_SIZE)

# iterste over data
# sample_batch_input,sample_batch_labels  = training_iterator.next()
 
# print(sample_batch_input.shape,sample_batch_labels.shape)

# build model
model = tf.keras.Sequential()
model.add(tf.keras.Input(shape=(128, 128, 3)))
model.add(tf.keras.layers.Conv2D(8, 3, strides=2, activation="relu")) 
model.add(tf.keras.layers.MaxPooling2D(
    pool_size=(2, 2), strides=(2,2)))
model.add(tf.keras.layers.Conv2D(8, 3, strides=2, activation="relu")) 
model.add(tf.keras.layers.MaxPooling2D(
    pool_size=(2,2), strides=(2,2)))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(16, activation="relu"))
model.add(tf.keras.layers.Dense(4, activation="softmax"))

# compile model
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss=tf.keras.losses.CategoricalCrossentropy(),
    metrics=[tf.keras.metrics.CategoricalAccuracy(),tf.keras.metrics.AUC()])

model.summary()

# fit model

# steps_per_epoch=training_iterator.samples/BATCH_SIZE

model.fit(
        training_iterator,
        steps_per_epoch=len(x_train)/5,
        epochs=8,
        validation_data=validation_iterator,
        validation_steps=len(x_valid)/5)

# visualize results
from visualize import visualize_activations
visualize_activations(model,validation_iterator)