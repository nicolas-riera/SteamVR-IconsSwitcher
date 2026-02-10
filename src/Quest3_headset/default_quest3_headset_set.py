import os
import shutil

from src.get_SteamVR_path import real_case_path, find_steam_path
from src.clear import clear

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SOURCE = os.path.join(BASE_DIR, "..", "..", "assets", "Quest 3 headset", "default", "icons")

DESTINATION = os.path.join(os.path.join(real_case_path(find_steam_path()), "steamapps", "common", "SteamVR", "drivers", "oculus", "resources", "icons"))

CUSTOM_SENSOR = os.path.join(os.path.join(real_case_path(find_steam_path()), "steamapps", "common", "SteamVR", "drivers", "oculus", "resources", "icons", "custom_headset_sensor"))

def default_quest3_headset_set():

    shutil.copytree(SOURCE, DESTINATION, dirs_exist_ok=True)

    if os.path.exists(CUSTOM_SENSOR):
        os.remove(str(CUSTOM_SENSOR))