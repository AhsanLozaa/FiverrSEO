from dataclasses import dataclass, field
from scraper.custom_web_driver import CustomWebDriver
from selenium.webdriver.common.by import By

@dataclass
class Technology:
    technologies: list = field(default_factory=list)
    
    def set_technology(self, custom_web_driver: CustomWebDriver):
        try:
            technologies_web_elements = custom_web_driver.driver.find_elements(By.CLASS_NAME, "metadata-attribute")[0].find_elements(By.TAG_NAME, "li")
            for element in technologies_web_elements:
                self.technologies.append(element.text)
        except Exception as e:
            print(e)
            print("Failed to set Technology")