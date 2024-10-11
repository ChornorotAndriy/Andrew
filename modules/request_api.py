import requests
#import function 
from .read_json import read_json
#Import json module
import json
#use the function for read json
data_api = read_json(name_file= 'config_api.json')
#get api key
API_KEY = data_api['api_key']
#get city
CITY_NAME = data_api['city_name']
#set url for requests
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
#send request to get the data
response = requests.get(URL)
#check if the request has been sent
if response.status_code == 200:
    #turns JSON into a python dictionary
    data_dict = json.loads(response.content)
    #displays the dictionary on screen
    print(json.dumps(data_dict, indent= 4))