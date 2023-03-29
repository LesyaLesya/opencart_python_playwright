import allure

from playwright.sync_api import expect
from helpers.locators import AlertsLocators


class Alert:
    def __init__(self, browser):
        self.browser = browser

    @property
    def success_alert(self):
        return self.browser.locator(AlertsLocators.SUCCESS_ALERT)

    @property
    def danger_alert(self):
        return self.browser.locator(AlertsLocators.DANGER_ALERT)

    @allure.step('Проверить, что выведен алерт с ошибкой')
    def check_danger_alert(self):
        """Проверка видимости алерта."""
        expect(self.danger_alert).to_be_visible()

    @allure.step('Кликнуть на кнопку Логина в алерте')
    def click_login_from_alert(self):
        """Клик по кнопке Логина в алерте."""
        self.success_alert.locator(AlertsLocators.LINK_LOGIN_ALERT).click()

    @allure.step('Кликнуть на кнопку в алерте')
    def click_link_from_alert(self):
        """Клик по кнопке Сравнения в алерте."""
        self.success_alert.locator(AlertsLocators.LINK_ALERT).click()

    @allure.step('Проверить сообщение об ошибке при пустом отзыве')
    def check_error_text(self, txt):
        """Проверить сообщение об ошибке."""
        with allure.step(
                f'Проверить, что текст ошибки при пустом отзыве - {txt}'):
            expect(self.danger_alert).to_have_text(txt)

    @allure.step('Проверить видимость успешного алерта')
    def check_success_alert(self):
        """Вывод успешного алерта."""
        expect(self.success_alert).to_be_visible()
