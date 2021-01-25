from enum import Enum


class Strs(Enum):
    # titles of some windows/dialogs
    Main_Window_Title = ('西班牙語學習', '西班牙语学习', 'Spanishing')
    Meaning_Form_Dialog_Title = ('新增/修改單字意義', '添加/修改单词意思', 'Add/Update the meaning')

    # items of the menu-list
    Menu_List_Item_Voc_List = ('單字列表', '单词列表', 'Vocabulary list')
    Menu_List_Item_Add_Voc = ('新增單字', '添加单词', 'Add vocabulary')
    Menu_List_Item_Verb_Conjugations = ('動詞變位', '动词变位', 'Verb conjugations')
    Menu_List_Item_Practices = ('練習挑戰', '练习挑战', 'Practices')
    Menu_List_Item_Preferences = ('個人設定', '个人设置', 'Preferences')

    # something pertains to the voc-adding-page
    Voc_Adding_Page_Word = ('單字', '单词', 'Word')
    Voc_Adding_Page_Word_Placeholder = ('欲新增的單字', '欲添加的单词', 'Type the word here')
    Voc_Adding_Page_New_Meaning_Button_Text = ('新增意義', '添加意思', 'Add a new meaning')
    Voc_Adding_Page_Translation_Chi = ('意義（中文）', '意思（中文）', 'Meaning (Chinese)')
    Voc_Adding_Page_Translation_Chi_Placeholder = ('在此輸入中文意義', '在此输入中文意思', 'Type the meaning in Chinese here')
    Voc_Adding_Page_Translation_Eng = ('意義（英文）', '意思（英文）', 'Meaning (English)')
    Voc_Adding_Page_Translation_Eng_Placeholder = ('在此輸入英文意義', '在此输入英文意思', 'Type the meaning in English here')
    Voc_Adding_Page_Select_Pos_Button_Text = ('選擇詞性', '选择词性', 'Select PoS')
    Voc_Adding_Page_New_Example_Sentence_Button_Text = ('新增例句', '添加例句', 'Add a new example sentence')
    Voc_Adding_Page_Notes_Placeholder = ('補充說明', '补充说明', 'Notes')

    # misc
    Cancel = ('取消', '取消', 'Cancel')
    Submit = ('送出', '提交', 'Submit')

    # something pertains to the preferences-page
    Preferences_Page_Lang = ('介面語言', '语言界面', 'Interface language')
