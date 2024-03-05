import allure
from locators.password_recovery_locators import PasswordRecoveryLocators
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):

    """Метод используется для ввода электронной почты в поле для восстановления пароля. /
    Он принимает параметр email и использует метод set_text_to_element для ввода текста в соответствующее поле с помощью локатора PasswordRecoveryLocators.INPUT_EMAIL."""
    @allure.step('Вводим емейл в поле для восстановления пароля')
    def set_email_for_reset_password(self, email):
        self.set_text_to_element(PasswordRecoveryLocators.INPUT_EMAIL, email)

    """Метод выполняет нажатие на кнопку "Восстановить". /
    Он использует метод move_to_element_and_click для перемещения к кнопке и выполнения клика с помощью локатора PasswordRecoveryLocators.RESET_BUTTON."""
    @allure.step('Нажимаем на кнопку Восстановить')
    def click_reset_button(self):
        self.move_to_element_and_click(PasswordRecoveryLocators.RESET_BUTTON)

    """Метод используется для нажатия на кнопку "Показать/скрыть пароль". /
    Он вызывает метод click_on_element с локатором PasswordRecoveryLocators.SHOW_PASSWORD_BUTTON, который выполняет клик на соответствующую кнопку."""
    @allure.step('Кликаем на кнопку Показать/скрыть пароль')
    def click_on_show_password_button(self):
        self.click_on_element(PasswordRecoveryLocators.SHOW_PASSWORD_BUTTON)

    """Метод используется для нажатия на кнопку "Показать/скрыть пароль". /
    Он вызывает метод click_on_element с локатором PasswordRecoveryLocators.SHOW_PASSWORD_BUTTON, который выполняет клик на соответствующую кнопку."""
    @allure.step('Найти кнопку Сохранить')
    def find_save_button(self):
        self.find_my_element(PasswordRecoveryLocators.SAVE_BUTTON)

    """Метод  используется для поиска активного поля пароля. /
    Он вызывает метод find_my_element с локатором PasswordRecoveryLocators.INPUT_ACTIVE, который ищет и возвращает активное поле пароля."""
    @allure.step('Найти активное поле Пароль')
    def find_input_active(self):
        return self.find_my_element(PasswordRecoveryLocators.INPUT_ACTIVE)