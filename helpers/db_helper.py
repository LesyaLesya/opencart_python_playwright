"""Модуль с методами для работы с тестовыми данными БД."""

import allure
import time

from helpers import db_queries


@allure.step('Проверить, что пользователь не появился в БД')
def check_user_not_in_db(db_connection, email=None, firstname=None, lastname=None, tel=None):
    """Проверка пользователя в БД."""

    result = db_queries.get_new_user(db_connection, email, firstname, lastname, tel)
    assert len(result) == 0, f'Найдено записей {len(result)}'


@allure.step(
    'Проверить, что пользователь появился в БД - с email {email}, именем {firstname}, фамилией {lastname}, телефоном {tel}')
def check_user_in_db(db_connection, firstname, lastname, email, tel, radio_idx):
    get_user_from_db(db_connection, firstname, lastname, email, tel, radio_idx)
    del_user_from_bd(db_connection, email, firstname)


def get_user_from_db(db_connection, firstname, lastname, email, tel, radio_idx):
    """Проверка пользователя в БД."""

    result = db_queries.get_new_user(db_connection, email)
    firstname_db = result[0][4]
    lastname_db = result[0][5]
    email_db = result[0][6]
    tel_db = result[0][7]
    newsletter_db = result[0][13]
    active_db = result[0][17]
    assert firstname_db == firstname, f'Имя пользователя в базе {firstname_db}, ОР {firstname}'
    assert lastname_db == lastname, f'Фамилия пользователя в базе {lastname_db}, ОР {lastname}'
    assert email_db == email, f'Email пользователя в базе {email_db}, ОР {email}'
    assert tel_db == tel, f'Телефон пользователя в базе {tel_db}, ОР {tel}'
    assert active_db == 1, f'Активность пользователя в базе {active_db}, ОР 1'
    if radio_idx == 0:
        assert newsletter_db == 1, f'Рассылка пользователя в базе {newsletter_db}, ОР 1'
    else:
        assert newsletter_db == 0, f'Рассылка пользователя в базе {newsletter_db}, ОР 0'


def del_user_from_bd(db_connection, email, fistname):
    """Удаление юзера из БД."""

    return db_queries.delete_user(db_connection, email, fistname)


@allure.step('Проверить, что ревью НЕ появилось в БД')
def check_review_not_in_db(db_connection, author, text):
    """Проверить, что ревью НЕ появилось в БД."""

    time.sleep(3)
    result = db_queries.get_review(db_connection, author, text)
    if result == 0:
        assert True
    else:
        assert False, f'Записей найдено - {result}'


@allure.step('Проверить, что ревью появилось в БД - автор {author}, текст {text}')
def check_review_in_db(db_connection, author, text):
    get_review_from_db(db_connection, author, text)
    del_review_from_bd(db_connection, author, text)


def get_review_from_db(db_connection, author, text):
    """Проверка, сколько записей возвращается по заданному условию."""

    time.sleep(3)
    result = db_queries.get_review(db_connection, author, text)
    if result > 0:
        assert True
    else:
        assert False, f'Записи не найдены - {result}'


def del_review_from_bd(db_connection, author, text):
    """Возвращает удаление отзыва из БД."""

    return db_queries.delete_review(db_connection, author, text)