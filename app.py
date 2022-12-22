import os
from flask import Flask, request, redirect, url_for
import pymysql
import maps 

app = Flask(__name__)

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Indiana2022!',
                             db='geoproject')

@app.route('/', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':
        # Get the form data
        location = request.form['location']



        #add an image variable
        title = request.form['title']
        description = request.form['description']

        # Insert the data into the database
        with connection.cursor() as cursor:
            sql = "INSERT INTO landmarks (location, title, description) VALUES (%s, %s, %s)"
            #also insert the data into the folium map
            
          


            output = "SELECT * from landmarks"
          
         
            cursor.execute(sql, (location, title, description))
            res = cursor.execute(output)
            print("HEY!!" + res)
        connection.commit()

    if request.method == 'GET':
        return render_template('index.html')






if __name__ == '__main__':
    app.run()


