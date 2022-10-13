import os
import sys
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BACKUP_DIR = os.getenv("BACKUP_DIR")
GAME_DIR = os.getenv("GAME_DIR")
SAVEFILE_DIR = "{:s}/F1Manager22/Saved/SaveGames".format(GAME_DIR)
HOME_DIR = os.path.abspath(os.path.curdir).replace("\src", "")

sys.path.append(HOME_DIR)
from savefile_packer import script as packer
# print(packer.CHNUK1_NAME)

def create_folder_if_not_exists(folder_name):
    Path("{}/{}".format(BACKUP_DIR, folder_name)).mkdir(parents=True, exist_ok=True)

create_folder_if_not_exists("backup")
create_folder_if_not_exists("save_db")