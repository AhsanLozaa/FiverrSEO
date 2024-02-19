from dataclasses import dataclass, field
import re

# from undetected_chromedriver.webelement import WebElement
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from scraper_old.custom_web_driver import CustomWebDriver



@dataclass
class Gig:
    url: str = field(default="")
    title: str = field(default="")
    ratings_count_str: str = field(default="")
    ratings_count: int = field(default=0)
    rating_score_str: str = field(default="")
    rating_score: float = field(default=0.0)
    gig_price_str: str = field(default="")
    gig_price: float = field(default=0.0)
    seller_level: str = field(default="")
    description: str = field(default="")
    description_html: str = field(default="")
    
    def navigate(self, url: str, custom_web_driver: CustomWebDriver):
        custom_web_driver.driver.get(url=url)
        
    
    def set_url(self, gig_element: WebElement):
        try:
            self.url = gig_element.find_elements(By.TAG_NAME, "a")[0].get_attribute("href")
        except Exception as e:
            print("Failed to set url")
    
    def set_title(self, gig_element: WebElement):
        try:
            self.title = gig_element.find_element(By.TAG_NAME, "h3").text
        except Exception as e:
            print("Failed to set title")
            
    def set_ratings_count(self, gig_element: WebElement):
        try:
            # int(''.join(re.findall(r'\d', self.raw_text)))
            self.ratings_count_str = gig_element.find_element(By.CLASS_NAME, "ratings-count").text
            self.ratings_count = int(''.join(re.findall(r'\d', self.ratings_count_str)))
        except Exception as e:
            print("Failed to set ratings count")
            
    def set_rating_score(self, gig_element: WebElement):
        try:
            self.rating_score_str = gig_element.find_element(By.CLASS_NAME, "rating-score").text
            self.rating_score = float(''.join(re.findall(r'\d', self.rating_score_str)))
        except Exception as e:
            print("Failed to set ratings score")
            
    def set_gig_price(self, gig_element: WebElement):
        try:
            self.gig_price_str = gig_element.find_elements(By.CLASS_NAME, "co-grey-1200")[0].text
            self.gig_price = float(''.join(re.findall(r'\d', self.gig_price_str)))
        except Exception as e:
            print("Failed to set gig price")

    def set_seller_level(self, gig_element: WebElement):
        try:
            self.seller_level = gig_element.find_element(By.CLASS_NAME, "text-semi-bold").text
        except Exception as e:
            print("Failed to set gig price")
    
    def set_description(self, custom_web_driver: CustomWebDriver):
        print("Set Gig Description")
        self.navigate(url=self.url, custom_web_driver=custom_web_driver)
        self.description_html = custom_web_driver.driver.find_element(By.CLASS_NAME, "description-wrapper").get_attribute('innerHTML')
        self.description = custom_web_driver.driver.find_element(By.CLASS_NAME, "description-wrapper").text
    
    def set_gig_data(self, gig_element: WebElement):
        self.set_url(gig_element=gig_element)
        self.set_title(gig_element=gig_element)
        self.set_ratings_count(gig_element=gig_element)
        self.set_rating_score(gig_element=gig_element)
        self.set_gig_price(gig_element=gig_element)
        self.set_seller_level(gig_element=gig_element)
        