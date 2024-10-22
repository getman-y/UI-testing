import time

import pytest
from selenium.webdriver.common.by import By

from page_object import data, user_data
from page_object.data import UrlData
from page_object.locators.order_page_locators import OrderPageLocators
from page_object.pages.main_page import MainPage
from page_object.pages.order_page import OrderPage


class TestOrderPage:

    @pytest.mark.parametrize('user_data', ['user_data_1', 'user_data_2'])
    def test_success_create_orders(self, driver, user_data):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        order_page.go_to_url(UrlData.MAIN_URL)
        main_page.accept_cookie()
        main_page.click_button_header_order()
        order_page.create_order_part_1(data.UserData.user_data[user_data])
        order_page.create_order_part_2()
        order_page.click_submit_order()
        elements = order_page.wait_status_order()
        assert 'Заказ оформлен' in elements
