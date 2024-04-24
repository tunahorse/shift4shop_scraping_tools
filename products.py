import json
import requests
from pprint import pprint
from requests.exceptions import JSONDecodeError
# Constants and headers
SECURE_URL = url
PRIVATE_KEY = key
TOKEN = token
#set these up as OS vars
headers = {
    'SecureURL': SECURE_URL,
    'PrivateKey': PRIVATE_KEY,
    'Token': TOKEN,
}
# API endpoint URL
url = "https://apirest.3dcart.com/3dCartWebAPI/v2/Products?limit=100"
# filter products as need from the above url 
# filtering docs, leave a lot to be desired play with it as they are not accurate. If you have 1000+ Products will most likely need some sort of pagination. 
# https://apirest.3dcart.com/v2/products/index.html#products
# Make a GET request to the API endpoint
response = requests.get(url, headers=headers)
# Print the response status code

print(response.status_code)
try:
    data = response.json()
    pprint(data)

    # Save the JSON data to a file
    with open('product_output.json', 'w') as f:
        json.dump(data, f, indent=4)
    # for product in response.json():
    #     print(product['SKUInfo']['Name'])
    #     print(product['SKUInfo']['Price'])
    #     print(product['SKUInfo']['CatalogID'])
   
    
    
    
except JSONDecodeError:
    # If a JSONDecodeError occurs, print the raw text of the response
    print("Error: The response is not a valid JSON.")
    print("Raw response:")
    print(response.text)
