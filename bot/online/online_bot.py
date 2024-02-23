from dataclasses import dataclass, field
from enum import Enum
from bot.settings.constants import BotConstants
from bot.online.my_business import MyBusiness
from bot.online.home_page import HomePage
from bot.online.account_mode import AccountMode
from scraper.custom_web_driver import CustomWebDriver

@dataclass
class OnlineBot:
    
    is_selling_mode: bool = field(default=False)
    custom_web_driver: CustomWebDriver = field(default_factory=CustomWebDriver)
    my_business: MyBusiness = field(default_factory=MyBusiness)
    home_page: HomePage = field(default_factory=HomePage)
    account_mode: AccountMode = field(default_factory=AccountMode)
    
    def set_selling_mode(self, value):
        self.is_selling_mode = value
    
    def click_on_dash_board(self) -> bool:
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
        self.home_page.click_on_site_logo(custom_web_driver=self.custom_web_driver)
        
    def click_on_my_business(self):
        self.my_business.click_on_my_business(custom_web_driver=self.custom_web_driver)
    
    def click_on_profile_from_business(self):
        self.my_business.click_on_profile(custom_web_driver=self.custom_web_driver)
        
    def swith_to_selling(self):
        self.account_mode.switch_to_selling_mode(custom_web_driver=self.custom_web_driver)
    
    def trigger_online_bot_automation(self):
        # 1.) Navigate to the fiverr.com url
        # 2.) Check if the mode is not in selling mode, if not in selling mode switch to selling mode
        # 3.) 
        self.custom_web_driver.navigate("https://fiverr.com/")
        if not self.is_selling_mode:
            self.swith_to_selling()

        breakpoint()
        
    