from dataclasses import dataclass, field
from bot.online.dashboard import Dashboard
from bot.online.my_business import MyBusiness
from bot.online.home_page import HomePage
from bot.online.account_mode import AccountMode
from scraper.custom_web_driver import CustomWebDriver

@dataclass
class OnlineBot:
    
    is_selling_mode: bool = field(default=False)
    custom_web_driver: CustomWebDriver = field(default_factory=CustomWebDriver)
    my_business: MyBusiness = field(default_factory=MyBusiness)
    home_page: HomePage = field(default_factory=HomePage)
    account_mode: AccountMode = field(default_factory=AccountMode)
    dashboard: Dashboard = field(default_factory=Dashboard)
    
    def set_selling_mode(self, value):
        self.is_selling_mode = value
    
    def click_on_dash_board(self) -> bool:
        self.dashboard.click_on_dash_board(custom_web_driver=self.custom_web_driver)
    
    def click_on_site_logo(self) -> bool:
        self.home_page.click_on_site_logo(custom_web_driver=self.custom_web_driver)
        
    def click_on_my_business(self):
        self.my_business.click_on_my_business(custom_web_driver=self.custom_web_driver)
    
    def click_on_profile_from_business(self):
        self.my_business.click_on_profile(custom_web_driver=self.custom_web_driver)
        
    def swith_to_selling(self):
        self.account_mode.switch_to_selling_mode(custom_web_driver=self.custom_web_driver)
    
    def trigger_online_bot_automation(self):
        # 1.) Navigate to the fiverr.com url
        # 2.) Check if the mode is not in selling mode, if not in selling mode switch to selling mode
        # 3.) 
        self.custom_web_driver.navigate("https://fiverr.com/")
        if not self.account_mode.mode.value == "buyer":
            self.swith_to_selling()

        breakpoint()
        
    