from dataclasses import dataclass, field
from enum import Enum
from bot.settings.constants import BotConstants
from bot.online.MyBusiness import MyBusiness
from scraper.custom_web_driver import CustomWebDriver

@dataclass
class OnlineBot:
    
    is_selling_mode: bool = field(default=False)
    custom_web_driver: CustomWebDriver = field(default_factory=CustomWebDriver)
    my_business: MyBusiness = field(default_factory=MyBusiness)
    
    
    def set_selling_mode(self, value):
        self.is_selling_mode = value
    
    def click_on_dah_board(self) -> bool:
        print("Clicking on nav dasboard")
        # Get the dashboard selector from BotConstants
        dashboard_selector = BotConstants.NAV_DAHBOARD_SELECTOR.value

        # Find all anchor tags with the specified class name
        nav_anchor_tags = self.custom_web_driver.find_elements_by_class_name(class_name=dashboard_selector.attribute)
        
        # Iterate over the anchor tags
        for tag in nav_anchor_tags:
            # Check if the text of the tag matches the dashboard value
            if tag.text.lower() == dashboard_selector.value:
                print("Clicking on dashboard")
                try:
                    # Attempt to click on the tag
                    self.custom_web_driver.click(web_element=tag, info="dashboard")
                    return True  # Return True if click is successful
                except Exception as e:
                    return  # Return None if click fails

        return False  # Return False if no matching tag is found
    
    def click_on_site_logo(self) -> bool:
        print("Clicking Site Logo")
        try:
            site_logo_web_element = self.custom_web_driver.find_element_by_class_name(class_name=BotConstants.SITE_LOGO_CLASS_NAME)
            self.custom_web_driver.click(web_element=site_logo_web_element, info="site logo")
            print("Succesfully clicked on the site logo")
            return True
        except Exception as e:
            print("Failed to click on the site logo")
            return False
        
    
    """ Profile Section """
    def click_on_profile_photo(self) -> bool:
        print("Clicking on profile photo")
    
    def click_on_profile(self) -> bool:
        if not self.click_on_profile_photo():
            # If clicking on the profile photo fails, return False
            return False
        print("Clicking on profile")
        
    def click_on_my_business(self):
        self.my_business.click_on_my_business(custom_web_driver=self.custom_web_driver)
    
    def click_on_profile_from_business(self):
        self.my_business.click_on_profile(custom_web_driver=self.custom_web_driver)
        
    def swith_to_selling(self):
        elements = self.custom_web_driver.find_elements_by_class_name("nav-link, nav-link-green")
        for elem in elements:
            if elem.text.lower() == "switch to Selling" and "seller_dashboard" in elem.get_attribute("href"):
                self.custom_web_driver.click(web_element=elem, info="Click on switched to selling")
                self.set_selling_mode(value=True)
                
    def trigger_online_bot_automation(self):
        self.custom_web_driver.navigate("https://fiverr.com/")
        if not self.is_selling_mode:
            self.swith_to_selling()
    
        
    