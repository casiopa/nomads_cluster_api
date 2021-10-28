# Cluster de usuarios para app Digital&Nomads
 
La app *Digital&Nomads* requería de un servicio que agrupara a los usuarios según sus intereses una vez hecho el registro y para ello hemos desarrollado una API que devuelve el grupo al que pertence cada usuario según sus intereses gracias a un modelo de clustering NMF.

## Creación de un entorno virtual

El primer paso es crear un entorno virtual en el que instalemos Python y las librerías necesarias para la lectura del modelo. Este paso es importante porque nos permitirá controlar qué versiones de Python y librerías se deben instalar en la máquina de Heroku. Esta información la volcaremos posteriormente en los archivos `runtime.txt` y `requirements.txt`. Una forma de crear el entorno virtual es utilizando conda, para lo que ejecutamos en la terminal:

```
conda create --name nombre_entorno
conda activate nombre_entorno
```

Más opciones para la creación y activación de entornos virtuales con Conda [aquí](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment).


## Modelo de clustering NMF
...

## Puesta en producción del modelo NMF de clustering con Flask y Heroku

Un vez entrenado el modelo lo exportamos como objeto pickle y ya podemos empezar a crear la API que dará el servicio. El proceso se activará en el momento en el que usuario, de manera opcional, rellena un formulario con sus intereses para que la aplicación le asigne un sala de chat con usuarios de intereses relacionados y que se encuentren en la misma ciudad.

En este caso montaremos un endpoint al que la app *Digital&Nomads* haga una petición POST enviando los datos del usuario como un objeto JSON. Este JSON lo recibe la aplicación Flask alojada en Heroku, con esos datos el modelo hace la predicción y se devuelve otro JSON con el cluster adjudicado.

IMAGEN ESQUEMA

Para un mínimo producto viable el alojamiento gratuito de la APP en Heroku puede resultar la mejor opción aunque hay que tener en cuenta que tras 30 minutos de inactividad la aplicación entra en modo reposo y que tenemos un límite de 512MB de RAM.

### Creación de la app
app_cluster.py

### Deploy en Heroku
La puesta en producción de una aplicación en Heroku es bastante sencilla. En primer lugar tenemos que preparar los archivos necesarios:

- `requirements.txt`: lista de dependencias de Python
```
Flask==1.1.1
gunicorn==20.0.4
numpy==1.20.3
pandas==1.2.4
requests==2.24.0
requests-oauthlib==1.3.0
scikit-learn==0.24.0
joblib==1.0.1
Flask-Cors==3.0.10
...
```
- `Procfile`: especifica qué se va a ejecutar en el entorno Heroku
```
web: gunicorn app_cluster:app
```
- `runtime.txt` (opcional): especifica la versión de Pyhton
```
python-3.8.8
```
- `app_cluster.py`: la app Flask


Lo siguiente que debemos hacer es abrir una cuenta en Heroku y crear una nueva app.

![Nueva app en Heroku](images/heroku-newApp.png)

Si entramos en la página de la app recién creada y en la pestaña Deploy, veremos que tenemos 3 formas de alojar la aplicación en Heroku. En este caso utilicé *Connnect to GitHub*. De esta forma solo tenemos que enlazar la app con un repositorio que ya tengamos subido a GitHub. 

![Deployment Methods](images/heroku-deployMethod.png)

En caso de que el repositorio tenga muchos archivos que los verdaderamente necesarios para el despligue de la app será mejor utilizar la primera opción que vemos en la imagen: Heroku Git. Alojando los archivos necesarios en el Git de Heroku podemos seleccionar exactamente qué archivos subimos.




Referencias:
- [Productionize a Machine Learning model with Flask and Heroku](https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2)
- [Serving a model with Flask](https://guillaumegenthial.github.io/serving.html)
