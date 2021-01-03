import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = input('Insira a URL do Ifood')

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get(url)

time.sleep(7)

html = driver.page_source

# res = requests.get(url)
# html = res.text

soup = BeautifulSoup(html, features='html.parser')

products = soup.find('div', class_ = "restaurant__fast-menu")

for products_group in products.find_all('div', class_ = "restaurant-menu-group"):
    print(products_group)
    section_title = products_group.find('h2', class_ = "restaurant-menu-group__title")
    list_cards = products_group.find('ul', class_ = "restaurant-menu-group__container")
    card_elements = list_cards.find_all('li', {"data-test-id":"restaurant-menu-group-item"})

    print(f'Seção: {section_title.text}\n')
    print(f'Card elements:\n {card_elements}')
    for card in card_elements:
        card_wrapper = card.find('div', class_ = "dish-card-wrapper")
        card_link = card_wrapper.find('a', class_ = "dish-card dish-card--horizontal dish-card--has-image")
        card_info = card_link.find('div', class_ = "dish-card__info")

        price = card_info.find('span', class_ = "dish-card__price")
        card_info_top = card_info.find('div', class_ = "dish-card__info-top")
        card_title = card_info_top.find('h3', class_ = "dish-card__description")
        print(f'Produto: {card_title.text}')
        print(f'Preço: {price.text}\n')

driver.quit()
