from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from data import Url
import allure


class HomePage(BasePage):
    @allure.step('Нажать на кнопку "Заказать" в хедере')
    def click_header_order_button(self):
        self.click_on_element(HomePageLocators.HEADER_ORDER_BUTTON)


    @allure.step('Нажать на кнопку "Заказать" на странице')
    def click_page_button(self):
        self.click_on_element(HomePageLocators.PAGE_ORDER_BUTTON)


    @allure.step('Нажать на вопрос')
    def click_question(self, number):
        method, locator = HomePageLocators.QUESTION
        locator = locator.format(number)
        return self.click_on_element((method, locator))


    @allure.step('Получить текст ответа на вопрос')
    def get_answer(self, number):
        method, locator = HomePageLocators.ANSWER
        locator = locator.format(number)
        return self.get_text((method, locator))


    @allure.step('Открыть главную страницу "Яндекс Самокат"')
    def open_home_page(self):
        self.open_page(Url.SCOOTER_HOME_PAGE)


    @allure.step('Нажать на лого "Яндекс"')
    def click_on_yandex_logo(self):
        self.click_on_element(HomePageLocators.LOGO_YANDEX)


    @allure.step('Нажать на лого "Самокат"')
    def click_on_scooter_logo(self):
        self.click_on_element(HomePageLocators.LOGO_SCOOTER)


    @allure.step('Проверить URL "Яндекс Самокат"')
    def check_redirection_on_scooter_page(self):
        self.cross_url(Url.SCOOTER_HOME_PAGE)


    @allure.step('Проверить URL "Дзен"')
    def check_redirection_on_dzen_page(self):
        self.cross_url(Url.DZEN_HOME_PAGE)


    @allure.step('Принять куки')
    def accept_cookie(self):
        self.wait_element(HomePageLocators.COOKIE)
        self.click_on_element(HomePageLocators.COOKIE)


    @allure.step('Проскролить к списку вопросов')
    def find_questions(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")