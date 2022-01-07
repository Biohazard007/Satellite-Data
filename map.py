import folium

# create map object
m = folium.Map(location=[27.656174, 85.327837], zoom_start=17)

# Global tooltip
tooltip = 'Nepal Academy of Science and Technology'
tooltips = 'Tribhuvan International Airport'

# Custom image
logoIcon = folium.features.CustomIcon('./static/MicrosoftTeams-image.png', icon_size=(50, 50))

# Circle marker
folium.CircleMarker(location=[27.696578, 85.358651],
                     radius=100,
                     popup='Lansat Image location',
                     color='#FF7F50',
                     fill=True,
                     fill_color='#FF7F50').add_to(m)

# Create markers
folium.Marker([27.656174, 85.327837],
              popup='<strong>Location One</strong>',
              icon=logoIcon).add_to(m)

folium.Marker([27.696578, 85.358651],
              popup='<strong>Location Two</strong>',
              tooltips=tooltips,
              icon=folium.Icon(color='red', icon='plane')).add_to(m)

# generate map
m.save('map.html')
