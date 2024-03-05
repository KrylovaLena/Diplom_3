import allure
from locators.orders_page_locators import OrdersPageLocators
from pages.header_page import HeaderPage
from data import Site


class TestHeaderPage:
    @allure.title('Проверка перехода по клику на «Лента заказов»')
    @allure.description(
        'Нажимаем на кнопку «Лента Заказов» и проверяем, '
        'что произошёл переход на страницу Ленты заказов'
    )
    def test_redirection_to_order_list(self, driver):
        page = HeaderPage(driver)
        page.click_orders_list_button()
        current_url = page.get_current_url()
        assert current_url == Site.feed_page

    @allure.title('Проверка перехода по клику на «Конструктор»')
    @allure.description(
        'Нажимаем кнопку «Конструктор» и проверяем, '
        'что произошёл переход на главную страницу'
    )
    def test_go_to_constructor(self, driver):
        page = HeaderPage(driver)
        page.click_orders_list_button()
        page.wait_orders_list_title()
        page.click_constructor_button()
        current_url = page.get_current_url()
        assert current_url == Site.main_page