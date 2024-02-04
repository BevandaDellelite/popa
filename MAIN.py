from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow


from random import *
class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.example)
    def example(self):
        signs = ''
        if self.ui.checkBox.isChecked():
            sings = 'qwertyuiopasdfghjklzxcvbnm'
        if self.ui.checkBox_2.isChecked():
            sings += '1234567890'


        result = ''
        for i in range(10)
            result += choice(sings)
        self.ui.label_2.setText(result)
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
