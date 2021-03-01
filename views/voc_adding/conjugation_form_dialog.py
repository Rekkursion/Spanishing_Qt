import copy

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup

from enums.add_modify_dialog_mode import AddModifyDialogMode
from enums.stem_changing_type import StemChangingType
from enums.strs import Strs
from models.verb_irregularity import VerbIrregularity
from utils import dimension as dim
from utils.conjugator import Conjugator
from utils.utility import Utils
from views.list_widgets.conjugation_chart_list.conjugation_chart_list_widget import ConjugationChartListWidget
from views.styled_views.styled import StyledLineEdit, StyledDialog, StyledComboBox, StyledHBox, StyledVBox, \
    StyledRadioButton, StyledCheckBox


# noinspection PyTypeChecker,PyUnresolvedReferences,NonAsciiCharacters
class ConjugationFormDialog(StyledDialog):
    def __init__(self, dialog_title, vocabulary_getter, verb_irregularity=None):
        super(ConjugationFormDialog, self).__init__(dialog_title)
        # the vocabulary-getter
        self.__vocabulary_getter = vocabulary_getter
        # the verb-irregularity
        self.__verb_irregularity = copy.deepcopy(verb_irregularity) if verb_irregularity is not None else VerbIrregularity()
        # initialize all views
        self.__init_views(verb_irregularity)
        # initialize all events
        self.__init_events()
        # resize to a proper one
        self.resize(*dim.conjugation_form_dialog_size)
        # the add-modify-dialog-mode
        self.__dialog_mode = AddModifyDialogMode.A if verb_irregularity is None else AddModifyDialogMode.M
        # initially update the irregularity and its conjugation-charts
        self.__event_update_irregularity()

    def __init_views(self, verb_irregularity):
        # the radio-buttons for determining it's a regular or an irregular verb
        self.__rdb_regular = StyledRadioButton(Strs.Regular_Verb)
        self.__rdb_irregular = StyledRadioButton(Strs.Irregular_Verb)
        self.__grp_irregularity = QButtonGroup()
        self.__grp_irregularity.addButton(self.__rdb_regular)
        self.__grp_irregularity.addButton(self.__rdb_irregular)
        # for selecting the type of stem-changing if it's a stem-changing verb
        self.__chk_stem_changing = StyledCheckBox(Strs.Is_Stem_Changing_Verb)
        self.__comb_stem_changing = StyledComboBox()
        self.__comb_stem_changing.add_items(*list(map(lambda x: x.format(), StemChangingType)))
        # for determining if it has a special yo-form
        self.__chk_special_yo_form = StyledCheckBox(Strs.Has_Special_Yo_Form)
        self.__le_special_yo_form = StyledLineEdit()
        # for determining if it has a special preterite stem
        self.__chk_special_preterite_stem = StyledCheckBox(Strs.Has_Special_Preterite_Stem)
        self.__le_special_preterite_stem = StyledLineEdit(Strs.Special_Stem_Placeholder)
        # for determining if it has a special imperfect stem
        self.__chk_special_imperfect_stem = StyledCheckBox(Strs.Has_Special_Imperfect_Stem)
        self.__le_special_imperfect_stem = StyledLineEdit(Strs.Special_Stem_Placeholder)
        # for determining if it has a special conditional-future stem
        self.__chk_special_future_stem = StyledCheckBox(Strs.Has_Special_Future_Stem)
        self.__le_special_future_stem = StyledLineEdit(Strs.Special_Stem_Placeholder)
        # for determining if it has a special conditional-future stem
        self.__chk_special_present_subjunctive_stem = StyledCheckBox(Strs.Has_Special_Present_Subjunctive_Stem)
        self.__le_special_present_subjunctive_stem = StyledLineEdit(Strs.Special_Stem_Placeholder)
        # for determining if it has a special tú-form of affirmative imperative
        self.__chk_special_tú_form_affirmative_imperative = StyledCheckBox(Strs.Has_Special_Tú_Form_Affirmative_Imperative)
        self.__le_special_tú_form_affirmative_imperative = StyledLineEdit()
        # the v-box for containing views of settings (at the left-side)
        self.__vbox_settings = StyledVBox(
            StyledHBox((self.__rdb_regular, 0), (self.__rdb_irregular, 0)),
            StyledHBox((self.__chk_stem_changing, 0), (self.__comb_stem_changing, 0)),
            StyledHBox((self.__chk_special_yo_form, 0), (self.__le_special_yo_form, 0)),
            StyledHBox((self.__chk_special_preterite_stem, 0), (self.__le_special_preterite_stem, 0)),
            StyledHBox((self.__chk_special_imperfect_stem, 0), (self.__le_special_imperfect_stem, 0)),
            StyledHBox((self.__chk_special_future_stem, 0), (self.__le_special_future_stem, 0)),
            StyledHBox((self.__chk_special_present_subjunctive_stem, 0), (self.__le_special_present_subjunctive_stem, 0)),
            StyledHBox((self.__chk_special_tú_form_affirmative_imperative, 0), (self.__le_special_tú_form_affirmative_imperative, 0)),
        )
        self.__vbox_settings.setAlignment(Qt.AlignTop)
        # the list of conjugation-charts
        self.__lis_conjugation_charts = ConjugationChartListWidget()
        # the h-box for containing all sub-views
        self.__hbox_base = StyledHBox((self.__vbox_settings, 0), (self.__lis_conjugation_charts, 1))
        # set the base grid-layout as the layout
        self.setLayout(self.__hbox_base)
        # initially set the data from the data-model of verb-irregularity, if exists
        if verb_irregularity is not None and isinstance(verb_irregularity, VerbIrregularity):
            self.__rdb_irregular.setChecked(True)
            self.__comb_stem_changing.setCurrentText(verb_irregularity.stem_changing_type.format())
            self.__le_special_yo_form.setText(verb_irregularity.sp_yo_form)
        # otherwise, viewing it as a regular verb is the default setting
        else:
            self.__rdb_regular.setChecked(True)

    def __init_events(self):
        self.__grp_irregularity.buttonClicked.connect(self.__event_update_irregularity)
        self.__chk_stem_changing.clicked.connect(self.__event_update_irregularity)
        self.__comb_stem_changing.currentIndexChanged.connect(self.__event_update_irregularity)
        self.__chk_special_yo_form.clicked.connect(self.__event_update_irregularity)
        self.__chk_special_preterite_stem.clicked.connect(self.__event_update_irregularity)
        self.__chk_special_imperfect_stem.clicked.connect(self.__event_update_irregularity)
        self.__chk_special_future_stem.clicked.connect(self.__event_update_irregularity)
        self.__chk_special_present_subjunctive_stem.clicked.connect(self.__event_update_irregularity)
        self.__chk_special_tú_form_affirmative_imperative.clicked.connect(self.__event_update_irregularity)

    # the event for switching the irregularity of this verb (regular or irregular)
    def __event_update_irregularity(self):
        self.__update_enabilities()
        self.__update_conjugation_charts()

    # update the enabilities of setting-widgets
    def __update_enabilities(self):
        # set the enabilities of all setting-widgets except for the radio-buttons for irregularity
        Utils.set_enabled_recursively(self.__vbox_settings, self.__rdb_irregular.isChecked())
        self.__rdb_regular.setEnabled(True); self.__rdb_irregular.setEnabled(True)
        # if it's an irregular verb
        if self.__rdb_irregular.isChecked():
            self.__comb_stem_changing.setEnabled(self.__chk_stem_changing.isChecked())
            self.__le_special_yo_form.setEnabled(self.__chk_special_yo_form.isChecked())
            self.__le_special_preterite_stem.setEnabled(self.__chk_special_preterite_stem.isChecked())
            self.__le_special_imperfect_stem.setEnabled(self.__chk_special_imperfect_stem.isChecked())
            self.__le_special_future_stem.setEnabled(self.__chk_special_future_stem.isChecked())
            self.__le_special_present_subjunctive_stem.setEnabled(self.__chk_special_present_subjunctive_stem.isChecked())
            self.__le_special_tú_form_affirmative_imperative.setEnabled(self.__chk_special_tú_form_affirmative_imperative.isChecked())

    # update the conjugation-charts according to the new settings
    def __update_conjugation_charts(self):
        # update the irregularity according to the current settings
        self.__verb_irregularity.stem_changing_type = list(StemChangingType)[self.__comb_stem_changing.currentIndex()] if self.__chk_stem_changing.isChecked() else None
        self.__verb_irregularity.sp_yo_form = self.__le_special_yo_form.text() if self.__chk_special_yo_form.isChecked() else None
        self.__verb_irregularity.sp_preterite_stem = self.__le_special_preterite_stem.text() if self.__chk_special_preterite_stem.isChecked() else None
        self.__verb_irregularity.sp_imperfect_stem = self.__le_special_imperfect_stem.text() if self.__chk_special_imperfect_stem.isChecked() else None
        self.__verb_irregularity.sp_cond_and_future_stem = self.__le_special_future_stem.text() if self.__chk_special_future_stem.isChecked() else None
        self.__verb_irregularity.sp_present_subjunctive_stem = self.__le_special_present_subjunctive_stem.text() if self.__chk_special_present_subjunctive_stem.isChecked() else None
        self.__verb_irregularity.sp_tú_form_affirmative_imperative = self.__le_special_tú_form_affirmative_imperative.text() if self.__chk_special_tú_form_affirmative_imperative.isChecked() else None
        # get the new conjugation according to the updated irregularity
        conjugation = Conjugator.conjugate(self.__vocabulary_getter().lower(), None if self.__rdb_regular.isChecked() else self.__verb_irregularity)
        # get the dictionary of the new conjugation
        conjugation_dict = conjugation.get_all()
        # iterate the whole dictionary to update all line-edits in the conjugation-chart-list
        for (tense, tense_dict) in conjugation_dict.items():
            if tense_dict is not None:
                for (personal, conjugated) in tense_dict.items():
                    self.__lis_conjugation_charts.get_certain_line_edit(tense, personal).setText('' if conjugated is None else conjugated)
