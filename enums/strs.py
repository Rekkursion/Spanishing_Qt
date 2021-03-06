from enum import Enum


# noinspection NonAsciiCharacters
class Strs(Enum):
    # titles of some windows/dialogs
    Main_Window_Title = ('西班牙語學習', '西班牙语学习', 'Spanishing')
    Meaning_Form_Dialog_Title_A = ('新增單字意義', '添加单词意思', 'Add the meaning')
    Meaning_Form_Dialog_Title_M = ('修改單字意義', '修改单词意思', 'Modify the meaning')
    Example_Form_Dialog_Title_A = ('新增例句', '添加例句', 'Add the example sentence')
    Example_Form_Dialog_Title_M = ('修改例句', '修改例句', 'Modify the example sentence')
    Conjugation_Form_Dialog_Title = ('編輯動詞變位', '编辑动词变位', 'Edit the verb conjugation')
    Make_Sure_For_Cancelling_Sth_Dialog_Title = ('確定要取消此動作？', '是否确定要取消此操作？', 'Make sure before doing this.')

    # some contents of message-boxes
    Make_Sure_For_Cancelling_Adding_New_Example_Sentence_Dialog_Content = (
        '確定要取消新增例句嗎？請注意系統並不會保留您所鍵入的資料。',
        '是否确定要取消添加例句？请注意系统并不会保留您所输入的数据。',
        'YOU ARE GIVING UP THE NEW EXAMPLE SENTENCE. Aware that the system will not keep anything you typed and this action cannot be undone.'
    )
    Make_Sure_For_Cancelling_Adding_New_Meaning_Dialog_Content = (
        '確定要取消新增單字意義嗎？請注意系統並不會保留您所鍵入的資料。',
        '是否确定要取消添加单词意思？请注意系统并不会保留您所输入的数据。',
        'YOU ARE GIVING UP THE NEW MEANING. Aware that the system will not keep anything you typed and this action cannot be undone.'
    )
    Make_Sure_For_Removing_Added_Example_Sentence_Dialog_Content = (
        '確定要刪除此例句嗎？此動作將無法還原。',
        '是否确定要删除此例句？此操作将无法恢复。',
        'YOU ARE DELETING THIS EXAMPLE SENTENCE. Aware that this action cannot be undone.'
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
    Voc_Adding_Page_Edit_Conjugation_Button_Text = ('編輯動詞變位', '编辑动词变位', 'Edit the verb conjugation')
    Voc_Adding_Page_Translation_Chi_Placeholder = ('在此鍵入中文意義', '在此输入中文意思', 'The meaning in Chinese goes here')
    Voc_Adding_Page_Translation_Eng_Placeholder = ('在此鍵入英文意義', '在此输入英文意思', 'The meaning in English goes here')
    Voc_Adding_Page_Select_Pos_Button_Text = ('選擇詞性', '选择词性', 'Select PoS')
    Voc_Adding_Page_New_Example_Sentence_Button_Text = ('新增例句', '添加例句', 'New example')
    Voc_Adding_Page_Example_Sentence_Placeholder = ('在此鍵入欲新增的例句', '在此输入欲添加的例句', 'The example sentence goes here')
    Voc_Adding_Page_Example_Sentence_New_Translation_Button_Text = ('新增翻譯', '添加翻译', 'New translation')
    Voc_Adding_Page_Example_Sentence_New_Translation_Placeholder = ('在此鍵入翻譯內容', '在此输入翻译文句', 'The translation goes here')
    Voc_Adding_Page_Notes_Placeholder = ('補充說明', '补充说明', 'Notes')

    # the word-variabilities
    Gender_Variability = ('性', '性', 'Gender')
    Number_Variability = ('數', '数', 'Number')
    Word_Variability_General = ('一般', '一般', 'General')
    Word_Variability_Special = ('特殊', '特殊', 'Special')
    Word_Variability_Invariant = ('不變', '不变', 'Invariant')
    Masculine_Singular_Placeholder = ('陽性單數形', '阳性单数形', 'Masculine & singular')
    Feminine_Singular_Placeholder = ('陰性單數形', '阴性单数形', 'Feminine & singular')
    Masculine_Plural_Placeholder = ('陽性複數形', '阳性复数形', 'Masculine & plural')
    Feminine_Plural_Placeholder = ('陰性複數形', '阴性复数形', 'Feminine & plural')

    # something related to the verb conjugation
    Regular_Verb = ('規則動詞', '规则动词', 'Regular verb')
    Irregular_Verb = ('不規則動詞', '不规则动词', 'Irregular verb')
    Is_Stem_Changing_Verb = ('字根變化', '字根变化', 'Stem-changing')
    Has_Special_Past_Particle = ('特殊過去分詞', '特殊过去分词', 'Special past particle')
    Has_Special_Yo_Form = ('特殊 Yo 型', '特殊 Yo 型', 'Special yo-form')
    Has_Special_Preterite_Stem = ('特殊過去時 (preterite) 字根', '特殊过去时（preterite）字根', 'Special stem of preterite tense')
    Has_Special_Future_Stem = ('特殊未來時/條件時字根', '特殊未来时/条件时字根', 'Special stem of future/conditional tense')
    Has_Special_Present_Subjunctive_Stem = ('特殊現在虛擬式字根', '特殊现在虚拟式字根', 'Special stem of present subjunctive')
    Has_Special_Tú_Form_Affirmative_Imperative = ('特殊肯定命令式的 Tú 型', '特殊肯定命令式的 Tú 型', 'Special tú-form of affirmative imperative')
    Special_Stem_Placeholder = ('只需鍵入字根', '只需输入字根', 'Stem only')

    # general usages
    Chinese = ('中文', '中文', 'Chinese')
    English = ('英文', '英文', 'English')
    Cancel = ('取消', '取消', 'Cancel')
    Submit = ('送出', '提交', 'Submit')
    Confirm = ('確定', '确定', 'Confirm')
    Yes = ('是', '是', 'Yes')
    No = ('不', '不', 'No')
    Remove = ('刪除', '删除', 'Remove')
    Modify = ('修改', '修改', 'Modify')
    Move_Up = ('上移', '上移', 'Move up')
    Move_Down = ('下移', '下移', 'Move down')
    Not_Appears_Next_Time = ('下次不要再提醒我', '下次不再显示此对话框', 'Don\'t show this next time')

    # something pertains to the preferences-page
    Preferences_Page_Lang = ('介面語言', '语言界面', 'Interface language')

    # all part-of-speeches
    MASCULINE = ('陽性名詞', '阳性名词', 'Masculine')
    FEMININE = ('陰性名詞', '阴性名词', 'Feminine')
    PLURAL_MASCULINE = ('陽性複數名詞', '阳性复数名词', 'Plural Masculine')
    PLURAL_FEMININE = ('陰性複數名詞', '阴性复数名词', 'Plural Feminine')
    MASCULINE_OR_FEMININE = ('陽性/陰性名詞', '阳性/阴性名词', 'Masculine or Feminine')
    PRONOUN = ('代名詞', '代词', 'Pronoun')
    PROPER_NOUN = ('專有名詞', '专有名词', 'Proper Noun')
    VERB = ('動詞', '动词', 'Verb')
    REFLEXIVE_VERB = ('反身動詞', '反身动词/自复动词', 'Reflexive Verb')
    TRANSITIVE_VERB = ('及物動詞', '及物动词', 'Transitive Verb')
    INTRANSITIVE_VERB = ('不及物動詞', '不及物动词', 'Intransitive Verb')
    ADJECTIVE = ('形容詞', '形容词', 'Adjective')
    ADVERB = ('副詞', '副词', 'Adverb')
    PHRASE = ('片語', '短语', 'Phrase')
    CONJUNCTION = ('連接詞', '连词', 'Conjunction')
    INTERJECTION = ('感嘆詞', '叹词', 'Interjection')
    PREPOSITION = ('介係詞/前置詞', '介词/前置词', 'Preposition')
    DEFINITE_ARTICLE = ('定冠詞', '定冠词', 'Definite Article')
    INDEFINITE_ARTICLE = ('不定冠詞', '不定冠词', 'Indefinite Article')
