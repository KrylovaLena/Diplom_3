import allure
import pytest
from locators.orders_page_locators import OrdersPageLocators
from locators.main_page_locators import MainPageLocators
from pages.orders_page import OrdersPage
from pages.main_page import MainPage
from pages.header_page import HeaderPage
from helpers import Helpers



class TestOrderListPage:
    @allure.title('Проверка появления всплывающего окна с деталями')
    @allure.description('Кликаем на заказ и проверяем, что появилось всплывающее окно с деталями')
    def test_get_order_popup(self, driver):
        page = HeaderPage(driver)
        page.click_orders_list_button()
        page = OrdersPage(driver)
        page.click_order()
        assert page.check_order_structure() == True

    @allure.title('Проверка отображения заказов пользователя в Ленте заказов')
    @allure.description(
        'Получаем номера всех заказов в Ленте, и проверяем, '
        'что номера заказов пользователя отображаются в Ленте заказов'
    )
    def test_find_order_in_list(self, authorization, orders_numbers):
        driver = authorization
        page = MainPage(driver)
        page.click_order_feed_button()
        orders_page = OrdersPage(driver)
        feed_orders = orders_page.get_orders_numbers(orders_numbers)
        for order_number in orders_numbers:
            assert str(order_number) in feed_orders, 'Заказы пользователя не отображаются в Ленте заказов'

    @allure.title('Проверка увеличения значения счетчика заказов после создания нового заказа')
    @allure.description(
        'Получаем значение счетчика заказов до и после создания нового заказа, '
        'и проверяем, что значение счетчика увеличилось'
    )
    @pytest.mark.parametrize('counter', [OrdersPageLocators.ALL_TIME_COUNTER, OrdersPageLocators.TODAY_COUNTER])
    def test_today_orders_counter(self, create_and_delete_user, authorization, counter):
        driver = authorization
        payload, token = create_and_delete_user
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        order_page = OrdersPage(driver)
        prev_counter_value = order_page.get_counter_value(counter)
        Helpers().create_order(token)
        current_counter_value = order_page.get_counter_value(counter)
        assert current_counter_value > prev_counter_value

    @allure.title('Проверка отображения номера заказа в разделе "В работе')
    @allure.description('Получаем номер нового заказа, и проверяем, что номер заказа появился в разделе "В работе"')
    def test_new_order_appears_in_work_list(self, authorization, orders_numbers):
        driver = authorization
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        order_page = OrdersPage(driver)
        last_order = order_page.get_user_order(orders_numbers)
        order_in_progress = order_page.get_user_order_in_progress()
        assert last_order == order_in_progress

