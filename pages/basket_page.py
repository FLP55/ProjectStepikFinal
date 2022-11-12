from .locators import MainPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def basket_is_empty(self):
        basket_is_empties = self.browser.find_element(*MainPageLocators.BASKET_IS_EMPTY).text
        assert "Your basket is empty." in basket_is_empties, "Basket is not empty"

    def products_is_no_present_in_basket(self):
        assert self.is_not_element_present(*MainPageLocators.ITEMS_IN_BASKET)

