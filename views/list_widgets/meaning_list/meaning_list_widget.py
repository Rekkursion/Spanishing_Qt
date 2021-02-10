from views.list_widgets.base_list_widget import BaseListWidget
from views.list_widgets.meaning_list.meaning_widget import MeaningWidget


class MeaningListWidget(BaseListWidget):
    def __init__(self):
        super(MeaningListWidget, self).__init__(MeaningWidget)

    # move a certain meaning up/down
    def move_certain_meaning(self, item_widget: MeaningWidget, is_going_up: bool):
        # get the row of the to-be-moved item-widget
        row = self.indexAt(item_widget.pos()).row()
        # if the user wants the first item to go up, or the last one to go down, return directly
        if (row == 0 and is_going_up) or (row == self.count() - 1 and not is_going_up):
            return
        # get the adjacent widget (the upper one if the user wants it to go up, the lower one otherwise)
        adjacent_widget = self.itemWidget(self.item(row - 1 if is_going_up else row + 1))
        # exchange the contents (meaning) between this one and the adjacent one
        to_be_moved_meaning = item_widget.meaning
        item_widget.meaning = adjacent_widget.meaning
        adjacent_widget.meaning = to_be_moved_meaning
