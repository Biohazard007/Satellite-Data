import folium

# create map object
m = folium.Map(location=[27.656174, 85.327837], zoom_start=8)

# Global tooltip
tooltip = 'Nepal Academy of Science and Technology'
tooltips = 'Tribhuvan International Airport'

# Custom image
logoIcon = folium.features.CustomIcon('./static/MicrosoftTeams-image.png', icon_size=(50, 50))

# Circle marker
#folium.CircleMarker(location=[27.696578, 85.358651], radius=100, popup='Lansat Image location', color='#FF7F50', fill=True, fill_color='#FF7F50').add_to(m)

#folium.CircleMarker(location=[27.505990145214593, 83.4163982296154], radius=100, popup='Lansat Image location', color='#00008b', fill=True, fill_color='#00008b').add_to(m)

#folium.CircleMarker(location=[27.97959051141473, 83.5804099189001], radius=100, popup='Lansat Image location', color='#006400', fill=True, fill_color='#006400').add_to(m)}

# Create markers
#folium.Marker([27.656174, 85.327837], popup='<strong>Location One</strong>',icon=logoIcon).add_to(m)

folium.Marker([27.696578, 85.358651],
              popup='<div id="popup" style="background: white; position: absolute; margin-top:5%; left:18%; z-index: 999;"> <button id="previous" class="btn btn btn-dark" style="height:50px; width:60px; position: absolute; margin-top:20%; left:1%;"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-left-circle" viewBox="0 0 16 16"> <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8zm15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-4.5-.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H11.5z"/> </svg></button> <button id="next" class="btn btn btn-dark" style="height:50px; width:60px; position: absolute; margin-top:20%; left: 94%;"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right-circle" viewBox="0 0 16 16"> <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8zm15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H4.5z"/> </svg></button> <select class="form-select" style="width:100px; position: absolute; margin-top:10px; left: 10px;"> <option selected id="30-meter">30 M</option> <option value="1" id="10-meter">10 M</option> </select> <img src="static/2000.png" id="satelliteImage" class="img-fluid " alt="Responsive image"> </div>',
              tooltips=tooltips,
              icon=folium.Icon(color='red', icon='plane')).add_to(m)

folium.Marker([27.505990145214593, 83.4163982296154],
              popup='<strong>Gautam Buddha International Airport</strong>',
              tooltips=tooltips,
              icon=folium.Icon(color='blue', icon='plane')).add_to(m)

folium.Marker([27.97959051141473, 83.5804099189001],
              popup='<strong>Kaligandaki A Hydro Power Dam</strong>',
              tooltips=tooltips,
              icon=folium.Icon(color='green', icon='plane')).add_to(m)

folium.Marker([27.776604, 85.300730],
              popup='<strong>Sanima</strong>',
              tooltips=tooltips,
              icon=folium.Icon(color='green')).add_to(m)

folium.Marker([27.697298384477698, 84.50595621178529],
              popup='<strong>kalika chitwan</strong>',
              tooltips=tooltips,
              icon=folium.Icon(color='green')).add_to(m)


# generate map
m.save('templates/map.html')
