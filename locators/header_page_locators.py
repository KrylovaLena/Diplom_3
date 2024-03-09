from selenium.webdriver.common.by import By


class HeaderPageLocators:
    PERSONAL_ACCOUNT = By.XPATH, '//*[@href="/account"]'  # Личный кабинет
    CONSTRUCTOR = By.XPATH, '//p[text()="Конструктор"]/parent::a'  # Конструктор
    ORDERS_LIST = By.XPATH, '//p[text()="Лента Заказов"]/parent::a'  # Лента Заказов
    EMAIL = (By.NAME, 'name')  # Поле для email
    PASSWORD = (By.NAME, 'Пароль')  # Поле для пароля
    LOGIN_BUTTON = (By.XPATH, '//button[(text()="Войти")]')  # Кнопка "Войти"