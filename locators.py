from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GO_BUTTON = (By.ID, 'submit')
    AUTORITHATION_NAME_TEXTBOX = (By.ID, "identifierId")
    AUTORITHATION_PASSWOED_TEXTBOX = (By.NAME, "password")
    SHOW_MORE_FIND_BUTTON = (By.XPATH, "//Button[@class='gb_1e'][@type='button']")
    FIND_FROM_TEXTBOX = (By.XPATH, "//input[@class='ZH nr aQa'][@type='text']")
    AUTORITHATION_PASSWOED_TEXTBOX = (By.NAME, "password")
    #LETTERS_IN_BLOCK = (By.XPATH, "//table[@class='F cf zt'][@cellpadding='0']/tbody/tr[@class = 'zA yO' | @class = 'zA zE'][@jsaction='bjyjJe:NOSeAe;pInidd:NOSeAe;']")
    LETTERS_IN_BLOCK = (By.XPATH, "//span[@email='ilya.filinin@simbirsoft.com'][@data-hovercard-id='ilya.filinin@simbirsoft.com'][@class='yP'| @class='zF']")
    COUNT_LETTERS = (By.XPATH, "//div[@class='J-J5-Ji amH J-JN-I'][@role='button']/span[@class='Dj']/span[@class='ts']")
    CREATE_NEW_LETTER_BUTTON = (By.XPATH, "//div[@class='z0']/div[@role='button']")
    TO_EMAIL_LETTER_TEXTBOX = (By.XPATH, "//textarea[@class='vO'][@name='to']")
    LETTER_THEME_TEXTBOX = (By.XPATH, "//input[@class='aoT'][@name='subjectbox']")
    LETTER_TEXT_TEXTBOX = (By.XPATH, "//div[@class='Am Al editable LW-avf'][@role='textbox']")
    SEND_LETTER_BUTTON = (By.XPATH, "//div[@class='T-I J-J5-Ji aoO T-I-atl L3']")
