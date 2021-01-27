from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QAbstractItemView

from utils import dimension
from views.voc_adding.example_form.example_translation_widget import ExampleTranslationWidget


class ExampleTranslationListWidget(QListWidget):
    def __init__(self):
        super(ExampleTranslationListWidget, self).__init__()
        # single-selection for this list
        self.setSelectionMode(QAbstractItemView.SingleSelection)

    # push an item into this list
    def push_back(self, translation: str = ''):
        widget = ExampleTranslationWidget(translation, self)
        item = QListWidgetItem(self)
        item.setSizeHint(widget.sizeHint())
        self.addItem(item)
        self.setItemWidget(item, widget)
        # adjust the height
        self.setMinimumHeight(min(
            dimension.example_translation_list_widget_max_height,
            sum(map(lambda x: x.sizeHint().height(), self.get_all_widgets()))
        ))
        # update rows of all added widgets
        for i in range(0, self.count()):
            self.itemWidget(self.item(i)).update_row()
        widget.setFocus()
        return widget

    # get all of the widgets in the list
    def get_all_widgets(self):
        return [self.itemWidget(self.item(i)) for i in range(0, self.count())]

    # get all the translations (str)
    def get_all_translations(self):
        return [self.itemWidget(self.item(i)).translation for i in range(0, self.count())]

    def takeItem(self, row: int) -> QListWidgetItem:
        ret = super(ExampleTranslationListWidget, self).takeItem(row)
        for i in range(0, self.count()):
            widget = self.itemWidget(self.item(i))
            widget.update_row(i)
        return ret
