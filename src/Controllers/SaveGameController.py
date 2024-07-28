import os
import sys
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

GAME_SAVE_DIR = os.getenv("GAME_SAVE_DIR")
MODDED_SAVE_DIR = os.getenv("MODDED_SAVE_DIR")
HOME_DIR = os.getenv("SRC_DIR")

sys.path.append(HOME_DIR)
from Utils.SaveFilePacker import SaveFilePacker as packer

def create_folder_if_not_exists(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def create_save_backup(savefile_path, target_save, backup_path):
    new_file_content = b''

    with open(savefile_path, 'rb') as f:
        new_file_content += f.read()
    
    timestamp = datetime.today().strftime('%Y_%m_%d_%X').replace(':', '-')
    bkp_path = r"{}\bkp_{}_{}.sav".format(backup_path, target_save, timestamp)
    
    with open(bkp_path, 'wb') as f:
        f.write(new_file_content)

def create_save_db(savefile_path, save_db_path):
    packer.main("unpack", savefile_path, save_db_path)

def main(target_save, target_game):
    SAVEFILE_PATH = f"{GAME_SAVE_DIR}\\{target_game}\\Saved\\SaveGames\\{target_save}.sav"
    GAME_MODDED_SAVES_DIR = f"{MODDED_SAVE_DIR}\\{target_game}"
    MODDED_SAVEFILE_PATH = f"{GAME_MODDED_SAVES_DIR}\\save_db\\{target_save}"
    BACKUP_DIR = f"{GAME_MODDED_SAVES_DIR}\\backup"
    MODDED_SAVES_DIR = f"{GAME_MODDED_SAVES_DIR}\\save_db"
    
    create_folder_if_not_exists(BACKUP_DIR)
    create_folder_if_not_exists(MODDED_SAVES_DIR)
    create_save_backup(SAVEFILE_PATH, target_save, BACKUP_DIR)
    create_save_db(SAVEFILE_PATH, MODDED_SAVEFILE_PATH)

class SaveGameController(object):
    
    def __init__(self, target_game, target_save):
        self.target_game = target_game
        self.target_save = target_save
        self.savefile_path = f"{GAME_SAVE_DIR}\\{target_game}\\Saved\\SaveGames\\{target_save}.sav"
        self.game_modded_saves_dir = f"{MODDED_SAVE_DIR}\\{target_game}"
        self.modded_savefile_path = f"{self.game_modded_saves_dir}\\save_db\\{target_save}"
        self.backup_dir = f"{self.game_modded_saves_dir}\\backup"
        self.modded_saves_dir = f"{self.game_modded_saves_dir}\\save_db"
    
    def create_save_backup(self):
        new_file_content = b''

        with open(self.savefile_path, 'rb') as f:
            new_file_content += f.read()
        
        timestamp = datetime.today().strftime('%Y_%m_%d_%X').replace(':', '-')
        bkp_path = r"{}\bkp_{}_{}.sav".format(self.backup_dir, self.target_save, timestamp)
        
        with open(bkp_path, 'wb') as f:
            f.write(new_file_content)

    def create_save_db(self):
        packer.process_unpack(self.savefile_path, self.modded_savefile_path)
    
    def unpack(self):
        create_folder_if_not_exists(self.backup_dir)
        create_folder_if_not_exists(self.modded_saves_dir)
        self.create_save_backup()
        self.create_save_db()
    
    def repack(self):
        packer.process_repack(input_dir=self.modded_savefile_path, result_file=self.savefile_path)
