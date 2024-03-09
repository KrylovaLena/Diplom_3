import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestMainPage:
    @allure.title('Проверка появления всплывающего окна с деталями')
    @allure.description('Кликаем на ингредиент и проверяем, что появилось всплывающее окно с деталями')
    def test_popup_of_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        actually_text = main_page.check_show_window_with_details()
        assert actually_text == "Детали ингредиента"

    @allure.title('Проверка закрывания окна кликом по крестику')
    @allure.description('Кликаем по крестику и проверяем, что всплывающее окно закрылось')
    def test_close_ingredient_details_window(self, driver):
        page = MainPage(driver)
        page.click_on_ingredient()
        page.click_cross_button()
        page.invisibility_ingredient_details()
        assert page.check_displayed_ingredient_details() == False

    @allure.title('Проверка увеличения счётчика ингридиента при добавлении в заказ')
    @allure.description('Получаем значение счетчика ингредиента до и после добавления в заказ, /'
                        'и проверяем, что значение счетчика увеличилось')
    def test_ingredient_counter(self, driver):
        page = MainPage(driver)
        prev_counter_value = page.get_count_value()
        page.add_filling_to_order()
        actual_value = page.get_count_value()
        assert actual_value > prev_counter_value

    @allure.title('Проверка возможности оформления заказ залогиненным пользователем')
    @allure.description(
        'Нажимаем кнопку «Оформить заказ» и проверяем, '
        ' что заказ оформлен и появился идентификатор заказа'
    )
    def test_successful_order(self, authorization):
        driver = authorization
        main_page = MainPage(driver)
        main_page.add_filling_to_order()
        main_page.click_order_button()
        actually_text = main_page.check_show_window_with_order_id()
        assert actually_text == "идентификатор заказа"
        assert main_page.check_displayed_order_status_text() == True