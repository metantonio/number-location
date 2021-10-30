import phonenumbers
#from thenumber import thenumber
import folium
from phonenumbers import geocoder, carrier
import os

thenumber=os.environ.get("Number")
sanNumber = phonenumbers.parse(thenumber)

yourLocation = "country: "+geocoder.description_for_number(sanNumber, "en")
print(yourLocation)

#getting carrier

service_provider = phonenumbers.parse(thenumber)
print("carrier: " + carrier.name_for_number(service_provider, "en"))
print("Número de Teléfono: " + thenumber)

from opencage.geocoder import OpenCageGeocode
##La API key es de opencage.com, se debe crear un archivo .env

Key=os.environ.get("Key")
geocoder = OpenCageGeocode(Key)

query = str(yourLocation)

result = geocoder.geocode(query)
#print(result)

latitude1 = result[0]['geometry']['lat']
longitude1 = result[0]['geometry']['lng']
latitude=[]
longitude=[]
for element in range(len(result)):
    latitude.append(result[element]['geometry']['lat'])
    longitude.append(result[element]['geometry']['lng'])
#latitude2 = result[1]['geometry']['lat']
#longitude2 = result[1]['geometry']['lng']
#latitude3 = result[2]['geometry']['lat']
#longitude3 = result[2]['geometry']['lng']
#latitude4 = result[3]['geometry']['lat']
#longitude4 = result[3]['geometry']['lng']
#latitude5 = result[4]['geometry']['lat']
#longitude5 = result[4]['geometry']['lng']
#latitude6 = result[5]['geometry']['lat']
#longitude6 = result[5]['geometry']['lng']
#latitude7 = result[6]['geometry']['lat']
#longitude7 = result[6]['geometry']['lng']

print("Position 0: ",latitude1, longitude1)
#print("Boundary 1: ",latitude2, longitude2)

myMap = folium.Map(location = [latitude1, longitude1], zoom_start = 9)
folium.Marker([latitude1, longitude1],popup = yourLocation).add_to((myMap))
folium.Circle([latitude1, longitude1], radius=9000, popup = "Ubication zone 1", line_color='#3186cc',
                    fill_color='#3186cc', fill=True).add_to((myMap))
#folium.Circle([latitude2, longitude2], radius=9000, popup = "Ubication antena", line_color='#86cc31',fill_color='#86cc31', fill=True).add_to((myMap))
#folium.Circle([latitude3, longitude3], radius=9000, popup = "Ubication antena", line_color='#cc7731',fill_color='#cc7731', fill=True).add_to((myMap))
#folium.Circle([latitude4, longitude4], radius=9000, popup = "Ubication antena", line_color='#3186cc',fill_color='#3186cc', fill=True).add_to((myMap))
#folium.Circle([latitude5, longitude5], radius=9000, popup = "Ubication antena", line_color='#3186cc',fill_color='#3186cc', fill=True).add_to((myMap))
#folium.Circle([latitude6, longitude6], radius=9000, popup = "Ubication antena", line_color='#3186cc',fill_color='#3186cc', fill=True).add_to((myMap))
#folium.Circle([latitude7, longitude7], radius=9000, popup = "Ubication antena", line_color='#3186cc',fill_color='#3186cc', fill=True).add_to((myMap))
for i in range(len(latitude)):
    folium.Circle([latitude[i], longitude[i]], radius=9000, popup = "Ubication antena", line_color='#86cc31',fill_color='#86cc31', fill=True).add_to((myMap))


##folium.Marker([latitude3, longitude3],popup = "Boundary 2").add_to((myMap))
##save ma in html file
myMap.save('Location.html')
print("map created at: Location.html")
