from PyQt5.QtCore import QSize

from views.pages.base_page import BasePage
from views.voc_adding.single_voc_form import SingleVocForm


class VocAddingPage(BasePage):
    def __init__(self, page_name):
        super(VocAddingPage, self).__init__(page_name)
        # initialize all views
        self._init_views()
        # initialize all events
        self._init_events()

    def _init_views(self):
        # the form for adding a single vocabulary
        self.__single_voc_form = SingleVocForm()
        self.addWidget(self.__single_voc_form)

    def _init_events(self):
        return NotImplemented

    def set_focus(self):
        self.__single_voc_form.setFocus()

    def sizeHint(self) -> QSize:
        # return QSize(500, sum(map(lambda x: x.sizeHint().height(), self._item_list)))
        return QSize(500, sum(map(lambda x: x.sizeHint().height(), self._item_list)))
