import allure
from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    @allure.step('Проверяем переход на страницу профиля')
    def check_switch_on_profile(self):
        self.wait_until_element_visibility(PersonalAccountLocators.PROFILE_BUTTON)
        return self.get_current_url()

    """Метод выполняет клик на ссылке "Восстановить пароль" на странице личного кабинета."""
    @allure.step('Нажать на "Восстановить пароль"')
    def click_password_reset_link(self):
        self.click_on_element(PersonalAccountLocators.RESET_PASSWORD_LINK)

    @allure.step('Проверяем переход на страницу Вход')
    def check_switch_on_login_page(self):
        self.wait_until_element_visibility(PersonalAccountLocators.LOGIN_HEADER)
        return self.get_current_url()

    @allure.step('Нажимаем кнопку «История заказов»')
    def click_order_history_button(self):
        self.wait_for_element_to_be_clickable(PersonalAccountLocators.ORDER_HISTORY_BUTTON)
        self.click_on_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)
