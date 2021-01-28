from models.example_sentence import ExampleSentence
from views.list_widgets.base_list_widget import BaseListWidget
from views.list_widgets.example_list.example_widget import ExampleWidget


class ExampleListWidget(BaseListWidget):
    def __init__(self):
        super(ExampleListWidget, self).__init__(ExampleWidget)

    # modify a certain example sentence
    def modify_certain_example(self, item_widget: ExampleWidget, new_example_sentence: ExampleSentence):
        row = self.indexAt(item_widget.pos()).row()
        widget = self.itemWidget(self.item(row))
        widget.example_sentence = new_example_sentence

    # move a certain example sentence up/down
    def move_certain_example(self, item_widget: ExampleWidget, is_going_up: bool):
        # get the row of the to-be-moved item-widget
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
