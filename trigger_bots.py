from utils import custom_print, bg_colors
from bot.online.OnlineBot import OnlineBot
from scraper.custom_web_driver import CustomWebDriver

def main():
    custom_print("Triggering the bots", bg_colors.OKGREEN)

    custom_web_driver = CustomWebDriver(un_detectable=True, user_data_dir="/Users/ahsanilyas/Documents/FiverrSEO/chrome/misterrtech")
    online_bot = OnlineBot(custom_web_driver=custom_web_driver)
    breakpoint()
    online_bot.click_on_my_business()
    online_bot.click_on_profile_from_business()
    
    # 

    
    

if __name__ == "__main__":
    main()