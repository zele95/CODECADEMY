import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

# load dataset
digits = datasets.load_digits()
# print(digits)
print(digits.DESCR)
print(digits.data)
print(digits.target)

# show one image
plt.matshow(digits.images[100]) 
plt.gray()
plt.show()
print(digits.target[100])

# Figure size (width, height)
fig = plt.figure(figsize=(6, 6))
 
# Adjust the subplots 
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
 
# For each of the 64 images
for i in range(64):
 
    # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position
    ax = fig.add_subplot(8, 8, i+1, xticks=[], yticks=[])
    # Display an image at the i-th position
    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
    # Label the image with the target value
    ax.text(0, 7, str(digits.target[i]))
plt.show()

# create and fit the model
model = KMeans(n_clusters=10, random_state=42)
model.fit(digits.data)

# show first 64 images
fig = plt.figure(figsize=(8, 3))
fig.suptitle('Cluser Center Images', fontsize=14, fontweight='bold')
for i in range(10):
 
  # Initialize subplots in a grid of 2X5, at i+1th position
  ax = fig.add_subplot(2, 5, i+1)
 
  # Display images
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)
plt.show()

# values of a number written by hand
new_sample = np.array([
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.45,6.34,6.79,4.51,1.22,0.00,0.00,0.00,3.82,7.63,5.42,7.56,6.79,0.00,0.00,0.00,2.75,7.63,6.64,7.40,4.43,0.00,0.00,0.00,0.00,2.52,5.65,7.63,2.98,0.00,0.00,0.00,0.00,0.00,0.77,7.63,2.29,0.00,0.00,0.00,0.00,5.03,4.58,7.63,2.29,0.00,0.00,0.00,0.00,5.11,7.63,7.41,1.15,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.38,0.00,0.00,0.00,0.00,0.00,0.46,4.97,7.63,1.46,0.00,0.00,0.69,2.82,6.87,7.63,7.63,1.30,0.00,0.00,5.19,7.63,6.26,4.58,7.63,0.23,0.00,0.00,0.69,1.53,0.15,3.05,7.63,0.00,0.00,0.00,0.00,0.00,0.00,3.05,7.63,0.00,0.00,0.00,0.00,0.00,0.00,3.05,7.63,0.46,0.00],
[0.00,0.00,0.00,0.61,0.00,0.00,0.00,0.00,0.00,0.00,1.83,7.63,1.30,0.00,0.00,0.00,0.00,0.08,5.80,7.32,0.54,0.00,0.00,0.00,0.00,3.59,7.63,2.75,4.96,4.35,0.00,0.00,0.00,7.26,7.10,3.89,7.63,6.11,2.98,0.00,0.00,5.34,6.87,7.25,7.63,6.94,5.72,0.00,0.00,0.00,0.00,3.82,7.10,0.00,0.00,0.00,0.00,0.00,0.00,3.82,6.87,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,0.61,0.77,0.15,0.00,0.00,0.46,4.12,6.33,7.63,7.63,4.51,0.00,0.00,1.83,7.63,5.80,3.74,7.48,5.04,0.00,0.00,0.00,0.00,3.67,6.72,7.56,1.99,0.00,0.00,0.00,0.00,5.04,6.57,7.63,0.69,0.00,0.00,2.29,1.68,0.08,3.59,7.63,0.77,0.00,0.00,6.41,7.63,7.10,7.63,6.03,0.08,0.00,0.00,0.61,3.05,4.58,3.59,0.53,0.00,0.00]
]) # 8143

# predicted values
new_labels = model.predict(new_sample)
print(new_labels)

for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, end='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')
# 5141 - not so good