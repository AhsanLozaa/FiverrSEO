import os
from dataclasses import dataclass, field
import pandas as pd
from enum import Enum

from utils import custom_print, get_input_from_user, console_multiple_select

from analyze.related_tags import analyze_related_tags
from analyze.information_type import analyze_information_types

class AnalyticType(Enum):
    RELATED_TAGS = "Related Tags"
    INFORMATION_TYPES = "Information Types"

@dataclass
class AnalyzeAutomationSettings:
    """
    Class for setting up and executing automation settings for Fiverr gig analysis.
    """

    
    root_data_folder_path: str
    data_directories: list[str] = field(default_factory=list)
    selected_data_directory: str = field(default="")
    urls_file_path: str = field(default="")
    gigs_file_path: str = field(default="")
    urls_df: pd.DataFrame = field(default_factory=pd.DataFrame)
    gigs_df: pd.DataFrame = field(default_factory=pd.DataFrame)
    selected_analytic_types: list[AnalyticType] = field(default_factory=list)
    filter_by_reviews_count_value: int = field(default=0)
    
    def set_data_directories(self):
        """
        Set the list of data directories available in the root data folder.
        """
        contents = os.listdir(self.root_data_folder_path)
        self.data_directories = [item for item in contents if "." not in item]
    
    def show_niche_selection_propmt(self):
        """
        Show prompt to select a niche data directory from the available data directories.
        """
        to_select_data_dict = {}
        for folder in self.data_directories:
            to_select_data_dict[folder] = folder
        selected_data_directory = get_input_from_user(to_select_data_dict=to_select_data_dict, message="Please select a niche")
        self.selected_data_directory = selected_data_directory
    
    def show_analytic_types_selection_prompt(self):
        """
        Show prompt to select analytic types to execute.
        """
        options = [x.value for x in list(AnalyticType)]
        selections = console_multiple_select(options=options)
        types_list = list(selections['chosen_menu_entries'])
        self.selected_analytic_types = [AnalyticType[type_str.replace(" ", "_").upper()] for type_str in types_list]

    
    def show_review_count_prompt(self):
        """
        Show prompt to get the reviews count to filter the data frame
        """
        self.filter_by_reviews_count_value = int(input("Enter reviews count: "))
        
        
    def set_urls_file_path(self):
        """
        Set the file path for the URLs file based on the selected data directory.
        """
        urls_file_path = os.path.join(self.root_data_folder_path, self.selected_data_directory, "urls.csv")
        if os.path.exists(urls_file_path):
            self.urls_file_path = urls_file_path
        else:
            print("Not set urls file path")
    
    def set_gigs_file_path(self):
        """
        Set the file path for the gigs file based on the selected data directory.
        """
        gigs_file_path = os.path.join(self.root_data_folder_path, self.selected_data_directory, "gigs.csv")
        if os.path.exists(gigs_file_path):
            self.gigs_file_path = gigs_file_path
        else:
            print("Not set gigs file path")
            
    def set_urls_df(self) -> None:
        """
        Read the URLs CSV file and set the URLs data frame.
        """
        if os.path.exists(self.urls_file_path):
            self.urls_df = pd.read_csv(self.urls_file_path)
    
    def set_gigs_df(self) -> None:
        """
        Read the gigs CSV file and set the gigs data frame.
        """
        if os.path.exists(self.gigs_file_path):
            if self.filter_by_reviews_count_value > 0:
                gigs_df = pd.read_csv(self.gigs_file_path)
                self.gigs_df = gigs_df[gigs_df['reviews_count'] > self.filter_by_reviews_count_value]
            else:
                self.gigs_df = pd.read_csv(self.gigs_file_path)
            
    def execute_analyze(self):
        """
        Execute the selected analytic types.
        """
        if AnalyticType.RELATED_TAGS in self.selected_analytic_types:
            if len(self.gigs_df) > 0:
                analyze_related_tags(gigs_data_frame=self.gigs_df)
            else:
                custom_print("Data frame is empty")
        
        if AnalyticType.INFORMATION_TYPES in self.selected_analytic_types:
            if len(self.gigs_df) > 0:
                analyze_information_types(gigs_data_frame=self.gigs_df)
            else:
                custom_print("Data frame is empty")
            
    def __post_init__(self):
        """
        Post initialization method to set up the analysis settings.
        """
        self.set_data_directories()
        self.show_niche_selection_propmt()
        self.show_analytic_types_selection_prompt()
        self.show_review_count_prompt()
        self.set_urls_file_path()
        self.set_gigs_file_path()
        self.set_urls_df()
        self.set_gigs_df()
        self.execute_analyze()
        