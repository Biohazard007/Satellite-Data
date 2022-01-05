import folium

# create map object

m= folium.Map(location=[27.6557582, 85.3283925], zoom_start=12)
# generate map
m.save('map.html')




