# from .fiverr import Fiverr

from scraper_old.fiverr import Fiverr
from scraper_old.custom_web_driver import CustomWebDriver
from description_scraper.description_scraper import execute_description_scraper
# from .scraper.custom_web_driver import
import os


def main():
    
    execute_description_scraper()
    return
    
    key_words_list = [
        "scraping",
        "web scraping",
        "scraping bot",
        "automated data collection",
        "python scraping",
        "web crawling",
        "data mining",
        "website scraping"
    ]
    
    ''' Code Snipper to scrape gig titles'''
    custom_web_driver = CustomWebDriver(headless=False, allow_proxy=False, port="9222")
    fiverr = Fiverr(driver_instance=custom_web_driver)
    # print("Please login to the google.com and fiverr.com, then hit c to continue")
    for key_word in key_words_list:
        if (os.path.exists(f"{key_word.replace(' ', '_')}.csv")):
            continue
        try:
            fiverr.set_search_string(key_word)
            fiverr.execute_scraping_gigs()
        except Exception as e:
            print(":fs lfs lflsfs ")
            print(e)
            breakpoint()
            
    
    
    ''' Code Snipper to scrape gig description '''
    custom_web_driver = CustomWebDriver(headless=False, allow_proxy=False, port="9222")
    fiverr = Fiverr(driver_instance=custom_web_driver)
    
if __name__ == '__main__':
    main()