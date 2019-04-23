from PyQt5 import QtCore, QtGui, QtWidgets
from expresion_eval import EvaluateStrExp as evalexp

helpMessage = """<center><b>How to use Tractorator</b></center>
<ul>
<li>Click on buttons to create expression</li>
<li>Click on '=' button to calculate expression</li>
<li>The result will be displayed in the text box located above the buttons</li>
</ul>"""


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(261, 340)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(230, 270))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnParenthesisRight = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnParenthesisRight.sizePolicy().hasHeightForWidth())
        self.btnParenthesisRight.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnParenthesisRight.setFont(font)
        self.btnParenthesisRight.setObjectName("btnParenthesisRight")
        self.gridLayout.addWidget(self.btnParenthesisRight, 1, 3, 1, 1)
        self.btnMultiplication = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnMultiplication.sizePolicy().hasHeightForWidth())
        self.btnMultiplication.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnMultiplication.setFont(font)
        self.btnMultiplication.setObjectName("btnMultiplication")
        self.gridLayout.addWidget(self.btnMultiplication, 4, 3, 1, 1)
        self.btnFive = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnFive.sizePolicy().hasHeightForWidth())
        self.btnFive.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnFive.setFont(font)
        self.btnFive.setObjectName("btnFive")
        self.gridLayout.addWidget(self.btnFive, 4, 1, 1, 1)
        self.btnParenthesisLeft = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnParenthesisLeft.sizePolicy().hasHeightForWidth())
        self.btnParenthesisLeft.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnParenthesisLeft.setFont(font)
        self.btnParenthesisLeft.setObjectName("btnParenthesisLeft")
        self.gridLayout.addWidget(self.btnParenthesisLeft, 1, 2, 1, 1)
        self.btnEquals = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnEquals.sizePolicy().hasHeightForWidth())
        self.btnEquals.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnEquals.setFont(font)
        self.btnEquals.setObjectName("btnEquals")
        self.gridLayout.addWidget(self.btnEquals, 6, 3, 1, 2)
        self.btnTwo = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnTwo.sizePolicy().hasHeightForWidth())
        self.btnTwo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnTwo.setFont(font)
        self.btnTwo.setObjectName("btnTwo")
        self.gridLayout.addWidget(self.btnTwo, 3, 1, 1, 1)
        self.btnComma = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnComma.sizePolicy().hasHeightForWidth())
        self.btnComma.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnComma.setFont(font)
        self.btnComma.setObjectName("btnComma")
        self.gridLayout.addWidget(self.btnComma, 6, 0, 1, 1)
        self.btnNine = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnNine.sizePolicy().hasHeightForWidth())
        self.btnNine.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnNine.setFont(font)
        self.btnNine.setObjectName("btnNine")
        self.gridLayout.addWidget(self.btnNine, 5, 2, 1, 1)
        self.btnOne = QtWidgets.QPushButton(self.centralwidget)
        self.btnOne.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnOne.sizePolicy().hasHeightForWidth())
        self.btnOne.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnOne.setFont(font)
        self.btnOne.setObjectName("btnOne")
        self.gridLayout.addWidget(self.btnOne, 3, 0, 1, 1)
        self.btnMinus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnMinus.sizePolicy().hasHeightForWidth())
        self.btnMinus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnMinus.setFont(font)
        self.btnMinus.setObjectName("btnMinus")
        self.gridLayout.addWidget(self.btnMinus, 5, 4, 1, 1)
        self.btnDivision = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnDivision.sizePolicy().hasHeightForWidth())
        self.btnDivision.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnDivision.setFont(font)
        self.btnDivision.setObjectName("btnDivision")
        self.gridLayout.addWidget(self.btnDivision, 4, 4, 1, 1)
        self.display = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.display.sizePolicy().hasHeightForWidth())
        self.display.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.display.setFont(font)
        self.display.setReadOnly(True)
        self.display.setObjectName("display")
        self.gridLayout.addWidget(self.display, 0, 0, 1, 5)
        self.btnPlus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnPlus.sizePolicy().hasHeightForWidth())
        self.btnPlus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnPlus.setFont(font)
        self.btnPlus.setObjectName("btnPlus")
        self.gridLayout.addWidget(self.btnPlus, 5, 3, 1, 1)
        self.btnEight = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnEight.sizePolicy().hasHeightForWidth())
        self.btnEight.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnEight.setFont(font)
        self.btnEight.setObjectName("btnEight")
        self.gridLayout.addWidget(self.btnEight, 5, 1, 1, 1)
        self.btnRoot = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnRoot.sizePolicy().hasHeightForWidth())
        self.btnRoot.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnRoot.setFont(font)
        self.btnRoot.setObjectName("btnRoot")
        self.gridLayout.addWidget(self.btnRoot, 6, 2, 1, 1)
        self.btnFactorial = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnFactorial.sizePolicy().hasHeightForWidth())
        self.btnFactorial.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnFactorial.setFont(font)
        self.btnFactorial.setObjectName("btnFactorial")
        self.gridLayout.addWidget(self.btnFactorial, 3, 3, 1, 1)
        self.btnModulo = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnModulo.sizePolicy().hasHeightForWidth())
        self.btnModulo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnModulo.setFont(font)
        self.btnModulo.setObjectName("btnModulo")
        self.gridLayout.addWidget(self.btnModulo, 3, 4, 1, 1)
        self.btnFour = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnFour.sizePolicy().hasHeightForWidth())
        self.btnFour.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnFour.setFont(font)
        self.btnFour.setObjectName("btnFour")
        self.gridLayout.addWidget(self.btnFour, 4, 0, 1, 1)
        self.btnSeven = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnSeven.sizePolicy().hasHeightForWidth())
        self.btnSeven.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnSeven.setFont(font)
        self.btnSeven.setObjectName("btnSeven")
        self.gridLayout.addWidget(self.btnSeven, 5, 0, 1, 1)
        self.btnZero = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnZero.sizePolicy().hasHeightForWidth())
        self.btnZero.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnZero.setFont(font)
        self.btnZero.setObjectName("btnZero")
        self.gridLayout.addWidget(self.btnZero, 6, 1, 1, 1)
        self.btnExponentiation = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnExponentiation.sizePolicy().hasHeightForWidth())
        self.btnExponentiation.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnExponentiation.setFont(font)
        self.btnExponentiation.setObjectName("btnExponentiation")
        self.gridLayout.addWidget(self.btnExponentiation, 1, 4, 1, 1)
        self.btnSix = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnSix.sizePolicy().hasHeightForWidth())
        self.btnSix.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnSix.setFont(font)
        self.btnSix.setObjectName("btnSix")
        self.gridLayout.addWidget(self.btnSix, 4, 2, 1, 1)
        self.btnThree = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnThree.sizePolicy().hasHeightForWidth())
        self.btnThree.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnThree.setFont(font)
        self.btnThree.setObjectName("btnThree")
        self.gridLayout.addWidget(self.btnThree, 3, 2, 1, 1)
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnClear.sizePolicy().hasHeightForWidth())
        self.btnClear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        self.gridLayout.addWidget(self.btnClear, 1, 0, 1, 1)
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnBack.sizePolicy().hasHeightForWidth())
        self.btnBack.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        self.gridLayout.addWidget(self.btnBack, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 261, 18))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnOne.clicked.connect(self.btnOneClicked)
        self.btnTwo.clicked.connect(self.btnTwoClicked)
        self.btnThree.clicked.connect(self.btnThreeClicked)
        self.btnFour.clicked.connect(self.btnFourClicked)
        self.btnFive.clicked.connect(self.btnFiveClicked)
        self.btnSix.clicked.connect(self.btnSixClicked)
        self.btnSeven.clicked.connect(self.btnSevenClicked)
        self.btnEight.clicked.connect(self.btnEightClicked)
        self.btnNine.clicked.connect(self.btnNineClicked)
        self.btnZero.clicked.connect(self.btnZeroClicked)
        self.btnPlus.clicked.connect(self.btnPlusClicked)
        self.btnMinus.clicked.connect(self.btnMinusClicked)
        self.btnDivision.clicked.connect(self.btnDivisionClicked)
        self.btnMultiplication.clicked.connect(self.btnMultiplicationClicked)
        self.btnComma.clicked.connect(self.btnCommaClicked)
        self.btnEquals.clicked.connect(self.btnEqualsClicked)
        self.btnBack.clicked.connect(self.btnBackClicked)
        self.btnExponentiation.clicked.connect(self.btnExponentiationClicked)
        self.btnRoot.clicked.connect(self.btnRootClicked)
        self.btnFactorial.clicked.connect(self.btnFactorialClicked)
        self.btnModulo.clicked.connect(self.btnModuloClicked)
        self.btnParenthesisRight.clicked.connect(
            self.btnParenthesisRightClicked)
        self.btnParenthesisLeft.clicked.connect(self.btnParenthesisLeftClicked)
        self.btnClear.clicked.connect(self.btnClearClicked)
        self.actionHelp.triggered.connect(self.menuHelpClicked)

    def btnOneClicked(self):
        self.display.setText(self.display.text() + "1")

    def btnTwoClicked(self):
        self.display.setText(self.display.text() + "2")

    def btnThreeClicked(self):
        self.display.setText(self.display.text() + "3")

    def btnFourClicked(self):
        self.display.setText(self.display.text() + "4")

    def btnFiveClicked(self):
        self.display.setText(self.display.text() + "5")

    def btnSixClicked(self):
        self.display.setText(self.display.text() + "6")

    def btnSevenClicked(self):
        self.display.setText(self.display.text() + "7")

    def btnEightClicked(self):
        self.display.setText(self.display.text() + "8")

    def btnNineClicked(self):
        self.display.setText(self.display.text() + "9")

    def btnZeroClicked(self):
        self.display.setText(self.display.text() + "0")

    def btnPlusClicked(self):
        self.display.setText(self.display.text() + "+")

    def btnMinusClicked(self):
        self.display.setText(self.display.text() + "−")

    def btnDivisionClicked(self):
        self.display.setText(self.display.text() + "÷")

    def btnMultiplicationClicked(self):
        self.display.setText(self.display.text() + "×")

    def btnCommaClicked(self):
        self.display.setText(self.display.text() + ".")

    def btnEqualsClicked(self):
        self.display.setText(evalexp(self.display.text()))

    def btnBackClicked(self):
        self.display.setText(self.display.text()[:-1])

    def btnExponentiationClicked(self):
        self.display.setText(self.display.text() + "^")

    def btnRootClicked(self):
        self.display.setText(self.display.text() + "√")

    def btnFactorialClicked(self):
        self.display.setText(self.display.text() + "!")

    def btnModuloClicked(self):
        self.display.setText(self.display.text() + "%")

    def btnParenthesisLeftClicked(self):
        self.display.setText(self.display.text() + "(")

    def btnParenthesisRightClicked(self):
        self.display.setText(self.display.text() + ")")

    def btnClearClicked(self):
        self.display.setText("")

    def menuHelpClicked(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(helpMessage)
        msgBox.setWindowTitle("Help")
        msgBox.setTextFormat(1)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Close)
        msgBox.exec()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tractorator"))
        self.btnParenthesisRight.setText(_translate("MainWindow", ")"))
        self.btnMultiplication.setText(_translate("MainWindow", "×"))
        self.btnFive.setText(_translate("MainWindow", "5"))
        self.btnParenthesisLeft.setText(_translate("MainWindow", "("))
        self.btnEquals.setText(_translate("MainWindow", "="))
        self.btnTwo.setText(_translate("MainWindow", "2"))
        self.btnComma.setText(_translate("MainWindow", "."))
        self.btnNine.setText(_translate("MainWindow", "9"))
        self.btnOne.setText(_translate("MainWindow", "1"))
        self.btnMinus.setText(_translate("MainWindow", "−"))
        self.btnDivision.setText(_translate("MainWindow", "÷"))
        self.btnPlus.setText(_translate("MainWindow", "+"))
        self.btnEight.setText(_translate("MainWindow", "8"))
        self.btnRoot.setText(_translate("MainWindow", "n√"))
        self.btnFactorial.setText(_translate("MainWindow", "x!"))
        self.btnModulo.setText(_translate("MainWindow", "%"))
        self.btnFour.setText(_translate("MainWindow", "4"))
        self.btnSeven.setText(_translate("MainWindow", "7"))
        self.btnZero.setText(_translate("MainWindow", "0"))
        self.btnExponentiation.setText(_translate("MainWindow", "^"))
        self.btnSix.setText(_translate("MainWindow", "6"))
        self.btnThree.setText(_translate("MainWindow", "3"))
        self.btnClear.setText(_translate("MainWindow", "C"))
        self.btnBack.setText(_translate("MainWindow", "←"))
        self.menuHelp.setTitle(_translate("MainWindow", "File"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
