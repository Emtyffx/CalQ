from cProfile import label
from decimal import DivisionByZero
from PyQt5 import QtWidgets
from calculator import Ui_CalQ  # импорт нашего сгенерированного файла
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_CalQ()
        self.ui.setupUi(self)
        self.calculable = ""

        self.ui.button_zero.clicked.connect(self.zero)
        self.ui.button_one.clicked.connect(self.one)
        self.ui.button_two.clicked.connect(self.two)
        self.ui.button_three.clicked.connect(self.three)
        self.ui.button_four.clicked.connect(self.four)
        self.ui.button_five.clicked.connect(self.five)
        self.ui.button_six.clicked.connect(self.six)
        self.ui.button_seven.clicked.connect(self.seven)
        self.ui.button_eight.clicked.connect(self.eight)
        self.ui.button_nine.clicked.connect(self.nine)
        self.ui.button_bs.clicked.connect(self.bs)
        self.ui.button_escape.clicked.connect(self.escape)
        self.ui.button_dot.clicked.connect(self.dot)
        self.ui.button_eq.clicked.connect(self.equals)
        self.ui.button_plus.clicked.connect(self.plus)
        self.ui.button_minus.clicked.connect(self.minus)
        self.ui.button_x.clicked.connect(self.multiplication)
        self.ui.button_div.clicked.connect(self.division)
        self.ui.button_lw.clicked.connect(self.lw)
        self.ui.button_rw.clicked.connect(self.rw)
    def nine(self):
        self.calculable += "9"
        self.ui.calculate.setText(self.calculable)

    def zero(self):

        self.calculable += "0"
        self.ui.calculate.setText(self.calculable)

    def one(self):
        self.calculable += "1"
        self.ui.calculate.setText(self.calculable)

    def two(self):
        self.calculable += "2"
        self.ui.calculate.setText(self.calculable)

    def three(self):
        self.calculable += "3"
        self.ui.calculate.setText(self.calculable)

    def four(self):
        self.calculable += "4"
        self.ui.calculate.setText(self.calculable)

    def five(self):
        self.calculable += "5"
        self.ui.calculate.setText(self.calculable)

    def six(self):
        self.calculable += "6"
        self.ui.calculate.setText(self.calculable)

    def seven(self):
        self.calculable += "7"
        self.ui.calculate.setText(self.calculable)

    def eight(self):
        self.calculable += "8"
        self.ui.calculate.setText(self.calculable)

    def nine(self):
        self.calculable += "9"
        self.ui.calculate.setText(self.calculable)

    def minus(self):
        self.calculable += "-"
        self.ui.calculate.setText(self.calculable)

    def plus(self):
        self.calculable += "+"
        self.ui.calculate.setText(self.calculable)

    def multiplication(self):
        self.calculable += "*"
        self.ui.calculate.setText(self.calculable)

    def division(self):
        self.calculable += "/"
        self.ui.calculate.setText(self.calculable)

    def dot(self):
        self.calculable += "."
        self.ui.calculate.setText(self.calculable)

    def bs(self):
        self.calculable = self.calculable[:-1]
        self.ui.calculate.setText(self.calculable)
    def escape(self):
        self.calculable = ""
        self.ui.calculate.setText(self.calculable)

    def lw(self):
        self.calculable += "("
        self.ui.calculate.setText(self.calculable)

    def rw(self):
        self.calculable += ")"
        self.ui.calculate.setText(self.calculable)

    def equals(self):
        if self.calculable == ".(1)":
            self.calculable = ""
            self.ui.calculate.setText("Made by WreckCrack")
        elif self.calculable == ".(2)":
            self.calculable = ""
            self.ui.calculate.setText("CalQ v1.0")
        elif self.calculable == ".(3)":
            self.calculable = ""
            self.ui.calculate.setText("Wish you luck")


        else:
            try:
                res = eval(self.calculable)
            except SyntaxError:
                self.ui.calculate.setText("Incorrect input")
                self.calculable = ""
            except ZeroDivisionError:
                self.ui.calculate.setText("Div by 0")
                self.calculable = ""
            else:
                self.calculable=str(round(float(res),6))
                self.ui.calculate.setText("="+self.calculable)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
