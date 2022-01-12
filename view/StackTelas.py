from PyQt5.QtWidgets import QStackedLayout


class StackTelas(QStackedLayout):
    def __init__(self, screens, parent=None):
        super(StackTelas, self).__init__(parent)

        self._screens = screens

        self._createScreens()


    @property
    def screens(self):
        return self._screens


    def _createScreens(self):
        for screen in self.screens:
            self.addWidget(screen)


    def open_screen(self, screen_index):
        self.setCurrentIndex(screen_index)
