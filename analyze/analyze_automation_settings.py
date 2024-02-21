import os
from dataclasses import dataclass, field
import pandas as pd

from utils import custom_print, bg_colors, get_input_from_user, console_multiple_select

from analyze.related_tags import analyze_related_tags

@dataclass
class AnalyzeAutomationSettings:
    
    root_data_folder_path: str
    data_directories: list[str] = field(default_factory=list)
    selected_data_directory: str = field(default="")
    urls_file_path: str = field(default="")
    gigs_file_path: str = field(default="")
    urls_df: pd.DataFrame = field(default_factory=pd.DataFrame)
    gigs_df: pd.DataFrame = field(default_factory=pd.DataFrame)
    
    selected_analytic_types: list[str] = field(default_factory=list)
    
    def set_data_directories(self):
        contents = os.listdir(self.root_data_folder_path)
        self.data_directories = [item for item in contents if "." not in item]
    
    def show_niche_selection_propmt(self):
        to_select_data_dict = {}
        for folder in self.data_directories:
            to_select_data_dict[folder] = folder
        selected_data_directory = get_input_from_user(to_select_data_dict=to_select_data_dict, message="Please select a niche")
        self.selected_data_directory = selected_data_directory
    
    def show_process_selection_prompt(self):
        selections = console_multiple_select(options=["Related Tags"])
        self.selected_analytic_types = list(selections['chosen_menu_entries'])
        
        
    def set_urls_file_path(self):
        
        urls_file_path = os.path.join(self.root_data_folder_path, self.selected_data_directory, "urls.csv")
        if os.path.exists(urls_file_path):
            self.urls_file_path = urls_file_path
        else:
            print("Not set urls file path")
    
    def set_gigs_file_path(self):
        
        gigs_file_path = os.path.join(self.root_data_folder_path, self.selected_data_directory, "gigs.csv")
        if os.path.exists(gigs_file_path):
            self.gigs_file_path = gigs_file_path
        else:
            print("Not set gigs file path")
            
    def set_urls_df(self) -> None:
        if os.path.exists(self.urls_file_path):
            self.urls_df = pd.read_csv(self.urls_file_path)
    
    def set_gigs_df(self) -> None:
        if os.path.exists(self.gigs_file_path):
            self.gigs_df = pd.read_csv(self.gigs_file_path)
            
    def execute_analyze(self):
        if "Related Tags" in self.selected_analytic_types:
            analyze_related_tags(gigs_data_frame=self.gigs_df)
            
    def __post_init__(self):
        self.set_data_directories()
        self.show_niche_selection_propmt()
        self.show_process_selection_prompt()
        self.set_urls_file_path()
        self.set_gigs_file_path()
        self.set_urls_df()
        self.set_gigs_df()
        self.execute_analyze()
        