import geojson
import folium
import pymysql

class Maps:
   

    def __init__(self, geojson_file):
        # Load the GeoJSON file
        with open(geojson_file) as f:
            geojson_data = f.read()


        # Create a Map instance
        self.map = folium.Map(location=[18.9712, 72.2852], zoom_start=15)

        # Add the GeoJSON data to the map
        folium.GeoJson(geojson_data).add_to(self.map)

        html = """
        <form method="post" style="background-color: rgba(0, 0, 0, 0.5); position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 1;">
          <label for="location" style="color: white;">Location:</label><br>
          <input type="text" id="location" name="location" style="color: white; background-color: transparent;"><br>
          <br>
          <label for="title" style="color: white;">Title:</label><br>
          <input type="text" id="title" name="title" style="color: white; background-color: transparent;"><br>
          <br>
          <label for="description" style="color: white;">Description:</label><br>
          <input type="text" id="description" name="description" style="color: white; background-color: transparent;"><br>
          <br>
          <input type="submit" value="Submit" style="color: white; background-color: transparent; border: 1px solid white;">
        </form> 
        """
        folium.Html(html, script=True).add_to(self.map)

    def add_marker(self, location, title, description):
        folium.Marker(location=location, popup=title, icon=folium.Icon(icon='cloud')).add_to(self.map)

    def save_map(self, filepath):
        self.map.save(filepath)

    def add_markers_from_database(self):
        # Connect to the database

        # Retrieve the data from the table
        with connection.cursor() as cursor:
            sql = "SELECT * FROM landmarks"
            cursor.execute(sql)
            rows = cursor.fetchall()

        # Add a marker for each row of data
        for row in rows:
            location = row['location']
            title = row['title']
            description = row['description']
            self.add_marker(location, title, description)
