import requests
from bs4 import BeautifulSoup
from lxml import etree

amazon_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
    "Accept-Language": "en-US,en;q=0.5",
}


class Amazon:
    product_page = 0

    def __init__(self, amazon_endpoint):
        """Creates an object of Amazon class. Retrieves product page."""
        amazon_response = requests.get(url=amazon_endpoint, headers=amazon_headers)
        amazon_response.raise_for_status()
        self.product_page = amazon_response.text

    def get_product_data(self):
        """Gets product data."""
        amazon_parse_response = BeautifulSoup(self.product_page, "lxml")

        product_name = amazon_parse_response.find(id="title").get_text()
        price_whole = amazon_parse_response.find(name="span", class_="a-price-whole").get_text()
        price_decimal = amazon_parse_response.find(name="span", class_="a-price-fraction").get_text()
        product_price = float(f"{price_whole}{price_decimal}")

        product = {
            "name": product_name,
            "price": product_price
        }

        return product
