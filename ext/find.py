from PySide import QtGui, QtCore
from PySide.QtCore import Qt

import re

class Find(QtGui.QDialog):
    def __init__(self, parent = None):
        
        QtGui.QDialog.__init__(self, parent)
        
        self.parent = parent
        
        self.lastMatch = None
        
        self.initUI()
        
    def initUI(self):
        
        #Button to search the document
        findButton = QtGui.QPushButton("Find", self)
        findButton.clicked.connect(self.find)
        
        #Button to replace last found
        replaceButton = QtGui.QPushButton("Replace", self)
        replaceButton.clicked.connect(self.replace)
        
        allButton = QtGui.QPushButton("Replace all", self)
        allButton.clicked.connect(self.replaceAll)
        
        #Normal mode
        self.normalRadio = QtGui.QRadioButton("Normal", self)
        self.normalRadio.toggled.connect(self.normalMode)
        
        #Regex mode
        self.regexRadio = QtGui.QRadioButton("RegEx", self)
        self.regexRadio.toggled.connect(self.regexMode)
        
        #Search field
        self.findField = QtGui.QTextEdit(self)
        self.findField.resize(250,50)
        
        #Replace text field
        self.replaceField = QtGui.QTextEdit(self)
        self.replaceField.resize(250,50)
        
        optionsLabel = QtGui.QLabel("Options: ", self)
        
        #Case sensitive
        self.caseSens = QtGui.QCheckBox("Case sensitive", self)
        
        #Whole word
        self.wholeWords = QtGui.QCheckBox("Whole words", self)
        
        #Laying out objects on the screen
        layout = QtGui.QGridLayout()
        
        layout.addWidget(self.findField, 1,0,1,4)
        layout.addWidget(self.normalRadio, 2,2)
        layout.addWidget(self.regexRadio, 2,3)
        layout.addWidget(findButton, 2,0,1,2)
        
        layout.addWidget(self.replaceField, 3,0,1,4)
        layout.addWidget(replaceButton, 4,0,1,2)
        layout.addWidget(allButton, 4,2,1,2)
        
        #Adds spacing
        spacer = QtGui.QWidget(self)
        
        spacer.setFixedSize(0,10)
        
        layout.addWidget(spacer, 5,0)
        
        layout.addWidget(optionsLabel, 6,0)
        layout.addWidget(self.caseSens, 6,1)
        layout.addWidget(self.wholeWords, 6,2)
        
        self.setGeometry(300, 300, 360, 250)
        self.setWindowTitle("Find and Replace")
        self.setLayout(layout)
        
        #Normal mode is default
        self.normalRadio.setChecked(True)
        
    def find(self):
        
        #Grab parent's text
        text = self.parent.text.toPlainText()
        
        query = self.findField.toPlainText()
        
        if self.wholeWords.isChecked():
            query = r'\W' + query + r'\W'
        
        flags = 0 if self.caseSens.isChecked() else re.I
        
        pattern = re.compile(query, flags)
        
        start = self.lastMatch.start() + 1 if self.lastMatch else 0
        
        self.lastMatch = pattern.search(text, start)
        
        if self.lastMatch:
            
            start = self.lastMatch.start()
            end = self.lastMatch.end()
            
            if self.wholeWords.isChecked():
                start += 1
                end -= 1
                
            self.moveCursor(start, end)
            
        else:
            
            self.parent.text.moveCursor(QtGui.QTextCursor.End)
            
    def replace(self):
        
        cursor = self.parent.text.textCursor()
        
        if self.lastMatch and cursor.hasSelection():
            
            cursor.insertText(self.replaceField.toPlainText())
            
            self.find()
            
            while self.lastMatch:
                self.replace()
                self.find()
                
    def replaceAll(self):
         
         self.lastMatch = None
         
         self.find()
         
         while self.lastMatch:
             self.replace()
             self.find()
    
    def regexMode(self):
        
        self.caseSens.setChecked(False)
        self.wholeWords.setChecked(False)
        
        self.caseSens.setEnabled(False)
        self.wholeWords.setEnabled(False)
        
    def normalMode(self):
        
        self.caseSens.setEnabled(True)
        self.wholeWords.setEnabled(True)
        
    def moveCursor(self, start, end):
        
        cursor = self.parent.text.textCursor()
        
        cursor.setPosition(start)
        
        cursor.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor, end - start)
        
        self.parent.text.setTextCursor(cursor)
