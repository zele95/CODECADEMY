# %%
import numpy as np
import re

# Importing our translations
# for example: "spa.txt" or "spa-eng/spa.txt"
data_path = "spa.txt"

# Defining lines as a list of each line
with open(data_path, 'r', encoding='utf-8') as f:
  lines = f.read().split('\n')

# Building empty lists to hold sentences
input_docs = []
target_docs = []
# Building empty vocabulary sets
input_tokens = set()
target_tokens = set()

# print(lines)
print(lines[-5:-1])

# line2 = 'In 1969, Roger Miller recorded a song called "You Don't Want My Love." Today, this song is better known as "In the Summer Time." It's the first song he wrote and sang that became popular.	En 1969, Roger Miller grabó una canción llamada "Tú no quieres mi amor". Hoy, esta canción es más conocida como "En el verano". Es la primera canción que escribió y cantó que se convirtió popular.	CC-BY 2.0 (France) Attribution: tatoeba.org #552259 (American) & #1940149 (teskmon)
# '
# line = 'One day, I woke up to find that God had put hair on my face. I shaved it off. The next day, I found that God had put it back on my face, so I shaved it off again. On the third day, when I found that God had put hair back on my face again, I decided to let God have his way. That''s why I have a beard.	Un día, me desperté y vi que Dios me había puesto pelo en la cara. Me lo afeité. Al día siguiente, vi que Dios me lo había vuelto a poner en la cara, así que me lo afeité otra vez. Al tercer día, cuando vi que Dios me había puesto pelo en la cara de nuevo, decidí que Dios se saliera con la suya. Por eso tengo barba.	CC-BY 2.0 (France) Attribution: tatoeba.org #10104877 (CK) & #10106093 (manufrutos)'
# input_doc, target_doc = line.split('\t')[:2]

# print(input_doc)
# print(target_doc)
# %%
print(lines[-1])
