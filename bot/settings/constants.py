from dataclasses import dataclass
from enum import Enum

@dataclass
class Selector:
    attribute: str
    value: str

    
class BotConstants(Enum):
    # selectors
    NAV_DAHBOARD_SELECTOR = Selector(attribute="seller-main-item", value="dashboard")
    NAV_MY_BUSINESS_SELECTOR = Selector(attribute="seller-main-item", value="my business")
    NAV_MY_BUSINESS_PROFILE_SELECTOR = Selector(attribute="nav-link", value="profile")
    NAV_MY_BUSINESS_ORDERS_SELECTOR = Selector(attribute="nav-link", value="orders")
    
    # class names
    SITE_LOGO_CLASS_NAME = "site-logo"