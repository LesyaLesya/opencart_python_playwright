"""Модуль c методами для страницы Сравнение товара."""

import allure

from helpers.locators import ComparePageLocators
from pages.base_page import BasePage


class ComparisonPage(BasePage):
    """Класс с методами для страницы сравнения товаров."""

    EMPTY_COMPARE = 'You have not chosen any products to compare.'

    @allure.step('Проверить, что товар в сравнении')
    def check_item_in_comparison(self, name, idx):
        """Проверка видимости товара в сравнении.

        :param name: название товара
        :param idx: порядковый индекс
        """
        self.is_having_text(ComparePageLocators.ITEM_NAMES, name, idx)

    @allure.step('Удалить товары из сравнения')
    def del_from_compare(self, all=True, idx=0):
        """Удаление товаров из сравнения."""
        if all:
            elements = self._element(ComparePageLocators.REMOVE_BUTTON)
            all_buttons = [i for i in range(elements.count())]
            while len(all_buttons) != 0:
                self.click_on_element(ComparePageLocators.REMOVE_BUTTON, idx)
                all_buttons.pop(0)
        else:
            self.click_on_element(*ComparePageLocators.REMOVE_BUTTON, idx)

    @allure.step('Проверить текст на пустой странице Сравнения')
    def check_empty_compare(self):
        """Проверка текста при отсутсвии товаров в сравнении."""
        self.is_having_text(
            ComparePageLocators.TEXT_FOR_EMTY_COMPARE, self.EMPTY_COMPARE)

    @allure.step('Добавить товар в корзину из сравнения')
    def add_to_cart_from_compare(self, idx):
        """Добавление товара в корзину из сравнения."""
        self.click_on_element(ComparePageLocators.ADD_TO_CART_BUTTON, idx)
