from dataclasses import dataclass
from bot.settings.constants import BotConstants
from scraper.custom_web_driver import CustomWebDriver

@dataclass
class Dashboard:
    
    def click_on_dash_board(self, custom_web_driver: CustomWebDriver) -> bool:
        print("Clicking on nav dasboard")
        # Get the dashboard selector from BotConstants
        dashboard_selector = BotConstants.NAV_DAHBOARD_SELECTOR.value

        # Find all anchor tags with the specified class name
        nav_anchor_tags = custom_web_driver.find_elements_by_class_name(class_name=dashboard_selector.attribute)

        # Iterate over the anchor tags
        for tag in nav_anchor_tags:
            # Check if the text of the tag matches the dashboard value
            if tag.text.lower() == dashboard_selector.value:
                print("Clicking on dashboard")
                try:
                    # Attempt to click on the tag
                    custom_web_driver.click(web_element=tag, info="dashboard")
                    return True  # Return True if click is successful
                except Exception as e:
                    return  # Return None if click fails

        return False  # Return False if no matching tag is found