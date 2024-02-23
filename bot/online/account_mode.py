from dataclasses import dataclass, field
from enum import Enum

from scraper.custom_web_driver import CustomWebDriver

class Mode(Enum):
    SELLER = "seller"
    BUYER = "buyer"

@dataclass
class AccountMode:
    
    mode: Mode = Mode.BUYER  # Default mode is buyer
    
    def set_mode(self, mode: Mode):
        self.mode = mode

    def switch_mode(self, mode: Mode):
        """
        Switches the mode to the specified mode.
        
        Args:
        - mode: The mode to switch to
        
        Returns:
        - None
        """
        self.mode = mode
    
    def switch_to_selling_mode(self, custom_web_driver: CustomWebDriver):
        elements = custom_web_driver.find_elements_by_class_name("nav-link, nav-link-green")
        for elem in elements:
            if elem.text.lower() == "switch to selling" and "seller_dashboard" in elem.get_attribute("href"):
                custom_web_driver.click(web_element=elem, info="Click on switched to selling")
                self.set_mode(mode=Mode.SELLER.value)