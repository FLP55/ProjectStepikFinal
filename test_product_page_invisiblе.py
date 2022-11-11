import pytest
from pages.product_page import ProductPage
from pages.base_page import BasePage
import time


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_push_add_to_basket()
    page.guest_should_be_not_see_info_about_what_product_added_to_basket()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.guest_should_be_not_see_info_about_what_product_added_to_basket()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_push_add_to_basket()
    page.guest_should_be_see_disappearance_info_about_add_to_basket()
