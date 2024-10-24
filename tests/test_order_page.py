from conftest import driver
from pages.home_page import HomePage
from pages.order_page import OrderPage
from data import Users
import allure


class TestOrderPage:
    @allure.title('Проверка оформления заказа через кнопку "Заказать" в хедере')
    def test_create_order_header_button(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        order_page = OrderPage(driver)
        home_page.accept_cookie()
        home_page.click_header_order_button()
        order_page.create_order(Users.user_header)
        assert 'Заказ оформлен' in order_page.check_success_order()


    @allure.title('Проверка оформления заказа через кнопку "Заказать" на странице')
    def test_create_order_page_button(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        order_page = OrderPage(driver)
        home_page.accept_cookie()
        home_page.click_page_button()
        order_page.create_order(Users.user_main)
        assert 'Заказ оформлен' in order_page.check_success_order()