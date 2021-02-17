import uuid

from PyQt5.QtWidgets import QWidget, QLayout


class Utils:
    # generate a string w/ random characters in a fixed length of 20
    @staticmethod
    def generate_random_string():
        return uuid.uuid4().hex[:20]

    # set the enability of a widget or a layout recursively
    @staticmethod
    def set_enabled_recursively(widget_or_layout, is_enabled: bool):
        # if it's a layout, set the enability recursively
        if isinstance(widget_or_layout, QLayout):
            for k in range(0, widget_or_layout.count()):
                Utils.set_enabled_recursively(widget_or_layout.itemAt(k).widget(), is_enabled)
                Utils.set_enabled_recursively(widget_or_layout.itemAt(k).layout(), is_enabled)
        # if it's a widget, simply set its enability
        elif isinstance(widget_or_layout, QWidget):
            widget_or_layout.setEnabled(is_enabled)
