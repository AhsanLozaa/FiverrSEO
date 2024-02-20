from scraper.search_suggestion_keywords import SearchSuggestion
from scraper.custom_web_driver import CustomWebDriver
from utils import custom_sleep_func_3


def main():
    
    custom_web_driver = CustomWebDriver(un_detectable=True, user_data_dir="/Users/ahsanilyas/Documents/FiverrSEO/chrome/1")
    custom_web_driver.navigate(url="https://fiverr.com/", idle=3)
    # base_words_list = ["web scraping", "data mining", "web automation", "selenium", "python selenium"]
    base_words_list = ['web scraping', 'web scraper', 'website scraping', 'website data scraping', 'amazon aws', 'web scraping python', 'data entry', 'excel data cleaning', 'data cleaning', 'data scraping', 'data collection', 'excel data analysis', 'data engineer', 'data mining', 'data merge excel', 'ms excel data entry', 'ms excel data cleaning', 'database management',  'web automation', 'automated website', 'amazon scraper', 'selenium', 'selenium automation', 'python', 'python programming', 'python bot', 'python scraping', 'python coder','python developer', 'python script', 'python web scraping']
    search_suggestion = SearchSuggestion()
    for base_word in base_words_list:
        search_suggestion.set_base_word(base_word=base_word)
        search_suggestion.scrape_and_set_search_suggestions(custom_web_driver=custom_web_driver)
        custom_sleep_func_3(message="Idle after scraping a base word", time_in_seconds=60)
    breakpoint()
    

if __name__ == "__main__":
    main()
    


['amazon scraper']
