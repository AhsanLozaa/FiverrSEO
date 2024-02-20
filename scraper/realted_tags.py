from dataclasses import dataclass, field
from typing import List


from scraper.custom_web_driver import CustomWebDriver
from contextlib import suppress

@dataclass
class RelatedTag:
    text: str
    link: str
    
@dataclass
class RelatedTagController:
    tags: List[RelatedTag] = field(default_factory=list)

    def add_tag(self, text: str, link: str):
        if text and text != "":
            self.tags.append(RelatedTag(text=text, link=link))

    def remove_tag(self, text: str):
        self.tags = [tag for tag in self.tags if tag.text != text]

    def clear_tags(self):
        self.tags = []

    def print_tags(self):
        for tag in self.tags:
            print(f"{tag.text}: {tag.link}")
            
    def scrape_and_add_tags(self, custom_web_driver: CustomWebDriver):
        
        try:
            gig_tags_container_element = custom_web_driver.find_element_by_class_name(class_name="gig-tags-container")
            li_tags = custom_web_driver.find_elements_by_tag_name(tag_name="li", parent_element=gig_tags_container_element)
            for li_tag in li_tags:
                text = ""
                link = ""
                with suppress(Exception): text = li_tag.text
                with suppress(Exception): link = custom_web_driver.find_element_by_tag_name(tag_name="a", parent_element=li_tag).get_attribute("href")
                self.add_tag(text=text, link=link)
        except Exception as e:
            print("Failed to get the related tags")
