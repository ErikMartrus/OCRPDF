#Importamos aquí la librería de poppler para poder tratar las imagenes
import shutil

#Importamos la biblioteca de Python para utilizar Tensorflow
import pip
import tensorflow as tf
from tensorflow import keras
import gensim
#De la librería Gensim importamos los métodos para aprender a detectar 'phrases'. La librería Gensim está
#hecha para encontrar phrases que son bigramas pero no trigramas. Si se quieren trigramas los phrases bigramas
#se pueden convertir en un token y luego volver a repetir el proceso. También se pueden aplicar los métodos
#explicados en el apartado 2.

from gensim.models.phrases import Phraser
from gensim.models import Phrases
from pandas import read_csv

import csv
import numpy
import numpy as np


from numpy.distutils.fcompiler import none
import math
#Importamos las librerias necesarias para realizar el OCR
import cv2
import pytesseract
import csv
#Por último añadimos los imports de las librerias necesarias para la creacion de los vectores identificativos

import nltk
import pandas as pd
import gensim
import re
from collections import Counter
from nltk import word_tokenize, pos_tag
from nltk.util import ngrams
from nltk.collocations import *

#Con este último import, importamos el método que crea un diccionario con la frecuencia de aparición de los elementos en fgggea lista
#importamos las librerias de wordcloud
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import(
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
#Importamos la libreria os para la creacion y eliminacion de directorios
#mkdir nos permite crear archivos, y si ponemos ".", hacemos referencia al directorio en el que estamos
import os
from wand.image import Image
class MyImage(Image):
    def brightness_contrast(self, brightness=0.0, contrast=0.0):
        slope=math.tan((math.pi * (contrast/100.0 +1.0)/4.0))
        if slope < 0.0:
            slope=0.0
        intercept=brightness/100.0+((100-brightness)/200.0)*(1.0-slope)
        self.function("polynomial",[slope,intercept])

path = "."
#Lista vacia para incluir los ficheros
lstFiles =[]

#Lista con todos los ficheros del directorio:
lstDir = os.walk(path)

#Creamos una lista de los ficheros pdf que existen en el directorio y los incluyo en la lista
for root,dirs,ficheros in lstDir:
    for fichero in ficheros:
        (nombreFichero, extension) = os.path.splitext(fichero)
        print(extension)
        if(extension == ".pdf"):
            lstFiles.append(nombreFichero+extension)

print(lstFiles)
print("LISTADO FINALIZADO")
print ("longitud de la lista = ", len(lstFiles))




for proyect in lstFiles:

    print(proyect)
    nombredirectorio="Directorio"+proyect
    os.mkdir(nombredirectorio)
#En esta parte realizamos el renderizado de las imagenes con Poppler que en Mac se refiere pdf2image
    pages = convert_from_path(proyect)
    #print(pages)

    print(pages)
    print("longitud de paginas: ", len(pages))
#Se crea la clase MyImage donde se definen los pasos a realizar para aumentar brillo  y contraste.
    for i,page in enumerate(pages):
            fname =proyect+'image'+str(i)+'.png'
            print(fname)
            page.save(fname,'PNG')
            shutil.copy(fname, nombredirectorio)



    if i>0:
        for i, page in enumerate(pages):
            imagenEdit = proyect+'imageEdit' + str(i) + '.png'
            fname = proyect+'image' + str(i) + '.png'
            with MyImage(filename=fname) as img:
                img.brightness_contrast(10, 33)
                img.save(filename=imagenEdit)
                shutil.copy(imagenEdit, nombredirectorio)
                os.remove(fname)

    else:
        with MyImage(filename=proyect+'image0.png') as img:
            img.brightness_contrast(10, 33)
            img.save(filename=proyect+'imagen0Edit.png')
            shutil.copy(proyect+'imagen0Edit.png',nombredirectorio)
            os.remove(fname)



#Ahora nos toca realizar OCR.
    if i>0:
        for i, page in enumerate(pages):
            imagenEdit = proyect+'imageEdit' + str(i) + '.png'
        #Cargamos la imagen utilizando opencv
            imagen = cv2.imread(filename=imagenEdit)
        #Extraemos texto de la imagen
            sret = pytesseract.image_to_string(imagen)
        #Mostramos el resultado
            text = proyect +'salida' + str(i) + '.txt'
            f = open (text,'w')
            f.write(sret)
            f.close()
            shutil.copy(text,nombredirectorio)
            os.remove(imagenEdit)

    else:
        imagen = cv2.imread(filename=proyect+'imagen0Edit.png')
        sret = pytesseract.image_to_string(imagen)
        #Mostramos el resultado
        text = proyect+'salida0.txt'
        f = open (text,'w')
        f.write(sret)
        f.close()
        shutil.copy(text,nombredirectorio)
        os.remove(proyect+'imagen0Edit.png')






    files = []
    for i, page in enumerate(pages):
        text = proyect+'salida' + str(i) + '.txt'
#Buscaremos listar las palabras de nuestro pdf que ha sido convertido en txt
        files.append(text)
        with open(proyect+'salidaUnida.txt', 'w') as outfile:
            for unido in files:
                with open(unido) as infile:
                    for line in infile:
                        if line:
                            outfile.write(line)




#Word_candidates es la lista de palabras resultado de hacer un split del texto allá donde hay un espacio en blanco.
#Consideramos que el resultado es una lista de candidatos porque en realidad, como se explica en el módulo,
#no todos son realmente palabras.

    textoUnido = open(proyect+'salidaUnida.txt', 'r')
    headline = textoUnido.read()
    word_candidates = headline.split()
    #nltk.download(), se ha de ejecutar siempre la primera vez que se ejecuta
#Número de veces que los candidatos a palabra aparecen en el texto
    print("CALCULO MÉTODO SPLIT: ", Counter(word_candidates), "\n")

#Creamos una lista de candidatos a los cuales les quitamos los símbolos '"' y '.'
    stripped_candidates = [w.strip('".') for w in word_candidates]

#Número de veces que los candidatos aparecen en el texto sin signos como puntos de puntuación
    print("CALCULO METODO SIGNIFICANTE-SIGNIFICADO: ", Counter(stripped_candidates), "\n")

#Ahora pasaremos el titulo a minuscula y crearemos una lista de candidatos sin los signos como antes y en minusculas aparecen en el texto
    lower_case_stripped_candidates = [s.lower() for s in stripped_candidates]
    print("CALCULO TRAS CONVERSION A MINUSCULAS: ", Counter(lower_case_stripped_candidates), "\n")

#Tokens es la lista de tokens resultado de aplicar el tokenizer del NLTK al texto headline
    tokens = [w for w in word_tokenize(headline)]
    print("Mostramos tokens")
    print(tokens)


#De la lista de candidatos, queremos quitar los candidatos que no tienen caracteres alfabéticos ('"', '.', etc.).
#Para ello, importamos la librería de Python encargada de la gestión de expresiones regulares

#%%

#alpha_tokens es la lista de tokens del texto que han pasado el filtro. Para obtener la lista:
#1. Se convierte el texto a minúsculas (headline.lower(e
#2. Se tokeniza el texto en minúsculas (word_tokenize(headline.lower()))
#3. Se añaden a la lista alpha_tokens los tokens que empiezan por un caracter alfabético (re.match("^[a-z]+.*))

    alpha_tokens = [w for w in word_tokenize(headline.lower()) if re.match("^[a-z]+.*", w)]
    print("Mostramos alpha_tokens")
    print(alpha_tokens)


#Lista de tokens del texto convertido en minúsculas
    tokens = [w for w in word_tokenize(headline.lower())]


    bigram_measures = nltk.collocations.BigramAssocMeasures()
    trigram_measures = nltk.collocations.TrigramAssocMeasures()


#get_coll_candidates: Obtiene los trigramas, bigramas candidatos a ser una colocación
    def get_coll_candidates(tokens):
        bigramcandidates = BigramCollocationFinder.from_words(tokens)
        trigramcandidates = TrigramCollocationFinder.from_words(tokens)
        return bigramcandidates, trigramcandidates

#re_filter_candidates: De la lista de candidatos se quitan aquellos que tienen algún non-word element
    def re_filter_candidates(bigram_coll_candidates, trigram_coll_candidates):
        bigram_coll_candidates.apply_word_filter(lambda w: (re.match(r'\W',w)))
        trigram_coll_candidates.apply_word_filter(lambda  w: (re.match(r'\W',w)))
        return bigram_coll_candidates, trigram_coll_candidates
#get_n_best_candidates: Obtiene los N mejores candidatos aplicando el calculo del PMI
    def get_n_best_candidates(bigram_candidates, trigram_candidates, n_best_collocations):
        nbest_bigram_candidates = bigram_candidates.nbest(bigram_measures.pmi, n_best_collocations)
        nbest_trigram_candidates = trigram_candidates.nbest(trigram_measures.pmi, n_best_collocations)
        return nbest_bigram_candidates, nbest_trigram_candidates




    stopwords=[]

# Los tokens inicial y final no pueden ser etiquetados con ninguno de los siguientes PoS
    no_pos_in = ['DT', 'IN', 'PRP', 'CC', 'CD', 'MD', 'VBG', 'VBD', 'RP']


# La función filter_collocation_candidates se ha modificado. Si no se ha elegido la opción de filtrar
# con stopwords, la función retorna la lista de candidatos a colocación que superan el test definido
# por la función good_PoS_candidate.

# La función good_PoS_candidate comprueba que el candidato a colocación no tiene un token inicial o final
# etiquetado con una etiqueta de la lista anterior. La función realiza lo siguiente:
# 1. Etiqueta los constituyentes del candidato a colocación con un PoS tagger
# 2. Comprueba que ni la etiqueta de PoS del token inicial ni la etiqueta de PoS del token final están en la lista
# no_pos_in

    def good_PoS_candidate(candidate):
        test = True
        tokens = list(candidate)  # Convertimos la tupla del candidato en una lista de tokens;
        # tokens = ['and', 'reason']
        tagged_tokens = nltk.pos_tag(tokens)  # PoS tagging [('calling', 'VBG'), ('everyone', 'NN')]
        if tagged_tokens[0][1] in no_pos_in or tagged_tokens[-1][1] in no_pos_in:
            test = False
        return test


    def filter_collocation_candidates(candidates):
        # Si hemos cargado una lista de stopwords
        if len(stopwords) > 0:
            # Creamos una lista de candidatos que pasan el test de stopwords
            col_candidates_filtered = [c for c in candidates if good_stw_candidate(c) == True]
        # Si no se filtra por stopwords,
        else:
            # Creamos una lista de candidatos que pasan el test de PoS
            col_candidates_filtered = [c for c in candidates if good_PoS_candidate(c) == True]
        return col_candidates_filtered


    # La función get_n_and_cn llama a la función patterns_and_parser para definir los patterns sintácticos de N y CN, y
    # también los parsers que construirán estos nodos en el árbol

    def patterns_and_parser():
        # Definición de los patterns sintácticos de un nodo N. La hoja de un nodo N es un nombre en singular (NN)
        # o en plural (NNS)
        n_patterns = """
                  N: {<NN>|<NNS>}
                  """
        # Definición de los patterns sintácticos de un nodo CN. Las hojas de un nodo CN son dos nombres en singular
        cn_patterns = """
                  CN: {<NN> <NN>}
                  """
        # Definición del parser que creará los nodos N del árbol
        n_parser = nltk.RegexpParser(n_patterns)
        # Definición del parser que creará los nodos CN del árbol
        cn_parser = nltk.RegexpParser(cn_patterns)
        return n_patterns, cn_patterns, n_parser, cn_parser


    def get_string_form(tuple_list):
        words = [cti[0] for cti in tuple_list]
        string_form = "_".join(words)
        return string_form


    def get_n_and_cn(tagged_tokens):
        # Definir patterns sintácticos y parser
        n_patterns, cn_patterns, n_parser, cn_parser = patterns_and_parser()
        # Creación de los árboles con los nodos N
        n_tree = n_parser.parse(tagged_tokens)
        # Creación de los árboles con los nodos CN
        cn_tree = cn_parser.parse(tagged_tokens)
        # Listado de las hojas de los nodos N
        n_leaves = [s.leaves() for s in n_tree.subtrees() if s.label() == 'N']  # Lista d hojas N. Una hoja es una lista
        # de tuplas (token, PoS)
        # (e.g: [[('philosophers', 'NNS')],...])
        # Listado de las hojas de los nodos CN
        cn_leaves = [s.leaves() for s in cn_tree.subtrees() if s.label() == 'CN']  # Lista de hojas CN
        # (e.g: [('world', 'NN'),
        #        ('event', 'NN')],...])
        # Se unen los dos listados
        n_cn_tuples = n_leaves + cn_leaves
        # Conversión de las tuplas que representan las hojas al término
        n_and_cn = [get_string_form(c) for c in
                    n_cn_tuples]  # e.g: [('world', 'NN'), ('event', 'NN')] -> world_event
        return n_and_cn


    # Tokenización del texto en minúsculas
    tokens = [w for w in word_tokenize(headline.lower())]
    # PoS tagging de los tokens
    tagged_tokens = nltk.pos_tag(tokens)
    # Lista de términos que forman un N o un CN
    n_and_cn = get_n_and_cn(tagged_tokens)
    print("A VER QUE SACAMOS POR AQUI",n_and_cn)



#Importamos la lista que esta en la libreria NLTK
    stopwords=nltk.corpus.stopwords.words('spanish')

#La función good_stw_candidate comprueba qye el candidato a colocación no tiene un token inicial o final en la lista de stopwords
    def good_stw_candidate(candidate):
        test=True
        if candidate[0] in stopwords or candidate[-1] in stopwords:
            test=False
        return test

    def filter_collocations_candidates(candidates):
    #Si hemos cargado una lista de stopwords
        if len(stopwords) >0:
        #Creamos una lista de candidatos que pasan el test de stopwords
            col_candidates_filtered = [c for c in candidates if good_stw_candidate(c) == True]
        else:
            col_candidates_filtered = candidates
        return col_candidates_filtered

    def get_collocations(headlines,n_best_collocations):
    #A partir de los tokens obtenemos los candidatos a colocaciones que son biagramas y trigramas
        bigram_coll_candidates, trigram_coll_candidates = get_coll_candidates(tokens)
        bigram_coll_candidates_filtered, trigram_coll_candidates_filtered = re_filter_candidates(bigram_coll_candidates,trigram_coll_candidates)
    #De los bigramas y trigramas filtrados obtenemos los N mejores candidatos con metodos estadisticos
        best_bigrams_cand, best_trigrams_cand = get_n_best_candidates(bigram_coll_candidates_filtered, trigram_coll_candidates_filtered, n_best_collocations)
    #Se unen los bigramas y trigramas candidatos
        collocation_candidates = best_bigrams_cand + best_trigrams_cand
        print("NGRAMAS CANDIDATOS A SER COLOCACIONES", collocation_candidates,'\n')
    #Se realiza un segundo filtrado a los candidatos a colocación
        collocation_candidates_filtered = filter_collocations_candidates(collocation_candidates)
    #Convertimos cada tupla en un string donde cada elemento de la tupla se une con el "_"
        collocations = ["_".join(cc) for cc in collocation_candidates_filtered]
        return collocations


    collocations = get_collocations(headline.lower(),300)
    collocations = np.array(collocations)
    with open(proyect+"salida.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in range(0, collocations.shape[0]):
            myList = []
            myList.append(collocations[row])
            writer.writerow(myList)
    shutil.copy(proyect + 'salida.csv', nombredirectorio)
    os.remove(proyect+ 'salida.csv')
    print("TERMINOS CANDIDATOS A SER COLOCACIONES", collocations)

#creacion del word cloud


    word2display=" ".join([lu.replace(' ','_') for lu in collocations])
    #print("WORD2DISPLAY VALE ESTO: ",word2display)
    wordcloud = WordCloud(background_color='white', max_font_size=500).generate(word2display)
    wordcloud.to_file(proyect+'salidaNube.png')
    shutil.copy(proyect + 'salidaNube.png', nombredirectorio)
    os.remove(proyect+'salidaNube.png')
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    for i, page in enumerate(pages):
        borrador = proyect + 'salida' + str(i) + '.txt'
        os.remove(borrador)
    print("SACAMOS LOS VALORES DE ESTA COSA", proyect+'salidaUnida.txt')
    shutil.copy(proyect + 'salidaUnida.txt', nombredirectorio)
    #En Windows tenemos que cerrar el pdf de salida Unida para poder borrarlo
    textoUnido.close()
    os.remove(proyect+'salidaUnida.txt')
