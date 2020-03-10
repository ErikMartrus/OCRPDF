# Integración de las diferentes herramientas utilizadas para la obtención de los vectores identificativos.

### ImageMagick

Con respecto al documento anterior en el que se explicaban que los PDFs se segmentaban en imágenes a través del uso de la librería Poppler, se ha decidido editar las propiedades de las imágenes haciendo uso de  [ImageMagick](https://imagemagick.org/index.php) que ya fue mencionada muy brevemente al final de dicho documento.

Es una suite de edición de imágenes en modo consola. Es decir, es un conjunto de comandos para trabajar con imágenes, con una serie de comandos que abarcan una serie de procesos que pueden cubrir todo el abanico de necesidades que un usuario pueda tener para cualquier actividad gráfica, tanto con mapa de bits como con vectores. 

Es software libre, por lo que, además todas la implicaciones que conlleva la libertad, garantiza que su calidad es muy superior a cualquier programa privativo, al tener una comunidad de desarrolladores que soluciona cualquier problema que pudiera tener, así como una continua evolución adaptándose siempre a las demandas de los usuarios.

Entre sus características podemos destacar algunas como:

- Es multiplataforma, por lo que podemos aprender a usar ImageMagick en un sistema operativo y podremos usarlo en cualquier otro sistema operativo con el que nos toque trabajar.
  Es en modo consola, por lo que podemos hacer scripts que automaticen los procesos, así como bibliotecas o funciones que permiten reutilizar ese código y repetir automáticamente los efectos sobre tantas imágenes como queramos. Por tanto muy útil para el procesamiento de datos en bloque.
- No necesita un entorno gráfico.
- Trabaja con más de 200 formatos gráficos, desde los más usuales en mapa de bits, como PNG, JPG, como formatos nativos de programas determinados (XCF, PSD, PSB...), formatos de fotografía (RAW, TIFF...), vectoriales (SVG, MVG...), ficheros de vídeo (MOV, MPG, MP4...), ficheros PDF...,etc.
- Más de 20 espacios de color distintos: además de los clásicos sRGB, RGB, RGBA y CMYK, permite trabajar con HSB, HSL, Lab... ofreciendo muchas más posibilidades que la mayoría de programas de edición de imágenes. 
  Permite trabajar independientemente con los canales. ImageMagick no sólo ofrece la posibilidad de trabajar con esos más de 20 espacios de color sino que permite trabajar individualmente con cada uno de los canales de cada espacio de color, tanto extrayendo el canal en cuestión como aplicando las modificaciones que deseemos únicamente a un canal, consiguiendo resultados mucho más precisos que trabajando con la imagen completa.
- Permite cambiar de espacio de color (y por lo tanto, trabajar con los canales de ese espacio de color) sobre la misma imagen en la misma instrucción. Es decir, podemos indicar a ImageMagick que aplique, por ejemplo, unas modificaciones en la capa de luminosidades del espacio Lab, otras independientes al canal rojo en el espacio RGB, otros cambios distinto a la capa de saturación en un espacio HSB y que el resultado de esos cambios lo transforme a un espacio de color de escala de grises.

Buscando en Internet podemos encontrar información sobre ImageMagick así como sus principales comandos: https://www.uv.es/scubero/recursos/imagemagik-cli.pdf

Destacar que desde ImageMagick también se nos permite extraer imágenes de PDF como hacia el Poppler.

Y que a través del comando:

*convert -brightness-contrast 10x33 nombreArchivoEntrada.ppm nombreArchivoSalida.ppm*

![Captura de pantalla 2020-02-14 a las 10.51.02](C:\Users\erik_\Downloads\Captura de pantalla 2020-02-14 a las 10.51.02.png)

Siendo los números 10x33 un indicador del brillo y contraste. Ambos números pueden ir desde -100 a 100, siendo los números negativos una reducción del efecto a editar. Por tanto en nuestro ejemplo aumentamos el brillo en un valor de 10 y el contraste en un valor de 33.

Como vemos el resultado es muy similar al que nos ofrecía GIMP pero la ventaja es que ImageMagick nos permite tratar un gran número de imágenes, mientras que con el GIMP perderíamos demasiado tiempo con cada imagen a editar.

## Nube de Tags.

Una vez que tenemos la salida del OCR en texto plano, en nuestro caso en formato txt, procederemos a obtener los vectores más significativos, por ello nos hemos de informar sobre cómo crear una nube de tags y las diferentes herramientas que nos permiten identificar las palabras que más se repiten o a las que se le da más importancia dentro del texto.

### ¿Qué es una nube de Tags?

Cuando hablamos de nubes de tags, nos referimos a la **representación visual de un grupo o familia de etiquetas o tags, agrupadas en una conjunto abstracto que se asemeja a la forma de una nube y que tienen un contexto o nexo de unión común**.

Es un recurso muy utilizado en el Marketing Online y el SEO, una representación de las tags más destacadas agrupadas y que reflejan en su conjunto el contenido temático o de actualidad, de la página o el sitio web.

En su aspecto visual, el usuario verá ese grupo de palabras clave etiquetadas en diferentes ubicaciones, formas, tamaños o colores, dentro de la nube. Normalmente **las de mayor tamaño y colores intensos, reflejan las temáticas de mayor importancia (por relevancia, volumen de contenido o actualidad)** siendo las menos significativas aquellas más pequeñas y de colores más degradados.

Siendo de este de aquí abajo, un ejemplo de lo que hemos escrito en estas líneas de introducción.

![Nube de tags](https://www.humanlevel.com/wp-content/uploads/nube-de-tags.jpg)

### Objetivo de la nube de tags

El principal objetivo de la nube de tags será el **facilitar al usuario la búsqueda de información**, al indicarle de manera recurrente las palabras y áreas más destacadas, actuales o abundantes en contenido relevante para él, representadas por esas etiquetas.

En segundo lugar, **ayudar al usuario en la navegabilidad por el sitio web**, de forma que al clicar en cualquiera de esas tags representadas, le haremos llegar al contenido agrupado bajo esa etiqueta, facilitando su acceso a aquellos que sean atractivos e interesantes para él.

En tercer lugar, **tenemos beneficios cara al SEO**, pues nos ayudarán a que las arañas accedan directamente a ciertos contenidos que nos resultan importantes, evitándoles tener que llegar a ellos teniendo que descender varios niveles en la arquitectura de la web, con lo que es **más fácil a la hora de conseguir que se indexe contenido relevante** para nosotros. Además **es un empuje a la popularidad** con los enlaces ubicados en esa nube de tags, a través de los cuales se traslada ese zumo de popularidad y se reparte entre las páginas a las que dirigen los enlaces contenidos en esas tags relevantes.

Dentro de las ventajas SEO de la nube de tags, destaca también que **nos van a ayudar a destacar temas de actualidad**, por ende de potencial tráfico, que nos mejore el tráfico para esos post o páginas referidas a esos temas de actualidad.

### Inconvenientes

Los gestores de contenido o CMS, permiten la creación de tags e incluso las recomiendan para poder resaltar *keyword* del sitio web. Por ejemplo, en [WordPress](https://www.humanlevel.com/diccionario-marketing-online/wordpress), se ofrecen al usuario ese etiquetado de contenidos pudiendo definir un listado de términos, separados por comas que se asociarán a la tag.

Muchos usuarios que construyen su sitio web con estos gestores de contenido, hacen **un uso abusivo de las tags**, pues para cada tag se crea una página y puede da lugar a generación de contenido basura o *thin content* y contenido duplicado. Cuando esto ocurre y se crean nubes de tags automáticas, se puede devaluar mucho la relevancia de las mismas, a la par que dar preeminencia a contenidos basura o duplicados, ya que **la generación de estas nubes de tags en WordPress suele basarse en el número de artículos bajo la tag**.

### ¿Cómo se hacen las nubes de tags?

Existen **distintas páginas y aplicaciones web que te ayudan a crear estas nubes de tags**, muchas de ellas son herramientas online que te permitirán crearlas, modificarlas y adaptarlas estructural y estéticamente, configurar el estilo de diseño, formas, fuentes, tamaños o colores; y te proporcionan el código o el modo de implementarla en tu sitio web.

Algunas de ellas pueden ser [Wordle](http://www.wordle.net/), [Wordaizer](http://www.mosaizer.com/Wordaizer/) o [Tagxedo](http://www.tagxedo.com/) entre muchas otras.

### Herramientas para hacer nubes de tags.

De los tres que mencionamos más arriba, descartaremos Tagxedo por lo mismo que hicimos con las herramientas de OCR, porque realiza el proceso online y no nos interesa por la privacidad de los datos a utilizar.

#### Wordle

En primer lugar probaremos Wordle, que lo podremos descargar desde el enlace: http://www.wordle.net/

Se puede ejecutar en local, y se trata de una  aplicación que tiene la opcion de ejecutarse en línea o en local y que sirve para generar **Nubes de palabras** a las que se les puede dar diversos formatos visuales, a partir de un texto cualquiera elegido por el usuario. 

![Captura de pantalla 2020-02-14 a las 12.44.21](C:\Users\erik_\Downloads\Captura de pantalla 2020-02-14 a las 12.44.21.png) 

Como vemos las palabras más significativas del txt que obtuvimos tras realizar el OCR y que provienen de la imagen de la izquierda, tiene su representación con los valores más significativos en el wordle donde se representan de mayor a menor tamaño indicando cual es su importancia en el texto.

En lo que respecta Wordaizer, solo se puede ejecutar en Windows, por tanto debido a su disponibilidad en diferentes plataformas nos quedamos con Wordle.

Por lo que vemos, el resultado que nos presenta Wordle se asemeja bastante a los vectores o palabras significativas que podamos buscar, ya que entre las más destacadas no se aprecia apenas ninguna palabra recurrente del lenguaje que no aporte nada y se destacan las que mas se repiten que tienen cierto valor, por tanto intentaremos ver los procesos que realiza antes de la obtención de la imagen PNG  que se nos presenta como salida.

Por desgracia, como vemos en su página, Wordle no comparte su [código](http://www.wordle.net/credits). El código pertenece a IBM. Y de las partes más destacadas IBM posee todos los derechos.

Por tanto decidimos buscar Internet alguna alternativa que nos permita realizar algo similar o alguna herramienta semejante a Wordle.

Finalmente encontramos [PyTagCloud](https://pypi.org/project/pytagcloud/).

#### PyTagCloud

PyTagCloud nos permite crear una nube de tags simple inspirada por la herramienta ya antes mencionada Wordle.

Las salidas que nos presenta PyTagCloud pueden ser tanto en PNG como en HTML/CSS.

Para la instalación de PyTagCloud podemos usar el enlace que anteriormente dimos, siempre y cuando habiendo instalado antes [pip](https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x) que como ya hemos explicado en documentos anteriores, se trata de un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python. 

##### Pruebas con PyTagCloud

Para probar PyTagCloud hemos decidido crear un pequeño script, llamado prueba.py donde iremos mostrando lo que vamos obteniendo y modificando el archivo en función de lo que queramos obtener.

![Captura de pantalla 2020-02-18 a las 9.03.40](C:\Users\erik_\Downloads\Captura de pantalla 2020-02-18 a las 9.03.40.png)

Como vemos para empezar utilizaremos un texto de ejemplo que nosotros mismos hemos insertado.

Con el get_tag_counts conseguimos obtener los tags y con el create_tag_image se consigue la imagen de la nube implementada.

![Captura de pantalla 2020-02-18 a las 9.06.37](C:\Users\erik_\Downloads\Captura de pantalla 2020-02-18 a las 9.06.37.png)

Una vez se ejecuta el script de python, a través de los comandos: 

*python prueba.py*

Obtendremos los tags más destacados del texto que hemos establecido como input y la imagen que los representa que como vemos en la primera foto hemos decidido llamar *cloud_large.png*.

![Captura de pantalla 2020-02-18 a las 9.09.10](C:\Users\erik_\Downloads\Captura de pantalla 2020-02-18 a las 9.09.10.png)

Como vemos si en lugar de de crear la imagen de los tags, decidimos ver la información que nos muestra los tags, cambiamos nuestro script para finalmente establecer un *print(tags)*, Mostrandonos la informacion que tienen los tags que a continuación analizaremos.

De lo que podemos destacar del método make_tags:

Podemos mencionar que como vemos en la salida de la última imagen, nuestros tags están formados por un color, un carácter que viene definido junto al 'tag' y un tamaño o un size que viene expresado por un número y que representa el tamaño que tendrá dicho tag en la nube.

Destacar además que se introducen términos tales como tuplas, que son conjuntos de datos ordenados e inmutables del mismo o diferente tipo.

A su vez también tenemos que decir que las etiquetas tienen tamaños asignados entre minsize y maxsize.

Si lo queremos probar con el ejemplo que hemos utilizado anteriormente hemos de cambiar unas cuantas líneas. Para así abrir nuestro archivo pdf y proceder a su lectura. 

Por ello hemos introducido las líneas:

*YOUR_TEXT = open("out.txt", "r")*

*texto = YOUR_TEXT.read()*

Como vimos anteriormente el archivo que tenemos definido como out.txt, es el ejemplo que hemos utilizado a lo largo de todo nuestro proyecto y que declaramos en la primera fase.

Si observamos los resultados.

![Captura de pantalla 2020-02-18 a las 12.21.25](C:\Users\erik_\Downloads\Captura de pantalla 2020-02-18 a las 12.21.25.png)

Podemos ver como se obtienen todos los tags de nuestro txt.

![Captura de pantalla 2020-02-18 a las 12.26.54](C:\Users\erik_\Downloads\Captura de pantalla 2020-02-18 a las 12.26.54.png)

Si deseamos ver el resultado representado en PNG vemos que comparado con respecto a Wordle, obtenemos un resultado donde aparecen palabras más concurrentes del idioma y donde perdemos la información de los correos electrónicos y demás.

![Captura de pantalla 2020-02-18 a las 13.45.59](C:\Users\erik_\Downloads\Captura de pantalla 2020-02-18 a las 13.45.59.png)

En la imagen podemos ver claramente las diferencias que se presentan entre ambas.



#### Otras herramientas

Como queremos configurar la nube de tags a nuestra voluntad para poder configurar el diccionario con las palabras o tags que más nos interesan decidimos probar otro método.

Se realizará una prueba usando diferentes scripts en Python que requieren de unas librerías especializadas en procesamiento del lenguaje natural (PLN) y en el análisis de textos. La librería que emplearemos para las pruebas serán NLTK (Natural Language Toolkit). En la siguiente dirección http://www.nltk.org y en el libro *Natural Language Processing with Python* (versión online: https://www.nltk.org/book/) se puede obtener información acerca de la instalación de esta librería y de cómo se puede hacer procesamiento del lenguaje con ella.

Además usaremos una librería que emplearemos para el análisis textual que será la librería Gensim. Para su instalación, consultar https://radimrehurek.com/gensim/install.html

**NOTA:** Se recomienda que para esta parte el Python que usemos sea de la versión 3.6.

En el primer caso importaremos las librerías que ya mencionamos anteriormente.

![image-20200221095629102](C:\Users\erik_\AppData\Roaming\Typora\typora-user-images\image-20200221095629102.png)

La siguiente instrucción que debéis ejecutar es nltk.download().

![image-20200221095924693](C:\Users\erik_\AppData\Roaming\Typora\typora-user-images\image-20200221095924693.png)

 Al ejecutarla, si esperáis un momento, se os abrirá una ventana emergente con los complementos de NLTK. Hay que seleccionar "ALL" e instalarlos todos, así lo tendréis todo listo.

![Captura de pantalla 2020-02-21 a las 9.54.53](C:\Users\erik_\Downloads\Captura de pantalla 2020-02-21 a las 9.54.53.png)

Como vemos no los tenemos instalados asi que procedemos a ello que tardará un poco.

![Captura de pantalla 2020-02-21 a las 9.57.25](C:\Users\erik_\Downloads\Captura de pantalla 2020-02-21 a las 9.57.25.png)

En nuestro caso obtendremos errores con los certificados SSL, indicandonos  que debamos instalar los certificados para el uso de SSL desde Python, mediante el comando "Install Certificates.command". Por ejemplo, basta con ejecutar una *shell* con:

*/Applications/Python\ 3.6/Install\ Certificates.command*

Solucionando los problemas que se nos presentaban al ejecutar el script.

##### 1. Detección de palabras sin preprocesado

A continuación  haremos el procesado  de las palabras utilizando el metodo split(). El método split () divide un String en una lista. Además podemos especificar el separador, el separador predeterminado es cualquier espacio en blanco.

![Captura de pantalla 2020-02-21 a las 10.33.44](C:\Users\erik_\Downloads\Captura de pantalla 2020-02-21 a las 10.33.44.png)

**NOTA:** Recordar que hay que integrar los archivos que proceden del procesado de los pdfs  e integrarlos en el proyecto.

##### 1.1. Contar los candidatos a palabra obtenidos con el método *split* y según la relación significante-significado

A continuación importamos el método que crea un diccionario con la frecuencia de aparición de los elementos en una lista:  *from collections import Counter*

Tras esto, usaremos el método Counter para contar el número de veces que los candidatos a palabra aparecen en el texto:

*print("CÁLCULO MÉTODO SPLIT:", Counter(word_candidates), "\n")*

![Captura de pantalla 2020-02-21 a las 10.22.15](C:\Users\erik_\Downloads\Captura de pantalla 2020-02-21 a las 10.22.15.png)

Seguiremos  con una relación significante-significado donde a la lista de candidatos se les quita los símbolos '"' y '.'

*stripped_candidates = [w.strip('".') for w in word_candidates]*  

Le podemos añadir otros símbolos (e.g: ?, !, :, etc.) Y después mostraremos el número de veces que los candidatos aparecen en el texto tras sacarles los signos de puntuación.

*print("CÁLCULO MÉTODO SIGNIFICANTE-SIGNIFICADO:", Counter(stripped_candidates), "\n")*

![Captura de pantalla 2020-02-21 a las 10.27.05](C:\Users\erik_\Downloads\Captura de pantalla 2020-02-21 a las 10.27.05.png)

Y por último establecemos una relación significante-significado tras convertir las palabras a minúsculas

Creamos una lista de candidatos sin signos de puntuación convertidos a minúsculas (lower())

*lower_case_stripped_candidates = [s.lower() for s in stripped_candidates]*

Y se muestra el número de veces que los candidatos sin signos de puntuación y en minúsculas aparecen en el texto

*print("CÁLCULO TRAS CONVERSIÓN A MINÚSCULAS:", Counter(lower_case_stripped_candidates),  "\n")*

![Captura de pantalla 2020-02-21 a las 10.30.10](C:\Users\erik_\Downloads\Captura de pantalla 2020-02-21 a las 10.30.10.png)

##### 2. Detección de palabras con preprocesado del texto

![image-20200221103125043](C:\Users\erik_\AppData\Roaming\Typora\typora-user-images\image-20200221103125043.png)

Importamos las librerías que mostramos arriba para obtener los tokens

Tokens es la lista de tokens resultado de aplicar el tokenizer del NLTK al nuestro texto.

*tokens = [w for w in word_tokenize(headline)]*

*print(tokens)*

##### 2.1 Obtención de la lista de tokens con un *tokenizer* y filtrado no alfabeticos

De la lista de candidatos, queremos quitar los candidatos que no tienen caracteres alfabéticos ('"', '.', etc.).
Para ello, importamos la librería de Python encargada de la gestión de expresiones regulares

*import re* 

Obtendremos una lista de tokens del texto que han pasado el filtro. Para obtener la lista:
#1. Se convierte el texto a minúsculas (headline.lower())
#2. Se tokeniza el texto en minúsculas (word_tokenize(headline.lower()))
#3. Se añaden a la lista alpha_tokens los tokens que empiezan por un caracter alfabético (re.match("^[a-z]+.*))

*alpha_tokens = [w for w in word_tokenize(headline.lower()) if re.match("^[a-z]+.*", w)]*

*print(alpha_tokens)*

![Captura de pantalla 2020-02-21 a las 10.40.30](C:\Users\erik_\Downloads\Captura de pantalla 2020-02-21 a las 10.40.30.png)



##### 2.2 PoS tagging

![image-20200221104758599](C:\Users\erik_\AppData\Roaming\Typora\typora-user-images\image-20200221104758599.png)

Tras realizar los imports procederemos a través del Pos a etiquetar las categorias gramaticales de cada palabra del texto

```
#Lista de tokens del texto convertido en minúsculas
tokens = [w for w in word_tokenize(headline.lower())]
#PoS tagging de los tokens de la lista
tagged_tokens = nltk.pos_tag(tokens)
```

![Captura de pantalla 2020-02-21 a las 10.52.24](C:\Users\erik_\Downloads\Captura de pantalla 2020-02-21 a las 10.52.24.png)

###### **Etiquetas PoS**

Destacar que las etiquetas PoS son estas:

- DT: Determinante
- JJ: Adjetivo
- NN: Nombre en singular
- NNS: Nombre en plural
- VBD: Verbo en pasado
- VBG: Verbo en gerundio
- MD: Verbo modal
- IN: Preposición
- PRP: Pronombre
- RB: Adverbio
- CC: Conjunción coordinada
- CD: Numeral

##### 2.3. Buscador de n-gramas

![image-20200221113314683](C:\Users\erik_\AppData\Roaming\Typora\typora-user-images\image-20200221113314683.png)

```
#Lista de tokens del texto convertido en minúsculas
tokens = [w for w in word_tokenize(headline.lower())]

#Lista de bigramas
print ("BIGRAMAS:", list(ngrams(tokens, 2)),"\n")

#Lista de trigramas
print ("TRIGRAMAS:", list(ngrams(tokens, 3)))
```

Una vez importamos todo lo que necesitamos, podemos obtener diferentes n-gramas que nos puedan interesar como puedan ser correos electrónicos, números de teléfonos y demás. Pero no todos los ngramas nos pueden interesar.

<img src="C:\Users\erik_\Downloads\Captura de pantalla 2020-02-21 a las 11.37.59.png" alt="Captura de pantalla 2020-02-21 a las 11.37.59" style="zoom:200%;" />

##### 2.4. Búsqueda de n-gramas que son colocaciones

```
#Para hacer la búsqueda de n-gramas que son colocaciones, importamos el tokenizer (word_tokenize) y los métodos de búsqueda de colocaciones, ambos de la librería NLTK

from nltk import word_tokenize
from nltk.collocations import *

#De los métodos de búsqueda de colocaciones, cargamos las métricas de cálculo de los bigramas y trigramas candidatos a ser colocaciones
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
```

Definimos las funciones a utilizar como pueden ser get_coll_candidates(), re_filter_candidates() y get_n_best_candidates().

Donde:

1. get_coll_candidates() recibe de parámetro de entrada los tokens que mencionamos antes y obtiene los trigramas y bigramas candidatos a ser una colocación.
2. re_filter_candidates() recibe de entrada tanto los bigramas como trigramas que sean candidatos y se quitan aquellos que tengan algun non-word element
3. get_n_best_candidates() recibe parametros de entrada tanto los bigramas, como trigramas como las mejores colocaciones, y obtiene por salida los mejores candidatos

![Captura de pantalla 2020-02-21 a las 12.45.44](C:\Users\erik_\Downloads\Captura de pantalla 2020-02-21 a las 12.45.44.png)



Y por último la función get_collocations:

```
#La función get_collocations realiza lo siguiente:
#1. Crea la lista de tokens del texto (word_tokenize)
#2. A partir de la lista de tokens, busca los bigramas y trigramas que son candidatos a ser colocaciones
#según unos cálculos estadísticos. En este caso, se realiza el cálculo del PMI (Pointwise Mutual Information)
#3. Retorna los N mejores candidatos
```



![Captura de pantalla 2020-02-21 a las 12.55.03](C:\Users\erik_\Downloads\Captura de pantalla 2020-02-21 a las 12.55.03.png)



Dando por salida los mejores bigramas,trigramas candidatos.

![Captura de pantalla 2020-02-21 a las 13.16.02](C:\Users\erik_\Downloads\Captura de pantalla 2020-02-21 a las 13.16.02.png)



Una vez tenemos esto, podemos ver que podemos obtener la nube de Tags tanto de esta manera como con PyTagCloud, como con esta ultima lo hemos conseguido de una manera mucho más rápida, aplicaremos esta, pero hemos de destacar que de la otra manera podemos realizar un filtrado con mayor personalización.



### Proyecto

Tras esto, buscamos unificar todos los procesos o pasos que hemos llevado a cabo para obtener nuestros vectores identificativos desde los pdfs recibidos en un único proyecto, que nos facilitará tratar los diferentes pdfs con una mayor rapidez y formar un gran banco de datos más fácilmente.

1) En primer lugar hemos de renderizar los PDF y convertirlos en imágenes como explicamos en su momento con el uso de Poppler.

**NOTA**: Como la mayoría de scripts o código, lo hemos encontrado implementado, o se puede desarrollar en  Python, decidimos realizar esta parte del proyecto en este lenguaje.

Si bien utilizamos Poppler y lo probamos a través de la ventana de comandos, decidimos utilizar pdf2image un módulo basado en poppler que envuelve pdftoppm y pdftocairo para convertir PDF a un objeto de imagen PIL .

En este link podremos ver como instalar en nuestro equipo independientemente del SO:

 https://pypi.org/project/pdf2image/

Destacar que para todos los SOs es necesario tener instalado previamente Poppler.

2) Tras esto, procedemos a implementar el ImageMagick en Python para editar las imágenes a nuestro gusto buscando eliminar defectos innecesarios como ruido, marcas de agua,etc..

En este caso utilizamos Wand, Wand es un enlace simple a ImageMagick basado en ctypes para Python.

Para ver los pasos a seguir para realizar su instalación, así como la guía de usuario y demás:

http://docs.wand-py.org/en/0.5.8/index.html

**NOTA:** Comentar que también se utilizará módulos matemáticos como math en la implementación del código.

3) Tras esto podemos realizar la implementación del OCR, Tesseract, para implementarlo tenemos que importar la libreria pytesseract y cv.

En el link de a continuación podemos ver los pasos a seguir para poder implementar Tesseract OCR en Python:

https://www.altaruru.com/tesseract-ocr-y-pytesseract/

Como vemos primero hemos de instalar haciendo uso de pip, Pytesseract, que es la libreria python que nos permitirá utilizar este OCR en nuestros desarrollos, y las librerias opencv para el tratamiento de imágenes que utiliza Tesseract.

Comentar que la salida del OCR en lugar de mostrarla por pantalla decidimos guardarla en un txt que es el formato con el que hemos trabajado anteriormente.

Por ello introducimos tres líneas sencillas.

*f = open('salida.txt','w')*

*f.write(sret)*

*f.close()*

Con la función open acepta la ruta del archivo que será creado y el segundo argumento es el modo en el que será abierto el archivo si existe, donde w indica que es para escritura y r que será solo de lectura.

Con el write escribimos el txt con la salida que nos da el OCR y cerramos ese txt.

4) Por ultimo nos falta sacar las palabras claves o vectores significativos de nuestro ejemplo y ya lo tendríamos. Que como ya hablamos lo podemos hacer con pytagcloud o de la otra manera que propusimos.

En primer lugar lo intentamos hacer con pytagcloud.

![Captura de pantalla 2020-02-28 a las 13.36.34](C:\Users\erik_\Downloads\Captura de pantalla 2020-02-28 a las 13.36.34.png)

Que tiene una implementación bastante sencilla, pero se nos presentan diferentes problemas.



![Captura de pantalla 2020-02-28 a las 13.37.00 (1)](C:\Users\erik_\Downloads\Captura de pantalla 2020-02-28 a las 13.37.00 (1).png)

Como vemos se nos presenta un error en el método get_tag_counts declarado en las librerías asi que decidimos buscar por internet para informarnos sobre el problema.

El problema ocurre principalmente es que en Python 2. X, los elementos () se utilizan para devolver una copia de la lista de todos los elementos (pares clave / valor) en D), que ocupa memoria adicional.

iteritems () se usa para devolver las iteraciones [Devuelve un iterador en todos los elementos (pares clave / valor) en D] después de la operación de su propia lista de diccionarios. No ocupa memoria extra.

En Python 3.x, los dos métodos de iteritems () y viewitems () han sido abolidos, y el resultado de items () es el mismo que el de viewitems () en 2.x. Reemplazar iteritems () con items () en 3.x se puede usar para recorrer el bucle como vemos en alguna solución en Internet.

Este es el error que se nos presenta.

> ```
> Rastreo (llamadas recientes más última):
>  Archivo "D: /code/pythonwork/Text.py", línea 96, en <module>
>   etiquetas = make_tags (get_tag_counts (YOUR_TEXT), maxsize = 120)
>  Archivo "C: \ Python34 \ lib \ site-packages \ pytagcloud \ lang \ counter.py", línea 25, en get_tag_counts
>   return sorted (counted.iteritems (), key = itemgetter (1), reverse = True)
> AttributeError: el objeto 'dict' no tiene el atributo 'iteritems'
> ```

Y el  problema encontrado en la Biblioteca:

> ```
> # counter.py
> return sorted (counted.iteritems (), key = itemgetter (1), reverse = True)
> ```

Si cambiamos a:

> ```
> # counter.py
> return sorted (counted.items (), key = itemgetter (1), reverse = True)
> ```

Descubrimos que no hay ningún error en la operación, pero no se genera una nube de etiquetas. Después de imprimirlo una y otra vez, finalmente encontramos el problema:

> ```
> desde pytagcloud import create_tag_image
> ```

Esto se utiliza para generar una tupla:

> ```
> # recuentos = [('nube', 3),
> # ('palabras', 2),
> # ('código', 1),
> # ('palabra', 1),
> # ('aparecer', 1)]
> ```

Pero los elementos () en Python 3 no pueden lograr este efecto.

**¡¡¡NOTA!!!:** Además cuando lo ejecutamos en local al principio de este documento, obviamos que los estabamos ejecutando con el python 2.7 y no con el python 3.x (donde la x en nuestro caso es el 6), ya que ejecutamos el fichero como: *python nombrescript.py*

Por tanto esta opcion no es valida para nuestro proyecto si pretendemos realizarlo en una versión como la 3.6.

En esta parte del proyecto llevaremos a cabo las herramientas que barajamos como posibilidad a PyTagCloud. Implementándolas en nuestro proyecto.

Destacar que nuestro proyecto nos generará cuatro archivos como mínimo, más en el caso de que los pdfs a los que les vayamos a realizar el OCR tengan más de una página.

Además de que nuestro proyecto variara ya que no se encuentra implementado para pdfs con varias páginas.

 //Falta por editar documento comentando el texto

#### Librerías utilizadas.

Como ya hemos hablado anteriormente nuestro proyecto utiliza distintas librerías, las mas destacadas las nombraremos a continuación:

1. Correspondiente al renderizado de los pdfs como imágenes en lo que se corresponde a la parte de Poopler (librería pdf2image).
2.  Otra libreria que se utiliza para eliminar efectos indeseados de las imagenes debido al escaneo es ImageMagick ( librería Wand)
3.  La que se corresponde a realizar el OCR a la imagen JPEG, que se llama pytesseract.
4. Y la que nos generá la nube de palabras que se llama WordCloud.

Además se incorporarán librerías como [shutil](https://docs.python.org/3/library/shutil.html) (para la copia de archivos), [math](https://docs.python.org/3/library/math.html) para realizar calculos en lo referente al brillo y contraste en la edición,  [NLTK](https://www.nltk.org/) para el tratado del lenguaje natutal, librerías naturales de Python como pueden ser Re(https://docs.python.org/3/library/re.html) y [Os](https://docs.python.org/3/library/os.html) para borrar archivos por ejemplo.

#### Comentación del código

Podemos dividir nuestro código en diferentes partes o segmentos de operación.

Tras ver los imports podemos ver la clase MyImage donde recibimos como parámetros de entrada un Image y que nos será de gran utilidad para tratar la edición de la imágenes resultantes de realizar el renderizado de los pdfs.

![Captura de pantalla 2020-03-06 a las 13.07.37](C:\Users\erik_\Downloads\Captura de pantalla 2020-03-06 a las 13.07.37.png)

A continuación a través del uso de bucles for, obtendremos la lista de los ficheros pdfs que tengamos en el directorio donde nos encontramos, destacar que path esta declarado para estar ubicados en el directorio donde se ejecuta el script.

![Captura de pantalla 2020-03-06 a las 13.07.58](C:\Users\erik_\Downloads\Captura de pantalla 2020-03-06 a las 13.07.58.png)

Con el método *os.walk(path)* obtendremos una lista de todos los ficheros que tengamos en el directorio donde estemos, si recorremos obtendremos dichos ficheros, con el splitext obtendremos una tupla con el tipo de objeto y su nombre, así pues con el siguiente if, obtendremos todos los ficheros .pdf y los añadiremos a un array vacío donde se tendrá con su valor.

Tras esto, recorreremos el array de pdfs uno por uno y separando en los imágenes en primer lugar.

![Captura de pantalla 2020-03-06 a las 13.08.23](C:\Users\erik_\Downloads\Captura de pantalla 2020-03-06 a las 13.08.23.png)



Mencionar que con fname daremos nombre a cada png en funcion del nombre del archivo y con el shutil haremos una copia del archivo a un directorio con el mismo nombre del archivo.

![Captura de pantalla 2020-03-06 a las 13.08.35](C:\Users\erik_\Downloads\Captura de pantalla 2020-03-06 a las 13.08.35.png)



Después usaremos Image para aumentar el brillo de las imagenes que nos han salido en función de la página, hay que decir que hemos tenido que contemplar los casos en los que los que los pdfs solo tengan una página.



![Captura de pantalla 2020-03-06 a las 13.08.56](C:\Users\erik_\Downloads\Captura de pantalla 2020-03-06 a las 13.08.56.png)



Tras esto llevaremos nuestras imágenes editadas a realizar el OCR , usando pytesseract y su método image_to_string() pasándole como parámetro de entrada una de las imágenes, generando así salidas.txt N siendo N el número de páginas del pdf.

![Captura de pantalla 2020-03-06 a las 13.09.09](C:\Users\erik_\Downloads\Captura de pantalla 2020-03-06 a las 13.09.09.png)



Para obtener un único diccionario, necesitaremos tener un único txt por pdf, por lo tanto decidimos concatenar los distintos archivos para obtener un único txt, del que obtendremos las palabras significativas y una nube de tags.

A continuación iría la parte de la obtención de las palabras claves, de la que hemos hablado en otros puntos del PDF, así que con el objetivo de no ser redundante no vamos a volver a mencionarlo.

![Captura de pantalla 2020-03-06 a las 13.09.32](C:\Users\erik_\Downloads\Captura de pantalla 2020-03-06 a las 13.09.32.png)

Por último en nuestro código podemos ver como se obtiene la nube de palabras o de tags y como se guarda.

Destacar que todo documento que se genera se usa en un método o un paso posterior, por eso una vez que los obtenemos los vamos copiando en nuestro directorio y se borra del directorio raíz, es por ello que que se incorporan los métodos os.remove().

![Captura de pantalla 2020-03-06 a las 13.41.30](C:\Users\erik_\Downloads\Captura de pantalla 2020-03-06 a las 13.41.30.png)



Como vemos nuestro proyecto funciona perfectamente, destacar que por ejemplo para el pdf documentoAsiento-8 tenemos 4 páginas y por tanto salen 4 imágenes primero, después se convierten en otras 4  editadas, se obtiene el OCR de cada una de ellas y una salida de las palabras claves en formato PNG.





