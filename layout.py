# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rpn01.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_RPNCalculator(object):
    def setupUi(self, RPNCalculator):
        if not RPNCalculator.objectName():
            RPNCalculator.setObjectName(u"RPNCalculator")
        RPNCalculator.resize(271, 236)
        self.centralwidget = QWidget(RPNCalculator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 50, 158, 160))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stack3 = QLabel(self.widget)
        self.stack3.setObjectName(u"stack3")
        self.stack3.setInputMethodHints(Qt.ImhNone)
        self.stack3.setFrameShape(QFrame.Box)
        self.stack3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.stack3)

        self.stack2 = QLabel(self.widget)
        self.stack2.setObjectName(u"stack2")
        self.stack2.setInputMethodHints(Qt.ImhNone)
        self.stack2.setFrameShape(QFrame.Box)
        self.stack2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.stack2)

        self.stack1 = QLabel(self.widget)
        self.stack1.setObjectName(u"stack1")
        self.stack1.setInputMethodHints(Qt.ImhNone)
        self.stack1.setFrameShape(QFrame.Box)
        self.stack1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.stack1)

        self.stack0 = QLabel(self.widget)
        self.stack0.setObjectName(u"stack0")
        self.stack0.setAutoFillBackground(False)
        self.stack0.setInputMethodHints(Qt.ImhNone)
        self.stack0.setFrameShape(QFrame.Box)
        self.stack0.setLineWidth(3)
        self.stack0.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.stack0)

        self.input1 = QLineEdit(self.widget)
        self.input1.setObjectName(u"input1")
        self.input1.setInputMethodHints(Qt.ImhNone)
        self.input1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.input1)

        RPNCalculator.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(RPNCalculator)
        self.statusbar.setObjectName(u"statusbar")
        RPNCalculator.setStatusBar(self.statusbar)

        self.retranslateUi(RPNCalculator)

        QMetaObject.connectSlotsByName(RPNCalculator)
    # setupUi

    def retranslateUi(self, RPNCalculator):
        RPNCalculator.setWindowTitle(QCoreApplication.translate("RPNCalculator", u"Simple RPN Calculator", None))
        self.stack3.setText(QCoreApplication.translate("RPNCalculator", u"0.0", None))
        self.stack2.setText(QCoreApplication.translate("RPNCalculator", u"0.0", None))
        self.stack1.setText(QCoreApplication.translate("RPNCalculator", u"0.0", None))
        self.stack0.setText(QCoreApplication.translate("RPNCalculator", u"<html><head/><body><p>0.0</p></body></html>", None))
    # retranslateUi

