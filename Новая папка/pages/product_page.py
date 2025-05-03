from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
    
    def __init__(self, browser, url):
        super().__init__(browser, url)
    
    def add_to_basket(self):
        add_button = self.browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        add_button.click()