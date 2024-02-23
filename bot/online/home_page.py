from dataclasses import dataclass
from scraper.custom_web_driver import CustomWebDriver
from bot.settings.constants import BotConstants

@dataclass
class HomePage:
    """
    Class representing the home page of the website.
    """

    def click_on_site_logo(self, custom_web_driver: CustomWebDriver) -> bool:
        """
        Clicks on the site logo on the home page.
        
        Args:
        - custom_web_driver: CustomWebDriver instance
        
        Returns:
        - bool: True if the click is successful, False otherwise
        """
        print("Clicking Site Logo")
        try:
            site_logo_web_element = custom_web_driver.find_element_by_class_name(class_name=BotConstants.SITE_LOGO_CLASS_NAME)
            custom_web_driver.click(web_element=site_logo_web_element, info="site logo")
            print("Succesfully clicked on the site logo")
            return True
        except Exception as e:
            print("Failed to click on the site logo")
            return False
