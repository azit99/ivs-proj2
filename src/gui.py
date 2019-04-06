from PyQt5 import QtCore, QtGui, QtWidgets, uic


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
        self.display.setText(self.display.text() + "/")

    def btnMultiplicationClicked(self):
        self.display.setText(self.display.text() + "*")

    def btnCommaClicked(self):
        self.display.setText(self.display.text() + ",")

    def btnEqualsClicked(self):
        print("process with string parser")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
