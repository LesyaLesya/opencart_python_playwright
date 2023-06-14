"""Модуль c методами для страницы Аккаунта пользователя."""

import allure

from helpers.locators import (
     AccountPageLocators, EditAccountPageLocators, LoginPageLocators,
     LogoutPageLocators, RegisterPageLocators, WishlistPageLocators)
from pages.base_page import BasePage


class AccountPage(BasePage):
    """Класс с методами для страницы Аккаунта пользователя."""

    TITLE = 'My Account'
    SUCCESS_CREATE_ACCOUNT = 'Your Account Has Been Created!'

    @allure.step('Открыть виш-лист')
    def open_wishlist(self):
        """Открытие вишлиста."""
        self.click_on_element(AccountPageLocators.WISH_LIST_LINK)

    @allure.step('Выполнить логаут из правого блока')
    def logout_from_right_block(self, ):
        """Логаут из правого блока."""
        self.click_on_element(AccountPageLocators.LOGOUT_RIGHT_BLOCK)

    @allure.step('Зайти в аккаунт')
    def click_my_account(self):
        """Заход в аккаунт."""
        self.click_on_element(AccountPageLocators.MY_ACCOUNT_RIGHT_BLOCK)

    @allure.step('Перейти на страницу редактирования аккаунта')
    def click_edit_account(self):
        """Заход на страницу редактирования аккаунта."""
        self.click_on_element(AccountPageLocators.EDIT_ACCOUNT_RIGHT_BLOCK)


class WishlistPage(AccountPage):
    """Класс с методами для страницы Вишлиста Аккаунта пользователя."""

    WISHLIST_CHANGE = 'Success: You have modified your wish list!'
    EMPTY_WISHLIST = 'Your wish list is empty.'
    TITLE = 'My Wish List'

    @allure.step('Проверить, что товары в виш-листе')
    def check_items_in_wish_list(self, names, n):
        """Проверка видимости товаров в вишлисте.

        :param names: названия товаров
        :param n: количество товаров в вишлисте
        """
        elements = self._element(WishlistPageLocators.ITEM_NAMES)
        product_names = [self.get_text_of_element(WishlistPageLocators.ITEM_NAMES, index=i) for i in range(elements.count())]
        with allure.step(f'Проверить, что в вишлисте {n} товаров'):
            assert elements.count() == n, f'Количество товаров - {elements.count()}'
        with allure.step(f'Проверить что в {product_names} есть товары {names}'):
            if type(names) == list:
                for i in names:
                    assert i in product_names, f'Название {i}, названия продуктов в вишлисте {product_names}'
            else:
                self.is_having_text(WishlistPageLocators.ITEM_NAMES, names, 0), \
                f'Название {names}, названия продуктов в вишлисте {product_names}'

    @allure.step('Проверить, что вишлист пустой')
    def check_empty_wish_list(self):
        """Проверка, что вишлист пустой."""
        self.is_having_text(
            WishlistPageLocators.EMPTY_WISHLIST_TEXT, self.EMPTY_WISHLIST)

    @allure.step('Удалить товары из вишлиста')
    def del_items_from_wish_list(self, all=False, idx=0):
        """Проверка удаления из вишлиста."""
        if all:
            elements = self._element(WishlistPageLocators.REMOVE_BUTTON)
            all_buttons = [i for i in range(elements.count())]
            while len(all_buttons) != 0:
                self.click_on_element(WishlistPageLocators.REMOVE_BUTTON, idx)
                self.alert.check_success_alert(txt=self.WISHLIST_CHANGE)
                all_buttons.pop(idx)
        else:
            self.click_on_element(WishlistPageLocators.REMOVE_BUTTON, idx)
            self.alert.check_success_alert(txt=self.WISHLIST_CHANGE)


class LogoutPage(AccountPage):
    """Класс с методами для страницы логаута из Аккаунта пользователя."""

    TITLE = 'Account Logout'
    LOGOUT = 'You have been logged off your account. It is now safe to leave the computer.'

    @allure.step('Проверить текст после логаута')
    def check_text_after_logout(self):
        """Проверка текста после логаута."""
        self.is_element_visible(LogoutPageLocators.TEXT_AFTER_LOGOUT)
        self.is_having_text(
            LogoutPageLocators.TEXT_AFTER_LOGOUT, self.LOGOUT)

    @allure.step('Проверить пункты в правом блоке после логаута')
    def check_right_block_after_logout(self):
        """Проверка пунктов в правом блоке после логаута."""
        self.is_element_visible(LogoutPageLocators.REGISTER_RIGHT_BLOCK)
        self.is_element_visible(LogoutPageLocators.LOGIN_RIGHT_BLOCK)


class LoginPage(AccountPage):
    """Класс с методами для страницы Логина."""

    TITLE = 'Account Login'

    @allure.step('Проверить видимость элементов на странице')
    def check_elements_visibility(self):
        """Проверка видимости элементов."""
        lst = [LoginPageLocators.NEW_CUSTOMER_FORM,
               LoginPageLocators.OLD_CUSTOMER_FORM,
               LoginPageLocators.RIGHT_LIST_MENU,
               LoginPageLocators.BUTTON_FOR_NEW_CUSTOMER,
               LoginPageLocators.BUTTON_FOR_OLD_CUSTOMER]
        for i in lst:
            self.is_element_visible(i)

    @allure.step('Залогиниться с email {email}, паролем {password}')
    def login_user(self, email, password="test"):
        """Процесс логина пользователя в аккаунт.

        :param email: email
        :param password: пароль
        """
        self.input_text(LoginPageLocators.EMAIL_INPUT, email)
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)


class RegisterPage(AccountPage):
    """Класс с методами для страницы Регистрации."""

    TITLE = 'Register Account'
    REGISTER_FIRST_NAME_ERROR = 'First Name must be between 1 and 32 characters!'
    REGISTER_LAST_NAME_ERROR = 'Last Name must be between 1 and 32 characters!'
    REGISTER_EMAIL_ERROR = 'E-Mail Address does not appear to be valid!'
    REGISTER_PHONE_ERROR = 'Telephone must be between 3 and 32 characters!'
    REGISTER_PASSW_ERROR = 'Password must be between 4 and 20 characters!'
    REGISTER_PASSW_CONFIRM_ERROR = 'Password confirmation does not match password!'
    REGISTER_PRIVACY_ERROR = 'Warning: You must agree to the Privacy Policy!'

    @allure.step('Проверить видимость элементов на странице')
    def check_elements_visibility(self):
        """Проверка видимости элементов."""
        lst = [RegisterPageLocators.HEADER,
               RegisterPageLocators.TEXT_FOR_LOGIN,
               RegisterPageLocators.FIRST_NAME_FIELD,
               RegisterPageLocators.LAST_NAME_FIELD,
               RegisterPageLocators.EMAIL_FIELD,
               RegisterPageLocators.TEL_FIELD,
               RegisterPageLocators.PASSW_FIELD,
               RegisterPageLocators.CONFIRM_FIELD,
               RegisterPageLocators.PRIVACY_POLICY,
               RegisterPageLocators.CONTINUE_BUTTON,
               RegisterPageLocators.RIGHT_MENU]
        for i in lst:
            self.is_element_visible(i)

    @allure.step(
        'Зарегистрировать пользователя с данными: email {email}, имя {firstname}, '
        'фамилия {lastname}, телефон {tel}, пароль {password}, повтор пароля {confirm}, '
        'согласие на рассылку {radio_idx}')
    def register_user(
            self, firstname, lastname, email, tel, password, confirm, radio_idx, checkbox=True):
        """Процесс регистрации пользователя.

        :param firstname: имя
        :param lastname: фамилия
        :param email: email
        :param password: пароль
        :param confirm: подтверждение пароля
        :param radio_idx: согласие на рассылку
        :param checkbox: принятие пользовательского соглашения
        """
        if firstname:
            self.input_text(RegisterPageLocators.FIRST_NAME_FIELD, firstname)
        if lastname:
            self.input_text(RegisterPageLocators.LAST_NAME_FIELD, lastname)
        if email:
            self.input_text(RegisterPageLocators.EMAIL_FIELD, email)
        if tel:
            self.input_text(RegisterPageLocators.TEL_FIELD, tel)
        if password:
            self.input_text(RegisterPageLocators.PASSW_FIELD, password)
        if confirm:
            self.input_text(RegisterPageLocators.CONFIRM_FIELD, confirm)
        if radio_idx == 0 or radio_idx == 1:
            self.click_on_element(RegisterPageLocators.SUBSCRIBE_RADIO, radio_idx)
        if checkbox:
            self.click_on_element(RegisterPageLocators.AGREE_CHECKBOX)
        self.click_on_element(RegisterPageLocators.CONTINUE_BUTTON)

    @allure.step('Проверить, что выведена ошибка  - имя обязательно')
    def check_fail_register_without_firstname(self):
        """Проверка отображения ошибки регистрации без firstname."""
        self.is_element_visible(RegisterPageLocators.FIRST_NAME_ERROR)
        self.is_having_text(
            RegisterPageLocators.FIRST_NAME_ERROR, self.REGISTER_FIRST_NAME_ERROR)

    @allure.step('Проверить, что выведена ошибка  - фамилия обязательна')
    def check_fail_register_without_lastname(self):
        """Проверка отображения ошибки регистрации без lastname."""
        self.is_element_visible(RegisterPageLocators.LAST_NAME_ERROR)
        self.is_having_text(
            RegisterPageLocators.LAST_NAME_ERROR, self.REGISTER_LAST_NAME_ERROR)

    @allure.step('Проверить, что выведена ошибка  - email обязателен')
    def check_fail_register_without_email(self):
        """Проверка отображения ошибки регистрации без email."""
        self.is_element_visible(RegisterPageLocators.EMAIL_ERROR)
        self.is_having_text(
            RegisterPageLocators.EMAIL_ERROR, self.REGISTER_EMAIL_ERROR)

    @allure.step('Проверить, что выведена ошибка  - телефон обязателен')
    def check_fail_register_without_telephone(self):
        """Проверка отображения ошибки регистрации без телефона."""
        self.is_element_visible(RegisterPageLocators.TEL_ERROR)
        self.is_having_text(
            RegisterPageLocators.TEL_ERROR, self.REGISTER_PHONE_ERROR)

    @allure.step('Проверить, что выведена ошибка  - пароль обязателен')
    def check_fail_register_without_password(self):
        """Проверка отображения ошибки регистрации без пароля."""
        self.is_element_visible(RegisterPageLocators.PASSWORD_ERROR)
        self.is_having_text(
            RegisterPageLocators.PASSWORD_ERROR, self.REGISTER_PASSW_ERROR)

    @allure.step('Проверить, что выведена ошибка  - подтверждение пароля обязательно')
    def check_fail_register_without_confirm(self):
        """Проверка отображения ошибки регистрации без подтверждения пароля."""
        self.is_element_visible(RegisterPageLocators.CONFIRM_ERROR)
        self.is_having_text(
            RegisterPageLocators.CONFIRM_ERROR, self.REGISTER_PASSW_CONFIRM_ERROR)


class EditAccountPage(AccountPage):
    """Класс с методами для страницы редактирования аккаунта."""

    TITLE = 'My Account Information'

    @allure.step('Изменить имя на {firstname}')
    def change_firstname(self, firstname):
        """Изменение имени пользователя.

        :param firstname: имя пользователя
        """
        self.input_text(EditAccountPageLocators.FIRSTNAME_FIELD, firstname)

    @allure.step('Сохранить изменения данных аккаунта')
    def save_changes(self):
        """Сохранение данных аккаунта."""
        self.click_on_element(EditAccountPageLocators.SUBMIT_BUTTON)

    def check_firstname(self, firstname):
        """Получение имени пользователя из инупта."""
        self.is_having_value(EditAccountPageLocators.FIRSTNAME_FIELD, firstname)

    def check_lastname(self, lastname):
        """Получение фамилии пользователя из инупта."""
        self.is_having_value(EditAccountPageLocators.LASTNAME_FIELD, lastname)

    def check_email(self, email):
        """Получение email пользователя из инупта."""
        self.is_having_value(EditAccountPageLocators.EMAIL_INPUT, email)

    def check_phone(self, phone):
        """Получение телефона пользователя из инупта."""
        self.is_having_value(EditAccountPageLocators.TELEPHONE_INPUT, phone)

    @allure.step('Нажать на кнопку назад')
    def press_back(self):
        """Сохранение данных аккаунта."""
        self.click_on_element(EditAccountPageLocators.BACK_BUTTON)
