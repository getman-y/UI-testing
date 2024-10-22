from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, '//*[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//*[@id="accordion__panel-{}"]'
    QUESTION_LOCATOR_8 = By.XPATH, '//*[@id="accordion__heading-7"]'

    BUTTON_COOKIE = By.XPATH, '//*[@id="rcc-confirm-button"]'
    BUTTON_ORDER_HEADER = By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']"
    BUTTON_ORDER_BODY = By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']"
    BUTTON_YANDEX_LOGO = By.XPATH, ".//img[@alt='Yandex']/parent::a"
    BUTTON_YANDEX_KEYBOARD = By.XPATH, ".//a[@href='https://ya.ru/?open_keyboard=1']"