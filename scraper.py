import requests
from bs4 import BeautifulSoup


url = "https://www.ceneo.pl/91714422#tab=reviews_scroll"
response = requests.get(url)

page = BeautifulSoup(response.text, 'html.parser')

opinions = page.select("div.js_product-review")
opinion = opinions.pop(0)
opinion_id = opinion["data-entry-id"]
author = opinion.select_one("span.user-post__author-name").get_text().strip()

useful = opinion.select_one("button.vote-yes > span").get_text().strip()
useless = opinion.select_one("button.vote-yes > span").get_text().strip()

print(type(opinion_id))
print((opinion_id))