from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QAbstractItemView

from managers.layout_manager import LayoutManager
from views.menu_list.menu_widget import MenuWidget
from views.pages.base_page import BasePage

from utils import configuration as cfg


class MenuListWidget(QListWidget):
    def __init__(self, *pages: BasePage):
        super(MenuListWidget, self).__init__()
        # single-selection for this list
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        # the event triggered when a certain item is clicked
        self.itemClicked.connect(self.__event_switch_page)
        # initially push the items back into the list
        for page in pages:
            self.push_back(page)
        # set the fixed width
        self.setFixedWidth(cfg.menu_list_width)

    # push an item into this list
    def push_back(self, page: BasePage):
        widget = MenuWidget(page, self.count())
        item = QListWidgetItem(self)
        item.setSizeHint(widget.sizeHint())
        self.addItem(item)
        self.setItemWidget(item, widget)
        return widget

    # get all of the widgets in the list
    def get_all_widgets(self):
        return [self.itemWidget(self.item(i)) for i in range(0, self.count())]

    # the event for switching the page
    # noinspection PyTypeChecker
    def __event_switch_page(self, item):
        # get the menu-widget
        widget = self.itemWidget(item)
        # switch to the corresponding page
        LayoutManager.switch_page_to(widget)
