from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TextBoxPageElement(object):
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
        EC.presence_of_element_located(self.locator)).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")

class ButtonPageElement(object):
    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        return WebDriverWait(driver, 100).until(
        EC.presence_of_element_located(self.locator))