import sys
import math
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtGui import QKeyEvent

from layout import Ui_RPNCalculator


class MainWindow(QtWidgets.QMainWindow, Ui_RPNCalculator):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

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
                if num_1 == 0:
                    return
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
        is_negativ = f[-1]
        if is_negativ == "-":
            f = f[:-1]
            try:
                f = float(f) * -1
            except:
                return
        if f == "":
            return
        if f == "pi":
            f = math.pi
        if f == "e":
            f = math.e
        if f == "tau":
            f = math.tau
        if f == "l" or f == "log":
            f = float(self.stack0.text())
            f = math.log(f)
            self.stack0.setText(str(f))
            self.input1.clear()
            return
        if f == "l1" or f == "log10":
            f = float(self.stack0.text())
            f = math.log10(f)
            self.stack0.setText(str(f))
            self.input1.clear()
            return
        if f == "l2" or f == "log":
            f = float(self.stack0.text())
            f = math.log2(f)
            self.stack0.setText(str(f))
            self.input1.clear()
            return
        if f == "sin":
            f = float(self.stack0.text())
            f = math.sin(f)
            self.stack0.setText(str(f))
            self.input1.clear()
            return
        if f == "cos":
            f = float(self.stack0.text())
            f = math.cos(f)
            self.stack0.setText(str(f))
            self.input1.clear()
            return
        if f == "tan":
            f = float(self.stack0.text())
            f = math.tan(f)
            self.stack0.setText(str(f))
            self.input1.clear()
            return
        if f == "p":
            f = float(self.stack0.text())
            g = float(self.stack1.text())
            f = math.pow(f, g)
            self.stack3.setText(self.stack2.text())
            self.stack2.setText(self.stack1.text())
            self.stack1.setText(self.stack0.text())
            self.stack0.setText(str(f))
            self.input1.clear()
            return
        if f == "sqr":
            f = float(self.stack0.text())
            f = math.sqrt(f)
            self.stack0.setText(str(f))
            self.input1.clear()
            return
        if f == "abs":
            f = float(self.stack0.text())
            f = math.fabs(f)
            self.stack0.setText(str(f))
            self.input1.clear()
            return
        if f == "rec":
            f = float(self.stack0.text())
            f = 1 / f
            self.stack0.setText(str(f))
            self.input1.clear()
            return
        if f == "!":
            f = float(self.stack0.text())
            f = math.factorial(f)
            self.stack0.setText(str(f))
            self.input1.clear()
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
