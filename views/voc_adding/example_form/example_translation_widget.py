from PyQt5.QtWidgets import QWidget

from enums.strs import Strs
from managers.lang_manager import LangManager
from views.styled_views.styled import StyledLabel, StyledLineEdit, StyledButton, StyledHBox


class ExampleTranslationWidget(QWidget):
    def __init__(self, index: int, translation: str, attached):
        super(ExampleTranslationWidget, self).__init__()
        # the original translation
        self.__original_translation = translation
        # the index of this widget
        self.__index = index
        # the list-widget that this widget attached on
        self.__attached = attached
        # initialize all views
        self.__init_views()
        # initialize all events
        self.__init_events()

    @property
    def translation(self):
        return self.__le_translation.text()

    def __init_views(self):
        # the label for displaying the index
        self.__lbl_index = StyledLabel('{:02d}. '.format(self.__index + 1))
        # the line-edit for displaying the translation
        self.__le_translation = StyledLineEdit(Strs.Voc_Adding_Page_Example_Sentence_New_Translation_Placeholder, text=self.__original_translation)
        # the button for removing the translation
        self.__btn_remove_translation = StyledButton(Strs.Remove)
        # the base h-box
        self.__hbox_base = StyledHBox(
            (self.__lbl_index, 0), (self.__le_translation, 1), (self.__btn_remove_translation, 0),
            spacing=-6
        )
        # set the h-box as the layout of this widget
        self.setLayout(self.__hbox_base)

    def __init_events(self):
        self.__btn_remove_translation.clicked.connect(self.__event_remove_translation)

    # set the index
    def set_index(self, new_index):
        self.__index = new_index
        self.__lbl_index.setText('{:02d}. '.format(self.__index + 1))

    # the event for removing this translation
    def __event_remove_translation(self):
        # unregister the registered views
        LangManager.unregister(self.__lbl_index, self.__le_translation, self.__btn_remove_translation)
        # remove the item in the list
        self.__attached.takeItem(self.__index)

    def setFocus(self) -> None:
        self.__le_translation.setFocus()
