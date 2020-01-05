from PyQt5.QtWidgets import QApplication, QDialog
from ui_about_author import Ui_About_Author_Dialog


class AboutAuthorDialog(QDialog, Ui_About_Author_Dialog):
    def __init__(self, parent=0):#定义了一个初始化的东西
        super().__init__()
        self.setupUi(self)#self就是类自己，调用了setupUi方法，而setupUi在ui_About_Author.py里面第14行。

#所以aboutauthor.py就可以调用自己