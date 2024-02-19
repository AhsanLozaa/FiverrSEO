from dataclasses import dataclass, field
from scraper.custom_web_driver import CustomWebDriver
from selenium.webdriver.common.by import By

@dataclass
class Description:
    text: str = field(default="")
    html: str = field(default="")
    
    def set_description(self, custom_web_driver: CustomWebDriver):
        try:
            self.text = custom_web_driver.driver.find_element(By.CLASS_NAME, "description-wrapper").text
            self.html = custom_web_driver.driver.find_element(By.CLASS_NAME, "description-wrapper").get_attribute("outerHTML")
        except Exception as e:
            print(e)
            print("Failed to set description")