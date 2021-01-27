from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QAbstractItemView

from models.example_sentence import ExampleSentence
from views.voc_adding.meaning_form.example_widget import ExampleWidget


class ExampleListWidget(QListWidget):
    def __init__(self):
        super(ExampleListWidget, self).__init__()
        # single-selection for this list
        self.setSelectionMode(QAbstractItemView.SingleSelection)

    # push an item into this list
    def push_back(self, example_sentence: ExampleSentence):
        widget = ExampleWidget(self.count(), example_sentence, self)
        item = QListWidgetItem(self)
        item.setSizeHint(widget.sizeHint())
        self.addItem(item)
        self.setItemWidget(item, widget)
        widget.setFocus()
        return widget

    # modify a certain example sentence located by its index
    def modify_certain_example(self, index: int, new_example_sentence: ExampleSentence):
        widget = self.itemWidget(self.item(index))
        widget.example_sentence = new_example_sentence

    # get all of the widgets in the list
    def get_all_widgets(self):
        return [self.itemWidget(self.item(i)) for i in range(0, self.count())]
