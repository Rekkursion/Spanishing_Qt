from PyQt5.QtWidgets import QListWidgetItem

from views.list_widgets.base_list_widget import BaseListWidget
from views.list_widgets.example_translation_list.example_translation_widget import ExampleTranslationWidget


class ExampleTranslationListWidget(BaseListWidget):
    def __init__(self):
        super(ExampleTranslationListWidget, self).__init__(ExampleTranslationWidget)

    # get all the translations (str)
    def get_all_translations(self):
        return [self.itemWidget(self.item(i)).translation for i in range(0, self.count())]

    # override the push-back method for updating rows in each item-widget when adding items
    def push_back(self, data_model, adjust_height: bool = True, max_height: int = 2147483647):
        super(ExampleTranslationListWidget, self).push_back(data_model, adjust_height, max_height)
        # update rows of all added widgets
        for i in range(0, self.count()):
            self.itemWidget(self.item(i)).update_row()

    # override the take-item method for updating rows in each item-widget when removing items
    def takeItem(self, row: int) -> QListWidgetItem:
        ret = super(ExampleTranslationListWidget, self).takeItem(row)
        for i in range(0, self.count()):
            widget = self.itemWidget(self.item(i))
            widget.update_row(i)
        return ret
