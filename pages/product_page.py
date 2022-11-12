from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By




class ProductPage(BasePage):
    def should_be_product_page(self):
        self.go_to_push_add_to_basket()
        self.guest_should_be_see_info_about_what_product_added_to_basket()

    def go_to_push_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def guest_should_be_see_info_about_what_product_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.INFO_ABOUT_ADD_TO_BASKET)

    def product_in_basket(self):
        in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET).text
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_ON_PAGE).text
        assert in_basket == product, "Product not in basket"

    def guest_should_be_see_info_about_price_basket(self):
        assert self.is_element_present(*ProductPageLocators.INFO_ABOUT_PRICE)

    def price_in_basket_equal_price_product(self):
        in_basket_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert in_basket_price == product_price, "Price not equals price product"

    def guest_should_be_not_see_info_about_what_product_added_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.INFO_ABOUT_ADD_TO_BASKET)

    def guest_should_be_see_disappearance_info_about_add_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.INFO_ABOUT_ADD_TO_BASKET)