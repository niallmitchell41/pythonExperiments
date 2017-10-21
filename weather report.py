
# fetching the weather station project (learning resources in raspberrypi.org/learning/fetchingthe weather)




from requests import get
import json
from pprint import pprint

# weather station in Londonderry

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/595229'


weather = get(url).json()['items']
pprint(weather)

