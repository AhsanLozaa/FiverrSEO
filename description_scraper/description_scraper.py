import os
from scraper_old.custom_web_driver import CustomWebDriver
from utils import get_specific_files_from_specific_folder, convert_multiple_csv_files_to_one_dataframe
import pandas as pd

from scraper_old.gig import Gig
from utils import custom_sleep_func_3


def execute_description_scraper():
    
    if (os.path.exists("final_data.csv")):
        filtered_data_frame = pd.read_csv("final_data.csv")
    else:
        # combine all the csv files together
        csv_files_list = get_specific_files_from_specific_folder("./Data", ".csv")
        data_frame = convert_multiple_csv_files_to_one_dataframe(files_list=csv_files_list)
        filtered_data_frame = data_frame[data_frame['ratings_count'] > 300].drop_duplicates()
    
    # 
    gigs = [Gig(**kwargs) for kwargs in filtered_data_frame.to_dict(orient='records')]
    
    # 
    custom_web_driver = CustomWebDriver(headless=False, allow_proxy=False, port="9222")
    
    for gig in gigs:
        if (str(gig.description).lower() == 'nan' or gig.description == ""):
            try:
                gig.set_description(custom_web_driver=custom_web_driver)
                gigs_dict_list = [g.__dict__ for g in gigs]
                df = pd.DataFrame(gigs_dict_list)
                df.to_csv(f"final_data.csv", index=False)
                custom_sleep_func_3(message="Idle after scraping item", time_in_seconds=5)
            except Exception as e:
                continue
        else:
            print(gig.rating_score)
            