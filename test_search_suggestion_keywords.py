from scraper.search_suggestion_keywords import SearchSuggestion
from scraper.custom_web_driver import CustomWebDriver
from utils import custom_sleep_func_3


def main():
    
    custom_web_driver = CustomWebDriver(un_detectable=True, user_data_dir="/Users/ahsanilyas/Documents/FiverrSEO/chrome/1")
    custom_web_driver.navigate(url="https://fiverr.com/", idle=3)
    # base_words_list = ["web scraping", "data mining", "web automation", "selenium", "python selenium"]
    # base_words_list = ["fiverr", "seo", "gig", "fiverr seo"]
    base_words_list = ["fiverr seo", "fiverr gig promotion", "fiverr gig image", "fiverr gig thumbnail", "fiverr gig description", "fiverr gig video", "gig seo", "gig description", "fiverr gig seo"]
    search_suggestion = SearchSuggestion()
    for base_word in base_words_list:
        search_suggestion.set_base_word(base_word=base_word)
        search_suggestion.scrape_and_set_search_suggestions(custom_web_driver=custom_web_driver)
        custom_sleep_func_3(message="Idle after scraping a base word", time_in_seconds=60)
        # custom_sleep_func_3(message="Idle after scraping a base word", time_in_seconds=5)
    breakpoint()
    

if __name__ == "__main__":
    main()



# TODO
# Integrate this in the main automation file
# Reduce the sleep time when the enable_variation_search is False for scrape_and_set_search_suggestions
# once th search_suggestions are generated filter out the releveant search suggestions related to the niche
# and use the above filtered saerch_suggestion to scrape the urls