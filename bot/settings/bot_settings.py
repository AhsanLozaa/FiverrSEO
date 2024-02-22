from dataclasses import dataclass, field
from scraper.custom_web_driver import CustomWebDriver

@dataclass
class BotSettings:
    custom_web_driver: CustomWebDriver = field(default_factory=CustomWebDriver)
    
    def some_func(self):
        print("This is bot settings class")
    