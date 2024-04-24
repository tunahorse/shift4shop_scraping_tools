import requests
from pprint import pprint
from requests.exceptions import JSONDecodeError
import json
# Constants and headers
SECURE_URL = secure_url
PRIVATE_KEY = pk
TOKEN = token
headers = {
    'SecureURL': SECURE_URL,
    'PrivateKey': PRIVATE_KEY,
    'Token': TOKEN,
}

url = "https://apirest.3dcart.com/3dCartWebAPI/v2/Customers"
# Make a GET request to the API endpoint
response = requests.get(url, headers=headers)
# Print the response status code
print(response.status_code)
try:
    data = response.json()
    pprint(data)

    # Save the JSON data to a file
    with open('customer_output.json', 'w') as f:
        json.dump(data, f, indent=4)

    
except JSONDecodeError:
    # If a JSONDecodeError occurs, print the raw text of the response
    print("Error: The response is not a valid JSON.")
    print("Raw response:")
    print(response.text)
