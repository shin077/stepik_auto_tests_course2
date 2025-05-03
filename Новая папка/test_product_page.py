import pytest
from pages.product_page import ProductPage

@pytest.mark.xfail(reason="Сообщение появляется после добавления")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    assert page.is_not_element_present(*ProductPage.SUCCESS_MESSAGE), \
        "Сообщение об успехе появилось"

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPage.SUCCESS_MESSAGE), \
        "Сообщение об успехе присутствует"

@pytest.mark.xfail(reason="Сообщение не исчезает")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    assert page.is_disappeared(*ProductPage.SUCCESS_MESSAGE), \
        "Сообщение не исчезло"