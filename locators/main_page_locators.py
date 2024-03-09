from selenium.webdriver.common.by import By



class MainPageLocators:

    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]')  # Кнопка "Лента Заказов"
    PERSONAL_ACCOUNT_BUTTON = (By.LINK_TEXT, 'Личный Кабинет')  # Кнопка "Личный кабинет"
    CREATE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'  # кнопка "Оформить заказ"
    ORDER_ID = (By.XPATH, '//p[text()="идентификатор заказа"]')  # Идентификатор заказа


    BUN_INGREDIENT = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')  # Ингредиент "Флюоресцентная булка R2-D3"
    INGREDIENT_COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')  # Счетчик
    INGREDIENT_DETAILS_POPUP = (By.XPATH, '//h2[text()="Детали ингредиента"]')  # Детали ингредиента
    ORDER_BASKET = (By.CLASS_NAME, 'BurgerConstructor_basket__list__l9dp_')  # Корзина для конструктора
    ORDER_STATUS_TEXT = By.XPATH, '//p[text()="Ваш заказ начали готовить"]'  # Ваш заказ начали готовить в попапе
    CROSS_BUTTON = By.XPATH, '//button[contains(@class,"close")]'  # закрытие всплывающего окна

