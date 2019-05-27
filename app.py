# Import class Flask
from flask import Flask, jsonify, render_template
import pymongo

# Conexion a BD Mongo
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db

# FLASK-----------------------------------------------------------------------------------------------------------------------------------------
# Generate the app
app = Flask(__name__)

# SCRAPE---------------------------------------------------------------------------------------------------------------------------------
@app.route("/scrape")
def scrape():

#Importing our function
    from scrape_mars import scrape

    diccionario = scrape()

    db.general.drop() #Limpiamos la collection
    db.general.insert_many(diccionario)

    return jsonify(scrape())
    

# Home page
@app.route('/')
def home():

    # Nos conectamos a la BD, guardamos el resultado y lo rendereamos
    mars_data = list(db.general.find())
  
    return render_template("index.html", dict=mars_data)

if __name__ == "__main__":
    app.run(debug=True)


