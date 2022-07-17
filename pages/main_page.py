from .base_page import BasePage
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
import math
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    pass

