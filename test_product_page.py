import pytest
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  # pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  #     marks = pytest.mark.xfail),
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_push_add_to_basket()
    page.solve_quiz_and_get_code()
    page.guest_should_be_see_info_about_what_product_added_to_basket()
    page.product_in_basket()
    page.guest_should_be_see_info_about_price_basket()
    page.price_in_basket_equal_price_product()


class TestGuestShouldSeeLoginLinkAndPage():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()


class TestChekInfoAboutProductAddedToBasket():
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_push_add_to_basket()
        page.guest_should_be_not_see_info_about_what_product_added_to_basket()

    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.guest_should_be_not_see_info_about_what_product_added_to_basket()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_push_add_to_basket()
        page.guest_should_be_see_disappearance_info_about_add_to_basket()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.products_is_no_present_in_basket()
    page.basket_is_empty()



class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = LoginPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(str(time.time()) + "blue_passport@mail.com", "12345plspls")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/")
        page.open()
        page.guest_should_be_not_see_info_about_what_product_added_to_basket()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0")
        page.open()
        page.go_to_push_add_to_basket()
        page.solve_quiz_and_get_code()
        page.guest_should_be_see_info_about_what_product_added_to_basket()
        page.product_in_basket()
        page.guest_should_be_see_info_about_price_basket()
        page.price_in_basket_equal_price_product()
