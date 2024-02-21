from utils import console_multiple_select


selection_menu = console_multiple_select(
        options=[
            "Fech data from facebook",
            "Fetch data from instagram",
            "Generate FB analytics report",
            "Generate Instagram analytics report",
        ]
    )
selections = list(selection_menu['chosen_menu_entries'])
print(selections)