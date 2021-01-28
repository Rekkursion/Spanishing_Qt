from managers.layout_manager import LayoutManager
from utils import dimension as dim
from views.list_widgets.base_list_widget import BaseListWidget
from views.list_widgets.menu_list.menu_widget import MenuWidget
from views.pages.base_page import BasePage


class MenuListWidget(BaseListWidget):
    def __init__(self, *pages: BasePage):
        super(MenuListWidget, self).__init__(MenuWidget)
        # the event triggered when a certain item is clicked
        self.itemClicked.connect(self.__event_switch_page)
        # initially push the items back into the list
        for page in pages:
            self.push_back(page, adjust_height=False)
        # set the fixed width
        self.setFixedWidth(dim.menu_list_width)

    # the event for switching the page
    # noinspection PyTypeChecker
    def __event_switch_page(self, item):
        # get the menu-widget
        widget = self.itemWidget(item)
        # switch to the corresponding page
        LayoutManager.switch_page_to(widget)
