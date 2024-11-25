#  Install the requests module and write a Python program that makes a simple HTTP GET request to a website and prints the response content (e.g., the HTML of the page).

import requests
url = "https://github.com"

response = requests.get(url)
print(response.text)