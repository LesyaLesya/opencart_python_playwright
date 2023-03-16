"""Модуль c методами для Подвала сайта."""


import allure

from helpers.locators import FooterPageLocators
from pages.base_page import BasePage


class FooterPage(BasePage):
    """Класс с методами для подвала сайта."""

    @allure.step('Проверить ссылки в подвале')
    def check_footer_links(self, lst):
        """Проверка ссылок в подвале.

        :param lst: список названий ссылок
        """

        elements = self._element(FooterPageLocators.LINKS)
        links_text = [self.get_text_of_element(FooterPageLocators.LINKS, index=i) for i in range(elements.count())]
        with allure.step(f'Проверить, что тексты ссылок {links_text} совпадают с {lst}'):
            assert links_text == lst, f'Список ссылок - {links_text}, ОР - {lst}'
