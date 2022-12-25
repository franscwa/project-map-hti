import os
from flask import Flask, request, redirect, url_for, render_template
import pymysql

def create_app():
    app = Flask(__name__)
    return app

app = create_app()
# Connect to the database
#connection = pymysql.connect(host='localhost',
#                             user='root',
 #                            password='Indiana2022!',
            #               db='geoproject')
@app.route('/')
def index():
    # Render the home.html template
    return render_template('index.html')

"""
@app.route('/new', methods=['GET', 'POST'])
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
            
          
         
            cursor.execute(sql, (location, title, description))


            output = "SELECT * from landmarks"
            cursor.execute(output)

            rows = cursor.fetchall()

            for row in rows:
                print(row)
        connection.commit()
        """

  





if __name__ == '__main__':
    app.run()


