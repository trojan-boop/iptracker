import geocoder
import folium
import webbrowser

print ('''
\033[1;33m
		$$$$$$\ $$$$$$$\        $$$$$$$$\ $$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\  
		\_$$  _|$$  __$$\       \__$$  __|$$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |$$  _____|$$  __$$\ 
  		  $$ |  $$ |  $$ |         $$ |   $$ |  $$ |$$ /  $$ |$$ /  \__|$$ |$$  / $$ |      $$ |  $$ |
  		  $$ |  $$$$$$$  |         $$ |   $$$$$$$  |$$$$$$$$ |$$ |      $$$$$  /  $$$$$\    $$$$$$$  |
  		  $$ |  $$  ____/\033[1;32m          $$ |   $$  __$$< $$  __$$ |$$ |      $$  $$<   $$  __|   $$  __$$< 
  		  $$ |  $$ |               $$ |   $$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  $$ |      $$ |  $$ |\033[1;31m{v3.0}\033[1;31m
		$$$$$$\ $$ |               $$ |   $$ |  $$ |$$ |  $$ |\$$$$$$  |$$ | \$$\ $$$$$$$$\ $$ |  $$ |
		\______|\__|               \__|   \__|  \__|\__|  \__| \______/ \__|  \__|\________|\__|  \__|\033[1;32m
\033[1;33m
''')
given_ip = input("Enter You Ip: ")
g = geocoder.ip(given_ip)

myAddress = g.latlng
myCity = g.city
myState = g.state
myCountry = g.country

print(myAddress)
print(myCity)
print(myState)
print(myCountry)

my_map1 = folium.Map(location=myAddress, zoom_start=12)

folium.CircleMarker(location=myAddress, redius=50, popup= "Yorkshire").add_to(my_map1)

folium.Marker(myAddress, popup="Yorkshire").add_to(my_map1)

my_map1.save("my_map.html")



