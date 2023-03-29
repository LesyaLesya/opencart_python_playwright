"""Модуль с локаторами элементов."""


class AlertsLocators:
    """Локаторы алертов."""

    LINK_LOGIN_ALERT = 'div.alert-success > i + a'
    LINK_ALERT = 'div.alert-success > a + a'
    FAIL_LOGIN_ALERT = '.alert-danger'
    DANGER_ALERT = '.alert.alert-danger.alert-dismissible'
    SUCCESS_ALERT = 'div.alert-success'


class HeaderPageLocators:
    """Локаторы для шапки сайта."""

    SEARCH_INPUT = 'div#search > input'
    SEARCH_BUTTON = '.btn.btn-default.btn-lg'
    LOGO = '#logo > a'
    MENU = '.navbar-collapse'
    CART_BUTTON = '#cart > button.btn-block'
    TOP_LINKS = '#top-links'
    SEARCH_FIELD = '#search'
    MY_ACCOUNT_LINK = '//a[@title = "My Account"]'
    LOGIN_LINK = '//a[text() = "Login"]'
    CURRENCY_DROP_DOWN_BUTTON = '.pull-left button.dropdown-toggle'
    CURRENCY_VALUES_BUTTONS = '.pull-left button.dropdown-toggle + ul > li > button'
    CURRENCY_DROP_DONW = '.pull-left button.dropdown-toggle + ul'
    DROPDOWN_FOR_DESKTOPS = '//a[text()="Desktops"]//following-sibling::div'
    COMPONENTS_FOR_DROPDOWN = '//a[text()="Components"]//following-sibling::div'
    LAPTOPS_FOR_DROPDOWN = '//a[text()="Laptops & Notebooks"]//following-sibling::div'
    DESKTOPS_IN_MENU = '//a[text()="Desktops"]'
    COMPONENTS_IN_MENU = '//a[text()="Components"]'
    LAPTOPS_IN_MENU = '//a[text()="Laptops & Notebooks"]'


class MainPageLocators:
    """Локаторы для главной страницы."""

    BANNER = '#content .swiper-viewport:nth-child(1)'
    BANNER_PAGINATION_BULLETS = '.swiper-pagination.slideshow0.swiper-pagination-clickable.swiper-pagination-bullets'
    HEADER_FEATURED = 'h3'
    CAROUSEL_BRAND = '#carousel0.swiper-container-horizontal'
    CAROUSEL_PAGINATION_BULLETS = '.swiper-pagination.carousel0.swiper-pagination-clickable.swiper-pagination-bullets'
    CAROUSEL_PAGINATION_BULLET = '.swiper-pagination.carousel0.swiper-pagination-clickable.swiper-pagination-bullets > .swiper-pagination-bullet'
    BANNER_MACBOOK = '//div[contains(@class, "swiper-slide-active")]/img[@alt="MacBookAir"]'
    BANNER_IPHONE = '//div[contains(@class, "swiper-slide-active")]/a/img[@alt="iPhone 6"]'
    BANNER_BULLET = 'div.slideshow0 > span.swiper-pagination-bullet'
    FEATURED_PRODUCT_LINK = 'h3 + div.row > div > div > div.image > a'
    FEATURED_PRODUCT_NAME = 'h3 + div.row > div > div > div.image +  div.caption > h4 > a'
    BRAND_IMAGE_IN_CAROUSEL = '#carousel0 .swiper-slide'


class ProductPageLocators:
    """Локаторы для страницы товара."""

    PRODUCT_HEADER = '.btn-group + h1'
    BUTTON_CART = '#product > div > #button-cart'
    IMAGES_BLOCK = '.thumbnails'
    RATING_BLOCK = '.rating'
    PRODUCT_DESCRIPTION = '#tab-description > p'
    MAIN_PRODUCT_IMAGE = '//ul[@class="thumbnails"]/li[1]'
    PRODUCT_IMAGE_IN_WINDOW = '.mfp-figure'
    TAB_CLASS = '//ul[@class="nav nav-tabs"]/li'
    TAB_DESCRIPTION_LINK = '//a[@href="#tab-description"]'
    TAB_SPECIFICATION_LINK = '//a[@href="#tab-specification"]'
    TAB_REVIEWS_LINK = '//a[@href="#tab-review"]'
    ITEM_TITLE = '.col-sm-4 > .btn-group + h1'
    WISH_LIST_BUTTON = '//button[@data-original-title="Add to Wish List"]'
    COMPARE_BUTTON = '//div[@class="btn-group"]/button[@data-original-title="Compare this Product"]'
    WRITE_REVIEW_BUTTON = '//a[text()="Write a review"]'
    REVIEW_NAME_FIELD = '#input-name'
    REVIEW_FIELD = '#input-review'
    RATING_RADIO_BUTTON = 'input[name="rating"]'
    REVIEW_BUTTON = 'div.pull-right > #button-review'
    RIGHT_BLOCK_INFO = '//div[@class="col-sm-4"]/ul[@class="list-unstyled"]'
    ELEMENTS_OF_RIGHT_BLOCK_INFO_FIRST = '//div[@class="col-sm-4"]/ul[@class="list-unstyled"][1]/li'
    ELEMENTS_OF_RIGHT_BLOCK_INFO_SECOND = '//div[@class="col-sm-4"]/ul[@class="list-unstyled"][2]/li'
    PRODUCT_PRICE = '//div[@class="col-sm-4"]/ul[@class="list-unstyled"][2]/li/h2'


class CataloguePageLocators:
    """Локаторы для страницы каталога."""

    BREADCRUMB = 'ul.breadcrumb'
    CATALOGUE_HEADER = 'h2'
    CATALOGUE_IMAGE = 'img.img-thumbnail'
    LEFT_MENU = '#column-left'
    BANNER_UNDER_LEFT_MENU = '#banner0'
    COMPARE_BUTTON = '//button[@data-original-title="Compare this Product"]'
    COMPARE_LINK = '#compare-total'
    SELECT_SORT = '#input-sort'
    ITEM_NAME = '.caption > h4 > a'
    ITEM_PRICE = '.caption > h4 + p + p.price'
    WISH_LIST_BUTTON = '//button[@data-original-title="Add to Wish List"]'
    ITEM_CART = 'div.row > div.product-layout'
    LIST_VIEW_BUTTON = '#list-view'
    GRID_VIEW_BUTTON = '#grid-view'
    ADD_TO_CART_BUTTON = '//div[@class="button-group"]/button[1]'
    DESKTOPS_IN_LEFT_MENU = 'a.list-group-item:has-text("Desktops (")'
    LAPTOPS_IN_LEFT_MENU = 'a.list-group-item:has-text("Laptops & Notebooks (")'
    COMPONENTS_IN_LEFT_MENU = 'a.list-group-item:has-text("Components (")'
    TABLETS_IN_LEFT_MENU = 'a.list-group-item:has-text("Tablets")'
    SOFTWARE_IN_LEFT_MENU = 'a.list-group-item:has-text("Software (")'
    PHONES_IN_LEFT_MENU = 'a.list-group-item:has-text("Phones & PDAs (")'
    CAMERAS_IN_LEFT_MENU = 'a.list-group-item:has-text("Cameras (")'
    MP3_IN_LEFT_MENU = 'a.list-group-item:has-text("MP3 Players (")'


class LoginPageLocators:
    """Локаторы для страницы логина."""

    NEW_CUSTOMER_FORM = '#content > .row > .col-sm-6:first-child >.well'
    OLD_CUSTOMER_FORM = '#content > .row > .col-sm-6:last-child >.well'
    RIGHT_LIST_MENU = 'div.list-group'
    BUTTON_FOR_NEW_CUSTOMER = 'a.btn.btn-primary'
    BUTTON_FOR_OLD_CUSTOMER = 'input.btn.btn-primary'
    EMAIL_INPUT = '#input-email'
    PASSWORD_INPUT = '#input-password'
    LOGIN_BUTTON = '//input[@value="Login"]'


class RegisterPageLocators:
    """Локаторы для страницы регистрации."""

    HEADER = 'div#content > h1'
    TEXT_FOR_LOGIN = 'div#content > p'
    FIRST_NAME_FIELD = 'input#input-firstname'
    LAST_NAME_FIELD = 'input#input-lastname'
    EMAIL_FIELD = 'input#input-email'
    TEL_FIELD = 'input#input-telephone'
    PASSW_FIELD = 'input#input-password'
    CONFIRM_FIELD = 'input#input-confirm'
    SUBSCRIBE_RADIO = '[name="newsletter"]'
    PRIVACY_POLICY = '.buttons > .pull-right'
    CONTINUE_BUTTON = '[type="submit"]'
    RIGHT_MENU = 'div.list-group'
    AGREE_CHECKBOX = '[name="agree"]'
    FIRST_NAME_ERROR = '#input-firstname + .text-danger'
    LAST_NAME_ERROR = '#input-lastname + .text-danger'
    EMAIL_ERROR = '#input-email + .text-danger'
    TEL_ERROR = '#input-telephone + .text-danger'
    PASSWORD_ERROR = '#input-password + .text-danger'
    CONFIRM_ERROR = '#input-confirm + .text-danger'


class AdminPageLocators:
    """Локаторы для администраторской страницы."""

    PANEL_HEADING = '.panel-heading'
    USERNAME_INPUT = '#input-username'
    PASSWORD_INPUT = '#input-password'
    LOGIN_BUTTON = 'button.btn.btn-primary'
    HELP_BLOCK = '.help-block'
    NEED_LOGIN_TEXT = '//h1[contains(text(), "enter your login")]'
    LOGOUT_BUTTON = '.nav > li:nth-child(2) > a'
    LEFT_MENU_CATALOGUE = '#menu-catalog > a'
    LEFT_MENU_PRODUCTS = '#collapse1 > li:nth-child(2) > a'
    PRODUCTS_TABLE = '.table-responsive'


class SearchPageLocators:
    """Локаторы для страницы поиска."""

    SEARCH_INPUT = '#input-search'
    SEARCH_BUTTON = '#button-search'
    SELECT_CATEGORY = 'select.form-control'
    CHECKBOX_CATEGORY = '//input[@name="sub_category"]'
    CHECKBOX_DESCRIPTION = '#description'
    PRODUCT_NAME = '.product-thumb > .image + div > .caption > h4 > a'
    EMPTY_RESULT = 'h2 + p'


class AccountPageLocators:
    """Локаторы для страницы аккаунта пользователя."""

    WISH_LIST_LINK = '//div[@id="content"]/ul[1]/li[4]/a'
    ITEM_NAMES = '#content > div > table > tbody > tr >td.text-left > a'
    LOGOUT_RIGHT_BLOCK = '//div[@class="list-group"]/a[contains(text(), "Logout")]'
    TEXT_AFTER_LOGOUT = 'h1 + p'
    LOGIN_RIGHT_BLOCK = '//div[@class="list-group"]/a[contains(text(), "Login")]'
    REGISTER_RIGHT_BLOCK = '//div[@class="list-group"]/a[contains(text(), "Register")]'
    MY_ACCOUNT_RIGHT_BLOCK = '//div[@class="list-group"]/a[contains(text(), "My Account")]'


class ComparePageLocators:
    """Локаторы для страницы сравнения."""

    ITEM_NAMES = 'h1 + table > tbody > tr > td > a > strong'
    REMOVE_BUTTON = 'a.btn-danger'
    TEXT_FOR_EMTY_COMPARE = '#content > h1 + p'
    ADD_TO_CART_BUTTON = 'input.btn-primary'


class CartPageLocators:
    """Локаторы для страницы корзины."""

    ITEM_NAMES = 'form > div.table-responsive > table > tbody > tr >td.text-left > a'
    REMOVE_BUTTONS = '//button[@data-original-title="Remove"]'
    TEXT_EMPTY_CART = 'h1 + p'
    QUANTITY_INPUT = 'div.btn-block > input.form-control'
    QUANTITY_REFRESH_BUTTON = '//button[@data-original-title="Update"]'
    UNIT_PRICE = 'form > div.table-responsive > table > tbody > tr > td:nth-child(5)'
    TOTAL_PRICE = 'form > div.table-responsive > table > tbody > tr > td:nth-child(6)'
    CONTINUE_SHOPPING_BUTTON = 'div.pull-left > a.btn.btn-default'


class FooterPageLocators:
    """Локаторы для подвала."""

    LINKS = 'footer div.col-sm-3 > ul.list-unstyled > li > a'
