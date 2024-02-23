from dataclasses import dataclass
from bot.settings.constants import BotConstants
from scraper.custom_web_driver import CustomWebDriver

@dataclass
class Dashboard:
    """
    Class representing the dashboard of the bot.
    """

    def click_on_dash_board(self, custom_web_driver: CustomWebDriver) -> bool:
        """
        Clicks on the dashboard link in the navigation bar.
        
        Args:
        - custom_web_driver: CustomWebDriver instance
        
        Returns:
        - bool: True if the click is successful, False otherwise
        """
        print("Clicking on nav dashboard")
        # Get the dashboard selector from BotConstants
        dashboard_selector = BotConstants.NAV_DASHBOARD_SELECTOR.value

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
                    return False  # Return False if click fails

        return False  # Return False if no matching tag is found
