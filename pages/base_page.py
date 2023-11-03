from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    # Поиск элемента который находится в зоне видимости
    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    # Поиск элементов которые находятся в зоне видимости
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    # Получение значения из элемента который не находится в поле видимости, поиск по дом дереву
    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    # Получение значений из элементов которые не находятся в поле видимости, поиск по дом дереву
    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    # Поиск элемента который не находится в зоне видимости
    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    # Поиск элемента который стал кликабельный
    def element_is_clicable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    # Переход к элементу (используя скрипт js)
    def go_to_element(self, element):
        self.driver.execute_script("argument[0].scrollIntoView();", element)
