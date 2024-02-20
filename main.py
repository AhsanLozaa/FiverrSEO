import pandas as pd
import os
from scraper.custom_web_driver import CustomWebDriver
from scraper.fiverr import Fiverr
from scraper.gig import Gig
from utils import custom_print, bg_colors

def main():
    
    urls_csv_file_path = "/Users/ahsanilyas/Documents/FiverrSEO/Data/mobile-application/urls.csv"
    gigs_csv_file_path = "/Users/ahsanilyas/Documents/FiverrSEO/Data/mobile-application/gigs.csv"
    custom_web_driver = CustomWebDriver(un_detectable=True, user_data_dir="/Users/ahsanilyas/Documents/FiverrSEO/chrome/1")
    
    
    # """ Step 01: Use the below code snippet to extract a list of urls for a given keywords"""
    # key_word_list = [
    #     'flutter',
    #     'cross platform',
    #     'mobile application',
    # ]
    
    # fiverr = Fiverr(
    #     driver_instance=custom_web_driver, 
    #     urls_csv_file_path=urls_csv_file_path,
    #     key_word_list=key_word_list,
    # )
    # fiverr.extract_and_save_gig_urls()
    
    # return
    
    """ Step 02: Use the code snippet below to extract all the required gig data """
    gigs_df = pd.DataFrame()
    if (os.path.exists(gigs_csv_file_path)):
        gigs_df = pd.read_csv(gigs_csv_file_path)
        
    urls_df = pd.read_csv(urls_csv_file_path) # read the csv file
    urls_df.drop_duplicates(inplace=True) # drop the duplicates
    gigs_list = [] # list to store the gigs data
    for index, row in urls_df.iterrows():
        custom_print(message=f"Processing -> {str(index)}/{str(len(urls_df))}", color=bg_colors.HL_GREEN)
        # extract the url
        url = row['url']
        # check if the url is present in the gigs_df
        if len(gigs_df) > 0 and len(gigs_df[gigs_df['url'].isin([url])]) > 0:
            custom_print("Already available")
            continue
            
        # create the gig instance
        gig = Gig(url=url)
        # set the relevant data for gig
        gig.set_gig_data(custom_web_driver=custom_web_driver)
        gigs_list.append(gig)
        Gig.save_gigs_to_csv_file(gigs=gigs_list, file_path=gigs_csv_file_path, previous_records_df=gigs_df)
        
    

if __name__ == "__main__":
    main()
    

# "https://www.fiverr.com/ultra_scrape/do-web-scraping-data-mining-any-website-in-just-few-hours?context_referrer=search_gigs_with_recommendations_row_3&source=top-bar&ref_ctx_id=a1d08c710c024716b8b7673a82139c39&pckg_id=1&pos=1&context_type=auto&funnel=a1d08c710c024716b8b7673a82139c39&seller_online=true&imp_id=0aa07925-f8e4-4b4d-b57a-017e2548568c"
# "https://www.fiverr.com/mlordjames/scrape-products-hotels-social-media-businesses-in-24hrs?context_referrer=search_gigs_with_recommendations_row_3&source=top-bar&ref_ctx_id=a1d08c710c024716b8b7673a82139c39&pckg_id=1&pos=2&context_type=auto&funnel=a1d08c710c024716b8b7673a82139c39&imp_id=114ceabe-aa07-400e-82a6-d41ec1731210",

# ""