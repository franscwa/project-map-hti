import os
from flask import Flask, request, redirect, url_for, render_template
import pymysql
from MapOOP import Maps
from dotenv import load_dotenv
import requests



app = Flask(__name__)
load_dotenv()


dbHost = os.getenv("DATABASE_HOST")
dbName = os.getenv("DATABASE_NAME")
dbUser = os.getenv("DATABASE_USERNAME")
dbPass = os.getenv("DATABASE_PASSWORD")
mapsAPI = os.getenv("MAP_API_KEY")


#connect to the databse
connection = pymysql.connect(host=dbHost,
                             user=dbUser,
                             password=dbPass,
                                db=dbName)


#get and post request on base '/' URL endpoint
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the form data
        city = request.form['location']

        #Google maps API to get latitude and longitude from city names
        response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={city}&key={mapsAPI}')

        if response.status_code == 200:
    # Load the response data into a dictionary
            data = response.json()

    # Extract the latitude and longitude from the response data
            latitude = data['results'][0]['geometry']['location']['lat']
            longitude = data['results'][0]['geometry']['location']['lng']

    # Print the latitude and longitude
            print(f'Latitude: {latitude}')
            print(f'Longitude: {longitude}')
        else:
            print('Request failed')
    
        #the Maps object takes a list of coordinates as an input so we store/retrieve the latitude and longitude as a list
        location = []

        location.append(latitude)
        location.append(longitude)

        location = repr(location)
        #put code to translate city name to lat long

        #add an image variable
        title = request.form['title']
        description = request.form['description']

        # Insert the new landmark data into the database
        with connection.cursor() as cursor:
            sql = "INSERT INTO landmarks (location, title, description) VALUES (%s, %s, %s)"
           
            #also insert the data into the folium map
            
            cursor.execute(sql, (location, title, description))

            updatedMap = Maps('haiti.geojson')
            

                # Retrieve the data from the table
            sql = "SELECT * FROM landmarks"
            cursor.execute(sql)
            rows = cursor.fetchall()

        # Add a marker for each row of data
            for row in rows:

                location = row['location']
                title = row['title']
                description = row['description']

                location = eval(location)
                updatedMap.add_marker(location, title, description)


            updatedMap.save_map('./templates/index.html')



    else: 
        #if the request to the url is not a post request render the current/newly generated map 
        return render_template('index.html') 

        connection.commit()
        

if __name__ == '__main__':
    app.run('0.0.0.0',port=8000)
