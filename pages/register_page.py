"""Модуль c методами для страницы Регистрации."""


import allure

from pages.base_page import BasePage
from helpers.locators import RegisterPageLocators


class RegisterPage(BasePage):
    """Класс с методами для страницы Регистрации."""

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
            RegisterPageLocators.FIRST_NAME_ERROR, 'First Name must be between 1 and 32 characters!')

    @allure.step('Проверить, что выведена ошибка  - фамилия обязательна')
    def check_fail_register_without_lastname(self):
        """Проверка отображения ошибки регистрации без lastname."""
        self.is_element_visible(RegisterPageLocators.LAST_NAME_ERROR)
        self.is_having_text(
            RegisterPageLocators.LAST_NAME_ERROR, 'Last Name must be between 1 and 32 characters!')

    @allure.step('Проверить, что выведена ошибка  - email обязателен')
    def check_fail_register_without_email(self):
        """Проверка отображения ошибки регистрации без email."""
        self.is_element_visible(RegisterPageLocators.EMAIL_ERROR)
        self.is_having_text(
            RegisterPageLocators.EMAIL_ERROR, 'E-Mail Address does not appear to be valid!')

    @allure.step('Проверить, что выведена ошибка  - телефон обязателен')
    def check_fail_register_without_telephone(self):
        """Проверка отображения ошибки регистрации без телефона."""
        self.is_element_visible(RegisterPageLocators.TEL_ERROR)
        self.is_having_text(
            RegisterPageLocators.TEL_ERROR, 'Telephone must be between 3 and 32 characters!')

    @allure.step('Проверить, что выведена ошибка  - пароль обязателен')
    def check_fail_register_without_password(self):
        """Проверка отображения ошибки регистрации без пароля."""
        self.is_element_visible(RegisterPageLocators.PASSWORD_ERROR)
        self.is_having_text(
            RegisterPageLocators.PASSWORD_ERROR, 'Password must be between 4 and 20 characters!')

    @allure.step('Проверить, что выведена ошибка  - подтверждение пароля обязательно')
    def check_fail_register_without_confirm(self):
        """Проверка отображения ошибки регистрации без подтверждения пароля."""
        self.is_element_visible(RegisterPageLocators.CONFIRM_ERROR)
        self.is_having_text(
            RegisterPageLocators.CONFIRM_ERROR, 'Password confirmation does not match password!')
