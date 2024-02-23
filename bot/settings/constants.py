from dataclasses import dataclass
from enum import Enum

@dataclass
class Selector:
    attribute: str
    value: str

    
class BotConstants(Enum):
    NAV_DAHBOARD_SELECTOR = Selector(attribute="seller-main-item", value="dashboard")
    SITE_LOGO_CLASS_NAME = "site-logo"