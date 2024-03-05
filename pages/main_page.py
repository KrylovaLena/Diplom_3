import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Переходим на страницу логина кликом по кнопке "Войти в аккаунт"')
    def click_personal_account_button(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Кликаем на ингредиент')
    def click_on_ingredient(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.BUN_INGREDIENT)
        self.click_on_element(MainPageLocators.BUN_INGREDIENT)

    @allure.step('Проверяем, что появилось всплывающее окно с деталями игридиента')
    def check_show_window_with_details(self):
        self.wait_for_visibility_of_element(MainPageLocators.INGREDIENT_DETAILS_POPUP)
        return self.get_actually_text(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    @allure.step('Закрываем попап крестиком')
    def click_cross_button(self):
        self.move_to_element_and_click(MainPageLocators.CROSS_BUTTON)

    @allure.step('Нажимаем на кнопку Оформить заказ')
    def click_order_button(self):
        self.move_to_element_and_click(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Проверяем, что заказ оформлен и появился идентификатор заказа')
    def check_show_window_with_order_id(self):
        self.wait_for_visibility_of_element(MainPageLocators.ORDER_ID)
        return self.get_actually_text(MainPageLocators.ORDER_ID)

    @allure.step('Добавить ингридиент в заказ')
    def add_filling_to_order(self):
        self.drag_and_drop_on_element(MainPageLocators.BUN_INGREDIENT, MainPageLocators.ORDER_BASKET)

    @allure.step('Получаем значение счетчика ингредиента')
    def get_count_value(self):
        return self.get_actually_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Проверить скрытость деталей ингредиентов')
    def invisibility_ingredient_details(self):
        self.check_invisibility(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    @allure.step('Проверить наличие деталей ингредиентов на экране')
    def check_displayed_ingredient_details(self) -> bool:
        return self.check_presense(MainPageLocators.INGREDIENT_DETAILS_POPUP).is_displayed()

    @allure.step('Проверить наличие, что заказа начали готовить')
    def check_displayed_order_status_text(self) -> bool:
        return self.check_presense(MainPageLocators.ORDER_STATUS_TEXT).is_displayed()

    @allure.step('Нажимаем кнопку «Лента Заказов»')
    def click_order_feed_button(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.ORDER_FEED_BUTTON)
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)


