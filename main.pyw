#####################################
# No need to Edit this main file.####
#####################################
# Edit Ui_Functions file to add functions or edit signal and slots.
# Setting Style sheet to widgets is also possible.

# APP Imports
import sys
import os
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                          QSize, QTime, QTimer, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                         QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

##############################
# Import user interface file
##############################
from Ui_main import Ui_MainWindow
from Ui_Functions import Ui_Functions
from datetime import datetime, time

# Global value for the windows status
WINDOW_SIZE = 0


# This will help us determine if the window is minimized or maximized

# Main class
class MainWindow(QMainWindow):
    def __init__(self, hide_title=False):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Apply shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(2)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        # Apply shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        # Button click events to our top bar buttons
        #
        # Minimize window
        if hasattr(self.ui, "minimizeButton"):
            self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())
        # Close window
        if hasattr(self.ui, "closeButton"):
            self.ui.closeButton.clicked.connect(lambda: self.close())
        # Restore/Maximize window
        if hasattr(self.ui, "restoreButton"):
            self.ui.restoreButton.clicked.connect(lambda: self.restore_or_maximize_window())

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        if hasattr(self.ui, "title_bar") or hide_title:
            # Remove window tlttle bar
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

            # Set main background to transparent
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            if hasattr(self.ui, "title_bar"):
                self.ui.title_bar.mouseMoveEvent = moveWindow

        # Show window
        self.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    # Restore or maximize your window
    def restore_or_maximize_window(self):

        # Global windows state
        global WINDOW_SIZE  # The default value is zero to show that the size is not maximized
        win_status = WINDOW_SIZE

        if win_status == 0:
            # If the window is not maximized
            WINDOW_SIZE = 1  # Update value to show that the window has been maxmized
            self.showMaximized()
            # Update button icon
            # self.ui.restoreButton.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-maximize.png"))  # Show maximized icon
        else:
            # If the window is on its default size
            WINDOW_SIZE = 0  # Update value to show that the window has been minimized/set to normal size (which is 800 by 400)
            self.showNormal()
            # Update button icon
            # self.ui.restoreButton.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-restore.png"))  # Show minized icon

    def keyPressEvent(self, e):
        functions.key_event(e)

# Execute app
#
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(hide_title=True)
    functions = Ui_Functions(window)

    sys.exit(app.exec_())
else:
    print(__name__, "hh")
# press ctrl+b in sublime to run
