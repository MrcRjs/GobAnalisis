Análisis Gubernamental
======================

Esta aplicación hace uso de la API de twitter para extraer y analizar tweets, específicamente realionados con candidatos a elecciones públicas.
#### Pre-requisitos
- [Python 3](https://www.python.org/download/releases/3.4.1/)
- [Tweepy](https://github.com/tweepy/tweepy)
- [Plotly](https://plot.ly/python/getting-started/)

#### Instalación
```
$ cd ~
$ git clone https://github.com/MrcRjs/GobAnalisis.git
```

Antes de iniciar la aplicación es necesario configurarla mediante el archivo *config.py*, con cualquier editor de texto:

- ###### Twitter App
 Los tokens de la aplicación *consumer_key/secret* y *access_token/_secret" se obtienen al crear una aplicación en [twitter apps](https://apps.twitter.com).
 
- ###### Candidates
 Es un arreglo de strings que serán utilizados para encontrar tweets relacionados con los candidatos, o usuarios especificados.
 
- ###### Excluded
 Es un arreglo de string para especificar las palabras que serán omitidas de los tweets, por defecto las palabras de dos o menos letras, serán omitidas.

Unas vez personalizadas las configuraciones, es posible iniciar la aplicación:

```
$ cd ~/GobAnalisis
$ python3 main.py
```