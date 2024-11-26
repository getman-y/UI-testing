import allure

from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Нажимаем на вопрос')
    def click_to_question(self, locator_q_formatted):
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_8)
        self.click_to_element(locator_q_formatted)

    @allure.step('Получаем текст ответа')
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        self.click_to_question(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Нажимаем на кнопку "Закаказать" в хедере страницы')
    def click_button_header_order(self):
        self.click_to_element(MainPageLocators.BUTTON_ORDER_HEADER)

    @allure.step('Нажимаем на кнопку "Заказать" в теле страницы')
    def click_button_body_order(self):
        self.click_to_element(MainPageLocators.BUTTON_ORDER_BODY)

    @allure.step('Нажимаем на логотип Яндекс')
    def click_button_yandex(self):
        self.click_to_element(MainPageLocators.BUTTON_YANDEX_LOGO)

    @allure.step('Нажимаем на логотип Самокат')
    def click_logo_samokat(self):
        self.click_to_element(MainPageLocators.BUTTON_SAMOKAT_LOGO)

    @allure.step('Принимаем куки')
    def accept_cookie(self):
        self.click_to_element(MainPageLocators.BUTTON_COOKIE)

    @allure.step('Переключаемся на последнюю открытую вкладку')
    def switch_to_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Дожидаемся отображения элемента на сайте Дзен')
    def find_element_on_dzen(self):
        self.find_element_with_wait(MainPageLocators.BUTTON_YANDEX_KEYBOARD)




