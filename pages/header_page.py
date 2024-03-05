import allure
from locators.header_page_locators import HeaderPageLocators
from locators.orders_page_locators import OrdersPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    @allure.step('Переход на страницу Лента заказов')
    def click_orders_list_button(self):
        self.move_to_element_and_click(HeaderPageLocators.ORDERS_LIST)
        self.wait_until_element_visibility(OrdersPageLocators.ORDERS_LIST_TITLE)

    @allure.step('Переход в "Конструктор"')
    def click_constructor_button(self):
        self.click_on_element(HeaderPageLocators.CONSTRUCTOR)

    @allure.step('Переход в Личный кабинет')
    def click_on_account(self):
        self.move_to_element_and_click(HeaderPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Ожидание ленты заказов')
    def wait_orders_list_title(self):
        self.wait_until_element_visibility(OrdersPageLocators.ORDERS_LIST_TITLE)

    @allure.step('Нажимаем на поле "email"')
    def click_email_field(self):
        self.wait_for_element_to_be_clickable(HeaderPageLocators.EMAIL)
        self.click_on_element(HeaderPageLocators.EMAIL)

    @allure.step('Заполняем поле "email"')
    def set_email(self, email):
        self.send_keys(HeaderPageLocators.EMAIL, email)

    @allure.step('Нажимаем на поле "Пароль"')
    def click_pass_field(self):
        self.click_on_element(HeaderPageLocators.PASSWORD)

    @allure.step('Заполняем поле "Пароль"')
    def set_pass(self, password):
        self.send_keys(HeaderPageLocators.PASSWORD, password)

    @allure.step('Нажимаем кнопку «Войти»')
    def click_login_button(self):
        self.click_on_element(HeaderPageLocators.LOGIN_BUTTON)\

    @allure.step('Авторизация')
    def login(self, email, password):
        self.click_email_field()
        self.set_email(email)
        self.click_pass_field()
        self.set_pass(password)
        self.click_login_button()