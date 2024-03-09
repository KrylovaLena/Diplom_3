import pytest
import requests
from selenium import webdriver
import random
import string
from data import Site
from locators.personal_account_locators import PersonalAccountLocators
from locators.header_page_locators import HeaderPageLocators
from pages.main_page import MainPage
from pages.header_page import HeaderPage
from pages.orders_page import OrdersPage
from pages.personal_account_page import PersonalAccountPage
from helpers import Helpers



@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    """Функция driver является фикстурой для инициализации веб-драйвера в зависимости от параметра, переданного в параметре pytest.fixture.
    В данном случае доступны два варианта: 'firefox' и 'chrome'.
    Веб-драйвер служит для взаимодействия с браузером."""

    if request.param == 'firefox':
        # Если параметр равен 'firefox', инициализируется экземпляр веб-драйвера для Firefox.
        driver = webdriver.Firefox()
        # Устанавливаем размер окна браузера в 1920x1080 пикселей.
        driver.set_window_size(1920, 1080)
        driver.get('https://stellarburgers.nomoreparties.site/')
    elif request.param == 'chrome':
        # Если параметр равен 'chrome', инициализируется экземпляр веб-драйвера для Chrome.
        driver = webdriver.Chrome()
        # Устанавливаем размер окна браузера в 1920x1080 пикселей.
        driver.set_window_size(1920, 1080)
        driver.get('https://stellarburgers.nomoreparties.site/')

    # Возвращаем экземпляр веб-драйвера для использования в тестах.
    yield driver
    driver.quit()

@pytest.fixture
def create_and_delete_user():
    """Фикстура для создания и удаления пользователя.
    Генерирует случайное имя, электронную почту и пароль.
    Отправляет POST-запрос на регистрацию пользователя.
    Возвращает данные для входа и токен доступа.
    После использования удаляет пользователя методом DELETE."""

    # Вспомогательная функция для генерации случайной строки
    def random_generator(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # Генерация случайного имени пользователя
    name = random_generator(10)
    # Генерация случайного адреса электронной почты
    email_domain = random.choice(["gmail.com", "yandex.ru", "mail.com"])
    random_number = random.randint(100, 999)
    email = f"Elena_Krylova_4_{random_number}@{email_domain}"
    # Генерация случайного пароля
    password = random_generator(10)

    # Создание словаря с данными пользователя
    payload = {
        "name": name,
        "email": email,
        "password": password
    }

    # Создание копии словаря для данных входа
    login_data = payload.copy()
    # Удаление имени из словаря данных входа
    login_data.pop("name")

    # Отправка POST-запроса для регистрации пользователя
    response = requests.post(Site.register_user, data=payload)
    # Получение токена доступа из ответа
    access_token = response.json()["accessToken"]
    # Возвращение данных входа и токена доступа в блоке yield
    yield login_data, access_token
    # Отправка DELETE-запроса для удаления пользователя с использованием токена доступа
    requests.delete(Site.delete_user, headers={'Authorization': access_token})

@pytest.fixture
def authorization(driver, create_and_delete_user):
    """Фикстура authorization представляет собой механизм для автоматического выполнения действий, связанных с входом в аккаунт пользователей. Она принимает два параметра: driver и create_and_delete_user.
    """

    payload, access_token = create_and_delete_user
    main_page = MainPage(driver)
    main_page.click_personal_account_button()
    header_page = HeaderPage(driver)
    header_page.login(payload["email"], payload["password"])
    return driver

@pytest.fixture
def orders_numbers(create_and_delete_user):
    payload, token = create_and_delete_user
    Helpers().create_order(token)
    user_orders = Helpers().get_user_orders(token)
    orders_numbers = []
    for order in user_orders:
        orders_numbers.append(order["number"])
    return orders_numbers