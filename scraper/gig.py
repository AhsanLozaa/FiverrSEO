from dataclasses import dataclass, field
import pandas as pd
from typing import List

from scraper.title import Title
from scraper.description import Description
from scraper.information_type import InformationType
from scraper.technology import Technology
from scraper.pricing import PricingData
from scraper.technique import Technique
from scraper.reviews_count import ReviewsCount
from scraper.custom_web_driver import CustomWebDriver
from scraper.pricing import PlanType


@dataclass
class Gig:
    url: str
    title: Title = field(default_factory=Title)
    description: Description = field(default_factory=Description)
    technology: Technology = field(default_factory=Technology)
    information_type: InformationType = field(default_factory=InformationType)
    technique: Technique = field(default_factory=Technique)
    reviews_count: ReviewsCount = field(default_factory=ReviewsCount)
    pricing_data: PricingData = field(default_factory=PricingData)
    
    @classmethod
    def save_gigs_to_csv_file(cls, gigs: List['Gig'], file_path: str, previous_records_df: pd.DataFrame) -> bool:
        
        try:
            gigs_as_dict = []
            for gig in gigs:
                gigs_as_dict.append(gig.__dict__())
            
            df = pd.json_normalize(gigs_as_dict)
            final_df = pd.concat([previous_records_df, df], ignore_index=True)
            final_df.to_csv(file_path, index=False)
            return True
        except Exception as e:
            return False

    def __dict__(self):
        
        # Custom implementation for __dict__
        return {
            # url
            'url': self.url,
            # title
            'title': self.title.text,
            'title_html': self.title.html,
            # description
            'description': self.description.text,
            'description_html': self.description.html,
            # technology
            'technology': self.technology.technologies,
            # information_type
            'information_type': self.information_type.information_types,
            # technique
            'technique': self.technique.technique,
            # reviews_count
            'reviews_count': self.reviews_count.value,
            'reviews_count_text': self.reviews_count.text,
            # pricing_data
            'basic': self.pricing_data.get_plan(plan_type=PlanType.BASIC),
            'standard': self.pricing_data.get_plan(plan_type=PlanType.STANDARD),
            'premium': self.pricing_data.get_plan(plan_type=PlanType.PREMIUM)
        }

    
    
    def set_gig_data(self, custom_web_driver: CustomWebDriver) -> None:
        custom_web_driver.navigate(self.url)
        breakpoint()
        self.title.set_title(custom_web_driver=custom_web_driver)
        self.description.set_description(custom_web_driver=custom_web_driver)
        self.technology.set_technology(custom_web_driver=custom_web_driver)
        self.information_type.set_information_type(custom_web_driver=custom_web_driver)
        self.technique.set_technique(custom_web_driver=custom_web_driver)
        self.reviews_count.set_reviews_count(custom_web_driver=custom_web_driver)
        self.pricing_data.set_pricing_data(custom_web_driver=custom_web_driver)
            
        custom_web_driver.find_element_by_class_name(class_name="gig-tags-container")


