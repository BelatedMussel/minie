from PySide import QtGui, QtCore
from PySide.QtCore import Qt

from time import strftime

class DateTime(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        
        self.parent = parent
        
        self.formats = ["%A, %d. %B %Y %H:%M",
                        "%A, %d. %B %Y",
                        "%d. %B %Y %H:%M",
                        "%d.%m.%Y %H:%M",
                        "%d. %B %Y",
                        "%d %m %Y",
                        "%d.%m.%Y",
                        "%x",
                        "%X",
                        "%H:%M"]
        
        self.initUI()
        
    def initUI(self):
        
        self.box = QtGui.QComboBox(self)
        
        for i in self.formats:
            self.box.addItem(strftime(i))
            
        insert = QtGui.QPushButton("Insert", self)
        insert.clicked.connect(self.insert)
        
        cancel = QtGui.QPushButton("Cancel", self)
        cancel.clicked.connect(self.close)
        
        layout = QtGui.QGridLayout()
        
        layout.addWidget(self.box, 0,0,1,2)
        layout.addWidget(insert, 1,0)
        layout.addWidget(cancel, 1,1)
        
        self.setGeometry(300,300,400,80)
        self.setWindowTitle("Date and Time")
        self.setLayout(layout)
        
    def insert(self):
        cursor = self.parent.text.textCursor()
        
        datetime = strftime(self.formats[self.box.currentIndex()])
        
        cursor.insertText(datetime)
        
        self.close()
