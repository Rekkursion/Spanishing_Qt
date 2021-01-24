from enum import Enum

from enums.pref_key import PrefKey
from managers.pref_manager import PrefManager


class Strs(Enum):
    # titles of some windows/dialogs
    Main_Window_Title = ('西班牙語學習', '西班牙语学习', 'Spanishing')

    # items of the menu-list
    Menu_List_Item_Voc_List = ('單字列表', '单词列表', 'Vocabulary List')
    Menu_List_Item_Add_Voc = ('新增單字', '添加单词', 'Add Vocabulary')
    Menu_List_Item_Verb_Conjugations = ('動詞變位', '动词变位', 'Verb Conjugations')
    Menu_List_Item_Practices = ('練習挑戰', '练习挑战', 'Practices')
    Menu_List_Item_Preferences = ('個人設定', '个人设置', 'Preferences')

    # for the convenience (no need to write Strs.XXX.value, Strs.XXX is enough)
    def __get__(self, instance, owner):
        return self.value[PrefManager.get_pref(PrefKey.LANG)]
