from dataclasses import dataclass, field
from bot.settings.constants import BotConstants
from scraper.custom_web_driver import CustomWebDriver

@dataclass
class MyBusiness:
    
    """ My Business Section """
    def click_on_my_business(self, custom_web_driver: CustomWebDriver) -> bool:
        print("Clicking on nav My Business")
        my_business_selector = BotConstants.NAV_MY_BUSINESS_SELECTOR.value

        # Find all anchor tags with the specified clas name
        nav_anchor_tags = custom_web_driver.find_elements_by_class_name(class_name=my_business_selector.attribute)
        
        # Iterate over the anchor tags
        for tag in nav_anchor_tags:
            # Check if the text of the tag matches the My Business value
            if tag.text.lower() == my_business_selector.value:
                print("Clicking on My Business")
                try:
                    # Attempt to click on the tag
                    custom_web_driver.click(web_element=tag, info="My Business")
                    return True  # Return True if click is successful
                except Exception as e:
                    return  # Return None if click fails

        return False  # Return False if no matching tag is found
    
    def click_on_profile(self, custom_web_driver: CustomWebDriver) -> bool:
        print("Clicking on profile")
        elements = custom_web_driver.find_elements_by_class_name(class_name="nav-link")
        for elem in elements:
            try:
                if (elem.text.lower() == "profile"):
                    custom_web_driver.click(web_element=elem, info="profile from business dropdown") 
                    return True
            except Exception as e:
                continue
            
        return False