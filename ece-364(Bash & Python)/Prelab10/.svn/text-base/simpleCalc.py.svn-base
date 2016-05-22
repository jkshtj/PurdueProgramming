# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from calculator import *

##global vars
prev_pressed = "" ## global var, tracks the button that was pressed previous to the current button
exp = "" ## math expression built uptil now

class CalculatorConsumer(QMainWindow, Ui_Calculator):

    def __init__(self, parent=None):
        super(CalculatorConsumer, self).__init__(parent)
        self.setupUi(self)

        self.btn0.clicked.connect(lambda :self.updateScreen('0'))
        self.btn1.clicked.connect(lambda :self.updateScreen('1'))
        self.btn2.clicked.connect(lambda :self.updateScreen('2'))
        self.btn3.clicked.connect(lambda :self.updateScreen('3'))
        self.btn4.clicked.connect(lambda :self.updateScreen('4'))
        self.btn5.clicked.connect(lambda :self.updateScreen('5'))
        self.btn6.clicked.connect(lambda :self.updateScreen('6'))
        self.btn7.clicked.connect(lambda :self.updateScreen('7'))
        self.btn8.clicked.connect(lambda :self.updateScreen('8'))
        self.btn9.clicked.connect(lambda :self.updateScreen('9'))
        self.btnClear.clicked.connect(lambda :self.clearScreen())
        self.btnEqual.clicked.connect(lambda :self.updateScreen('='))
        self.btnDivide.clicked.connect(lambda :self.updateScreen('/'))
        self.btnMultiply.clicked.connect(lambda :self.updateScreen('*'))
        self.btnMinus.clicked.connect(lambda :self.updateScreen('-'))
        self.btnPlus.clicked.connect(lambda :self.updateScreen('+'))
        self.btnDot.clicked.connect(lambda :self.dot())


    def updateScreen(self,num):
        global prev_pressed
        global exp

        if num == "+" or num == "-" or num == "/" or num =="*":
            if exp != "":
                second = self.txtDisplay.text()
                exp += second
                self.eval()
            prev_pressed = num

        elif prev_pressed == '+' or prev_pressed == '-' or prev_pressed == '*' or prev_pressed == '/':
            operator = prev_pressed ## store operator value to be used later
            prev_pressed = "" ## clear the previous_pressed flag so that user can enter the second number which might be multiple digits
            first = self.txtDisplay.text()

            if self.chkSeparator.isChecked():
                self.txtDisplay.setText(('{:,.' + self.cboDecimal.currentText() + 'f}').format(float(num.replace(",",""))))
            else:
                self.txtDisplay.setText("%0.*f" % (int(self.cboDecimal.currentText()),float(num)))

            exp += first + " " + operator + " "  ## second num to be added when equal is pressed
            return

        elif num == "=":
            second = self.txtDisplay.text()
            exp += second
            self.eval()
            exp = ""
            prev_pressed = ""

        else:
            if len(self.txtDisplay.text()) == 12:
                return

            if self.txtDisplay.text() == '0.':
                self.txtDisplay.clear()
            str = self.txtDisplay.text()
            if str != "":
                str = str.split('.')[0]
                str = str.replace(',',"")
                str = float(str) * 10 + float(num)
            else:
                str += num

            final_str = "%0.*f" % (int(self.cboDecimal.currentText()),float(str))
            if self.chkSeparator.isChecked():
                self.txtDisplay.setText(('{:,.' + self.cboDecimal.currentText() + 'f}').format(float(final_str)))
            else:
                self.txtDisplay.setText(final_str)

    def clearScreen(self):
        self.txtDisplay.clear()



    def eval(self):
        global exp
        global prev_pressed

        self.clearScreen()
        list_args = exp.split()
        #print(list_args)

        if len(list_args) < 3: ## if 3 args not present clears exp and prev_pressed
            self.clearScreen()
            exp = ""
            prev_pressed = ""
            return

        exp = "" ## resetting exp for new calculations



        first = float(list_args[0].replace(',',""))
        second = float(list_args[2].replace(',',""))
        operator = list_args[1]

        if operator == '+':
            ans = first + second
        elif operator == '-':
            ans = first - second
        elif operator == '/':
            ans = first / second
        elif operator == '*':
            ans = first * second


        if self.chkSeparator.isChecked():
            self.txtDisplay.setText(('{:,.' + self.cboDecimal.currentText() + 'f}').format(float(ans)))
        else:
            self.txtDisplay.setText("%0.*f" % (int(self.cboDecimal.currentText()),float(ans)))


    def dot(self):
        self.updateScreen('.')



currentApp = QApplication(sys.argv)
currentForm = CalculatorConsumer()

currentForm.show()
currentApp.exec_()
