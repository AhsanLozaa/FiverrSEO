from dataclasses import dataclass, field
from typing import List, Dict
from scraper.custom_web_driver import CustomWebDriver
from scraper.search import Search


@dataclass
class Keyword:
    start: str = field(default="")
    keywords: list[str] = field(default_factory=list)
     
    def add_keyword(self, keyword: str):
        self.keywords.append(keyword)
        
    def remove_keyword(self, keyword: str):
        self.keywords.remove(keyword)
    
    def clear_keywords(self):
        self.keywords = []
    
    def scrape_key_words(self, custom_web_driver, search, key_words: Dict):
        self.start = key_words["start"]
        
        
    def scrape_and_set_keywords(self, custom_web_driver: CustomWebDriver, search: Search):
        
        search.set_search_text()
        search.enter_search_text()
        search_suggestions = custom_web_driver.find_element_by_class_name(class_name="gig-suggestions-wrapper, no-header")
        
