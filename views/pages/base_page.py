import abc

from PyQt5.QtCore import QSize, QRect
from PyQt5.QtWidgets import QLayout, QLayoutItem, QFrame

from utils import configuration as cfg


class BasePage(QLayout):
    def __init__(self, page_name):
        super(BasePage, self).__init__()
        # the name of this page
        self.page_name = page_name
        self._item_list = []

    @abc.abstractmethod
    def _init_views(self):
        raise NotImplementedError

    @abc.abstractmethod
    def _init_events(self):
        raise NotImplementedError

    @abc.abstractmethod
    def set_focus(self):
        raise NotImplementedError

    # wrap this page (a layout) as a frame (a widget)
    def wrap_as_frame(self):
        frame = QFrame()
        frame.setLayout(self)
        return frame

    # wrap a certain layout as a frame and add it
    def _add_layout(self, l: QLayout):
        f = QFrame()
        f.setLayout(l)
        self.addWidget(f)

    def addItem(self, a0: QLayoutItem) -> None:
        self._item_list.append(a0)

    def setGeometry(self, a0: QRect) -> None:
        parent_size = self.parentWidget().size()
        w, h = parent_size.width(), self.sizeHint().height()
        y = 0
        for item in self._item_list:
            item.setGeometry(QRect(0, y, w, h))
            y += h

    # def setGeometry(self, a0: QRect) -> None:
    #     parent_size = self.parentWidget().size()
    #     w, h = self.sizeHint().width(), self.sizeHint().height()
    #     x, y = 0, 0
    #     for item in self._item_list:
    #         item.setGeometry(QRect(x, y, w, h))
    #         x += w
    #         if x + w > parent_size.width():
    #             x = 0
    #             y += h

    def count(self) -> int:
        return len(self._item_list)

    def itemAt(self, index: int) -> QLayoutItem:
        return self._item_list[index] if 0 <= index < self.count() else None

    def sizeHint(self) -> QSize:
        return QSize(500, cfg.general_widget_height)
