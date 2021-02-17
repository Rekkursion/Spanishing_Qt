from PyQt5.QtWidgets import QAbstractItemView

from enums.personal import Personal
from enums.tense import Tense
from views.list_widgets.base_list_widget import BaseListWidget
from views.list_widgets.conjugation_chart_list.conjugation_chart_widget import ConjugationChartWidget


class ConjugationChartListWidget(BaseListWidget):
    def __init__(self):
        super(ConjugationChartListWidget, self).__init__(ConjugationChartWidget)
        # no selection for this list
        self.setSelectionMode(QAbstractItemView.NoSelection)
        # initially push all tenses back into this list-widget
        self.__push_all_tenses_back()

    # get a certain line-edit by the mood, tense, & personal, e.g., indicative-present-nosotros
    def get_certain_line_edit(self, tense: Tense, personal: Personal):
        for i in range(0, self.count()):
            widget = self.itemWidget(self.item(i))
            if widget.tense == tense:
                return widget.get_certain_line_edit(personal)
        return None

    # push all tenses back into this list-widget
    # noinspection PyTypeChecker
    def __push_all_tenses_back(self):
        for tense in list(Tense):
            self.push_back(data_model=tense, adjust_height=False)
        self.scrollToTop()
