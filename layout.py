# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_RPNCalculator(object):
    def setupUi(self, RPNCalculator):
        if not RPNCalculator.objectName():
            RPNCalculator.setObjectName(u"RPNCalculator")
        RPNCalculator.resize(281, 293)
        self.actionpi_3_14 = QAction(RPNCalculator)
        self.actionpi_3_14.setObjectName(u"actionpi_3_14")
        self.actione_2_71 = QAction(RPNCalculator)
        self.actione_2_71.setObjectName(u"actione_2_71")
        self.actionsin_Sinus = QAction(RPNCalculator)
        self.actionsin_Sinus.setObjectName(u"actionsin_Sinus")
        self.actioncos_Cosinus = QAction(RPNCalculator)
        self.actioncos_Cosinus.setObjectName(u"actioncos_Cosinus")
        self.actiontan_Tangents = QAction(RPNCalculator)
        self.actiontan_Tangents.setObjectName(u"actiontan_Tangents")
        self.actiontau_6_28 = QAction(RPNCalculator)
        self.actiontau_6_28.setObjectName(u"actiontau_6_28")
        self.actionl1_or_log10 = QAction(RPNCalculator)
        self.actionl1_or_log10.setObjectName(u"actionl1_or_log10")
        self.actionl2_or_log2 = QAction(RPNCalculator)
        self.actionl2_or_log2.setObjectName(u"actionl2_or_log2")
        self.actionl_or_log = QAction(RPNCalculator)
        self.actionl_or_log.setObjectName(u"actionl_or_log")
        self.actionabs_2 = QAction(RPNCalculator)
        self.actionabs_2.setObjectName(u"actionabs_2")
        self.actionp_or_pow_Power = QAction(RPNCalculator)
        self.actionp_or_pow_Power.setObjectName(u"actionp_or_pow_Power")
        self.action_Factorial = QAction(RPNCalculator)
        self.action_Factorial.setObjectName(u"action_Factorial")
        self.actionrec_Reciprocal = QAction(RPNCalculator)
        self.actionrec_Reciprocal.setObjectName(u"actionrec_Reciprocal")
        self.actionsqr_Square_root = QAction(RPNCalculator)
        self.actionsqr_Square_root.setObjectName(u"actionsqr_Square_root")
        self.action_Minus = QAction(RPNCalculator)
        self.action_Minus.setObjectName(u"action_Minus")
        self.action_Plus = QAction(RPNCalculator)
        self.action_Plus.setObjectName(u"action_Plus")
        self.action_Multiplication = QAction(RPNCalculator)
        self.action_Multiplication.setObjectName(u"action_Multiplication")
        self.action_Division = QAction(RPNCalculator)
        self.action_Division.setObjectName(u"action_Division")
        self.actioninput_generat_an_negativ_number = QAction(RPNCalculator)
        self.actioninput_generat_an_negativ_number.setObjectName(u"actioninput_generat_an_negativ_number")
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
        self.menuBar = QMenuBar(RPNCalculator)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 281, 31))
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuTrigonometry = QMenu(self.menuHelp)
        self.menuTrigonometry.setObjectName(u"menuTrigonometry")
        self.menuConstants = QMenu(self.menuHelp)
        self.menuConstants.setObjectName(u"menuConstants")
        self.menuLogarithms = QMenu(self.menuHelp)
        self.menuLogarithms.setObjectName(u"menuLogarithms")
        self.menuBasics = QMenu(self.menuHelp)
        self.menuBasics.setObjectName(u"menuBasics")
        RPNCalculator.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.menuBasics.menuAction())
        self.menuHelp.addAction(self.menuConstants.menuAction())
        self.menuHelp.addAction(self.menuLogarithms.menuAction())
        self.menuHelp.addAction(self.menuTrigonometry.menuAction())
        self.menuTrigonometry.addAction(self.actioncos_Cosinus)
        self.menuTrigonometry.addAction(self.actionsin_Sinus)
        self.menuTrigonometry.addAction(self.actiontan_Tangents)
        self.menuConstants.addAction(self.actione_2_71)
        self.menuConstants.addAction(self.actionpi_3_14)
        self.menuConstants.addAction(self.actiontau_6_28)
        self.menuLogarithms.addAction(self.actionl_or_log)
        self.menuLogarithms.addAction(self.actionl2_or_log2)
        self.menuLogarithms.addAction(self.actionl1_or_log10)
        self.menuBasics.addAction(self.actioninput_generat_an_negativ_number)
        self.menuBasics.addAction(self.action_Plus)
        self.menuBasics.addAction(self.action_Minus)
        self.menuBasics.addAction(self.action_Multiplication)
        self.menuBasics.addAction(self.action_Division)
        self.menuBasics.addAction(self.action_Factorial)
        self.menuBasics.addAction(self.actionabs_2)
        self.menuBasics.addAction(self.actionp_or_pow_Power)
        self.menuBasics.addAction(self.actionrec_Reciprocal)
        self.menuBasics.addAction(self.actionsqr_Square_root)

        self.retranslateUi(RPNCalculator)

        QMetaObject.connectSlotsByName(RPNCalculator)
    # setupUi

    def retranslateUi(self, RPNCalculator):
        RPNCalculator.setWindowTitle(QCoreApplication.translate("RPNCalculator", u"Simple RPN Calculator", None))
        self.actionpi_3_14.setText(QCoreApplication.translate("RPNCalculator", u"pi - 3.14...", None))
        self.actione_2_71.setText(QCoreApplication.translate("RPNCalculator", u"e - 2.71...", None))
        self.actionsin_Sinus.setText(QCoreApplication.translate("RPNCalculator", u"sin - Sinus", None))
        self.actioncos_Cosinus.setText(QCoreApplication.translate("RPNCalculator", u"cos - Cosinus", None))
        self.actiontan_Tangents.setText(QCoreApplication.translate("RPNCalculator", u"tan - Tangents", None))
        self.actiontau_6_28.setText(QCoreApplication.translate("RPNCalculator", u"tau - 6.28...", None))
        self.actionl1_or_log10.setText(QCoreApplication.translate("RPNCalculator", u"l1 or log10", None))
        self.actionl2_or_log2.setText(QCoreApplication.translate("RPNCalculator", u"l2 or log2", None))
        self.actionl_or_log.setText(QCoreApplication.translate("RPNCalculator", u"l or log", None))
        self.actionabs_2.setText(QCoreApplication.translate("RPNCalculator", u"abs - Absolute", None))
        self.actionp_or_pow_Power.setText(QCoreApplication.translate("RPNCalculator", u"p - Power", None))
        self.action_Factorial.setText(QCoreApplication.translate("RPNCalculator", u"! - Factorial", None))
        self.actionrec_Reciprocal.setText(QCoreApplication.translate("RPNCalculator", u"rec - Reciprocal", None))
        self.actionsqr_Square_root.setText(QCoreApplication.translate("RPNCalculator", u"sqr - Square root", None))
        self.action_Minus.setText(QCoreApplication.translate("RPNCalculator", u"- - Minus", None))
        self.action_Plus.setText(QCoreApplication.translate("RPNCalculator", u"+ - Plus", None))
        self.action_Multiplication.setText(QCoreApplication.translate("RPNCalculator", u"* - Multiplication", None))
        self.action_Division.setText(QCoreApplication.translate("RPNCalculator", u"/ - Division", None))
        self.actioninput_generat_an_negativ_number.setText(QCoreApplication.translate("RPNCalculator", u"input- generat a negativ number", None))
        self.stack3.setText(QCoreApplication.translate("RPNCalculator", u"0.0", None))
        self.stack2.setText(QCoreApplication.translate("RPNCalculator", u"0.0", None))
        self.stack1.setText(QCoreApplication.translate("RPNCalculator", u"0.0", None))
        self.stack0.setText(QCoreApplication.translate("RPNCalculator", u"<html><head/><body><p>0.0</p></body></html>", None))
        self.menuHelp.setTitle(QCoreApplication.translate("RPNCalculator", u"Help", None))
        self.menuTrigonometry.setTitle(QCoreApplication.translate("RPNCalculator", u"Trigonometry", None))
        self.menuConstants.setTitle(QCoreApplication.translate("RPNCalculator", u"Constants", None))
        self.menuLogarithms.setTitle(QCoreApplication.translate("RPNCalculator", u"Logarithms", None))
        self.menuBasics.setTitle(QCoreApplication.translate("RPNCalculator", u"Basics", None))
    # retranslateUi

