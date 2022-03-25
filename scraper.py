import requests

url = "https://www.ceneo.pl/91714422#tab=reviews_scroll"

response = requests.get(url)

print(response.status_code)