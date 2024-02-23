from dataclasses import dataclass, field
from enum import Enum
from bot.settings.bot_settings import BotSettings
from bot.settings.constants import BotConstants

@dataclass
class OnlineBot:
    bot_settings: BotSettings = field(default_factory=BotSettings)
    
    def click_on_dah_board(self) -> bool:
        print("Clicking on nav dasboard")
        # Get the dashboard selector from BotConstants
        dashboard_selector = BotConstants.NAV_DAHBOARD_SELECTOR.value

        # Find all anchor tags with the specified class name
        nav_anchor_tags = self.bot_settings.custom_web_driver.find_elements_by_class_name(class_name=dashboard_selector.attribute)
        
        # Iterate over the anchor tags
        for tag in nav_anchor_tags:
            # Check if the text of the tag matches the dashboard value
            if tag.text.lower() == dashboard_selector.value:
                print("Clicking on dashboard")
                try:
                    # Attempt to click on the tag
                    self.bot_settings.custom_web_driver.click(web_element=tag, info="dashboard")
                    return True  # Return True if click is successful
                except Exception as e:
                    return  # Return None if click fails

        return False  # Return False if no matching tag is found
    
    def click_on_site_logo(self) -> bool:
        print("Clicking Site Logo")
        try:
            site_logo_web_element = self.bot_settings.custom_web_driver.find_element_by_class_name(class_name=BotConstants.SITE_LOGO_CLASS_NAME)
            self.bot_settings.custom_web_driver.click(web_element=site_logo_web_element, info="site logo")
            print("Succesfully clicked on the site logo")
            return True
        except Exception as e:
            print("Failed to click on the site logo")
            return False
        
    
    def click_on_profile_photo(self) -> bool:
        print("Clicking on profile photo")
    
    def click_on_profile(self) -> bool:
        if not self.click_on_profile_photo():
            # If clicking on the profile photo fails, return False
            return False
        print("Clicking on profile")
        
    

# ! IMPORTANT
# NOTE: do the balance coding from here, please check the constants.py file
# NOTE: Also try to move the attribute(class name, tag_name or whatever) and text(text inside the element) to a different class, so its easy to understand that the element is dependent on each other attribute and text
