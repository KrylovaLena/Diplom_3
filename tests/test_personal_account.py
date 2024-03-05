import allure
from data import Site
from locators.personal_account_locators import PersonalAccountLocators
from locators.main_page_locators import MainPageLocators
from pages.personal_account_page import PersonalAccountPage
from pages.main_page import MainPage
from pages.orders_page import OrdersPage



class TestPersonalAccount:
    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    @allure.description(
        'Нажимаем на кнопку «Личный кабинет» и проверяем, '
        'что произошёл переход на страницу профиля'
    )
    def test_go_to_account_from_header(self, authorization):
        driver = authorization
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        personal_page = PersonalAccountPage(driver)
        current_url = personal_page.check_switch_on_profile()
        assert current_url == Site.profile_page

    @allure.title('Проверка перехода в раздел «История заказов»')
    @allure.description(
        'Нажимаем на кнопку «История заказов» и проверяем, '
        'что произошёл переход в раздел истории заказов'
    )
    def test_go_to_order_history(self, authorization):
        driver = authorization
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        personal_page = PersonalAccountPage(driver)
        personal_page.click_order_history_button()
        order_page = OrdersPage(driver)
        current_url = order_page.check_switch_on_order_history()
        assert current_url == Site.orders_history

    @allure.title('Проверка выхода из аккаунта')
    @allure.description(
        'Нажимаем на кнопку «Выход» и проверяем, '
        'что произошёл выхода из аккаунта и переход на страницу входа'
    )
    def test_logout(self, authorization):
        driver = authorization
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        order_page = OrdersPage(driver)
        order_page.click_log_out_button()
        personal_page = PersonalAccountPage(driver)
        current_url = personal_page.check_switch_on_login_page()
        assert current_url == Site.login_page