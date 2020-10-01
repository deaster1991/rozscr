import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
    'From': 'newbie217@gmail.com'
}


def get_price_rozetka(url):
    r = requests.get(url, headers)
    html_as_string = r.text
    parsed_html = BeautifulSoup(html_as_string, "html.parser")
    price_of = parsed_html.find(class_="product-prices__symbol")
    final_price = int(str(price_of.previous_sibling).replace('\xa0', ''))
    return final_price


url_rozetka = input()
print(get_price_rozetka(url_rozetka))
