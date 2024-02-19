from dataclasses import dataclass, field
from typing import List, Dict
from scraper.custom_web_driver import CustomWebDriver
from scraper.search import Search
from selenium.webdriver.remote.webelement import WebElement



@dataclass
class SearchSuggestion:
    base_word: str = field(default="")
    search_suggestions: list[str] = field(default_factory=list)
     
    def add_keyword(self, keyword: str):
        self.search_suggestions.append(keyword)
        
    def remove_keyword(self, keyword: str):
        self.search_suggestions.remove(keyword)
    
    def clear_keywords(self):
        self.search_suggestions = []
        
    def generate_variations(self) -> List[str]:
        return [self.base_word[:i] for i in range(1, min(len(self.base_word) + 1, 50))]
        

    
    
    def scrape_key_words(self, custom_web_driver: CustomWebDriver):
        """ 
        NOTE Don't use this function where threading is implemented, 
             it can cause unexpected errors, only use this for single instance running
        """
        variations = self.generate_variations()
        for variation in variations:
            search = Search(search_text=variation)
            search.set_search_text(variation)
            search.enter_search_text(variation, clear_input_before_typing=False)
            # write the code below to scrape the suggested keywords
            x: WebElement = custom_web_driver.find_element_by_class_name(class_name="gig-suggestions-wrapper, no-header")
            x