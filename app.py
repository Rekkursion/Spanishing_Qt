import sys

from PyQt5.QtWidgets import QApplication

from managers.layout_manager import LayoutManager
from managers.pref_manager import PrefManager
from utils.word_analyzer import WordAnalyzer
from views.main_win.main_window import MainWindow


# start the application
def start_app():
    app = QApplication([])
    main_win = MainWindow()
    main_win.show()
    LayoutManager.set_main_window(main_win)
    sys.exit(app.exec())


if __name__ == '__main__':
    # initialize the preferences
    PrefManager.init_pref()
    # start the application
    # start_app()
    WordAnalyzer.split_syllables('las ficciones')
