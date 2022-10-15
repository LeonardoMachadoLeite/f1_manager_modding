import os
import sys
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BACKUP_DIR = os.getenv("BACKUP_DIR")
SAVEFILE_DIR = "{:s}/F1Manager22/Saved/SaveGames".format(os.getenv("GAME_DIR"))
HOME_DIR = os.path.abspath(os.path.curdir).replace("\src", "")

TARGET_SAVE = "save8"

SAVEFILE_PATH = "{}/{}.sav".format(SAVEFILE_DIR, TARGET_SAVE)

sys.path.append(HOME_DIR)
from savefile_packer import script as packer
# print(packer.CHNUK1_NAME)

def create_folder_if_not_exists(folder_name):
    Path("{}/{}".format(BACKUP_DIR, folder_name)).mkdir(parents=True, exist_ok=True)

create_folder_if_not_exists("backup")
create_folder_if_not_exists("save_db")

def create_save_backup():
    new_file_content = b''
    with open(SAVEFILE_PATH, 'rb') as f:
        new_file_content += f.read()
    
    timestamp = datetime.today().strftime('%Y_%m_%d_%X').replace(':', '-')
    bkp_path = r"{}\backup\bkp_{}_{}.sav".format(BACKUP_DIR, TARGET_SAVE, timestamp)
    
    with open(bkp_path, 'wb') as f:
        f.write(new_file_content)

def create_save_db():
    save_db_path = "{}\\save_db\\{}".format(BACKUP_DIR, TARGET_SAVE)
    packer.main("unpack", SAVEFILE_PATH, save_db_path)

# "{}".foormat(date.today())
# print(datetime.today().strftime('%Y_%m_%d_%X').replace(':', '-'))

create_save_backup()
create_save_db()