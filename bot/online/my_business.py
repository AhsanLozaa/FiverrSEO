from dataclasses import dataclass, field
from bot.settings.constants import BotConstants
from scraper.custom_web_driver import CustomWebDriver

@dataclass
class MyBusiness:

    def click_on_my_business(self, custom_web_driver: CustomWebDriver) -> bool:
        """
        Clicks on the 'My Business' link in the navigation bar.
        
        Args:
        - custom_web_driver: CustomWebDriver instance
        
        Returns:
        - bool: True if the click is successful, False otherwise
        """
        print("Clicking on nav My Business")
        my_business_selector = BotConstants.NAV_MY_BUSINESS_SELECTOR.value
        return custom_web_driver.find_and_click_by_text(class_name=my_business_selector.attribute, text=my_business_selector.value, info="My Business")

    def click_on_profile(self, custom_web_driver: CustomWebDriver) -> bool:
        """
        Clicks on the 'Profile' link in the My Business dropdown.
        
        Args:
        - custom_web_driver: CustomWebDriver instance
        
        Returns:
        - bool: True if the click is successful, False otherwise
        """
        print("Clicking on profile")
        my_business_profile_selector = BotConstants.NAV_MY_BUSINESS_PROFILE_SELECTOR.value
        return custom_web_driver.find_and_click_by_text(class_name=my_business_profile_selector.attribute, text=my_business_profile_selector.value, info="profile from business dropdown")

    def click_on_orders(self, custom_web_driver: CustomWebDriver) -> bool:
        """
        Clicks on the 'Orders' link in the My Business dropdown.
        
        Args:
        - custom_web_driver: CustomWebDriver instance
        
        Returns:
        - bool: True if the click is successful, False otherwise
        """
        print("Clicking on Orders")
        my_business_orders_selector = BotConstants.NAV_MY_BUSINESS_ORDERS_SELECTOR.value
        return custom_web_driver.find_and_click_by_text(class_name=my_business_orders_selector.attribute, text=my_business_orders_selector.value, info="orders from business dropdown")
