from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QAbstractItemView

from views.voc_adding.example_form.example_translation_widget import ExampleTranslationWidget


class ExampleTranslationListWidget(QListWidget):
    def __init__(self):
        super(ExampleTranslationListWidget, self).__init__()
        # single-selection for this list
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        # narrow the spacing among the items
        self.setSpacing(-5)

    # push an item into this list
    def push_back(self, translation: str = ''):
        widget = ExampleTranslationWidget(self.count(), translation, self)
        item = QListWidgetItem(self)
        item.setSizeHint(widget.sizeHint())
        self.addItem(item)
        self.setItemWidget(item, widget)
        widget.setFocus()
        return widget

    # get all of the widgets in the list
    def get_all_widgets(self):
        return [self.itemWidget(self.item(i)) for i in range(0, self.count())]

    def takeItem(self, row: int) -> QListWidgetItem:
        ret = super(ExampleTranslationListWidget, self).takeItem(row)
        for i in range(0, self.count()):
            widget = self.itemWidget(self.item(i))
            widget.set_index(i)
        return ret
