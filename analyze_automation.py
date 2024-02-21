from utils import custom_print, bg_colors
from analyze.analyze_automation_settings import AnalyzeAutomationSettings
    
def main():
    custom_print("Running Script -> Analayze Automation", bg_colors.OKCYAN)
    
    analyze_automation_settings = AnalyzeAutomationSettings(
       root_data_folder_path="/Users/ahsanilyas/Documents/FiverrSEO/Data" 
    )
    
    print(analyze_automation_settings.selected_analytic_types)


if __name__ == "__main__":
    main()