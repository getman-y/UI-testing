import allure
import pytest

from page_object.data import AnswerData, UrlData
from page_object.pages.main_page import MainPage


class TestQuestions:

    @pytest.mark.parametrize(
        'num, result',
        [
            (0, AnswerData.ANSWER_1),
            (1, AnswerData.ANSWER_2),
            (2, AnswerData.ANSWER_3),
            (3, AnswerData.ANSWER_4),
            (4, AnswerData.ANSWER_5),
            (5, AnswerData.ANSWER_6),
            (6, AnswerData.ANSWER_7),
            (7, AnswerData.ANSWER_8),
        ]
    )
    @allure.description('Проверяем, корректные ответы на вопросы')
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.go_to_url(UrlData.MAIN_URL)
        assert main_page.get_answer_text(num) == result



