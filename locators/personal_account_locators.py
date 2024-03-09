from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    LOGIN_HEADER = (By.XPATH, '.// h2[text() = "Вход"]')  # Заголовок "Вход"
    RESET_PASSWORD_LINK = By.XPATH, '//*[@href="/forgot-password"]'  # Восстановить пароль
    PROFILE_BUTTON = (By.LINK_TEXT, 'Профиль')  # Кнопка "Профиль"
    ORDER_HISTORY_BUTTON = (By.LINK_TEXT, 'История заказов')  # Кнопка "История заказов"