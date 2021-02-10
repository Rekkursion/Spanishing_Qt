import json

from enums.pref_key import PrefKey
from utils import configuration as cfg


class PrefManager:
    # the dictionary of preferences
    __pref_dict = None

    # set a single preference
    @staticmethod
    def set_pref(key: PrefKey, value):
        PrefManager.__pref_dict[key.value] = value
        PrefManager.__update_json()

    # get a single preference
    @staticmethod
    def get_pref(key: PrefKey):
        return PrefManager.__pref_dict.get(key.value)

    # initially load the preferences from the json-file
    @staticmethod
    def init_pref():
        with open(cfg.pref_json_file_path) as jf:
            PrefManager.__pref_dict = json.load(jf)

    # update the json-file of preferences
    @staticmethod
    def __update_json():
        with open(cfg.pref_json_file_path, 'w') as jf:
            json.dump(PrefManager.__pref_dict, jf, indent=2)
