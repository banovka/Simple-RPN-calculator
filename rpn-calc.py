import sys
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtGui import QKeyEvent

from layout import Ui_RPNCalculator


class MainWindow(QtWidgets.QMainWindow, Ui_RPNCalculator):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        #key_pressed = QtGui.QKeyEvent
        #key_pressed.key.connect(key_pressed)

        self.input1.returnPressed.connect(self.input_value)
        self.input1.textEdited.connect(self.input_edit)

    def input_edit(self, e):
        if e == "+" or e == "-" or e == "*" or e == "/":
            try:
                num_1 = float(self.stack0.text())
                num_2 = float(self.stack1.text())
            except:
                self.input1.clear()
                return
            if e == "+":
                res = num_2 + num_1
            if e == "-":
                res = num_2 - num_1
            if e == "*":
                res = num_1 * num_2
            if e == "/":
                res = num_2 / num_1
            self.stack0.setText(str(res))
            self.stack1.setText(self.stack2.text())
            self.stack2.setText(self.stack3.text())
            self.stack3.setText("0.0")
            self.input1.clear()
            return
        return

    def input_value(self):
        e = self.sender()
        f = e.text()
        if f == "":
            return
        try:
            f = float(f)
        except:
            return
        self.stack3.setText(self.stack2.text())
        self.stack2.setText(self.stack1.text())
        self.stack1.setText(self.stack0.text())
        self.stack0.setText(str(f))
        self.input1.clear()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
