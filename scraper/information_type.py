from dataclasses import dataclass, field
from scraper.custom_web_driver import CustomWebDriver
from selenium.webdriver.common.by import By


@dataclass
class InformationType:
    information_types: list = field(default_factory=list)
    
    def set_information_type(self, custom_web_driver: CustomWebDriver):
        try:
            information_types_web_elements = custom_web_driver.driver.find_elements(By.CLASS_NAME, "metadata-attribute")[1].find_elements(By.TAG_NAME, "li")
            for element in information_types_web_elements:
                self.information_types.append(element.text)
        except Exception as e:
            print(e)
            print("Failed to set Information Type")