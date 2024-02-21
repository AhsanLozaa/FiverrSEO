import re
from dataclasses import dataclass, field

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from scraper.custom_web_driver import CustomWebDriver
from contextlib import suppress

@dataclass
class ReviewsCount:
    text: str = field(default="")
    value: int = field(default=0)
    
    # custom_web_driver.driver.find_element(By.CLASS_NAME, "seller-overview").find_elements(By.CLASS_NAME, "rating-count-number")[1].text
    def set_reviews_count(self, custom_web_driver: CustomWebDriver):
        reviews_count_elements = []
        with suppress(Exception): reviews_count_elements = custom_web_driver.driver.find_element(By.CLASS_NAME, "seller-overview").find_elements(By.CLASS_NAME, "rating-count-number")
        for element in reviews_count_elements:
            try:
                self.text = element.text
                self.value = int(''.join(re.findall(r'\d', self.text)))
                break
            except Exception as e:
                # print("Failed to set ratings count")
                continue