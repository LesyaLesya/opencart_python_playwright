"""Модуль c общими методами для всех страниц."""

import allure
from playwright.sync_api import expect

from pages.common.alert import Alert
from pages.common.footer import Footer
from pages.common.header import Header


class BasePage:
    """Класс, описывающий базовую страницу."""

    def __init__(self, browser, url, db_connection=None):
        """Конструктор класса.

        :param browser: фикстура для запуска драйвера и открытия страница
        :param url: фикстура с урлом тестируемого ресурса
        :param db_connection: фикстура коннекта к БД
        """
        self.browser = browser
        self.url = url
        self.db_connection = db_connection
        self.alert = Alert(self.browser)
        self.footer = Footer(self.browser)
        self.header = Header(self.browser)

    def open_url(self, path='/'):
        """Открытие url.

        :param path: путь
        """
        with allure.step(f'Перейти по ссылке {self.url}{path}'):
            return self.browser.goto(f'{self.url}{path}')

    @allure.step('Найти элемент {el_path} с индексом {index}')
    def _element(self, el_path, index=None):
        """Возвращает результат поиска элемента.

        :param el_path: путь до элемента
        :param index: порядковый индекс элемента
        """
        if index is not None:
            return self.browser.locator(el_path).nth(index)
        return self.browser.locator(el_path)

    @allure.step('Кликнуть по элементу {el_path} с индексом {index}')
    def click_on_element(self, el_path, index=None):
        """Возвращает клик по найденному элементу.

        :param el_path: путь до элемента
        :param index: порядковый индекс элемента
        """
        element = self._element(el_path, index)
        return element.click()

    @allure.step('Получить текст элемента {el_path} с индексом {index}')
    def get_text_of_element(self, el_path, index=None):
        """Возвращает текст найденного элемента.

        :param el_path: путь до элемента
        :param index: порядковый индекс элемента
        """
        element = self._element(el_path, index)
        return element.text_content()

    @allure.step('Проверить корректность заголовка {title}')
    def is_title_correct(self, title):
        """Проверка тайтла страницы.

        :param title: заголовок страницы
        """
        return expect(self.browser).to_have_title(title)

    @allure.step('Проверить что элемент {el_path} с индексом {index} виден на странице')
    def is_element_visible(self, el_path, index=None):
        """Проверка видимости элемента.

        :param el_path: путь до элемента
        :param index: порядковый индекс элемента
        """
        element = self._element(el_path, index)
        return expect(element).to_be_visible()

    @allure.step('Получить title страницы')
    def get_title(self):
        """Возвращает title страницы."""
        return self.browser.title()

    @allure.step('Найти выпадающий список по пути {el_path} и выбрать значение')
    def select_products(self, el_path, **kwargs):
        """Возвращает выбор элемента в выпадающем списке.

        :param el_path: путь до элемента
        """
        return self._element(el_path).select_option(**kwargs)

    @allure.step('Получить атрибут {attr} у элемента {el_path} с индексом {index}')
    def getting_attr(self, attr, el_path, index=None):
        """Возвращает атрибут найденного элемента.

        :param el_path: путь до элемента
        :param attr: атрибут элемента
        :param index: порядковый индекс элемента
        """
        element = self._element(el_path, index)
        return element.get_attribute(attr)

    @allure.step('Проверить, что элемент {el_path} с индексом {index} имеет атрибут {attr} со значением {value}')
    def is_having_attr(self, el_path, attr, value, index=None):
        """Возвращает проверку наличия атрибута у элемента.

        :param el_path: путь до элемента
        :param attr: атрибут элемента
        :param value: значение атрибута
        :param index: порядковый индекс элемента
        """
        element = self._element(el_path, index)
        return expect(element).to_have_attribute(attr, value)

    @allure.step('Проверить, что элемент {el_path} с индексом {index} имеет текст {value}')
    def is_having_text(self, el_path, value, index=None):
        """Возвращает проверку наличия текста у элемента.

        :param el_path: путь до элемента
        :param value: текст
        :param index: порядковый индекс элемента
        """
        element = self._element(el_path, index)
        return expect(element).to_have_text(value)

    @allure.step('Проверить, что инпут {el_path} с индексом {index} имеет текст {value}')
    def is_having_value(self, el_path, value, index=None):
        """Возвращает проверку текста в инпуте.

        :param el_path: путь до элемента
        :param value: текст
        :param index: порядковый индекс элемента
        """
        element = self._element(el_path, index)
        return expect(element).to_have_value(value)

    @allure.step('Проверить, что элемент {el_path} с индексом {index} содержит текст {value}')
    def is_contain_text(self, el_path, value, index=None, case=True):
        """Возвращает проверку содержания текста у элемента.

        :param el_path: путь до элемента
        :param value: текст
        :param index: порядковый индекс элемента
        :param case: значение для ignore_case
        """
        element = self._element(el_path, index)
        return expect(element).to_contain_text(value, ignore_case=case)

    @allure.step('Ввести текст {value} в инпут {el_path} с индексом {index}')
    def input_text(self, el_path, value, index=None):
        """Возвращает ввод текста в найденный инпут.

        :param el_path: путь до элемента
        :param value: вводимое значение в инпут
        :param index: порядковый индекс элемента
        """
        element = self._element(el_path, index)
        element.clear()
        return element.fill(value)

    @allure.step('Навести курсор мыши на элемент {el_path} с индексом {index}')
    def mouse_move_to_element(self, el_path, index=None):
        """Наводит курсор мыши на элемент.

        :param el_path: путь до элемента
        :param index: порядковый индекс элемента
        """
        element = self._element(el_path, index)
        return element.hover()

    def get_current_url(self):
        """Получение текущего урла."""
        return self.browser.url

    @allure.step('Проверить, что элемент {el_path} с индексом {index} имеет css свойство {css_prop}={value}')
    def is_have_css_property(self, el_path, css_prop, value, index=None):
        """Возвращает проверку наличия css свойства элемента.

        :param el_path: путь до элемента
        :param value: значение css свойства
        :param index: порядковый индекс элемента
        :param css_prop: css свойство
        """
        element = self._element(el_path, index)
        return expect(element).to_have_css(css_prop, value)

    @allure.step('Получить id у товара {el_path} с индексом {index}')
    def get_item_id(self, el_path, index=None):
        """Возвращает id товара.

        :param el_path: путь до элемента
        :param index: порядковый индекс элемента
        """
        element = self._element(el_path, index)
        value = element.get_attribute('onclick')
        return int(''.join([i for i in value if i.isdigit()]))
