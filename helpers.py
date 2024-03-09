import allure
import requests
from data import Site
from locators.orders_page_locators import OrdersPageLocators

class Helpers:
    @allure.step('Создать заказ')
    def create_order(self, token):
        requests.post(Site.order, headers={'Authorization': token}, data=OrdersPageLocators.INGREDIENTS)

    @allure.step('Получить заказы пользователя')
    def get_user_orders(self, token):
        user_orders = requests.get(Site.order, headers={'Authorization': token}).json()["orders"]
        return user_orders