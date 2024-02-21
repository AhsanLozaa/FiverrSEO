import random
import time
from tqdm import tqdm
import glob
from contextlib import suppress
import pandas as pd
import inquirer

class bg_colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    YELLOW = '\033[33m'
    MAGENTA_BOLD_BRIGHT = "\033[1;95m"
    RED_BOLD_BRIGHT = "\033[1;91m"
    RED = '\033[0;31m'
    FAIL = '\033[91m'
    HL_RED = '\33[101m'
    HL_GREEN = '\33[102m'


def custom_print(message, color= bg_colors.FAIL, is_next_line=True, is_allign_center=False, terminal_columns=""):
    # METHOD - Custom print method
    # params message
    # params color
    if (is_allign_center):
        print('{}{}'.format(color, bg_colors.BOLD), end='')
        print(message.center(terminal_columns))
        print('{}'.format(bg_colors.ENDC), end='')
        return
    elif (not (is_next_line)):  # The curesor will be moved to the next line 
        print('{}{}'.format(color, bg_colors.BOLD), end='')
        print(message, end='')
        print('{}'.format(bg_colors.ENDC), end='')
    else:
        print('{}{}'.format(color, bg_colors.BOLD), end='')
        print(message, end='')
        print('{}'.format(bg_colors.ENDC))
        

def send_keys_delay_random(controller, keys, min_delay=0.10, max_delay=0.20):
    for key in keys:
        controller.send_keys(key)
        time.sleep(random.uniform(min_delay, max_delay))
        

def custom_sleep_func_3(message='', time_in_seconds=1, progress_bar_color='green'):

    pbar = tqdm(range(time_in_seconds), colour=progress_bar_color)
    wait_time_count_down = time_in_seconds
    for i in pbar:
        time.sleep(1)
        wait_time_count_down = wait_time_count_down-1
        if (message != ''):
            pbar.set_description(f"{message} - Back online in {wait_time_count_down} seconds")
        else:
            pbar.set_description("System back online in %s seconds" % (wait_time_count_down))

    print('\n')
    

def get_specific_files_from_specific_folder(folderPath, fileType):
    # METHOD Function to get all the files(only a specific file type) inside a specific folder
    # params folderPath
    # params fileType

    allAvailableFilesList = glob.glob1(folderPath, fileType)


    if len(allAvailableFilesList) <= 0:
        allAvailableFilesList = glob.glob1(folderPath, fileType.upper())

    if (len(allAvailableFilesList) <= 0):
        allAvailableFilesList = glob.glob('{}/*{}'.format(
            folderPath, fileType))


    return allAvailableFilesList


def convert_multiple_csv_files_to_one_dataframe(files_list, header=0):
    # METHOD - Function to convert a list of csv files (including the path of the file) to a single dataframe
    # param files_list => list of file names (the file name must include the full path of the location of it)
    data_frame = pd.DataFrame()
    data_frame_list = []
    try:
        if (len(files_list) > 0):
            for f in files_list:
                data_frame = pd.DataFrame()
                with suppress(ValueError, TypeError, TypeError): data_frame = pd.read_csv(f, header=header)
                if (len(data_frame) > 0):
                    data_frame_list.append(data_frame)

                # data_frame = pd.read_csv(f, header=header)
                # data_frame = pd.concat([pd.read_csv(f, header=header) for f in files_list])
            
            if (len(data_frame_list) > 0):
                df = pd.concat(data_frame_list)
                return df
    except Exception as e:
        print(e)
        print("Failed to convert a list to csv files to one dataframe...")
    
    

def get_input_from_user(to_select_data_dict: dict, message: str):

    choices = to_select_data_dict.keys()

    questions = [
        inquirer.List('mode',
        message=message,
        choices=choices,),
    ]

    mode = inquirer.prompt(questions)

    user_selected_item = mode["mode"]

    user_selected_acccounts_to_process = user_selected_item

    return to_select_data_dict[user_selected_acccounts_to_process]
