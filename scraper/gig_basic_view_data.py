from dataclasses import dataclass, field
from selenium.webdriver.remote.webelement import WebElement
from scraper.custom_web_driver import CustomWebDriver
from selenium.webdriver.common.by import By

@dataclass
class GigBasicViewData:
    url: str = field(default="")
    reviews_count: int = field(default=0)
    
    def _set_url(self, url: str) -> None:
        self.url = url
    
    def _set_reviews_count(self, reviews_count: str) -> None:
        self.reviews_count = reviews_count
    
    def scrape_and_set_url(self, gig_element: WebElement) -> None:
        url = gig_element.find_elements(By.TAG_NAME, "a")[0].get_attribute("href")
        self._set_url(url=url)
        
    def scrape_and_set_reviews_count(self, gig_element: WebElement) -> None:
        # TODO
        self.reviews_count = 0
        
    def set_data_by_scraping(self, custom_web_driver: CustomWebDriver) -> None:
        web_elements = custom_web_driver.find_elements_by_class_name(class_name="gig-card-layout")
        for element in web_elements:
            self.scrape_and_set_url(gig_element=element)
            self.scrape_and_set_reviews_count(gig_element=element)
    