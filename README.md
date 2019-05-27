# Webscrapping-Homework

Descripción de archivos:

--IMAGENES----------------------------------------------------------------------------------------------------
capture1.jpg: Imagen del sitio web final generado con render y flask.
capture2.jpg: Continuación imagen del sitio web final generado con render y flask
capture3.jpg: Continuación imagen del sitio web final generado con render y flask

result_scrapping.jpg: resultado en el browser del scrapping ya insertado en Mongo (utilizando jsonify para presentarlo)

record mongo.jpg: documento insertado en Mongo DB proveniente del scrapping

Insercion en Mongo.png: Visualización del documento insertado en Mongo DB a partir del web scrapping realizado 
                        por app.py utilizando la función scrape() que se encuentra en scrape_mars.py

--CODIGO------------------------------------------------------------------------------------------------------
mission_to_mars.ipynb:  Jupyter Notebook con el código que realiza el scrapping
app.py:                 Código que llama a la función scrape y genera el render en flask
scrape_mars.py:         Código proveniente del Jupyter Notebook para realizar el scrapping de los distintos sitios

--ADICIONALES-------------------------------------------------------------------------------------------------
mars_planet_profile.html: pagina generada a partir de los datos del dataframe de Marte (adicional)
chromedriver.exe: Utilería para manipular con Splinter el browser y realizar el scrapping de las páginas visitadas
