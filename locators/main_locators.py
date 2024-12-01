from selenium.webdriver.common.by import By

class CookieBaLocator:
    BUTTON_COOKIE = By.ID, "rcc-confirm-button" # Кнопка "Да все привыкли", куки

class OrderButtonLocators:
    BUTTON_ORDER_TOP = By.XPATH, "//button[@class='Button_Button__ra12g']" # Кнопка заказать вверху страницы
    BUTTON_ORDER_CENTER = By.XPATH, "//button[contains(@class, 'Button_Button__ra12g Button')]"  # Кнопка заказать по центру внизу страницы

class MainPageLocators:
    LOGO_YANDEX = By.XPATH, "//*[@class='Header_LogoYandex__3TSOI']" # Логотип Яндекс
    QUESTION = By.XPATH, "//*[@id='accordion__heading-{}']" # Локатор вопроса
    ANSWER = By.XPATH, "//*[@id='accordion__panel-{}']" # Локатор ответа
    QUESTION_8 = By.XPATH, "//*[@id='accordion__heading-7']" # Вопрос 8
