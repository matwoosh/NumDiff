import numpy as np
import sys
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot, Qt

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
import matplotlib.pyplot as plt

from plot import Plot


class Window(QtGui.QDialog):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.figure = plt.figure()  # a figure instance to plot on
        self.canvas = FigureCanvas(self.figure)
        self.combo = QtGui.QComboBox()
        self.plot_button = QtGui.QPushButton('Plot')
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.init_ui()

    def init_ui(self):
        self.init_combo()
        self.plot_button.clicked.connect(self.plot)

        layout = QtGui.QVBoxLayout(self)
        left = QtGui.QFrame()
        left.setFrameShape(QtGui.QFrame.StyledPanel)

        splitter1 = QtGui.QSplitter(Qt.Vertical)
        splitter1.addWidget(self.combo)
        splitter1.addWidget(left)

        splitter0 = QtGui.QSplitter(Qt.Horizontal)
        splitter0.addWidget(splitter1)

        splitter2 = QtGui.QSplitter(Qt.Vertical)
        splitter2.addWidget(self.toolbar)
        splitter2.addWidget(self.canvas)
        splitter2.addWidget(self.plot_button)

        splitter0.addWidget(splitter2)

        layout.addWidget(splitter0)

        self.setLayout(layout)

    def plot(self):
        x1 = np.arange(0, 10, 0.1)
        y1 = np.sin(x1)
        p1 = Plot(y1, x1)
        p1.plot_function(self.canvas)

    def init_combo(self):
        self.combo.addItem("sin(x)")
        self.combo.addItem("cos(x)")
        self.combo.addItem("x^2")
        self.combo.addItem("x^3+2x^2")
        self.combo.addItem("x^4-3x^2")
        self.combo.addItem("sqrt(x)")
        self.combo.addItem("exp(x)")
        self.combo.move(10, 100)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    w = Window()
    w.show()
    w.resize(1000, 600)

    # Set window title
    w.setWindowTitle("NumDiff")


    # btn = QtGui.QPushButton('Test button', w)
    # btn.setToolTip('Click to quit!')
    # btn.resize(btn.sizeHint())
    # btn.move(10, 40)
    #
    # # Create the actions
    # @pyqtSlot()
    # def on_click():
    #     print('clicked')
    #
    # @pyqtSlot()
    # def on_press():
    #     print('pressed')
    #
    # @pyqtSlot()
    # def on_release():
    #     print('released')
    #
    # # connect the signals to the slots
    # btn.clicked.connect(on_click)
    # btn.pressed.connect(on_press)
    # btn.released.connect(on_release)
    #

    sys.exit(app.exec_())

###########################################333

# # Create an PyQT4 application object.
# from plot import Plot
#
# a = QApplication(sys.argv)
#
# # The QWidget widget is the base class of all user interface objects in PyQt4.
# w = QMainWindow()
#
#
#
# # Add a button
# btn = QPushButton('Test button', w)
# btn.setToolTip('Click to quit!')
# btn.resize(btn.sizeHint())
# btn.move(10, 40)
#
# # Create the actions
# @pyqtSlot()
# def on_click():
#     print('clicked')
#
# @pyqtSlot()
# def on_press():
#     print('pressed')
#
# @pyqtSlot()
# def on_release():
#     x1 = np.arange(0, 10, 0.1)
#     y1 = np.sin(x1)
#     p1 = Plot(y1, x1)
#     p1.plot_function()
#     print('released')
#
# # connect the signals to the slots
# btn.clicked.connect(on_click)
# btn.pressed.connect(on_press)
# btn.released.connect(on_release)
#
#
# # Create main menu
# mainMenu = w.menuBar()
# mainMenu.setNativeMenuBar(False)
# fileMenu = mainMenu.addMenu('File')
# helpMenu = mainMenu.addMenu('Help')
#
# # Add exit button
# exitButton = QAction(QIcon('exit24.png'), 'Exit', w)
# exitButton.setShortcut('Ctrl+Q')
# exitButton.setStatusTip('Exit application')
# exitButton.triggered.connect(w.close)
# fileMenu.addAction(exitButton)
#
# helpButton = QAction(QIcon('exit24.png'), 'Help', w)
# helpButton.setShortcut('Ctrl+H')
# helpButton.setStatusTip('Show help')
# helpButton.triggered.connect(w.close)
# fileMenu.addAction(exitButton)
#
# # Create combobox
# combo = QComboBox(w)
# combo.addItem("sin(x)")
# combo.addItem("cos(x)")
# combo.addItem("x^2")
# combo.addItem("x^3+2x^2")
# combo.addItem("x^4-3x^2")
# combo.addItem("sqrt(x)")
# combo.addItem("exp(x)")
# combo.move(10, 100)
#
#
# # Show window
# w.show()
#
# sys.exit(a.exec_())
#
# a.exec_()