"""Модуль c методами для Шапки сайта."""


import allure

from helpers.locators import HeaderPageLocators
from helpers.styles import Colors, Cursor, Gradients, SIZES
from pages.base_page import BasePage


class HeaderPage(BasePage):
    """Класс с методами для Шапки сайта."""

    @allure.step('Проверить видимость элементов на странице')
    def check_elements_visibility(self):
        """Проверка видимости элементов."""
        lst = [HeaderPageLocators.LOGO,
               HeaderPageLocators.MENU,
               HeaderPageLocators.CART_BUTTON,
               HeaderPageLocators.TOP_LINKS,
               HeaderPageLocators.SEARCH_FIELD]
        for i in lst:
            self.is_element_visible(i)

    @allure.step('Осуществить поиск по значению {value}')
    def search(self, value):
        """Ввод текста в поле поиска.

        :param value: искомое значение
        """
        self.input_text(HeaderPageLocators.SEARCH_INPUT, value)
        self.click_on_element(HeaderPageLocators.SEARCH_BUTTON)

    @allure.step('Перейти на страницу логина')
    def go_to_login_page(self):
        """Проверка перехода на страницу Логина."""
        self.click_on_element(HeaderPageLocators.MY_ACCOUNT_LINK)
        self.click_on_element(HeaderPageLocators.LOGIN_LINK)

    @allure.step('Проверить стили кнопки корзины')
    def check_cart_button_css(self):
        """Проверка стилей кнопки корзины без наведения."""
        locator = HeaderPageLocators.CART_BUTTON
        self.is_have_css_property(locator, 'font-size', SIZES.SIZE_12)
        self.is_have_css_property(locator, 'line-height', SIZES.SIZE_18)
        self.is_have_css_property(locator, 'color', Colors.WHITE)
        self.is_have_css_property(locator, 'background-color', Colors.DARK_GRAY)
        self.is_have_css_property(locator, 'background-image', Gradients.LIGHT_BLACK)
        self.is_have_css_property(locator, 'border-top-color', Colors.LIGHT_BLACK)
        self.is_have_css_property(locator, 'border-right-color', Colors.LIGHT_BLACK)
        self.is_have_css_property(locator, 'border-bottom-color', Colors.BLACK)
        self.is_have_css_property(locator, 'border-left-color', Colors.LIGHT_BLACK)
        self.is_have_css_property(locator, 'border-radius', SIZES.SIZE_4)
        self.is_have_css_property(locator, 'cursor', Cursor.POINTER)

    @allure.step('Проверить стили кнопки корзины при наведении')
    def check_cart_button_css_hover(self):
        """Проверка стилей кнопки корзины при наведении."""
        locator = HeaderPageLocators.CART_BUTTON
        self.mouse_move_to_element(locator)
        self.is_have_css_property(locator, 'font-size', SIZES.SIZE_12)
        self.is_have_css_property(locator, 'line-height', SIZES.SIZE_18)
        self.is_have_css_property(locator, 'color', Colors.WHITE)
        self.is_have_css_property(locator, 'background-color', Colors.LIGHT_BLACK)
        self.is_have_css_property(locator, 'background-image', Gradients.MEDIUM_BLACK)
        self.is_have_css_property(locator, 'border-top-color', Colors.LIGHT_BLACK)
        self.is_have_css_property(locator, 'border-right-color', Colors.LIGHT_BLACK)
        self.is_have_css_property(locator, 'border-bottom-color', Colors.BLACK)
        self.is_have_css_property(locator, 'border-left-color', Colors.LIGHT_BLACK)
        self.is_have_css_property(locator, 'border-radius', SIZES.SIZE_4)
        self.is_have_css_property(locator, 'cursor', Cursor.POINTER)

    @allure.step('Проверить стили кнопки корзины при клике')
    def check_cart_button_css_click(self):
        """Проверка стилей кнопки корзины при клике."""
        locator = HeaderPageLocators.CART_BUTTON
        self.click_on_element(locator)
        self.is_have_css_property(locator, 'font-size', SIZES.SIZE_12)
        self.is_have_css_property(locator, 'line-height', SIZES.SIZE_18)
        self.is_have_css_property(locator, 'color', Colors.MEDIUM_GRAY)
        self.is_have_css_property(locator, 'background-color', Colors.WHITE)
        self.is_have_css_property(locator, 'background-image', 'none')
        self.is_have_css_property(locator, 'border-radius', SIZES.SIZE_4)
        self.is_have_css_property(locator, 'cursor', Cursor.POINTER)
        self.check_cart_button_dropdown_open()

    @allure.step('Проверить, что открылась выпадашка корзины')
    def check_cart_button_dropdown_open(self):
        """Проверка отображения выпадашки у кнопки корзины."""
        self.is_having_attr(HeaderPageLocators.CART_BUTTON, 'aria-expanded', 'true')

    @allure.step('Кликнуть на выпадающий список валют')
    def click_on_currency_drop_down(self):
        """Клик по списку валют и проверка, что список раскрыт."""
        self.click_on_element(HeaderPageLocators.CURRENCY_DROP_DOWN_BUTTON)
        self.is_have_css_property(HeaderPageLocators.CURRENCY_DROP_DONW, 'display', 'block')

    @allure.step('Проверить значения валют в выпадающем списке')
    def check_currency_values(self, lst):
        """Проверка значений валют.

        :param lst: список названий валют
        """
        elements = self._element(HeaderPageLocators.CURRENCY_VALUES_BUTTONS)
        names = [self.get_text_of_element(HeaderPageLocators.CURRENCY_VALUES_BUTTONS, index=i) for i in range(elements.count())]
        with allure.step(f'Проверить, что полученный список - {names} - совпадает с - {lst}'):
            for i in names:
                assert i in lst, f'ФР - {names}, ОР - {lst}'

    @allure.step('Выбрать значение валюты {value}')
    def choose_currency(self, value):
        """Выбор значения валюты.

        :param value: значение валюты
        """
        self.click_on_currency_drop_down()
        elements = self._element(HeaderPageLocators.CURRENCY_VALUES_BUTTONS)
        for i in range(elements.count()):
            element = self.get_text_of_element(HeaderPageLocators.CURRENCY_VALUES_BUTTONS, index=i)
            if element == value:
                with allure.step(f'Кликнуть по значению валюты {value}'):
                    self.click_on_element(HeaderPageLocators.CURRENCY_VALUES_BUTTONS, index=i)

    @allure.step('Навести на раздел главного меню и проверить, что есть выпадашка')
    def check_dropdown_menu(self, menu_locator, dropdown_locator):
        """Наведение на разделы главног меню."""
        self.mouse_move_to_element(menu_locator)
        self.is_element_visible(dropdown_locator)
