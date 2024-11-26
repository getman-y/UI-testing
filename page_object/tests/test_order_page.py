import allure
import pytest
from page_object import data
from page_object.data import UrlData
from page_object.pages.main_page import MainPage
from page_object.pages.order_page import OrderPage


class TestOrderPage:

    @allure.description('Проверяем, что заказ успешно оформлен')
    @pytest.mark.parametrize('user_data', ['user_data_1', 'user_data_2'])
    def test_success_create_order(self, driver, user_data):
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

    @allure.description('Проверяем, что отображаются ошибки, если не заполнены поля на форме "Для кого самокат"')
    def test_show_error_after_dont_fill_fields(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        order_page.go_to_url(UrlData.MAIN_URL)
        main_page.accept_cookie()
        main_page.click_button_header_order()
        order_page.click_button_next()
        elements = order_page.return_text_errors()
        assert ('Введите корректное имя' in elements[0] and 'Введите корректную фамилию' in elements[1]
                and 'Выберите станцию' in elements[2] and 'Введите корректный номер' in elements[3])
