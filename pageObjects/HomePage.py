
import pytest
from selenium import webdriver
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver


    shop= (By.XPATH,"//a[normalize-space()='Shop']")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)