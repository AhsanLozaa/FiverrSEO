from dataclasses import dataclass, field
from scraper.custom_web_driver import CustomWebDriver
from scraper.search import Search

from typing import List
import pandas as pd

from selenium.webdriver.common.by import By
import time

@dataclass
class GigBasicViewData:
    url: str
    reviews_count: int = field(default=0)
    
    def set_url(self, custom_web_driver: CustomWebDriver):
        self.url = ""
    
    def set_reviews_count(self, custom_web_driver: CustomWebDriver):
        self.reviews_count = 0
    
    
@dataclass
class Fiverr:
    # url: str
    driver_instance: CustomWebDriver
    search_string: str = field(default="")
    s: Search = field(default_factory=Search)
    # gigs: list[Gig] = field(default_factory=list)
    urls: list[str] = field(default_factory=list)
    gig_basic_view_data: list[GigBasicViewData] = field(default_factory=list)
    
    
    key_word_list: list[str] = field(default_factory=list)
    urls_csv_file_path: str = field(default="")
    
    def navigate(self, url):
        print("Navigating to ", url)
        self.driver_instance.driver.get(url=url)
        print("Navigated to ", url)
        
    def set_search_string(self, search_string):
        self.search_string = search_string
        
    def search(self):
        self.s.execute_search(search_text=self.search_string, custom_web_driver=self.driver_instance)
    
    def set_urls(self, limit: int = 100):
        try:
            web_elements = self.driver_instance.driver.find_elements(By.CLASS_NAME, "gig-card-layout")[:limit]
            for element in web_elements:
                url = element.find_elements(By.TAG_NAME, "a")[0].get_attribute("href")
                self.urls.append(url)
        except Exception as e:
            self.urls = []
            print(e)
    
    def sort_search_results(self):
        try:
            # write the code here to sort the saerch result by best selling
            sort_by_button = self.driver_instance.find_element_by_class_name(class_name="sort-by-wrapper")
            sort_by_button.click()
            time.sleep(1.5)
            sort_by_options = self.driver_instance.find_elements_by_class_name(class_name="label-item")
            for sort_by_option in sort_by_options:
                if (sort_by_option.text.lower() == "best selling"):
                    sort_by_option.click()
                    return
        except Exception as e:
            print("Failed to sort search results")
    
    def save_gig_urls_to_csv(self, csv_file_path: str):
        try:
            print("Saving the urls in ", csv_file_path)
            df = pd.DataFrame(columns=["url"], data=self.urls)
            df.to_csv(csv_file_path, index=False)
            print("Successfully saved the urls in ", csv_file_path)
        except Exception as e:
            print(e)
            print("Failed to save the urls in ", csv_file_path)
    
    # @classmethod
    def extract_gig_urls(self):
        urls_list = []
        for key_word in self.key_word_list:
            self.set_search_string(key_word)
            self.search()
            self.sort_search_results()
            self.set_urls(limit=40)
            urls_list += self.urls
    
    def extract_and_save_gig_urls(self):
        
        if (self.key_word_list.__len__() <= 0 or self.urls_csv_file_path == ""):
            # handling missing attributes
            print("key_word_list: ", self.key_word_list)
            print("urls_csv_file_path: ", self.urls_csv_file_path)
            print("Missing attributes at extract_and_save_gig_urls")
            return
        self.navigate("https://fiverr.com/")
        self.extract_gig_urls()
        self.save_gig_urls_to_csv(csv_file_path=self.urls_csv_file_path)
        
