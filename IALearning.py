# A continuacion implementaremos machine learning de Tensor Flow

from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf

import tensorflow_datasets as tfds
import os
from os import scandir


path = "."
#Lista vacia para incluir los ficheros
lstFiles =[]

#Lista con todos los ficheros del directorio:
lstDir = os.walk(path)

def ls2(path):
    return [obj.name for obj in scandir(path) if obj.is_file()]



#Creamos una lista de los ficheros pdf que existen en el directorio y los incluyo en la lista
for root,dirs,ficheros in lstDir:
    for fichero in ficheros:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if(extension == ".pdf"):
            lstFiles.append(nombreFichero+extension)
            print("EL NOMBRE DE LOS FICHEROS: ", nombreFichero)

print(lstFiles)
print("LISTADO FINALIZADO")
print ("longitud de la lista = ", len(lstFiles))

ficheroSalida = []
for proyect in lstFiles:

    print(proyect)
    nombredirectorio="Directorio"+proyect
    ficheroSalida.append(nombredirectorio)
    print("EL NOMBRE DEL DIRECTORIO ES: ", nombredirectorio)


print(ficheroSalida)
print("LISTADO FINALIZADO DE DIRECTORIOS")
print ("longitud de la lista = ", len(ficheroSalida))




ficherosObjetivo = []
for proyect in lstFiles:
    for archivos in ficheroSalida:
        files = ls2(archivos)
        print("ESPERAMOS QUE SALGAN LOS NOMBRES DE LOS ARCHIVOS DENTRO DE UN DIRECTORIO", files)
        for file in files:
            (nombreFichero, extension) = os.path.splitext(file)
            print("AQUI TENEMOS LOS NOMBRES DE LOS ARCHIVOS: ",nombreFichero)
            if(nombreFichero==proyect+ "salidaUnida"):
                ficherosObjetivo.append(file)
                print("MOSTRAMOS COMO AUMENTA EL ARRAY CON LOS SALIDAS UNIDAS",ficherosObjetivo)

    print("AQUI TENEMOS LOS SALIDA UNIDAS BUSCADOS:",ficherosObjetivo)
    print("LISTADO FINALIZADO")
    print ("longitud de la lista = ", len(ficherosObjetivo))


for name in ficherosObjetivo:
    print("AQUI TENEMOS LOS NOMBRES DE LAS SALIDAS", name)
    DIRECTORY_URL = 'https://storage.googleapis.com/download.tensorflow.org/data/illiad/'
    text_dir = tf.keras.utils.get_file(name, origin=DIRECTORY_URL+name)
    parent_dir = os.path.dirname(text_dir)

    parent_dir




def labeler(example, index):
    return example, tf.cast(index, tf.int64)


labeled_data_sets = []

for i, file_name in enumerate(ficherosObjetivo):
    lines_dataset = tf.data.TextLineDataset(os.path.join(parent_dir, file_name))
    labeled_dataset = lines_dataset.map(lambda ex: labeler(ex, i))
    labeled_data_sets.append(labeled_dataset)

BUFFER_SIZE = 50000
BATCH_SIZE = 64
TAKE_SIZE = 5000

all_labeled_data = labeled_data_sets[0]
for labeled_dataset in labeled_data_sets[1:]:
    all_labeled_data = all_labeled_data.concatenate(labeled_dataset)

all_labeled_data = all_labeled_data.shuffle(
    BUFFER_SIZE, reshuffle_each_iteration=False)


for ex in all_labeled_data.take(5):
    print(ex)

tokenizer = tfds.features.text.Tokenizer()

vocabulary_set = set()
for text_tensor, _ in all_labeled_data:
    some_tokens = tokenizer.tokenize(text_tensor.numpy())
    vocabulary_set.update(some_tokens)

vocab_size = len(vocabulary_set)
vocab_size

encoder = tfds.features.text.TokenTextEncoder(vocabulary_set)
example_text = next(iter(all_labeled_data))[0].numpy()
print(example_text)

encoded_example = encoder.encode(example_text)
print(encoded_example)


def encode(text_tensor, label):
    encoded_text = encoder.encode(text_tensor.numpy())
    return encoded_text, label


def encode_map_fn(text, label):
  # py_func doesn't set the shape of the returned tensors.
  encoded_text, label = tf.py_function(encode,
                                       inp=[text, label],
                                       Tout=(tf.int64, tf.int64))

  # `tf.data.Datasets` work best if all components have a shape set
  #  so set the shapes manually:
  encoded_text.set_shape([None])
  label.set_shape([])

  return encoded_text, label


all_encoded_data = all_labeled_data.map(encode_map_fn)

train_data = all_encoded_data.skip(TAKE_SIZE).shuffle(BUFFER_SIZE)
train_data = train_data.padded_batch(BATCH_SIZE, padded_shapes=([None],[]))

test_data = all_encoded_data.take(TAKE_SIZE)
test_data = test_data.padded_batch(BATCH_SIZE, padded_shapes=([None],[]))

sample_text, sample_labels = next(iter(test_data))

sample_text[0], sample_labels[0]

vocab_size += 1

model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(vocab_size, 64))
model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)))
# One or more dense layers.
# Edit the list in the `for` line to experiment with layer sizes.
for units in [64, 64]:
  model.add(tf.keras.layers.Dense(units, activation='relu'))

# Output layer. The first argument is the number of labels.
model.add(tf.keras.layers.Dense(3))

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_data, epochs=3, validation_data=test_data)
eval_loss, eval_acc = model.evaluate(test_data)

print('\nEval loss: {:.3f}, Eval accuracy: {:.3f}'.format(eval_loss, eval_acc))

#sample_text, sample_labels = next(iter(test_data))

#sample_text[0], sample_labels[0]
#vocab_size += 1
#model = tf.keras.Sequential()
#model.add(tf.keras.layers.Embedding(vocab_size, 64))
#model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)))
# One or more dense layers.
# Edit the list in the `for` line to experiment with layer sizes.
#for units in [64, 64]:
 #   model.add(tf.keras.layers.Dense(units, activation='relu'))

# Output layer. The first argument is the number of labels.
#model.add(tf.keras.layers.Dense(3))
#model.compile(optimizer='adam',
 #             loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
  #            metrics=['accuracy'])
#model.fit(train_data, epochs=3, validation_data=test_data)
#eval_loss, eval_acc = model.evaluate(test_data)

#print('\nEval loss: {:.3f}, Eval accuracy: {:.3f}'.format(eval_loss, eval_acc))
