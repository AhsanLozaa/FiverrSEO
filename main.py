import pandas as pd
import os
from random import randint
from scraper.custom_web_driver import CustomWebDriver
from scraper.fiverr import Fiverr
from scraper.gig import Gig
from utils import custom_print, bg_colors, console_multiple_select, custom_sleep_func_3

def execute_scrape_urls(custom_web_driver: CustomWebDriver, urls_csv_file_path: str, key_word_list: list) -> None:
    """ Step 01: Use the below code snippet to extract a list of urls for a given keywords"""
    # key_word_list = [
    #     'flutter',
    #     'cross platform',
    #     'mobile application',
    # ]
    
    fiverr = Fiverr(
        driver_instance=custom_web_driver, 
        urls_csv_file_path=urls_csv_file_path,
        key_word_list=key_word_list,
    )
    fiverr.extract_and_save_gig_urls()
    

def execute_scrape_gigs(custom_web_driver: CustomWebDriver, urls_csv_file_path: str, gigs_csv_file_path: str) -> None:
    """ Step 02: Use the code snippet below to extract all the required gig data """
    gigs_df = pd.DataFrame()
    if (os.path.exists(gigs_csv_file_path)):
        gigs_df = pd.read_csv(gigs_csv_file_path)
        
    urls_df = pd.read_csv(urls_csv_file_path) # read the csv file
    urls_df.drop_duplicates(inplace=True) # drop the duplicates
    urls_df = urls_df[urls_df["reviews_count"] > 0]
    gigs_list = [] # list to store the gigs data
    count = 0
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
        count += 1
        if count >= 5:
            custom_sleep_func_3(message=f"Idle after scraping {count} gigs", time_in_seconds=randint(240, 300))
            count = 0
        

def main():
    
    niche = str(input("Enter the niche: "))
    
    if not niche or niche == "":
        custom_print(message="Invalid niche", color=bg_colors.HL_RED)
        return
    
    
    base_data_dir_path = "/Users/ahsanilyas/Documents/FiverrSEO/Data"
    niche_folder_path = os.path.join(base_data_dir_path, niche)
    os.makedirs(niche_folder_path, exist_ok=True)
    urls_csv_file_path = os.path.join(niche_folder_path, "urls.csv")
    gigs_csv_file_path = os.path.join(niche_folder_path, "gigs.csv")
    # urls_csv_file_path = "/Users/ahsanilyas/Documents/FiverrSEO/Data/mobile-application/urls.csv"
    # gigs_csv_file_path = "/Users/ahsanilyas/Documents/FiverrSEO/Data/mobile-application/gigs.csv"
    
    
    selection_menu = console_multiple_select(
        options=[
            "Scrape urls by keywords list",
            "Scrape gigs by urls.csv file"
        ]
    )
    selections_list = list(selection_menu['chosen_menu_entries'])

    if 'Scrape urls by keywords list' in selections_list or 'Scrape gigs by urls.csv file' in selections_list:
        custom_web_driver = CustomWebDriver(un_detectable=True, user_data_dir="/Users/ahsanilyas/Documents/FiverrSEO/chrome/fathunus")
        # custom_web_driver = None
        
        if 'Scrape urls by keywords list' in selections_list:
            # key_word_list = input("Please enter keywords (comma seperated)")
            # key_word_list = ["fiverr seo", "fiverr gig promotion", "fiverr gig image", "fiverr gig thumbnail", "fiverr gig description", "fiverr gig video", "gig seo", "gig description", "fiverr gig seo"]
            key_word_list = ["python csv", "data cleaning", "data automation", "python excel", "python pdf", "python file handling", "python large file handling", "csv file processing", "numpy", "pandas", "python json"]
            execute_scrape_urls(custom_web_driver=custom_web_driver, urls_csv_file_path=urls_csv_file_path, key_word_list=key_word_list)
        
        if 'Scrape gigs by urls.csv file' in selections_list:
            execute_scrape_gigs(custom_web_driver=custom_web_driver, urls_csv_file_path=urls_csv_file_path, gigs_csv_file_path=gigs_csv_file_path)


if __name__ == "__main__":
    main()