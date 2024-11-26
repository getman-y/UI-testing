from selenium.webdriver.common.by import By


class OrderPageLocators:
    INPUT_NAME_ORDER = By.XPATH, "//input[@placeholder='* Имя']"
    INPUT_SURNAME_ORDER = By.XPATH, "//input[@placeholder='* Фамилия']"
    INPUT_ADDRESS_ORDER = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    INPUT_SUBWAY_ORDER = By.XPATH, "//input[@placeholder='* Станция метро']"
    BUTTON_SUBWAY_ORDER = By.XPATH, '//button[@value="2"]/div[1]'
    INPUT_PHONE_ORDER = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"

    INPUT_ARRIVAL_TIME = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    DATE_ARRIVAL_TIME = By.XPATH, "//div[@aria-label='Choose суббота, 2-е ноября 2024 г.']"
    INPUT_RENTAL_DATE = By.XPATH, './/div[text()="* Срок аренды"]'
    DATE_RENTAL_DATE = By.XPATH, './/div[text()="сутки"]'

    ORDER_BUTTON_CREATE = By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']"
    ORDER_SUBMIT = By.XPATH, ".//button[text()='Да']"
    ORDER_STATUS_MODAL = By.XPATH, ".//div[text()='Заказ оформлен']"
    ORDER_BUTTON_NEXT = By.XPATH, './/button[text()="Далее"]'

    ERRORS_NAME = By.XPATH, ".//div[text()='Введите корректное имя']"
    ERRORS_SURNAME = By.XPATH, ".//div[text()='Введите корректную фамилию']"
    ERRORS_SUBWAY = By.XPATH, ".//div[text()='Выберите станцию']"
    ERRORS_PHONE = By.XPATH, ".//div[text()='Введите корректный номер']"
