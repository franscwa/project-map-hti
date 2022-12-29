import os
from flask import Flask, request, redirect, url_for, render_template
import pymysql
from MapOOP import Maps
from geopy.geocoders import Nomatim
from dotenv import load_dotenv


load_dotenv()

def create_app():
    app = Flask(__name__)
    return app

app = create_app()
 #Connect to the database

dbHost = os.getenv("DATABASE_HOST")
dbName = os.getenv("DATABASE_NAME")
dbUser = os.getenv("DATABASE_USERNAME")
dbPass = os.getenv("DATABASE_PASSWORD")



connection = pymysql.connect(host=dbHost,
                             user=dbUser,
                             password=dbPass,
                                db=dbName)



@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        # Get the form data
        location = request.form['location']

        #put code to translate city name to lat long

        #add an image variable
        title = request.form['title']
        description = request.form['description']

        # Insert the data into the database
        with connection.cursor() as cursor:
            sql = "INSERT INTO landmarks (location, title, description) VALUES (%s, %s, %s)"
           
            #also insert the data into the folium map
            
            cursor.execute(sql, (location, title, description))

            updatedMap = Maps('haiti.geojson')
            
            updatedMap.add_markers_from_database()

            updatedMap.save_map('./templates/index.html')



    else: 
        return render_template('index.html') 
        connection.commit()
        

  





if __name__ == '__main__':
    app.run()


