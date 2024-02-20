from dataclasses import dataclass, field
from scraper.custom_web_driver import CustomWebDriver
from selenium.webdriver.common.by import By
from contextlib import suppress
from utils import custom_print

@dataclass
class Description:
    text: str = field(default="")
    html: str = field(default="")
    
    def set_description(self, custom_web_driver: CustomWebDriver) -> None:
        
        try:
            self.text = custom_web_driver.find_element_by_class_name(class_name="description-wrapper").text
            self.html = custom_web_driver.find_element_by_class_name(class_name="description-wrapper").get_attribute("outerHTML")
            return
        except Exception as e:
            pass
        
        try:
            about_gig_web_element = custom_web_driver.find_element_by_class_name(class_name="about-gig")
            read_more_element = custom_web_driver.find_element_by_tag_name(tag_name="a", parent_element=about_gig_web_element)
            with suppress(Exception): read_more_element.click()
            about_gig_web_element = custom_web_driver.find_element_by_class_name(class_name="about-gig")
            self.text = about_gig_web_element.text.split("Read Less")[0]
            self.html = about_gig_web_element.get_attribute("outerHTML")
            return
        except Exception as e:
            pass
        
        custom_print(message="Failed to get the description")
            