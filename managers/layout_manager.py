from views.menu_list.menu_widget import MenuWidget


class LayoutManager:
    # the main-window
    __main_win = None

    # set the main-window
    @staticmethod
    def set_main_window(main_window):
        LayoutManager.__main_win = main_window

    # switch the page to a certain page
    @staticmethod
    def switch_page_to(menu_widget: MenuWidget):
        if LayoutManager.__main_win is not None:
            # set the page corresponding to the passed-in menu-widget
            LayoutManager.__main_win.set_page_by_index(menu_widget.index)
