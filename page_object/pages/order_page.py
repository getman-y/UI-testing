import time

from page_object import user_data
from page_object.locators.main_page_locators import MainPageLocators
from page_object.locators.order_page_locators import OrderPageLocators
from page_object.pages.base_page import BasePage


class OrderPage(BasePage):
    def create_order_part_1(self, data: dict):
        self.fill_name(data['name'])
        self.fill_surname(data['surname'])
        self.fill_address(data['address'])
        self.fill_subway()
        self.fill_phone(data['phone'])
        self.click_button_next()

    def create_order_part_2(self):
        self.fill_arrival_date()
        self.fill_renta()
        self.click_button_create()

    def fill_name(self, name):
        self.add_text_to_element(OrderPageLocators.INPUT_NAME_ORDER, name)

    def fill_surname(self, surname):
        self.add_text_to_element(OrderPageLocators.INPUT_SURNAME_ORDER, surname)

    def fill_address(self, address):
        self.add_text_to_element(OrderPageLocators.INPUT_ADDRESS_ORDER, address)

    def fill_subway(self):
        self.click_to_element(OrderPageLocators.INPUT_SUBWAY_ORDER)
        self.click_to_element(OrderPageLocators.BUTTON_SUBWAY_ORDER)

    def fill_phone(self, phone):
        self.add_text_to_element(OrderPageLocators.INPUT_PHONE_ORDER, phone)

    def fill_arrival_date(self):
        self.click_to_element(OrderPageLocators.INPUT_ARRIVAL_TIME)
        self.click_to_element(OrderPageLocators.DATE_ARRIVAL_TIME)

    def fill_renta(self):
        self.click_to_element(OrderPageLocators.INPUT_RENTAL_DATE)
        self.click_to_element(OrderPageLocators.DATE_RENTAL_DATE)

    def click_button_next(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_NEXT)

    def click_button_create(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_CREATE)

    def click_submit_order(self):
        self.click_to_element(OrderPageLocators.ORDER_SUBMIT)

    def wait_status_order(self):
        order_status_text = self.find_element_with_wait(OrderPageLocators.ORDER_STATUS_MODAL)
        return order_status_text.text
