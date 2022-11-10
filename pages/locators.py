from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-lg.btn-primary")
    INFO_ABOUT_ADD_TO_BASKET = (By.CSS_SELECTOR, "div div.alert:nth-child(1)")
    PRODUCT_ON_PAGE = (By.CSS_SELECTOR, "div h1")
    PRODUCT_ADDED_TO_BASKET = (By.CSS_SELECTOR, "div div.alert:nth-child(1) strong")
    INFO_ABOUT_PRICE = (By.CSS_SELECTOR, "div div.alert:nth-child(3)")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "div div.alert:nth-child(3) strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div p.price_color")