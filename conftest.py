"""Модуль с фикстурами."""

import allure
import pytest
import mysql.connector

from faker import Faker
from playwright.sync_api import sync_playwright
from types import SimpleNamespace

from helpers import allure_helper
from helpers import db_queries


def pytest_addoption(parser):
    """Получение аргументов из командной строки."""
    parser.addoption(
        '--url', action='store', required=True, help='Укажите url приложения')
    parser.addoption(
        '--head', action='store_false', help='Запуск в headless режиме: если указан, то запуск в режиме headed')
    parser.addoption(
        '--browser_name', action='store', default='chromium', help='Укажите браузер - firefox, chromium, webkit')
    parser.addoption(
        '--devices', action='store', required=False, help='Укажите девайс - iPhone 12, iPhone 11, Pixel 2')


@pytest.fixture(scope='session')
def get_playwright():
    """Возвращает сущность playwright."""
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture
def url(request):
    """Возвращает url, переданный в командной строке."""
    get_url = request.config.getoption('--url')
    return f'http://{get_url}'


@pytest.fixture
def browser(get_playwright, request):
    """Запуск драйвера, создание контекста и страницы в зависимости от параметров."""
    head = request.config.getoption('--head')
    browser = request.config.getoption('--browser_name')
    device = request.config.getoption('--devices')
    if head:
        headless = True
    else:
        headless = False
    if device: dev = get_playwright.devices[device]
    if browser == 'chromium':
        driver = get_playwright.chromium.launch(headless=headless)
    elif browser == 'firefox':
        driver = get_playwright.firefox.launch(headless=headless)
    elif browser == 'webkit':
        driver = get_playwright.webkit.launch(headless=headless)
    else:
        assert False, 'Unsupported browser type'
    if device:
        context = driver.new_context(
            **dev, record_video_dir='videos/', record_video_size={'width': 1440, 'height': 900})
    else:
        context = driver.new_context(
            record_video_dir='videos/', record_video_size={'width': 1440, 'height': 900})
    context.set_default_timeout(10000)
    page = context.new_page()
    allure_helper.add_allure_env(browser, device)
    yield page
    page.close()
    context.close()
    driver.close()


@pytest.fixture(scope='session')
def db_connection(request):
    """Подключение к БД."""
    db_host = request.config.getoption('--url')
    config = SimpleNamespace(
        DB_NAME='bitnami_opencart',
        HOST=db_host,
        PORT='3306',
        USER='bn_opencart',
        PASSWORD=''
    )
    connection = mysql.connector.connect(
        user=config.USER,
        password=config.PASSWORD,
        host=config.HOST,
        port=config.PORT,
        database=config.DB_NAME
    )
    request.addfinalizer(connection.close)
    return connection


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """Хук для установки статуса теста."""
    outcome = yield
    result = outcome.get_result()
    setattr(item, f'result_{result.when}', result)


@pytest.fixture(autouse=True)
def make_attachments(request, browser):
    """Создание скриншота при падении теста и прикрепление к отчету скриншота и видео."""
    yield
    if not request.node.result_call.passed:
        allure.attach(body=browser.screenshot(full_page=True),
                      name=f'{request.node.nodeid}.png',
                      attachment_type=allure.attachment_type.PNG)

        video_path = browser.video.path()
        browser.context.close()
        allure.attach(
            open(video_path, 'rb').read(),
            name=f'{request.node.nodeid}.webm',
            attachment_type=allure.attachment_type.WEBM
        )


@pytest.fixture
def do_fake():
    fake = Faker(['en_US'])
    return fake


@pytest.fixture
def delete_user(db_connection):
    """Фикстура, удаляющая пользователя."""
    def __del_user_from_bd(user_id):
        return db_queries.delete_user(db_connection, user_id)
    return __del_user_from_bd


@pytest.fixture
def create_user(db_connection, do_fake):
    """Фикстура, создающая пользователя."""
    @allure.step(
        'Создать пользователя: firstname={firstname}, lastname={lastname}, email={email}, telephone={telephone}')
    def __create_user(email=None, firstname=None, lastname=None, telephone=None):
        if email is None:
            email = do_fake.ascii_free_email()
        else:
            email = email

        if firstname is None:
            firstname = do_fake.first_name()
        else:
            firstname = firstname

        if lastname is None:
            lastname = do_fake.last_name()
        else:
            lastname = lastname

        if telephone is None:
            telephone = do_fake.phone_number()
        else:
            telephone = telephone

        db_queries.create_test_user(db_connection, email, firstname, lastname, telephone)
        user_id = db_queries.get_user_id(db_connection, email, firstname, lastname, telephone)
        return email, firstname, lastname, telephone, user_id
    return __create_user


@pytest.fixture
def fixture_create_delete_user(create_user, delete_user):
    """Фикстура создания и удаления пользователя."""
    email, firstname, lastname, telephone, user_id = create_user()
    yield email, firstname, lastname, telephone, user_id
    delete_user(user_id)
