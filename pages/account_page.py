"""Модуль c методами для страницы Аккаунта пользователя."""

import allure

from pages.base_page import BasePage
from helpers.locators import AccountPageLocators
from helpers.db_helper import del_user_from_bd


class AccountPage(BasePage):
    """Класс с методами для страницы Аккаунта пользователя."""

    @allure.step('Открыть виш-лист')
    def open_wishlist(self):
        """Открытие вишлиста."""

        self.click_on_element(AccountPageLocators.WISH_LIST_LINK)

    @allure.step('Проверить, что товар в виш-листе')
    def check_item_in_wish_list(self, name):
        """Проверка видимости товара в вишлисте.

        :param name: название товара
        """

        elements = self._element(AccountPageLocators.ITEM_NAMES)
        for i in range(elements.count()):
            self.is_having_text(AccountPageLocators.ITEM_NAMES, name, i)

    @allure.step('Логаут из правого блока')
    def logout_from_right_block(self,):
        """Логаут из правого блока."""

        self.click_on_element(AccountPageLocators.LOGOUT_RIGHT_BLOCK)

    @allure.step('Проверка текста после логаута')
    def check_text_after_logout(self):
        """Проверка текста после логаута."""

        self.is_element_visible(AccountPageLocators.TEXT_AFTER_LOGOUT)
        self.is_having_text(
            AccountPageLocators.TEXT_AFTER_LOGOUT,
            'You have been logged off your account. It is now safe to leave the computer.')

    @allure.step('Проверка пунктов в правом блоке после логаута')
    def check_right_block_after_logout(self):
        """Проверка пунктов в правом блоке после логаута."""
        self.is_element_visible(AccountPageLocators.REGISTER_RIGHT_BLOCK)
        self.is_element_visible(AccountPageLocators.LOGIN_RIGHT_BLOCK)

    @allure.step('Заход в аккаунт после логаута')
    def click_my_account_after_logout(self, db_connection, email, fistname, del_user=True):
        """Заход в аккаунт после логаута."""
        self.click_on_element(AccountPageLocators.MY_ACCOUNT_RIGHT_BLOCK)
        if del_user:
            del_user_from_bd(db_connection, email, fistname)
