from views.pages.base_page import BasePage


class VocAddingPage(BasePage):
    def __init__(self, page_name):
        super(VocAddingPage, self).__init__(page_name)
        # initialize all views
        self._init_views()
        # initialize all events
        self._init_events()

    def _init_views(self):
        return NotImplemented

    def _init_events(self):
        return NotImplemented
