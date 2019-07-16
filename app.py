# import necessary libraries
from flask import Flask, render_template
from flask_pymongo import PyMongo
import pymongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_data")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():


   # Find one record of data from the mongo database
    destination_data = mongo.db.collection.find_one()

    return  render_template('index.html', mars_data=mars_data)

@app.route("/scrape")
def scrape():


   # Run the scrape function
    mars1_data = scrape_mars.scrape_info()

   # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars1_data, upsert=True)

   # Redirect back to home page
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)