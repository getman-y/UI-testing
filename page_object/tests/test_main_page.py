import pytest

from page_object.data import ANSWER_1, ANSWER_2, ANSWER_3, ANSWER_4, ANSWER_5, ANSWER_6, ANSWER_7, ANSWER_8
from page_object.pages.main_page import MainPage


class TestMainPage:

    @pytest.mark.parametrize(
        'num, result',
        [
            (0, ANSWER_1),
            (1, ANSWER_2),
            (2, ANSWER_3),
            (3, ANSWER_4),
            (4, ANSWER_5),
            (5, ANSWER_6),
            (6, ANSWER_7),
            (7, ANSWER_8),
        ]
    )
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        assert main_page.get_answer_text(num) == result



