import unittest
from selenium import webdriver
import page
from selenium.webdriver.common.keys import Keys
import time
import pytest



class TestGmail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(desired_capabilities={
            "browserName": "chrome",
        })
        self.driver.get("https://www.google.com/gmail/")
        
    def test_Gmail(self):
        main_page = page.MainPage(self.driver)

        assert main_page.is_title_matches(), "Gmail title doesn't match."
        
        main_page.enter_autorithation_username('Your_name')
        
        main_page.enter_autorithation_password('Your_pass')        
  

        main_page.search_from_letter('Филинин Илья')
        count_letter = main_page.get_count_letter()

        main_page.click_create_new_letter()

        main_page.enter_to_email_letter('cwwc@bk.ru')
        main_page.enter_theme_letter('Тестовое задание. Романов')
        main_page.enter_text_letter("От вас получено:%d"%count_letter)
        main_page.send_letter()
        time.sleep(5)

        assert main_page.is_title_matches(), "Gmail title doesn't match."

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()