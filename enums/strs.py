from enum import Enum


class Strs(Enum):
    # titles of some windows/dialogs
    Main_Window_Title = ('西班牙語學習', '西班牙语学习', 'Spanishing')
    Meaning_Form_Dialog_Title = ('新增/修改單字意義', '添加/修改单词意思', 'Add/Modify the meaning')
    Example_Form_Dialog_Title = ('新增/修改例句', '添加/修改例句', 'Add/Modify the example sentence')
    Make_Sure_For_Cancelling_Sth_Dialog_Title = ('確定要取消此動作？', '是否确定要取消此操作？', 'Make sure before cancelling.')

    # some contents of message-boxes
    Make_Sure_For_Cancelling_Adding_New_Example_Sentence_Dialog_Content = (
        '確定要取消新增例句嗎？請注意系統並不會保留您所鍵入的資料。',
        '是否确定要取消添加例句？请注意系统并不会保留您所输入的数据。',
        'YOU ARE GIVING UP THE EXAMPLE SENTENCE. Please aware that the system will not keep anything you typed and this action cannot be undone.'
    )
    Make_Sure_For_Removing_Added_Example_Sentence_Dialog_Content = (
        '確定要刪除此例句嗎？此動作將無法還原。',
        '是否确定要删除此例句？此操作将无法恢复。',
        'YOU ARE DELETING THIS EXAMPLE SENTENCE. Please aware that this action cannot be undone.'
    )

    # items of the menu-list
    Menu_List_Item_Voc_List = ('單字列表', '单词列表', 'Vocabulary list')
    Menu_List_Item_Add_Voc = ('新增單字', '添加单词', 'Add vocabulary')
    Menu_List_Item_Verb_Conjugations = ('動詞變位', '动词变位', 'Verb conjugations')
    Menu_List_Item_Practices = ('練習挑戰', '练习挑战', 'Practices')
    Menu_List_Item_Preferences = ('個人設定', '个人设置', 'Preferences')

    # something pertains to the voc-adding-page
    Voc_Adding_Page_Word = ('單字', '单词', 'Word')
    Voc_Adding_Page_Word_Placeholder = ('欲新增的單字', '欲添加的单词', 'The word goes here')
    Voc_Adding_Page_New_Meaning_Button_Text = ('新增意義', '添加意思', 'New meaning')
    Voc_Adding_Page_Translation_Chi_Placeholder = ('在此鍵入中文意義', '在此输入中文意思', 'The meaning in Chinese goes here')
    Voc_Adding_Page_Translation_Eng_Placeholder = ('在此鍵入英文意義', '在此输入英文意思', 'The meaning in English goes here')
    Voc_Adding_Page_Select_Pos_Button_Text = ('選擇詞性', '选择词性', 'Select PoS')
    Voc_Adding_Page_New_Example_Sentence_Button_Text = ('新增例句', '添加例句', 'New example')
    Voc_Adding_Page_Example_Sentence_Placeholder = ('在此鍵入欲新增的例句', '在此输入欲添加的例句', 'The example sentence goes here')
    Voc_Adding_Page_Example_Sentence_New_Translation_Button_Text = ('新增翻譯', '添加翻译', 'New translation')
    Voc_Adding_Page_Example_Sentence_New_Translation_Placeholder = ('在此鍵入翻譯內容', '在此输入翻译文句', 'The translation goes here')
    Voc_Adding_Page_Notes_Placeholder = ('補充說明', '补充说明', 'Notes')

    # general usages
    Chinese = ('中文', '中文', 'Chinese')
    English = ('英文', '英文', 'English')
    Cancel = ('取消', '取消', 'Cancel')
    Submit = ('送出', '提交', 'Submit')
    Confirm = ('確定', '确定', 'Confirm')
    Yes = ('是', '是', 'Yes')
    No = ('不', '不', 'No')
    Remove = ('刪除', '删除', 'Remove')
    View = ('查看', '查看', 'View')
    Move_Up = ('上移', '上移', 'Move up')
    Move_Down = ('下移', '下移', 'Move down')
    Not_Appears_Next_Time = ('下次不要再提醒我', '下次不再显示此对话框', 'Don\'t show this next time')

    # something pertains to the preferences-page
    Preferences_Page_Lang = ('介面語言', '语言界面', 'Interface language')
