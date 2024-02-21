# https://form.run/@admin-IxAwIcoizyxVgV2IzW3m
import pandas as pd
from dataclasses import dataclass, field

from utils import custom_print, bg_colors, custom_sleep_func_3
from scraper.custom_web_driver import CustomWebDriver

@dataclass
class Form:
    url: str
    inquiry_item: str
    company_name: str
    name: str # required
    furigana: str # required
    postal_code: str
    region: str
    municipality: str
    block_number: str
    building: str
    phone_number: str # required
    email_address: str # required
    inquiry: str # required
    
    def fill_form(self, custom_web_driver: CustomWebDriver) -> None:
        """ Function derived to fill the form """
        custom_print("Filling form", bg_colors.OKBLUE)
        custom_web_driver.find_element_by_css_selector(css_selector=f"option[value='{self.inquiry_item}']").click()
        custom_web_driver.find_element_by_id(element_id="_field_5").send_keys(self.company_name)
        custom_web_driver.find_element_by_id(element_id="_field_3").send_keys(self.name)
        custom_web_driver.find_element_by_id(element_id="_field_4").send_keys(self.furigana)
        custom_web_driver.find_element_by_id(element_id="_field_14_postal_code").send_keys(self.postal_code)
        custom_web_driver.find_element_by_css_selector(css_selector=f"option[value='{self.region}']").click()
        custom_web_driver.find_element_by_id(element_id="_field_14_municipality").send_keys(self.municipality)
        
        custom_web_driver.find_element_by_id(element_id="_field_14_block_number").send_keys(self.block_number)
        custom_web_driver.find_element_by_id(element_id="_field_14_building").send_keys(self.building)
        
        custom_web_driver.find_element_by_id(element_id="_field_7").send_keys(self.phone_number)
        custom_web_driver.find_element_by_id(element_id="_field_1").send_keys(self.email_address)
        custom_web_driver.find_element_by_id(element_id="_field_18").send_keys(self.inquiry)
    
    def submit_form(self, custom_web_driver: CustomWebDriver) -> None:
        """ Fucntion derived to submit the form """
        custom_print("Submit form", bg_colors.OKBLUE)
        custom_web_driver.find_element_by_tag_name(tag_name="button").click()
        custom_print("Form submission successful", bg_colors.OKGREEN)
        
        
    def read_csv_file_to_process(csv_file_path: str) -> pd.DataFrame:
        """ Function derived to read and return a csv file as a dataframe """
        data_frame = pd.read_csv(csv_file_path)
        return data_frame

    def fill_form_from_csv_file(self):
        data_frame = self.read_csv_file_to_process(csv_file_path="/Users/ahsanilyas/Documents/FiverrSEO/input.csv")
        print(data_frame)
    


def main():
    print()
    
    custom_sleep_func_3(message="Setting up the environment", time_in_seconds=20)
    
    data_frame = pd.read_csv("/Users/ahsanilyas/Documents/FiverrSEO/input.csv")
    custom_web_driver = CustomWebDriver(headless=False, allow_proxy=False)
    for index, row in data_frame.iterrows():
        custom_web_driver.navigate(row["url"], idle=1)
        form = Form(**row.to_dict())
        form.fill_form(custom_web_driver=custom_web_driver)
        form.submit_form(custom_web_driver=custom_web_driver)
        custom_sleep_func_3(message="Idle after submitting form", time_in_seconds=3)

if __name__ == "__main__":
    main()
    

