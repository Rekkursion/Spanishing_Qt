from views.list_widgets.base_list_widget import BaseListWidget
from views.list_widgets.meaning_list.meaning_widget import MeaningWidget


class MeaningListWidget(BaseListWidget):
    def __init__(self):
        super(MeaningListWidget, self).__init__(MeaningWidget)
