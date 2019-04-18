from PyQt5 import QtCore, QtGui, QtWidgets, uic
from expresion_eval import EvaluateStrExp as evalexp

helpMessage = """<center><b>How to use Tractorator</b></center>
<ul>
<li>Click on buttons to create expression</li>
<li>Click on '=' button to calculate expression</li>
<li>The result will be displayed in the text box located above the buttons</li>
</ul>"""


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("gui.ui", self)

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
