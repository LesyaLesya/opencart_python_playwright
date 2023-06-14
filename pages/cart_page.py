"""Модуль c методами для страницы Корзины."""
import time

import allure

from helpers.locators import CartPageLocators
from pages.base_page import BasePage


class CartPage(BasePage):
    """Класс с методами для страницы корзины."""

    EMPTY_CART = 'Your shopping cart is empty!'
    TITLE = 'Shopping Cart'

    @allure.step('Проверить, что страница корзины открыта')
    def check_cart_page(self):
        """Проверка, что находимся на странице корзины."""
        self.is_title_correct(self.TITLE)

    @allure.step('Проверить, что товар в корзине')
    def check_item_in_cart(self, name, n):
        """Проверка видимости товара в корзине.

        :param name: название товара
        :param n: количество товаров в корзине
        """
        elements = self._element(CartPageLocators.ITEM_NAMES)
        with allure.step(f'Проверить, что в корзине {n} товаров'):
            assert elements.count() == n, f'Количество товаров - {elements.count()}'
        product_names = [self.get_text_of_element(CartPageLocators.ITEM_NAMES, index=i) for i in
                         range(elements.count())]
        with allure.step(f'Проверить что в {product_names} есть товары {name}'):
            if type(name) == list:
                for i in name:
                    assert i in product_names, f'Название {i}, названия продуктов в вишлисте {product_names}'
            else:
                self.is_having_text(CartPageLocators.ITEM_NAMES, name, 0), \
                f'Название {name}, названия продуктов в вишлисте {product_names}'

    @allure.step('Удалить товар из корзины')
    def remove_product_from_cart(self, idx=0, all=False):
        """Проверка удаления товаров из корзины.

        :param idx: порядковый индекс товара
        :param all: все ли товары удалять из корзины
        """
        if all:
            elements = self._element(CartPageLocators.REMOVE_BUTTONS)
            all_buttons = [i for i in range(elements.count())]
            while len(all_buttons) != 0:
                self.click_on_element(CartPageLocators.REMOVE_BUTTONS, idx)
                all_buttons.pop(idx)
        else:
            self.click_on_element(CartPageLocators.REMOVE_BUTTONS, idx)
        time.sleep(1)

    @allure.step('Проверить, что корзина пуста')
    def check_empty_cart(self):
        """Проверка удаления товаров из корзины."""
        self.is_having_text(CartPageLocators.TEXT_EMPTY_CART, self.EMPTY_CART)

    @allure.step('Обновить цену, указав количество {value}')
    def update_price(self, value):
        """Ввод значения в инпут и клик по кнопке обновления цены.

        :param value: количество товара
        """
        self.input_text(CartPageLocators.QUANTITY_INPUT, str(value))
        self.click_on_element(CartPageLocators.QUANTITY_REFRESH_BUTTON)

    @allure.step('Проверить, что цена обновилась')
    def check_updating_price(self, value):
        """Проверка обновленной цены.

        :param value: количество товара
        """
        with allure.step('Получить цену за единицу товара'):
            unit_price = self.get_text_of_element(CartPageLocators.UNIT_PRICE)
        unit_price_in_float = float(unit_price.replace('$', ''))
        with allure.step('Получить общую цену за товар'):
            total_price = self.get_text_of_element(CartPageLocators.TOTAL_PRICE)
        total_price_in_float = float(total_price.replace('$', ''))
        with allure.step(f'Проверить, что общая цена {total_price_in_float} == {unit_price_in_float} * {value}'):
            assert total_price_in_float == unit_price_in_float * value, \
                f'Общая цена - {total_price_in_float}, цена за единицу {unit_price_in_float}'

    @allure.step('Нажать на кнопку возврата к покупкам')
    def click_continue_shopping(self):
        """Проверка нажатия на кнопку возврата к покупкам."""
        self.click_on_element(CartPageLocators.CONTINUE_SHOPPING_BUTTON)
