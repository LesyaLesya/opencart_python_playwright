"""Модуль с фикстурами."""

import allure
import pytest
import mysql.connector

from playwright.sync_api import sync_playwright
from types import SimpleNamespace

from helpers import allure_helper


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
        context = driver.new_context(**dev,)
    else:
        context = driver.new_context()
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
def make_screenshots(request, browser):
    """Создание скриншота при падении теста и его прикрепление к отчету."""
    yield
    if not request.node.result_call.passed:
        allure.attach(body=browser.screenshot(full_page=True),
                      name=f'{request.node.nodeid}.png',
                      attachment_type=allure.attachment_type.PNG)
