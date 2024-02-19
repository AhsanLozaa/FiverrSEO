
from dataclasses import dataclass, field
from contextlib import suppress
from random import randint
from scraper.custom_web_driver import CustomWebDriver
from selenium.webdriver.common.by import By

from selenium.common.exceptions import ElementNotInteractableException

from utils import send_keys_delay_random, custom_sleep_func_3


@dataclass
class Search:
    
    search_text: str = field(default="")
    
    def click_on_search_button(self, custom_web_driver: CustomWebDriver):
        search_button_elements_list = custom_web_driver.driver.find_elements(By.CLASS_NAME, "submit-button-icon")
        for elem in search_button_elements_list:
            try:
                elem.click()
                print("Successfully clicked on search button")
            except ElementNotInteractableException as e:
                continue
        
    
    def enter_search_text(self, custom_web_driver: CustomWebDriver):
        # locate the search input field
        input_field_elements = custom_web_driver.driver.find_elements(By.CLASS_NAME, "long-placeholder")
        for elem in input_field_elements:
            try:
                elem.click()
                with suppress(Exception): elem.clear()
                print("Entering search text: ", self.search_text)
                send_keys_delay_random(controller=elem, keys=self.search_text)
                print("Entered the search text")
            except ElementNotInteractableException as e:
                continue
            
    
    def execute_search(self, search_text: str, custom_web_driver: CustomWebDriver):
        self.search_text = search_text
        self.enter_search_text(custom_web_driver=custom_web_driver)
        custom_sleep_func_3(message="Idle before clicking search", time_in_seconds=randint(5, 8))
        self.click_on_search_button(custom_web_driver=custom_web_driver)
        custom_sleep_func_3(message="Idle after clicking search", time_in_seconds=randint(6, 10))
        
        