"""Модуль c методами для страницы Каталога."""

import allure

from helpers.locators import CataloguePageLocators
from helpers.styles import Cursor, Colors, FontWeight
from pages.base_page import BasePage


class CataloguePage(BasePage):
    """Класс с методами для страницы Каталога."""

    @allure.step('Проверить видимость элементов на странице')
    def check_elements_visibility(self):
        """Проверка видимости элементов."""

        lst = [CataloguePageLocators.BREADCRUMB,
               CataloguePageLocators.CATALOGUE_HEADER,
               CataloguePageLocators.CATALOGUE_IMAGE,
               CataloguePageLocators.LEFT_MENU,
               CataloguePageLocators.BANNER_UNDER_LEFT_MENU]
        for i in lst:
            self.is_element_visible(i)

    @allure.step('Добавить товар с индексом {idx} в сравнение')
    def add_to_compare(self, idx):
        """Добавление товара в сравнение. Возвращает название
        добавленного товара.

        :param idx: порядковый индекс
        """

        name = self.get_text_of_element(CataloguePageLocators.ITEM_NAME, idx)
        self.click_on_element(CataloguePageLocators.COMPARE_BUTTON, idx)
        return name

    @allure.step('Кликнуть на кнопку Сравнения в алерте')
    def go_to_compare_page(self):
        """Клик по ссылке Сравнения."""

        self.click_on_element(CataloguePageLocators.COMPARE_LINK)

    @allure.step('Проверить, что товар добавился к сравнению - значение в ссылке увеличилось на {value}')
    def check_adding_in_compare_link(self, value):
        """Проверка изменения количества товаров в сравнении
        после добавления в сравнение.

        :param value: количество товаров в сравнении
        """
        self.is_having_text(CataloguePageLocators.COMPARE_LINK, f'Product Compare ({value})')

    @allure.step('Сортировать товары по {txt}')
    def select_by_text(self, txt):
        """Сортировка товаров по значению из списка (тексту).

        :param txt: значения в выпадающем списке
        """

        self.select_products(CataloguePageLocators.SELECT_SORT, label=txt)

    @allure.step('Проверить, что товары отсортированы от A до Z')
    def check_sort_by_name_a_z(self):
        """Получение всех названий товаров после сортировки и проверка
        заданной сортировки."""

        elements = self._element(CataloguePageLocators.ITEM_NAME)
        names = [self.get_text_of_element(CataloguePageLocators.ITEM_NAME, index=i) for i in range(elements.count())]
        with allure.step(f'Проверить порядок в списке названий {names}'):
            assert all(names[i] < names[i+1] for i in range(len(names)-1)), f'Порядок названий - {names}'

    @allure.step('Проверить, что товары отсортированы от Z до A')
    def check_sort_by_name_z_a(self):
        """Получение всех названий товаров после сортировки и проверка
        заданной сортировки."""

        elements = self._element(CataloguePageLocators.ITEM_NAME)
        names = [self.get_text_of_element(CataloguePageLocators.ITEM_NAME, index=i) for i in range(elements.count())]
        with allure.step(f'Проверить порядок в списке названий {names}'):
            assert all(names[i] > names[i + 1] for i in range(len(names) - 1)), f'Порядок названий - {names}'

    @allure.step('Проверить, что товары отсортированы по возрастанию цены')
    def check_sort_by_price_low_high(self):
        """Получение всех цен товаров после сортировки и проверка
        заданной сортировки."""

        elements = self._element(CataloguePageLocators.ITEM_PRICE)
        prices_with_tax = [(self.get_text_of_element(CataloguePageLocators.ITEM_PRICE, index=i)).strip() for i in range(elements.count())]
        prices_without_tax = [i.split('\n')[0] for i in prices_with_tax]
        prices_in_float = [float(i.replace(',', '').replace('$', '')) for i in prices_without_tax]
        with allure.step(f'Проверить порядок в списке цен {prices_in_float}'):
            assert all(prices_in_float[i] <= prices_in_float[i+1] for i in range(len(prices_in_float)-1)), \
                f'Порядок цен - {prices_in_float}'

    @allure.step('Перейти в карточку продукта со страницы каталога')
    def go_to_product_from_catalogue(self, index):
        """Клик по товару из каталога.
        Возвращает название товара.

        :param index: порядковый индекс элемента
        """

        name = self.get_text_of_element(CataloguePageLocators.ITEM_NAME, index)
        self.click_on_element(CataloguePageLocators.ITEM_NAME, index)
        return name

    @allure.step('Добавить продукт в виш лист')
    def add_to_wishlist(self, index):
        """Добавление товара в вишлист. Возвращает название
        добавленного товара.

        :param index: порядковый индекс элемента
        """

        name = self.get_text_of_element(CataloguePageLocators.ITEM_NAME, index)
        self.click_on_element(CataloguePageLocators.WISH_LIST_BUTTON, index)
        return name

    @allure.step('Кликнуть на кнопку Логина в алерте')
    def click_login_from_alert(self):
        """Клик по кнопке Логина в алерте."""

        self.click_on_element(CataloguePageLocators.LOGIN_LINK_IN_ALERT)

    @allure.step('Кликнуть на кнопку вида Список')
    def click_list_view(self):
        """Клик по кнопке с видом списка и проверка изменения вида."""

        elements = self._element(CataloguePageLocators.ITEM_CART)
        self.click_on_element(CataloguePageLocators.LIST_VIEW_BUTTON)
        for i in range(elements.count()):
            attr = self.getting_attr('class', CataloguePageLocators.ITEM_CART, i)
            with allure.step(f'Проверить, что товар с индексом {i} имеет класс со значением product-list'):
                assert 'product-list' in attr, f'Значение атрибута -  {attr}'

    @allure.step('Кликнуть на кнопку вида Сетка')
    def click_list_grid(self):
        """Клик по кнопке с видом сетки и проверка изменения вида."""

        elements = self._element(CataloguePageLocators.ITEM_CART)
        self.click_on_element(CataloguePageLocators.GRID_VIEW_BUTTON)
        for i in range(elements.count()):
            attr = self.getting_attr('class', CataloguePageLocators.ITEM_CART, i)
            with allure.step(f'Проверить, что товар с индексом {i} имеет класс со значением product-grid'):
                assert 'product-grid' in attr, f'Значение атрибута -  {attr}'

    @allure.step('Сравнить символ в ценах товаров с символом выбранной валюты')
    def check_currency_in_price(self, idx, symbol):
        """Проверка отображения значка валюты в ценах."""

        elements = self._element(CataloguePageLocators.ITEM_PRICE)
        prices_with_tax = [(self.get_text_of_element(CataloguePageLocators.ITEM_PRICE, index=i)).strip() for i in
                           range(elements.count())]
        prices_without_tax = [i.split('\n')[0] for i in prices_with_tax]
        with allure.step(f'Проверить, что во всех ценах {prices_without_tax} символ {symbol}'):
            assert all([i[idx] == symbol for i in prices_without_tax]), f'{prices_without_tax} - список цен'

    @allure.step('Проверить стиль кнопки добавления в корзину без наведения')
    def check_add_to_cart_css(self):
        """Проверка стилей кнопки добавления в корзину без наведения."""

        locator = CataloguePageLocators.ADD_TO_CART_BUTTON
        elements = self._element(locator)
        for i in range(elements.count()):
            self.is_have_css_property(locator, 'background-color', Colors.GRAY_238, i)
            self.is_have_css_property(locator, 'color', Colors.GRAY_136, i)
            self.is_have_css_property(locator, 'font-weight', FontWeight.WEIGHT_700, i)

    @allure.step('Проверить стиль кнопки добавления в корзину с наведением')
    def check_add_to_cart_css_hover(self):
        """Проверка стилей кнопки добавления в корзину с наведением."""

        locator = CataloguePageLocators.ADD_TO_CART_BUTTON
        elements = self._element(locator)
        for i in range(elements.count()):
            self.mouse_move_to_element(locator, i)
            self.is_have_css_property(locator, 'color', Colors.GRAY_68, i)
            self.is_have_css_property(locator, 'background-color', Colors.GRAY_221, i)
            self.is_have_css_property(locator, 'cursor', Cursor.POINTER, i)

    @allure.step('Проверить заголовок страницы каталога')
    def check_catalogue_page_header(self, name):
        """Проверка заголовка страницы каталога."""

        self.is_having_text(CataloguePageLocators.CATALOGUE_HEADER, name)
