import allure

from helpers.locators import FooterPageLocators


class Footer:
    def __init__(self, browser):
        self.browser = browser

    @property
    def footer_links(self):
        return self.browser.locator(FooterPageLocators.LINKS)

    @allure.step('Проверить ссылки в подвале')
    def check_footer_links(self, lst):
        """Проверка ссылок в подвале.

        :param lst: список названий ссылок
        """
        links_text = [(self.footer_links.nth(i)).text_content() for i in range(self.footer_links.count())]
        with allure.step(f'Проверить, что тексты ссылок {links_text} совпадают с {lst}'):
            assert links_text == lst, f'Список ссылок - {links_text}, ОР - {lst}'
