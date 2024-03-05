import allure
import requests
from locators.orders_page_locators import OrdersPageLocators
from pages.base_page import BasePage
from data import Site


class OrdersPage(BasePage):
    @allure.step('Нажимаем на заказ в списке Лента заказов')
    def click_order(self):
        self.click_on_element(OrdersPageLocators.ORDER_LINK)

    @allure.step('Получаем номер заказа')
    def get_user_order(self, orders_numbers):
        last_order = '0' + str(orders_numbers[-1])
        self.wait_for_text_to_be_present_in_element(OrdersPageLocators.NUMBER_IN_PROGRESS, last_order)
        return last_order

    @allure.step('Получаем номер заказа в работе')
    def get_user_order_in_progress(self):
        return self.get_actually_text(OrdersPageLocators.NUMBER_IN_PROGRESS)

    @allure.step('Проверка отображения состава')
    def check_order_structure(self):
        return self.check_presense(OrdersPageLocators.ORDER_STRUCTURE).is_displayed()

    @allure.step('Проверяем переход на страницу История заказов')
    def check_switch_on_order_history(self):
        self.wait_for_visibility_of_element(OrdersPageLocators.ENABLED_ORDER_HISTORY_BUTTON)
        return self.get_current_url()

    @allure.step('Получаем номера всех заказов в Ленте заказов')
    def get_orders_numbers(self, user_orders):
        last_order = '0' + str(user_orders[-1])
        self.wait_for_text_to_be_present_in_element(OrdersPageLocators.NUMBER_IN_PROGRESS, last_order)
        text = '#0' + str(user_orders[-1])
        self.wait_for_text_to_be_present_in_element(OrdersPageLocators.LAST_ORDER, text)
        all_elements = self.find_elements(OrdersPageLocators.ORDER_NUMBERS)
        return [elm.text.strip('#0') for elm in all_elements]

    @allure.step('Получаем значение счетчика заказов')
    def get_counter_value(self, counter):
        self.wait_for_visibility_of_element(OrdersPageLocators.ORDERS_LIST_TITLE)
        return self.get_actually_text(counter)

    @allure.step('Нажимаем кнопку «Выход»')
    def click_log_out_button(self):
        self.wait_for_element_to_be_clickable(OrdersPageLocators.EXIT_BUTTON)
        self.click_on_element(OrdersPageLocators.EXIT_BUTTON)

    @allure.step('Создать заказ')
    def create_order(self, token):
        requests.post(Site.order, headers={'Authorization': token}, data=OrdersPageLocators.INGREDIENTS)

    @allure.step('Получить заказы пользователя')
    def get_user_orders(self, token):
        user_orders = requests.get(Site.order, headers={'Authorization': token}).json()["orders"]
        return user_orders