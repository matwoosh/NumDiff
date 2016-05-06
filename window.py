import sys

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *

# Create an PyQT4 application object.
a = QApplication(sys.argv)

# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QMainWindow()

# Set window size.
w.resize(800, 600)

# Set window title
w.setWindowTitle("NumDiff")

# Add a button
btn = QPushButton('Test button', w)
btn.setToolTip('Click to quit!')
btn.resize(btn.sizeHint())
btn.move(10, 40)

# Create the actions
@pyqtSlot()
def on_click():
    print('clicked')

@pyqtSlot()
def on_press():
    print('pressed')

@pyqtSlot()
def on_release():
    print('released')

# connect the signals to the slots
btn.clicked.connect(on_click)
btn.pressed.connect(on_press)
btn.released.connect(on_release)


# Create main menu
mainMenu = w.menuBar()
mainMenu.setNativeMenuBar(False)
fileMenu = mainMenu.addMenu('File')
helpMenu = mainMenu.addMenu('Help')

# Add exit button
exitButton = QAction(QIcon('exit24.png'), 'Exit', w)
exitButton.setShortcut('Ctrl+Q')
exitButton.setStatusTip('Exit application')
exitButton.triggered.connect(w.close)
fileMenu.addAction(exitButton)

helpButton = QAction(QIcon('exit24.png'), 'Help', w)
helpButton.setShortcut('Ctrl+H')
helpButton.setStatusTip('Show help')
helpButton.triggered.connect(w.close)
fileMenu.addAction(exitButton)

# Create combobox
combo = QComboBox(w)
combo.addItem("sin(x)")
combo.addItem("cos(x)")
combo.addItem("x^2")
combo.addItem("x^3+2x^2")
combo.addItem("x^4-3x^2")
combo.addItem("sqrt(x)")
combo.addItem("exp(x)")
combo.move(10, 100)


# Show window
w.show()

sys.exit(a.exec_())

a.exec_()