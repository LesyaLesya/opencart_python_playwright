"""Модуль c методами для страницы Корзины."""

import allure

from helpers.locators import CartPageLocators
from pages.base_page import BasePage


class CartPage(BasePage):
    """Класс с методами для страницы корзины."""

    @allure.step('Проверить, что товар в корзине')
    def check_item_in_cart(self, name):
        """Проверка видимости товара в корзине.

        :param name: название товара
        """

        elements = self._element(CartPageLocators.ITEM_NAMES)
        for i in range(elements.count()):
            with allure.step(f'Проверить, что продукт с индексом {i} в корзине'):
                self.is_having_text(CartPageLocators.ITEM_NAMES, name, i)

    @allure.step('Удалить товар из корзины')
    def remove_product_from_cart(self):
        """Проверка удаления товаров из корзины."""

        self.click_on_element(CartPageLocators.REMOVE_BUTTONS)

    @allure.step('Проверить, что корзина пуста')
    def check_empty_cart(self):
        """Проверка удаления товаров из корзины."""

        self.is_having_text(CartPageLocators.TEXT_EMPTY_CART, 'Your shopping cart is empty!')

    @allure.step('Обновить цену, указав количество {value}')
    def update_price(self, value):
        """Ввод значения в инпут и клик по кнопке обновления цены.

        :param value: количество товара
        """

        self.input_text(CartPageLocators.QUANTITY_INPUT, str(value))
        self.click_on_element(CartPageLocators.QUANTITY_REFRESH_BUTTON)

    @allure.step('Проверить, что цена обновилась')
    def check_updating_price(self, value):
        """Проверка обновленной цены."""

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