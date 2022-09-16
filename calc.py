import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon


class MyCalc(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('calculator.ui', self)
        self.setWindowIcon(QIcon('калькулятор.ico'))
        self.setWindowTitle('Калькулятор')
        self.label.setText('0')

        self.btn_0.clicked.connect(self.write_number)
        self.btn_1.clicked.connect(self.write_number)
        self.btn_2.clicked.connect(self.write_number)
        self.btn_3.clicked.connect(self.write_number)
        self.btn_4.clicked.connect(self.write_number)
        self.btn_5.clicked.connect(self.write_number)
        self.btn_6.clicked.connect(self.write_number)
        self.btn_7.clicked.connect(self.write_number)
        self.btn_8.clicked.connect(self.write_number)
        self.btn_9.clicked.connect(self.write_number)

        self.btn_C.clicked.connect(self.write_sign)
        self.btn_backspace.clicked.connect(self.write_sign)
        self.btn_point.clicked.connect(self.write_sign)
        self.btn_plus.clicked.connect(self.write_sign)
        self.btn_minus.clicked.connect(self.write_sign)
        self.btn_plus_minus.clicked.connect(self.write_sign)
        self.btn_mult.clicked.connect(self.write_sign)
        self.btn_div.clicked.connect(self.write_sign)

        self.btn_iseq.clicked.connect(self.results)

    def write_number(self):
        num = self.sender().text()
        text = self.label.text()
        if 'ZeroDivisionError' in text:
            self.label.setText('0')
            return
        self.label.setText(num) if text == '0' \
            else self.label.setText(f'{text}{num}')

    def write_sign(self):
        sign = self.sender().text()
        text = self.label.text()
        if sign == '+/-':
            sign = '_'

        if 'ZeroDivisionError' in text:
            self.label.setText('0')
            return

        if sign == '_':
            try:
                if text[-1] != '.':
                    self.label.setText(f'-{text}') if float(text) > 0\
                        else self.label.setText(text[1:])
            except Exception:
                pass
            return

        elif sign == '.':
            t = text
            for i in range(len(t)):
                if t[i] in '+-*/':
                    t = t.replace(t[i], '!')
            t = t.split('!')
            if '.' in t[-1]:
                return

        elif sign == 'C':
            self.label.setText('0')
            return

        elif sign == '<-':
            self.label.setText(text[:-1]) if len(text) > 1\
                else self.label.setText('0')
            return

        if text[-1] in '+-*/.' and sign in '+-*/.':
            return

        else:
            self.label.setText(text + sign)

    def results(self):
        if self.label.text()[-1] in '+-*/.':
            return
        try:
            res = str(eval(self.label.text()))
        except ZeroDivisionError:
            res = 'ZeroDivisionError'
        self.label.setText(res)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyCalc()
    MainWindow.show()
    sys.exit(app.exec_())
