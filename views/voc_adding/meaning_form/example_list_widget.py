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
        widget = ExampleWidget(example_sentence, self)
        item = QListWidgetItem(self)
        item.setSizeHint(widget.sizeHint())
        self.setItemWidget(item, widget)
        self.addItem(item)
        return widget

    # modify a certain example sentence
    def modify_certain_example(self, item_widget: ExampleWidget, new_example_sentence: ExampleSentence):
        row = self.indexAt(item_widget.pos()).row()
        widget = self.itemWidget(self.item(row))
        widget.example_sentence = new_example_sentence

    # move a certain example sentence up/down
    def move_certain_example(self, item_widget: ExampleWidget, is_going_up: bool):
        # get the row-index of the to-be-moved item-widget
        row = self.indexAt(item_widget.pos()).row()
        # if the user wants the first item to go up, or the last one to go down, return directly
        if (row == 0 and is_going_up) or (row == self.count() - 1 and not is_going_up):
            return
        # get the adjacent widget (the upper one if the user wants it to go up, the lower one otherwise)
        adjacent_widget = self.itemWidget(self.item(row - 1 if is_going_up else row + 1))
        # exchange the contents (example sentences) between this one and the adjacent one
        to_be_moved_example_sentence = item_widget.example_sentence
        item_widget.example_sentence = adjacent_widget.example_sentence
        adjacent_widget.example_sentence = to_be_moved_example_sentence

    # get all of the widgets in the list
    def get_all_widgets(self):
        return [self.itemWidget(self.item(i)) for i in range(0, self.count())]
