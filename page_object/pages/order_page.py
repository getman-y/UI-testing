import allure

from page_object.locators.order_page_locators import OrderPageLocators
from page_object.pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполняем первую часть заказа, блок "Для кого самокат" ')
    def create_order_part_1(self, data: dict):
        self.fill_name(data['name'])
        self.fill_surname(data['surname'])
        self.fill_address(data['address'])
        self.fill_subway()
        self.fill_phone(data['phone'])
        self.click_button_next()

    @allure.step('Заполняем вторую часть заказа, блок "Про аренду" ')
    def create_order_part_2(self):
        self.fill_arrival_date()
        self.fill_rental()
        self.click_button_create()

    @allure.step('Заполняем поле "Имя"')

    def fill_name(self, name):
        self.add_text_to_element(OrderPageLocators.INPUT_NAME_ORDER, name)

    @allure.step('Заполняем поле "Фамилия"')
    def fill_surname(self, surname):
        self.add_text_to_element(OrderPageLocators.INPUT_SURNAME_ORDER, surname)

    @allure.step('Заполняем поле "Адрес"')
    def fill_address(self, address):
        self.add_text_to_element(OrderPageLocators.INPUT_ADDRESS_ORDER, address)

    @allure.step('Заполняем поле "Станция"')
    def fill_subway(self):
        self.click_to_element(OrderPageLocators.INPUT_SUBWAY_ORDER)
        self.click_to_element(OrderPageLocators.BUTTON_SUBWAY_ORDER)

    @allure.step('Заполняем поле "Телефон"')
    def fill_phone(self, phone):
        self.add_text_to_element(OrderPageLocators.INPUT_PHONE_ORDER, phone)

    @allure.step('Заполняем поле "Когда привезти самокат"')
    def fill_arrival_date(self):
        self.click_to_element(OrderPageLocators.INPUT_ARRIVAL_TIME)
        self.click_to_element(OrderPageLocators.DATE_ARRIVAL_TIME)

    @allure.step('Заполняем поле "Срок аренды"')
    def fill_rental(self):
        self.click_to_element(OrderPageLocators.INPUT_RENTAL_DATE)
        self.click_to_element(OrderPageLocators.DATE_RENTAL_DATE)

    @allure.step('Клик на кнопку "Далее"')
    def click_button_next(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_NEXT)

    @allure.step('Клик на кнопку "заказать"')
    def click_button_create(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_CREATE)

    @allure.step('Клик на "Да"')
    def click_submit_order(self):
        self.click_to_element(OrderPageLocators.ORDER_SUBMIT)

    @allure.step('Ожидаем отображение статуса заказа')
    def wait_status_order(self):
        order_status_text = self.find_element_with_wait(OrderPageLocators.ORDER_STATUS_MODAL)
        return order_status_text.text

    @allure.step('Получаем текст ошибку в форме "Для кого самокат"')
    def return_text_errors(self):
        text_errors_name = self.find_element_with_wait(OrderPageLocators.ERRORS_NAME)
        text_errors_surname = self.find_element_with_wait(OrderPageLocators.ERRORS_SURNAME)
        text_errors_subway = self.find_element_with_wait(OrderPageLocators.ERRORS_SUBWAY)
        text_errors_phone = self.find_element_with_wait(OrderPageLocators.ERRORS_PHONE)
        return [text_errors_name.text, text_errors_surname.text, text_errors_subway.text, text_errors_phone.text]
