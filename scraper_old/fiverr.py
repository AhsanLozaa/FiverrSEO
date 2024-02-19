from dataclasses import dataclass, field
from .custom_web_driver import CustomWebDriver
# from custom_web_driver import CustomWebDriver
import re
import pandas as pd

# from undetected_chromedriver.webelement import WebElement
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from utils import custom_sleep_func_3


from scraper_old.search_old import Search
from scraper_old.gig import Gig

@dataclass
class Fiverr:
    # url: str
    driver_instance: CustomWebDriver
    search_string: str = field(default="")
    s: Search = field(default_factory=Search)
    gigs: list[Gig] = field(default_factory=list)
    
    # def __post_init__(self):
    #     self.driver_instance = CustomWebDriver(headless=False, allow_proxy=False, port="9222")
    
    def navigate(self):
        self.driver_instance.driver.get(url=self.url)
        
    def set_search_string(self, search_string):
        self.search_string = search_string
        
    def search(self):
        self.s.execute_search(search_text=self.search_string, custom_web_driver=self.driver_instance)
    
    def execute_scraping_gigs(self):
        # self.navigate()
        self.search()
        gig_elements_list = self.driver_instance.driver.find_elements(By.CLASS_NAME, "gig-card-layout")
        for elem in gig_elements_list:
            print("Extracting gig data")
            gig = Gig()
            gig.set_gig_data(gig_element=elem)
            self.gigs.append(gig)
        
        gigs_dict_list = [g.__dict__ for g in self.gigs]
        df = pd.DataFrame(gigs_dict_list)
        df.to_csv(f"{self.search_string.replace(' ', '_')}.csv", index=False)
        self.gigs = []

    def execute_scrape_gig_description(self, url):
        self.driver_instance.driver.get(url=url)
        custom_sleep_func_3(message="Idle after navigating to the gig url", time_in_seconds=5)
        
        breakpoint()        