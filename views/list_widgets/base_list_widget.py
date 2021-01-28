from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QAbstractItemView


class BaseListWidget(QListWidget):
    def __init__(self, widget_type):
        super(BaseListWidget, self).__init__()
        # single-selection for this list
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        # set the type of item-widgets
        self._widget_type = widget_type

    # push an item into this list
    def push_back(self, data_model, adjust_height: bool = True, max_height: int = 2147483647):
        widget = self._widget_type(data_model, self)
        item = QListWidgetItem(self)
        item.setSizeHint(widget.sizeHint())
        self.setItemWidget(item, widget)
        self.addItem(item)
        # adjust the height if needs
        if adjust_height:
            all_widgets = self.get_all_widgets()
            self.setMinimumHeight(min(
                max_height,
                int(sum(map(lambda x: x.sizeHint().height(), all_widgets)) * 1.2)
            ))
        # set the focus-point to this new widget
        widget.setFocus()
        # scroll this list-widget to bottom
        self.scrollToBottom()
        # return the new widget
        return widget

    # get all of the widgets in the list
    def get_all_widgets(self):
        return [self.itemWidget(self.item(i)) for i in range(0, self.count())]
