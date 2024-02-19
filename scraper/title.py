from dataclasses import dataclass, field

from scraper.custom_web_driver import CustomWebDriver

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

@dataclass
class Title:
    text: str = field(default="")
    html: str = field(default="")
    
    def set_title(self, custom_web_driver: CustomWebDriver):
        try:
            self.text = custom_web_driver.driver.find_element(By.TAG_NAME, "h1").text
            self.html = custom_web_driver.driver.find_element(By.TAG_NAME, "h1").get_attribute("outerHTML")
        except Exception as e:
            print("Failed to set title")