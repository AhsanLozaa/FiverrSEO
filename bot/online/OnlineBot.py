from dataclasses import dataclass, field
from enum import Enum
from bot.settings.bot_settings import BotSettings
from bot.settings.constants import BotConstants

@dataclass
class OnlineBot:
    bot_settings: BotSettings = field(default_factory=BotSettings)
    
    def click_on_dah_board(self):
        nav_anchor_tags = self.bot_settings.custom_web_driver.find_elements_by_class_name(class_name=BotConstants.NAV_DASH_BOARD_ANCHOR_TAG.value)
        for tag in nav_anchor_tags:
            if tag.text.lower() == "dashboard":
                print("Clicking on dashboard")

# ! IMPORTANT
# NOTE: do the balance coding from here, please check the constants.py file
# NOTE: Also try to move the attribute(class name, tag_name or whatever) and text(text inside the element) to a different class, so its easy to understand that the element is dependent on each other attribute and text
