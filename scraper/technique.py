from dataclasses import dataclass, field
from scraper.custom_web_driver import CustomWebDriver
from selenium.webdriver.common.by import By


@dataclass
class Technique:
    technique: str = field(default="")
    

    def set_technique(self, custom_web_driver: CustomWebDriver):
        try:
            self.technique = custom_web_driver.driver.find_elements(By.CLASS_NAME, "metadata-attribute")[2].find_elements(By.TAG_NAME, "li")[0].text
        except Exception as e:
            print(e)
            print("Failed to set Technique")