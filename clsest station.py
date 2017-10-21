from requests import get
import json
from pprint import pprint
from haversine import haversine




stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/595229'



my_lat = 54.506446
my_lon = -6.295293



all_stations = get(stations).json()['items']

