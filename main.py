import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
class IfoodScrapper():
    def __init__(self):
        self.count = 0
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(executable_path="./chromedriver", options=self.options)

    def select_categories(self):
        select_button = self.driver.find_element_by_css_selector("#__next > div > main > div.restaurant-container > div.restaurant-column > div.restaurant-menu.restaurant-menu--hidden-search > div > div:nth-child(1) > div.restaurant-menu__header.restaurant-menu__header--sticky > div > div.restaurant-menu__fast-menu.restaurant-menu__fast-menu--sticky > div > div.marmita-dropdown-menu__button > button")
        select_button.click()
        time.sleep(2)
        dropdown = self.driver.find_element_by_css_selector("#__next > div > main > div.restaurant-container > div.restaurant-column > div.restaurant-menu.restaurant-menu--hidden-search > div > div:nth-child(1) > div.restaurant-menu__header.restaurant-menu__header--sticky > div > div.restaurant-menu__fast-menu.restaurant-menu__fast-menu--sticky > div > ul")
        categories = dropdown.find_elements_by_tag_name("li")

        for categorie in categories:
            categorie_button = categorie.find_element_by_tag_name("button")
            categorie_button.click()
            # categorie_span= categorie_button.find_elements_by_tag_name("span")
            # categorie_name = categorie_span.text
            self.count += 1

            self.build_cheet()


    def build_cheet(self):
        time.sleep(7)

        # res = requests.get(url)
        # html = res.text

        html = self.driver.page_source

        soup = BeautifulSoup(html, features='html.parser')

        products = soup.find('div', class_ = "restaurant__fast-menu")

        for products_group in products.find_all('div', class_ = "restaurant-menu-group"):
            section_title = products_group.find('h2', class_ = "restaurant-menu-group__title")
            list_cards = products_group.find('ul', class_ = "restaurant-menu-group__container")
            card_elements = list_cards.find_all('li', {"data-test-id":"restaurant-menu-group-item"})

            print(f'Seção: {section_title.text}\n')
            # print(f'Card elements:\n {card_elements}')

            for _ in range(0, len(card_elements) - 1):
                card_wrapper = card_elements[self.count].find('div', class_ = "dish-card-wrapper")
                card_link = card_wrapper.find('a', class_ = "dish-card dish-card--horizontal dish-card--has-image")
                card_info = card_link.find('div', class_ = "dish-card__info")

                price = card_info.find('span', class_ = "dish-card__price")
                card_info_top = card_info.find('div', class_ = "dish-card__info-top")
                card_title = card_info_top.find('h3', class_ = "dish-card__description")
                print(f'Produto: {card_title.text}')
                print(f'Preço: {price.text}\n')

if __name__ == "__main__":
    url = "https://www.ifood.com.br/delivery/recife-pe/cacau-show---sh-recife-plaza-casa-forte-parnamirim/df79fc61-be2c-4236-a3a2-ad8832cc40d0"
    #url = input('Insira a URL do Ifood')

    scrapper = IfoodScrapper()
    
    scrapper.driver.get(url)
    time.sleep(5)

    scrapper.driver.execute_script("window.scrollTo(0, 480)")
    time.sleep(2)

    scrapper.select_categories()
    scrapper.driver.quit()
