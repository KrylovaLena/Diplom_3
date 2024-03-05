import allure
from locators.personal_account_locators import PersonalAccountLocators
from locators.header_page_locators import HeaderPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    @allure.step('Проверяем переход на страницу профиля')
    def check_switch_on_profile(self):
        self.wait_for_visibility_of_element(PersonalAccountLocators.PROFILE_BUTTON)
        return self.get_current_url()

    """Метод выполняет клик на ссылке "Восстановить пароль" на странице личного кабинета."""
    @allure.step('Нажать на "Восстановить пароль"')
    def click_password_reset_link(self):
        self.click_on_element(PersonalAccountLocators.RESET_PASSWORD_LINK)

    # """Метод выполняет клик на кнопке, чтобы перейти в личный кабинет. /
    # Он также ожидает, пока элемент с профилем пользователя станет видимым."""
    # @allure.step('Переход в личный кабинет')
    # def click_account_button(self):
    #     self.wait_for_element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    #     self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Проверяем переход на страницу Вход')
    def check_switch_on_login_page(self):
        self.wait_for_visibility_of_element(PersonalAccountLocators.LOGIN_HEADER)
        return self.get_current_url()

    # """Метод выполняет клик на ссылке "История заказов" для перехода в раздел с историей заказов."""
    # @allure.step('Переход в раздел "История заказов"')
    # def click_order_list_link(self):
    #     self.click_on_element(PersonalAccountLocators.ORDERS_HISTORY)
    #
    # """Метод извлекает номер заказа из элемента на странице с историей заказов."""
    # @allure.step('Получаем номер заказа в Истории заказов')
    # def get_order_number(self):
    #     return self.get_text_of_element(PersonalAccountLocators.ORDER_NUMBER)

    # """Метод ищет элемент с конструкторами на странице."""
    # @allure.step('Найти конструкторы')
    # def find_constructor(self):
    #     return self.find_my_element(HeaderPageLocators.CONSTRUCTOR)

    # """Метод ожидает, пока элемент с профилем пользователя станет видимым."""
    # @allure.step('Дождаться открытия профиля')
    # def wait_profile(self):
    #     return self.wait_until_element_visibility(PersonalAccountLocators.PROFILE)

    @allure.step('Нажимаем кнопку «История заказов»')
    def click_order_history_button(self):
        self.wait_for_element_to_be_clickable(PersonalAccountLocators.ORDER_HISTORY_BUTTON)
        self.click_on_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)

    # """Метод ожидает, пока кнопка входа станет видимой."""
    # @allure.step('Дождаться кнопки войти')
    # def wait_enter(self):
    #     return self.wait_until_element_visibility(PersonalAccountLocators.ENTER_BUTTON)

    # """Метод извлекает текст с кнопки входа."""
    # @allure.step('Получаем текст с кнопки входа')
    # def get_text_enter(self):
    #     return self.get_text_of_element(PersonalAccountLocators.ENTER_BUTTON)

    # """Метод ищет элемент со статусом заказа."""
    # @allure.step('Найти статус заказа')
    # def find_order_status(self):
    #     return self.find_my_element(PersonalAccountLocators.ORDER_STATUS)