from page_object.data import UrlData
from page_object.pages.main_page import MainPage


class TestMainPage:

    def test_click_button_header_order_show_order_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(UrlData.MAIN_URL)
        main_page.accept_cookie()
        main_page.click_button_header_order()
        assert main_page.current_url() == UrlData.ORDER_PAGE_URL

    def test_click_button_body_order_show_order_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(UrlData.MAIN_URL)
        main_page.accept_cookie()
        main_page.click_button_body_order()
        assert main_page.current_url() == UrlData.ORDER_PAGE_URL

    def test_click_button_yandex_redirect_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(UrlData.MAIN_URL)
        main_page.accept_cookie()
        main_page.click_button_yandex()
        main_page.switch_to_tab()
        main_page.find_element_on_dzen()
        assert UrlData.DZEN_PAGE_URL in main_page.current_url()
