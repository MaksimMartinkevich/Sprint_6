from selenium.webdriver.common.by import By


class HomePageLocators:
    HEADER_ORDER_BUTTON = [By.XPATH, './/div[contains(@class, "Header_Nav")]/button[text()="Заказать"]'] #кнопка Заказать в хедере
    PAGE_ORDER_BUTTON = [By.XPATH, './/div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]'] #кнопка Заказать на странице
    QUESTION = [By.XPATH, './/div[@id = "accordion__heading-{}"]'] #вопрос
    ANSWER = [By.XPATH, './/div[@id="accordion__panel-{}"]/p'] #ответ
    COOKIE = [By.ID, 'rcc-confirm-button'] #принять куки
    LOGO_SCOOTER = [By.XPATH, './/a[@href = "/"]'] #лого Самокат
    LOGO_YANDEX = [By.XPATH, './/a[@href = "//yandex.ru"]'] #лого Яндекс
