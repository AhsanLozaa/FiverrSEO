# from scraper_ol,/d.custom_web_driver import CustomWebDriver
# from scraper.reviews_count import ReviewsCount
# from scraper.custom_web_driver import CustomWebDriver
import scraper.custom_web_driver as custom_web_driver


def url_extractor(keywords_list: list = []):
    for index, item in enumerate(keywords_list):
        print("Index: ", index, " | Item: ", item)

# gig-suggestions-wrapper no-header
# get all the lis in it