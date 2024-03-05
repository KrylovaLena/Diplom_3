from selenium.webdriver.common.by import By


class OrdersPageLocators:
    ORDERS_LIST_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]') # Заголовок "Лента заказов"
    ORDER_LINK = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'  # ссылка на заказ в Ленте заказов
    ORDER_STRUCTURE = By.XPATH, '//p[text()="Cостав"]'  # Состав
    ALL_TIME_COUNTER = (By.XPATH, '//p[text()="Выполнено за все время:"]/../p[contains(@class, "digits")]') # заказы за всё время
    TODAY_COUNTER = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/../p[contains(@class, "digits")]')
    INGREDIENTS = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
    NUMBER_IN_PROGRESS = (By.CSS_SELECTOR, 'ul.OrderFeed_orderListReady__1YFem li')  # Номер в разделе "В работе"
    ORDER_NUMBERS = (By.XPATH, '//p[@class="text text_type_digits-default"]')  # Номера всех заказов в ленте
    LAST_ORDER = (By.XPATH, '//li[1]//p[@class="text text_type_digits-default"]')  # Номер последнего заказа в ленте
    ENABLED_ORDER_HISTORY_BUTTON = (By.XPATH, '//ul/li[2]/a[contains(@class, "Account_link_active")]')  # Включенная кнопка "История заказов"
    EXIT_BUTTON = (By.XPATH, '//button[(text()="Выход")]')  # Кнопка "Выход"
