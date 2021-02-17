from PyQt5.QtWidgets import QWidget

from enums.fixed_size import FixedSizes
from enums.personal import Personal
from enums.tense import Tense
from views.styled_views.styled import StyledLabel, StyledLineEdit, StyledGridLayout


# noinspection NonAsciiCharacters
class ConjugationChartWidget(QWidget):
    def __init__(self, tense: Tense, attached):
        super(ConjugationChartWidget, self).__init__()
        # the mood & tense for this conjugation chart
        self.__tense = tense
        # the list-widget that this widget attached on
        self.__attached = attached
        # initialize all views
        self.__init_views()
        # initialize all events
        self.__init_events()

    @property
    def tense(self):
        return self.__tense

    def __init_views(self):
        # the base grid-layout
        self.__grid_layout = StyledGridLayout()
        # the label for displaying the mood & tense for this conjugation chart
        self.__lbl_tense = StyledLabel(f'<strong>{self.__tense.format()}</strong>', FixedSizes.LARGE)
        self.__grid_layout.addWidget(self.__lbl_tense, 0, 0, 1, 13)
        # the list of all line-edits
        self.__all_le_arr = []
        # the labels & line-edits for typing the forms of all personals
        for index, personal in enumerate(self.__tense.get_personals()):
            le = StyledLineEdit()
            if index < 3:
                self.__grid_layout.addWidget(StyledLabel(''), (index % 3) + 1, 0, 1, 1)
            self.__grid_layout.addWidget(StyledLabel(personal.format()), (index % 3) + 1, (((index // 3) * 6) + 1), 1, 1)
            self.__grid_layout.addWidget(le, (index % 3) + 1, (((index // 3) * 6) + 2), 1, 5)
            self.__all_le_arr.append(le)
            if self.__tense == Tense.IMPERATIVE_AFFIRMATIVE or self.__tense == Tense.IMPERATIVE_NEGATIVE:
                if personal == Personal.YO:
                    le.setEnabled(False)
        # set the grid-layout as the layout of this widget
        self.setLayout(self.__grid_layout)

    def __init_events(self):
        pass

    # get a certain line-edit by the personal
    def get_certain_line_edit(self, personal: Personal):
        return self.__all_le_arr[personal.value]
