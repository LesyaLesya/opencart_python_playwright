import allure
from playwright.sync_api import expect

from helpers.locators import HeaderPageLocators
from helpers.styles import Border, Colors, Cursor, Gradients, SIZES


class Header:
    def __init__(self, browser):
        self.browser = browser

    @property
    def cart_button(self):
        return self.browser.locator(HeaderPageLocators.CART_BUTTON)

    @property
    def cart_link(self):
        return self.browser.locator(HeaderPageLocators.SHOPPING_CART_TOP_LINK)

    @property
    def search_input(self):
        return self.browser.locator(HeaderPageLocators.SEARCH_INPUT)

    @property
    def search_button(self):
        return self.browser.locator(HeaderPageLocators.SEARCH_BUTTON)

    @property
    def account_link(self):
        return self.browser.locator(HeaderPageLocators.MY_ACCOUNT_LINK)

    @property
    def login_link(self):
        return self.browser.locator(HeaderPageLocators.LOGIN_LINK)

    @property
    def currency_dropdown_button(self):
        return self.browser.locator(HeaderPageLocators.CURRENCY_DROP_DOWN_BUTTON)

    @property
    def currency_dropdown(self):
        return self.browser.locator(HeaderPageLocators.CURRENCY_DROP_DONW)

    @property
    def currency_dropdown_values(self):
        return self.browser.locator(HeaderPageLocators.CURRENCY_VALUES_BUTTONS)

    @allure.step('Проверить видимость элементов на странице')
    def check_elements_visibility(self):
        """Проверка видимости элементов."""
        lst = [HeaderPageLocators.LOGO,
               HeaderPageLocators.MENU,
               HeaderPageLocators.CART_BUTTON,
               HeaderPageLocators.TOP_LINKS,
               HeaderPageLocators.SEARCH_FIELD]
        for i in lst:
            expect(self.browser.locator(i)).to_be_visible()

    @allure.step('Осуществить поиск по значению {value}')
    def search(self, value):
        """Ввод текста в поле поиска.

        :param value: искомое значение
        """
        self.search_input.clear()
        self.search_input.fill(value)
        self.search_button.click()

    @allure.step('Перейти на страницу логина')
    def go_to_login_page(self):
        """Проверка перехода на страницу Логина."""
        self.account_link.click()
        self.login_link.click()

    @allure.step('Проверить стили кнопки корзины')
    def check_cart_button_css(self):
        """Проверка стилей кнопки корзины без наведения."""
        expect(self.cart_button).to_have_css('font-size', SIZES.SIZE_12)
        expect(self.cart_button).to_have_css('line-height', SIZES.SIZE_18)
        expect(self.cart_button).to_have_css('color', Colors.WHITE)
        expect(self.cart_button).to_have_css('background-color', Colors.DARK_GRAY)
        expect(self.cart_button).to_have_css('background-image', Gradients.LIGHT_BLACK)
        expect(self.cart_button).to_have_css('border-top-color', Colors.LIGHT_BLACK)
        expect(self.cart_button).to_have_css('border-right-color', Colors.LIGHT_BLACK)
        expect(self.cart_button).to_have_css('border-bottom-color', Colors.BLACK)
        expect(self.cart_button).to_have_css('border-left-color', Colors.LIGHT_BLACK)
        expect(self.cart_button).to_have_css('border-radius', SIZES.SIZE_4)
        expect(self.cart_button).to_have_css('cursor', Cursor.POINTER)

    @allure.step('Проверить стили кнопки корзины при наведении')
    def check_cart_button_css_hover(self):
        """Проверка стилей кнопки корзины при наведении."""
        self.cart_button.hover()
        expect(self.cart_button).to_have_css('font-size', SIZES.SIZE_12)
        expect(self.cart_button).to_have_css('line-height', SIZES.SIZE_18)
        expect(self.cart_button).to_have_css('color', Colors.WHITE)
        expect(self.cart_button).to_have_css('background-color', Colors.LIGHT_BLACK)
        expect(self.cart_button).to_have_css('background-image', Gradients.MEDIUM_BLACK)
        expect(self.cart_button).to_have_css('border-top-color', Colors.LIGHT_BLACK)
        expect(self.cart_button).to_have_css('border-right-color', Colors.LIGHT_BLACK)
        expect(self.cart_button).to_have_css('border-bottom-color', Colors.BLACK)
        expect(self.cart_button).to_have_css('border-left-color', Colors.LIGHT_BLACK)
        expect(self.cart_button).to_have_css('border-radius', SIZES.SIZE_4)
        expect(self.cart_button).to_have_css('cursor', Cursor.POINTER)

    @allure.step('Проверить стили кнопки корзины при клике')
    def check_cart_button_css_click(self):
        """Проверка стилей кнопки корзины при клике."""
        self.cart_button.click()
        expect(self.cart_button).to_have_css('font-size', SIZES.SIZE_12)
        expect(self.cart_button).to_have_css('line-height', SIZES.SIZE_18)
        expect(self.cart_button).to_have_css('color', Colors.MEDIUM_GRAY)
        expect(self.cart_button).to_have_css('background-color', Colors.WHITE)
        expect(self.cart_button).to_have_css('background-image', 'none')
        expect(self.cart_button).to_have_css('border', Border.LIGHT_GRAY)
        expect(self.cart_button).to_have_css('border-radius', SIZES.SIZE_4)
        expect(self.cart_button).to_have_css('cursor', Cursor.POINTER)
        self.check_cart_button_dropdown_open()

    def check_cart_button_dropdown_open(self):
        """Прверка отображения выпадашки у кнопки корзины."""
        expect(self.cart_button).to_have_attribute('aria-expanded', 'true')

    @allure.step('Кликнуть на выпадающий список валют')
    def click_on_currency_drop_down(self):
        """Клик по списку валют и проверка, что список раскрыт."""
        self.currency_dropdown_button.click()
        expect(self.currency_dropdown).to_have_css('display', 'block')

    @allure.step('Проверить значения валют в выпадающем списке')
    def check_currency_values(self, lst):
        """Проверка значений валют.

        :param lst: список названий валют
        """
        names = [(self.currency_dropdown_values.nth(i)).text_content() for i in
                 range(self.currency_dropdown_values.count())]
        with allure.step(f'Проверить, что полученный список - {names} - совпадает с - {lst}'):
            for i in names:
                assert i in lst, f'ФР - {names}, ОР - {lst}'

    @allure.step('Выбрать значение валюты {value}')
    def choose_currency(self, value):
        """Выбор значения валюты.

        :param value: значение валюты
        """
        self.click_on_currency_drop_down()
        for i in range(self.currency_dropdown_values.count()):
            element = (self.currency_dropdown_values.nth(i)).text_content()
            if element == value:
                with allure.step(f'Кликнуть по значению валюты {value}'):
                    self.currency_dropdown_values.nth(i).click()

    @allure.step('Проверить выпадающие списки горизонтального меню')
    def check_dropdown_menu(self, lst):
        """Проверка выпадающих списков горизонтального меню.

        :param lst: список локторов пунктов меню и выпадающих списков меню
        """
        for i in lst:
            with allure.step(f'Навести курсок на пункт меню {i[0]}'):
                self.browser.locator(i[0]).nth(0).hover()
            with allure.step(f'Проверить выпадающее меню {i[1]}'):
                expect(self.browser.locator(i[1])).to_be_visible()

    @allure.step('Перейти на страницу корзины')
    def go_to_cart_page(self):
        """Проверка перехода на страницу корзины."""
        self.cart_link.click()
