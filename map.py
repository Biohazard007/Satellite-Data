import folium

# create map object

m = folium.Map(location=[27.6557582, 85.3283925], zoom_start=14)

# Create markers
folium.Marker([27.6557587, 85.3283922], popup='<strong>Location One</strong>')

# generate map
m.save('map.html')




