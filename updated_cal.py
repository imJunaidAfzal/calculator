# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.setEnabled(True)
        Calculator.resize(450, 444)
        Calculator.setMinimumSize(QtCore.QSize(0, 0))
        Calculator.setMaximumSize(QtCore.QSize(99999, 99999))
        Calculator.setAutoFillBackground(False)
        Calculator.setStyleSheet("background-color: rgb(106, 106, 106);\n"
"background-color: rgb(71, 69, 68);\n"
"")
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.num1_input = QtWidgets.QLineEdit(self.centralwidget)
        self.num1_input.setGeometry(QtCore.QRect(30, 90, 401, 81))
        self.num1_input.setStyleSheet("background-color: rgb(81, 81, 81);\n"
"font: 14pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.num1_input.setText("")
        self.num1_input.setObjectName("num1_input")
        self.one_button = QtWidgets.QPushButton(self.centralwidget)
        self.one_button.setGeometry(QtCore.QRect(30, 280, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.one_button.setFont(font)
        self.one_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.one_button.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.one_button.setObjectName("one_button")
        self.three_button = QtWidgets.QPushButton(self.centralwidget)
        self.three_button.setGeometry(QtCore.QRect(130, 280, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.three_button.setFont(font)
        self.three_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.three_button.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.three_button.setObjectName("three_button")
        self.two_button = QtWidgets.QPushButton(self.centralwidget)
        self.two_button.setGeometry(QtCore.QRect(80, 280, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.two_button.setFont(font)
        self.two_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.two_button.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.two_button.setObjectName("two_button")
        self.six_button = QtWidgets.QPushButton(self.centralwidget)
        self.six_button.setGeometry(QtCore.QRect(130, 310, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.six_button.setFont(font)
        self.six_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.six_button.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.six_button.setObjectName("six_button")
        self.five_button = QtWidgets.QPushButton(self.centralwidget)
        self.five_button.setGeometry(QtCore.QRect(80, 310, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.five_button.setFont(font)
        self.five_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.five_button.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.five_button.setObjectName("five_button")
        self.four_button = QtWidgets.QPushButton(self.centralwidget)
        self.four_button.setGeometry(QtCore.QRect(30, 310, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.four_button.setFont(font)
        self.four_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.four_button.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.four_button.setObjectName("four_button")
        self.nine_button = QtWidgets.QPushButton(self.centralwidget)
        self.nine_button.setGeometry(QtCore.QRect(130, 340, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.nine_button.setFont(font)
        self.nine_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.nine_button.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.nine_button.setObjectName("nine_button")
        self.eight_button = QtWidgets.QPushButton(self.centralwidget)
        self.eight_button.setGeometry(QtCore.QRect(80, 340, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.eight_button.setFont(font)
        self.eight_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.eight_button.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.eight_button.setObjectName("eight_button")
        self.seven_button = QtWidgets.QPushButton(self.centralwidget)
        self.seven_button.setGeometry(QtCore.QRect(30, 340, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.seven_button.setFont(font)
        self.seven_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.seven_button.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.seven_button.setObjectName("seven_button")
        self.backspace_button = QtWidgets.QPushButton(self.centralwidget)
        self.backspace_button.setGeometry(QtCore.QRect(130, 370, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.backspace_button.setFont(font)
        self.backspace_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.backspace_button.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.backspace_button.setObjectName("backspace_button")
        self.dot_button = QtWidgets.QPushButton(self.centralwidget)
        self.dot_button.setGeometry(QtCore.QRect(80, 370, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.dot_button.setFont(font)
        self.dot_button.setMouseTracking(False)
        self.dot_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dot_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.dot_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.dot_button.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.dot_button.setObjectName("dot_button")
        self.zero_button = QtWidgets.QPushButton(self.centralwidget)
        self.zero_button.setGeometry(QtCore.QRect(30, 370, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.zero_button.setFont(font)
        self.zero_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.zero_button.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.zero_button.setObjectName("zero_button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 351, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(190, 280, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setKerning(True)
        self.clear_button.setFont(font)
        self.clear_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.clear_button.setObjectName("clear_button")
        self.mod_button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.mod_button_3.setGeometry(QtCore.QRect(190, 200, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.mod_button_3.setFont(font)
        self.mod_button_3.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.mod_button_3.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);")
        self.mod_button_3.setObjectName("mod_button_3")
        self.sin_button = QtWidgets.QPushButton(self.centralwidget)
        self.sin_button.setGeometry(QtCore.QRect(190, 230, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.sin_button.setFont(font)
        self.sin_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.sin_button.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);")
        self.sin_button.setObjectName("sin_button")
        self.cosh_button = QtWidgets.QPushButton(self.centralwidget)
        self.cosh_button.setGeometry(QtCore.QRect(390, 230, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.cosh_button.setFont(font)
        self.cosh_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.cosh_button.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);")
        self.cosh_button.setObjectName("cosh_button")
        self.tan_button = QtWidgets.QPushButton(self.centralwidget)
        self.tan_button.setGeometry(QtCore.QRect(290, 230, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.tan_button.setFont(font)
        self.tan_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tan_button.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);")
        self.tan_button.setObjectName("tan_button")
        self.mod_button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.mod_button_5.setGeometry(QtCore.QRect(290, 200, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.mod_button_5.setFont(font)
        self.mod_button_5.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.mod_button_5.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);")
        self.mod_button_5.setObjectName("mod_button_5")
        self.sinh_button = QtWidgets.QPushButton(self.centralwidget)
        self.sinh_button.setGeometry(QtCore.QRect(390, 200, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.sinh_button.setFont(font)
        self.sinh_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.sinh_button.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);")
        self.sinh_button.setObjectName("sinh_button")
        self.cos_button = QtWidgets.QPushButton(self.centralwidget)
        self.cos_button.setGeometry(QtCore.QRect(240, 230, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.cos_button.setFont(font)
        self.cos_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.cos_button.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);")
        self.cos_button.setObjectName("cos_button")
        self.mod_button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.mod_button_4.setGeometry(QtCore.QRect(240, 200, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.mod_button_4.setFont(font)
        self.mod_button_4.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.mod_button_4.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);")
        self.mod_button_4.setObjectName("mod_button_4")
        self.mod_button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.mod_button_6.setGeometry(QtCore.QRect(340, 230, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.mod_button_6.setFont(font)
        self.mod_button_6.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.mod_button_6.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);")
        self.mod_button_6.setObjectName("mod_button_6")
        self.tanh_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.tanh_button_2.setGeometry(QtCore.QRect(340, 200, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.tanh_button_2.setFont(font)
        self.tanh_button_2.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tanh_button_2.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);")
        self.tanh_button_2.setObjectName("tanh_button_2")
        self.mul_button = QtWidgets.QPushButton(self.centralwidget)
        self.mul_button.setGeometry(QtCore.QRect(130, 200, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.mul_button.setFont(font)
        self.mul_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.mul_button.setStyleSheet("gridline-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));\n"
"background-color: rgb(199, 199, 199);")
        self.mul_button.setObjectName("mul_button")
        self.subtract_button = QtWidgets.QPushButton(self.centralwidget)
        self.subtract_button.setGeometry(QtCore.QRect(80, 200, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.subtract_button.setFont(font)
        self.subtract_button.setStyleSheet("gridline-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));\n"
"background-color: rgb(199, 199, 199);")
        self.subtract_button.setObjectName("subtract_button")
        self.mod_button = QtWidgets.QPushButton(self.centralwidget)
        self.mod_button.setGeometry(QtCore.QRect(30, 230, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.mod_button.setFont(font)
        self.mod_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.mod_button.setStyleSheet("gridline-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));\n"
"background-color: rgb(199, 199, 199);")
        self.mod_button.setObjectName("mod_button")
        self.pow_button = QtWidgets.QPushButton(self.centralwidget)
        self.pow_button.setGeometry(QtCore.QRect(130, 230, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setKerning(True)
        self.pow_button.setFont(font)
        self.pow_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.pow_button.setStyleSheet("gridline-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));\n"
"background-color: rgb(199, 199, 199);")
        self.pow_button.setObjectName("pow_button")
        self.sum_button = QtWidgets.QPushButton(self.centralwidget)
        self.sum_button.setGeometry(QtCore.QRect(30, 200, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sum_button.setFont(font)
        self.sum_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.sum_button.setStyleSheet("gridline-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));\n"
"background-color: rgb(199, 199, 199);")
        self.sum_button.setObjectName("sum_button")
        self.div_button = QtWidgets.QPushButton(self.centralwidget)
        self.div_button.setGeometry(QtCore.QRect(80, 230, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.div_button.setFont(font)
        self.div_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.div_button.setStyleSheet("gridline-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));\n"
"background-color: rgb(199, 199, 199);")
        self.div_button.setObjectName("div_button")
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        self.menuCalculator = QtWidgets.QMenu(self.menubar)
        self.menuCalculator.setObjectName("menuCalculator")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)
        self.menuCalculator.addSeparator()
        self.menubar.addAction(self.menuCalculator.menuAction())

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.one_button.setText(_translate("Calculator", "1"))
        self.three_button.setText(_translate("Calculator", "3"))
        self.two_button.setText(_translate("Calculator", "2"))
        self.six_button.setText(_translate("Calculator", "6"))
        self.five_button.setText(_translate("Calculator", "5"))
        self.four_button.setText(_translate("Calculator", "4"))
        self.nine_button.setText(_translate("Calculator", "9"))
        self.eight_button.setText(_translate("Calculator", "8"))
        self.seven_button.setText(_translate("Calculator", "7"))
        self.backspace_button.setText(_translate("Calculator", "←"))
        self.dot_button.setText(_translate("Calculator", "."))
        self.zero_button.setText(_translate("Calculator", "0"))
        self.label_2.setText(_translate("Calculator", "The Amazing Calculator"))
        self.clear_button.setText(_translate("Calculator", "C"))
        self.mod_button_3.setText(_translate("Calculator", "|x|"))
        self.sin_button.setText(_translate("Calculator", "Sin"))
        self.cosh_button.setText(_translate("Calculator", "Cos"))
        self.tan_button.setText(_translate("Calculator", "Tan"))
        self.mod_button_5.setText(_translate("Calculator", "log"))
        self.sinh_button.setText(_translate("Calculator", "Sin"))
        self.cos_button.setText(_translate("Calculator", "Cos"))
        self.mod_button_4.setText(_translate("Calculator", "sqrt"))
        self.mod_button_6.setText(_translate("Calculator", "x-1"))
        self.tanh_button_2.setText(_translate("Calculator", "Tan"))
        self.mul_button.setText(_translate("Calculator", "*"))
        self.subtract_button.setText(_translate("Calculator", "-"))
        self.mod_button.setText(_translate("Calculator", "%"))
        self.pow_button.setText(_translate("Calculator", "x^y"))
        self.sum_button.setText(_translate("Calculator", "+"))
        self.div_button.setText(_translate("Calculator", "/"))
        self.menuCalculator.setTitle(_translate("Calculator", "Calculator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())