from dataclasses import dataclass, field
from typing import List, Dict
from scraper.custom_web_driver import CustomWebDriver
from scraper.search import Search
from selenium.webdriver.remote.webelement import WebElement
from utils import custom_sleep_func_3, custom_print, bg_colors

from random import randint



@dataclass
class SearchSuggestion:
    base_word: str = field(default="")
    search_suggestions: list[str] = field(default_factory=list)
     
    def add_search_suggestion(self, keyword: str):
        self.search_suggestions.append(keyword)
        
    def remove_keyword(self, keyword: str):
        self.search_suggestions.remove(keyword)
    
    def clear_keywords(self):
        self.search_suggestions = []
        
    def generate_variations(self) -> List[str]:
        return [self.base_word[:i] for i in range(1, min(len(self.base_word) + 1, 50))]
        
    
    def set_base_word(self, base_word) -> None:
        self.base_word = base_word        
    
    def scrape_and_set_search_suggestions(self, custom_web_driver: CustomWebDriver):
        """ 
        NOTE Don't use this function where threading is implemented, 
             it can cause unexpected errors, only use this for single instance running
        """
        variations = self.generate_variations()
        search = Search()
        
        empty_li_tags_occurance = 0
        for variation in variations:
            
            search.set_search_text(variation)
            search.enter_search_text(custom_web_driver=custom_web_driver, clear_input_before_typing=False)
            custom_sleep_func_3("Idle before scraping", time_in_seconds=randint(4, 5))
            # write the code below to scrape the suggested keywords
            element = None
            try:
                element = custom_web_driver.find_element_by_class_name(class_name="gig-suggestions-wrapper, no-header", wait_time=5)
            except Exception as e:
                element = custom_web_driver.find_element_by_class_name(class_name="search-bar-panel, logged-in", wait_time=5)
                
            try:
                li_tags = custom_web_driver.find_elements_by_tag_name(tag_name="li", parent_element=element)
                if (len(li_tags) <= 2):
                    empty_li_tags_occurance += 1
                for li_tag in li_tags:
                    text = li_tag.text
                    if (text and text != "") and not(text in self.search_suggestions):
                        self.add_search_suggestion(li_tag.text)
            except Exception as e:
                empty_li_tags_occurance += 1
                print(e)
            
            search.clear_input(custom_web_driver=custom_web_driver)
            custom_sleep_func_3(message="Idling", time_in_seconds=3)
            
            if (empty_li_tags_occurance >= 4):
                custom_print(message="No more", color=bg_colors.HL_RED)
                break
            
            
            
            # x = custom_web_driver.find_element_by_class_name(class_name="gig-suggestions-wrapper, no-header").find_element_by_class_name(class_name="a-new-class")