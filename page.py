from locators import MainPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from element import TextBoxPageElement, ButtonPageElement
import allure

class TextBoxElement(TextBoxPageElement):
    locator = 'q'
    def __init__ (self, locator):
        self.locator = locator

class ButtonElement(ButtonPageElement):
    locator = 'q'
    def __init__ (self, locator):
        self.locator = locator


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver




class MainPage(BasePage):
    nameUserAutorithation = TextBoxElement(MainPageLocators.AUTORITHATION_NAME_TEXTBOX)
    passwordAutorithation = TextBoxElement(MainPageLocators.AUTORITHATION_PASSWOED_TEXTBOX)
    fromLetterSend = TextBoxElement(MainPageLocators.FIND_FROM_TEXTBOX)
    toEmailLetter = TextBoxElement(MainPageLocators.TO_EMAIL_LETTER_TEXTBOX)
    themeLetter = TextBoxElement(MainPageLocators.LETTER_THEME_TEXTBOX)
    textLetter = TextBoxElement(MainPageLocators.LETTER_TEXT_TEXTBOX)
    btnShowMoreFieldFromFind = ButtonElement(MainPageLocators.SHOW_MORE_FIND_BUTTON)
    btnCreateLetter = ButtonElement(MainPageLocators.CREATE_NEW_LETTER_BUTTON)
    countLetters = ButtonElement(MainPageLocators.COUNT_LETTERS)
    btnsendLetter = ButtonElement(MainPageLocators.SEND_LETTER_BUTTON)

    def is_title_matches(self):
        return "Gmail" in self.driver.title

    def GetElements(self, locator, timeOut = 10):
        elements = WebDriverWait(self.driver, timeOut).until(
        EC.presence_of_all_elements_located(locator))
        return elements

    def enter_autorithation_username(self, name):
        self.nameUserAutorithation = name
        self.nameUserAutorithation = Keys.RETURN

    def enter_autorithation_password(self, pwd):
        self.passwordAutorithation = pwd
        self.passwordAutorithation = Keys.RETURN

    def enter_to_email_letter(self, email):
        self.toEmailLetter = email

    def enter_theme_letter(self, theme):
        self.themeLetter = theme

    def click_show_moere_find_button(self):
        self.btnShowMoreFieldFromFind.click()

    def search_from_letter(self, name):
        self.click_show_moere_find_button()
        self.fromLetterSend = name
        self.fromLetterSend = Keys.RETURN

    def get_count_letter(self):
        elements = self.GetElements(MainPageLocators.LETTERS_IN_BLOCK)
        return len(elements)/2

    def click_create_new_letter(self):
        self.btnCreateLetter.click()

    def enter_text_letter(self, text):
        self.textLetter = text

    def send_letter(self):
        self.textLetter = (Keys.CONTROL + Keys.RETURN)

