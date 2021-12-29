import requests
import os

url_base = "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/13/"

base_x = 2915
base_y = 1486

max_x = 500
max_y = 500

pas_x = 1
pas_y = 1

if not os.path.exists("data/"):
    os.makedirs("data/")

counter = 1
for x in range(0, max_x, pas_x):
    for y in range(0, max_y, pas_y):
        req = requests.get(url_base+"/"+str(base_x+x)+"/"+str(base_y+y))
        with open("data/{}.jpg".format(counter), "wb+") as f:
            f.write(req.content)
        counter = counter + 1
