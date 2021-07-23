# Mouse click input
# differentiate between click and hold by using thresh-holds.
# anything before 0.3 secs is a click. Anything after 0.6 secs is a hold
# it has to continuously record input from the pushbutton
# clicks get recorded as zeros, holds get recorded as ones.
# sends the result to the encoder.
# (also, must check for interval between two different sessions of clicks
# and holds. So one sentence or word does not get mixed up with anothers.
# maybe like 5 secs?)


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import QTimer, pyqtSignal


class MorseButton(QtWidgets.QPushButton):
    hold = pyqtSignal()
    click = pyqtSignal()
    rest = pyqtSignal()
    def __init__(self, title, short_interval=100, long_interval=300, *args, **kwargs):
        QtWidgets.QPushButton.__init__(self, title, *args, **kwargs)
        self.setAutoRepeat(True)
        self.long_interval = long_interval
        self.setAutoRepeatDelay(self.long_interval)

        self.setAutoRepeatInterval(50)
        self.clicked.connect(self.handleClicked)
        self._state = 0

        # self.hold = pyqtSignal()
        # self.click = pyqtSignal()
        # self.rest = pyqtSignal()

        self.timer_id = 0


    def handleClicked(self):
        if self.isDown():
            if self._state == 0:
                self._state = 1
                self.setAutoRepeatInterval(50)
                print('hold')
                # self.hold.emit()

            # else:
            #     print('repeat')
        elif self._state == 1:
            self._state = 0
            self.setAutoRepeatInterval(self.long_interval)
            try:
                self.killTimer(self.timer_id)
            except:
                print("error")

            print('release')
        else:
            print('click')
            # self.startTimer(1000)
            # self.click.emit()

    def timerEvent(self, e):
        print("rest")
        self.timer_id = e.timerId()
        self.killTimer(e.timerId())
        self.rest.emit()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    button = MorseButton('Test Button')
    button.show()
    sys.exit(app.exec_())
