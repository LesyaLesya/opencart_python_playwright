"""Модуль c методами для страницы Аккаунта пользователя."""

import allure

from helpers.db_helper import del_user_from_bd
from helpers.locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    """Класс с методами для страницы Аккаунта пользователя."""

    @allure.step('Открыть виш-лист')
    def open_wishlist(self):
        """Открытие вишлиста."""
        self.click_on_element(AccountPageLocators.WISH_LIST_LINK)

    @allure.step('Проверить, что товар в виш-листе')
    def check_item_in_wish_list(self, name, idx):
        """Проверка видимости товара в вишлисте.

        :param name: название товара
        :param idx: порядковый индекс
        """
        self.is_having_text(AccountPageLocators.ITEM_NAMES, name, idx)

    @allure.step('Выполнить логаут из правого блока')
    def logout_from_right_block(self,):
        """Логаут из правого блока."""
        self.click_on_element(AccountPageLocators.LOGOUT_RIGHT_BLOCK)

    @allure.step('Проверить текст после логаута')
    def check_text_after_logout(self):
        """Проверка текста после логаута."""
        self.is_element_visible(AccountPageLocators.TEXT_AFTER_LOGOUT)
        self.is_having_text(
            AccountPageLocators.TEXT_AFTER_LOGOUT,
            'You have been logged off your account. It is now safe to leave the computer.')

    @allure.step('Проверить пункты в правом блоке после логаута')
    def check_right_block_after_logout(self):
        """Проверка пунктов в правом блоке после логаута."""
        self.is_element_visible(AccountPageLocators.REGISTER_RIGHT_BLOCK)
        self.is_element_visible(AccountPageLocators.LOGIN_RIGHT_BLOCK)

    @allure.step('Зайти в аккаунт после логаута')
    def click_my_account_after_logout(self, db_connection, email, fistname, del_user=True):
        """Заход в аккаунт после логаута."""
        self.click_on_element(AccountPageLocators.MY_ACCOUNT_RIGHT_BLOCK)
        if del_user:
            del_user_from_bd(db_connection, email, fistname)
