from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.base_page import BasePage


class MainPage(BasePage):
    def click_to_question(self, locator_q_formatted):
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_8)
        self.click_to_element(locator_q_formatted)

    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        self.click_to_question(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

