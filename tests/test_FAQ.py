from conftest import driver
from pages.home_page import HomePage
from data import HomePageFAQ
import pytest
import allure


class TestFAQ:
    @allure.title('Проверка соответсвия вопрос-ответ из выпадающего списка «Вопросы о важном»')
    @pytest.mark.parametrize('number, answer', HomePageFAQ.answers)
    def test_faq(self, driver, number, answer):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.find_questions()
        home_page.accept_cookie()
        home_page.click_question(number)
        assert home_page.get_answer(number) == answer
