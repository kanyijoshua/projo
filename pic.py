import sys
from  PyQt5.QtWidgets import *
from  PyQt5.QtGui import *
class wes(QWidget):
    def __init__(self):
        super().__init__()
        self.title='kanyi wewr'
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(10, 10, 740, 500)
        label=QLabel(self)
        pic=QPixmap('kanyi.png')
        label.setPixmap(pic)
        self.show()
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=wes()
    sys.exit(app.exec_())




