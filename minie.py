#!/usr/bin/python

import sys
from PySide import QtGui, QtCore, QtUiTools
from PySide.QtCore import Qt, QXmlStreamAttributes
from ext import *

class Main(QtGui.QMainWindow):
    
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        
        self.fname = ("") #filename
        
        self.initUI()
    
    def initToolbar(self):
        
        self.printAction = QtGui.QAction(QtGui.QIcon.fromTheme("document-print"), "Print document", self)
        self.printAction.setStatusTip("Print document")
        self.printAction.setShortcut("Ctrl+P")
        self.printAction.triggered.connect(self.prints)
        
        self.previewAction = QtGui.QAction(QtGui.QIcon.fromTheme("document-print-preview"), "Page view", self)
        self.previewAction.setStatusTip("Preview page before printing")
        self.previewAction.setShortcut("Ctrl+Shift+P")
        self.previewAction.triggered.connect(self.preview)
        
        self.newAction = QtGui.QAction(QtGui.QIcon.fromTheme("document-new"), "New", self)
        self.newAction.setStatusTip("Create a new document.")
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.triggered.connect(self.new)
        
        self.openAction = QtGui.QAction(QtGui.QIcon.fromTheme("document-open"), "Open file", self)
        self.openAction.setStatusTip("Open an existing document.")
        self.openAction.setShortcut("Ctrl+O")
        #self.openAction.triggered.connect(self.open)
        self.openAction.triggered.connect(self.showDialogOpen)
        
        self.saveAsAction = QtGui.QAction(QtGui.QIcon.fromTheme("document-save-as"), "Save As", self)
        self.saveAsAction.setStatusTip("Save document as")
        self.saveAsAction.setShortcut("Ctrl+Shift+S")
        self.saveAsAction.triggered.connect(self.saveAs)
        
        self.saveAction = QtGui.QAction(QtGui.QIcon.fromTheme("document-save"), "Save", self)
        self.saveAction.setStatusTip("Save document as")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save)
        
        self.cutAction = QtGui.QAction(QtGui.QIcon.fromTheme("edit-cut"), "Cut", self)
        self.cutAction.setStatusTip("Delete and copy text to clipboard")
        self.cutAction.setShortcut("Ctrl+X")
        self.cutAction.triggered.connect(self.text.cut)
        
        self.copyAction = QtGui.QAction(QtGui.QIcon.fromTheme("edit-copy"), "Copy", self)
        self.copyAction.setStatusTip("Copy text to clipboard")
        self.copyAction.setShortcut("Ctrl+C")
        self.copyAction.triggered.connect(self.text.copy)
        
        self.pasteAction = QtGui.QAction(QtGui.QIcon.fromTheme("edit-paste"), "Paste", self)
        self.pasteAction.setStatusTip("Paste text from clipboard")
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.triggered.connect(self.text.paste)
        
        self.undoAction = QtGui.QAction(QtGui.QIcon.fromTheme("edit-undo"), "Undo", self)
        self.undoAction.setStatusTip("Undo last action")
        self.undoAction.setShortcut("Ctrl+Z")
        self.undoAction.triggered.connect(self.text.undo)
        
        self.redoAction = QtGui.QAction(QtGui.QIcon.fromTheme("edit-redo"), "Redo", self)
        self.redoAction.setStatusTip("Redo last undone action")
        self.redoAction.setShortcut("Ctrl+Y")
        self.redoAction.triggered.connect(self.text.redo)
        
        self.bulletAction = QtGui.QAction("Insert bullet List", self)
        self.bulletAction.setStatusTip("Insert bullet list")
        self.bulletAction.setShortcut("Ctrl+Shift+B")
        self.bulletAction.triggered.connect(self.bulletList)
        
        self.numberedAction = QtGui.QAction("Insert numbered List", self)
        self.numberedAction.setStatusTip("Insert numbered list")
        self.numberedAction.setShortcut("Ctrl+Shift+L")
        self.numberedAction.triggered.connect(self.numberList)
        
        self.findAction = QtGui.QAction(QtGui.QIcon.fromTheme("edit-find"), "Find and replace", self)
        self.findAction.setStatusTip("Find and replace words in your document")
        self.findAction.setShortcut("Ctrl+F")
        self.findAction.triggered.connect(find.Find(self).show)
        
        self.wordCountAction = QtGui.QAction("Word count", self)
        self.wordCountAction.setStatusTip("See word/character count")
        self.wordCountAction.setShortcut("Ctrl+W")
        self.wordCountAction.triggered.connect(self.wordCount)
        
        self.dateTimeAction = QtGui.QAction(QtGui.QIcon.fromTheme("appointment-new"), "Insert date and time", self)
        self.dateTimeAction.setStatusTip("Insert current date and time")
        self.dateTimeAction.setShortcut("Ctrl+D")
        self.dateTimeAction.triggered.connect(datetime.DateTime(self).show)
        
        self.toolbar = self.addToolBar("Options")
        
        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAsAction)
        self.toolbar.addAction(self.saveAction)
        
        self.toolbar.addSeparator()
        
        self.toolbar.addAction(self.printAction)
        self.toolbar.addAction(self.previewAction)
        
        self.toolbar.addSeparator()
        
        self.toolbar.addAction(self.cutAction)
        self.toolbar.addAction(self.copyAction)
        self.toolbar.addAction(self.pasteAction)
        self.toolbar.addAction(self.undoAction)
        self.toolbar.addAction(self.redoAction)
        
        self.toolbar.addSeparator()
        
        self.toolbar.addAction(self.findAction)
        self.toolbar.addAction(self.dateTimeAction)
        
        #self.addToolBarBreak()
        
    def initFormatbar(self):
        
        #doesn't play nicely with fontBox
        #self.formatFont = QtGui.QAction('Font...', self)
        #self.formatFont.setStatusTip("Format font")
        #self.formatFont.triggered.connect(self.showFontDialog)
        
        fontBox = QtGui.QFontComboBox(self)
        fontBox.currentFontChanged.connect(self.fontFamily)
        
        fontSize = QtGui.QComboBox(self)
        fontSize.setEditable(True)
        
        fontSize.setMinimumContentsLength(3)
        
        fontSize.editTextChanged.connect(self.fontSize)
        
        fontSizes = ['6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '18', '20', '22', '24', '26', '28', '32', '36', '40', '44', '48', '54', '60', '66', '72', '80', '88', '96']
        
        for i in fontSizes:
            fontSize.addItem(i)
        
        fontSize.setCurrentIndex(6)
        
        self.fontColor = QtGui.QAction("Change font color", self)
        self.fontColor.setShortcut("Ctrl+Shift+F")
        self.fontColor.setStatusTip("Change the font color")
        self.fontColor.triggered.connect(self.fontColors)
        
        self.backColor = QtGui.QAction("Change background color", self)
        self.backColor.setShortcut("Ctrl+Shift+H")
        self.backColor.setStatusTip("Changes text background color/highlight")
        self.backColor.triggered.connect(self.highlight)
        
        self.boldAction = QtGui.QAction(QtGui.QIcon.fromTheme("format-text-bold"), "Bold", self)
        self.boldAction.setShortcut("Ctrl+B")
        self.boldAction.triggered.connect(self.bold)
        
        self.italicAction = QtGui.QAction(QtGui.QIcon.fromTheme("format-text-italic"), "Italic", self)
        self.italicAction.setShortcut("Ctrl+I")
        self.italicAction.triggered.connect(self.italic)
        
        self.underlAction = QtGui.QAction(QtGui.QIcon.fromTheme("format-text-underline"), "Underline", self)
        self.underlAction.setShortcut("Ctrl+U")
        self.underlAction.triggered.connect(self.underline)
        
        self.strikeAction = QtGui.QAction(QtGui.QIcon.fromTheme("format-text-strikethrough"), "Strikethrough", self)
        self.strikeAction.setShortcut("Ctrl+T")
        self.strikeAction.triggered.connect(self.strike)
        
        self.superAction = QtGui.QAction("Superscript", self)
        self.superAction.setShortcut("Ctrl+Shift+=")
        self.superAction.triggered.connect(self.superScript)
        
        self.subAction = QtGui.QAction("Subscript", self)
        self.subAction.setShortcut("Ctrl+-")
        self.subAction.triggered.connect(self.subScript)
        
        self.alignLeft = QtGui.QAction(QtGui.QIcon.fromTheme("format-justify-left"), "Align left", self)
        self.alignLeft.setShortcut("Ctrl+L")
        self.alignLeft.triggered.connect(self.alignsLeft)
        
        self.alignCenter = QtGui.QAction(QtGui.QIcon.fromTheme("format-justify-center"), "Align center", self)
        self.alignCenter.setShortcut("Ctrl+M")
        self.alignCenter.triggered.connect(self.alignsCenter)
        
        self.alignRight = QtGui.QAction(QtGui.QIcon.fromTheme("format-justify-right"), "Align right", self)
        self.alignRight.setShortcut("Ctrl+R")
        self.alignRight.triggered.connect(self.alignsRight)
        
        self.alignJustify = QtGui.QAction(QtGui.QIcon.fromTheme("format-justify-fill"), "Align justify", self)
        self.alignJustify.setShortcut("Ctrl+J")
        self.alignJustify.triggered.connect(self.alignsJustify)
        
        self.formatbar = self.addToolBar("Format")
        
        self.formatbar.addWidget(fontBox)
        self.formatbar.addWidget(fontSize)
        
        self.formatbar.addSeparator()
        
        self.formatbar.addAction(self.boldAction)
        self.formatbar.addAction(self.italicAction)
        self.formatbar.addAction(self.underlAction)
        self.formatbar.addAction(self.strikeAction)
        
        self.formatbar.addSeparator()
        
        self.formatbar.addAction(self.alignLeft)
        self.formatbar.addAction(self.alignCenter)
        self.formatbar.addAction(self.alignRight)
        self.formatbar.addAction(self.alignJustify)
        
        self.formatbar.addSeparator()
        
    def initMenubar(self):
        
        menubar = self.menuBar()
        
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        formating = menubar.addMenu("Format")
        fontmenu = formating.addMenu("Font Effects")
        alignment = formating.addMenu("Alginment")
        tools = menubar.addMenu("Tools")
        view = menubar.addMenu("View")
        
        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAsAction)
        file.addAction(self.saveAction)
        file.addAction(self.printAction)
        file.addAction(self.previewAction)
        
        edit.addAction(self.undoAction)
        edit.addAction(self.redoAction)
        edit.addAction(self.cutAction)
        edit.addAction(self.copyAction)
        edit.addAction(self.pasteAction)
        
        #formating.addAction(self.formatFont) was to bring up a font format window, it did not play nicely with the scroll box
        formating.addAction(self.bulletAction)
        formating.addAction(self.numberedAction)
        formating.addAction(self.fontColor)
        formating.addAction(self.backColor)
        
        fontmenu.addAction(self.boldAction)
        fontmenu.addAction(self.italicAction)
        fontmenu.addAction(self.underlAction)
        fontmenu.addAction(self.strikeAction)
        fontmenu.addAction(self.subAction)
        fontmenu.addAction(self.superAction)
        
        alignment.addAction(self.alignLeft)
        alignment.addAction(self.alignCenter)
        alignment.addAction(self.alignRight)
        alignment.addAction(self.alignJustify)
        
        toolbarAction = QtGui.QAction("Toggle Toolbar", self)
        toolbarAction.setShortcut("Ctrl+1")
        toolbarAction.triggered.connect(self.toggleToolbar)
        
        formatbarAction = QtGui.QAction("Toggle Formatbar", self)
        formatbarAction.setShortcut("Ctrl+2")
        formatbarAction.triggered.connect(self.toggleFormatbar)
        
        statusbarAction = QtGui.QAction("Toggle Statusbar", self)
        statusbarAction.setShortcut("Ctrl+3")
        statusbarAction.triggered.connect(self.toggleStatusbar)
        
        tools.addAction(self.findAction)
        tools.addAction(self.dateTimeAction)
        tools.addAction(self.wordCountAction)
        
        view.addAction(toolbarAction)
        view.addAction(formatbarAction)
        view.addAction(statusbarAction)
    
    
    def initUI(self):
        
        self.text = QtGui.QTextEdit(self)
        self.setCentralWidget(self.text)
        
        self.initToolbar()
        self.initFormatbar()
        self.initMenubar()
        
        self.statusbar = self.statusBar()
        
        self.setGeometry(100, 100, 1030, 800)
        
        self.setWindowTitle('MinIE')
        
        self.text.setTabStopWidth(33)
        
        self.setWindowIcon(QtGui.QIcon.fromTheme("accessories-text-editor"))
        
        self.text.cursorPositionChanged.connect(self.cursorPosition)
        
    def new(self):
            
        spawn = Main(self)
        spawn.show()
            
    def showDialogOpen(self):
            
        self.fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open File', ".", "(*.jaz)")
            
        if self.fname:
            with open(self.fname, "rt") as file:
                    self.text.setText(file.read())
                    
        #self.fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        
        #myfile = open(self.fname, 'r')
        
        #with myfile:
            #data = myfile.read()
            #self.text.setText(data)
                    
    def saveAs(self):
        
        #First Attemt
        if not self.fname: #filename
            self.fname, _ = QtGui.QFileDialog.getSaveFileName(self, 'Save File As', "/home/") #filename
                
        if not unicode(self.fname).endswith(".jaz"): #filename
            self.fname += ".jaz" #filename
                
        with open(self.fname, "wt") as file2write: #filename
            file2write.write(self.text.toHtml())
    
        #Second Attempt
        #self.fname = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '/home/')
        
        #f2 = open(self.fname, 'wt')
        
        #text2write = self.text.toPlainText()
        
        #fname.write(text2write)
        
        #fname.close()
        
        #Third Attempt
        #self.fname, _ = QtGui.QFileDialog.getSaveFileName(self, 'Save File As', '/home')
        #myfile = open(self.fname, 'w')
        #data = self.text.toHtml()
        #myfile.write(data)
        #myfile.close()
        
    def save(self):
        #myfile = open(self.fname, 'w')
        #data = self.text.toHtml()
        #myfile.write(data)
        if not self.fname: #filename
            self.fname, _ = QtGui.QFileDialog.getSaveFileName(self, 'Save File As', "/home/") #filename
                
        if not unicode(self.fname).endswith(".jaz"): #filename
            self.fname += ".jaz" #filename
                
        with open(self.fname, "wt") as file2write: #filename
            file2write.write(self.text.toHtml())
    
    
    def preview(self):
        
        preview = QtGui.QPrintPreviewDialog()
        
        preview.paintRequested.connect(lambda p: self.text.print_(p))
        
        preview.exec_()
        
    def prints(self):
        
        dialog = QtGui.QPrintDialog()
        
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.text.document().print_(dialog.printer())
    
    def bulletList(self):
        
        cursor = self.text.textCursor()
        
        cursor.insertList(QtGui.QTextListFormat.ListDisc)
        
    def numberList(self):
        
        cursor = self.text.textCursor()
        
        cursor.insertList(QtGui.QTextListFormat.ListDecimal)
    
    def cursorPosition(self):
        
        cursor = self.text.textCursor()
        
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()
        
        self.statusbar.showMessage("Line: {} | Column: {}".format(line,col))
        
    #def showFontDialog(self):
        #font, ok = QtGui.QFontDialog.getFont()
        #if ok:
            #self.text.setCurrentFont(font)
    
    def fontFamily(self, font):
        self.text.setCurrentFont(font)
        
    def fontSize(self, fontsize):
        self.text.setFontPointSize(int(fontsize))
        
    def fontColors(self):
        
        color = QtGui.QColorDialog.getColor()
        
        self.text.setTextColor(color)
        
    def highlight(self):
        
        color = QtGui.QColorDialog.getColor()
        
        self.text.setTextBackgroundColor(color)
    
    def bold(self):
        
        if self.text.fontWeight() == QtGui.QFont.Bold:
            
            self.text.setFontWeight(QtGui.QFont.Normal)
            
        else:
            
            self.text.setFontWeight(QtGui.QFont.Bold)
            
    def italic(self):
        
        state = self.text.fontItalic()
        
        self.text.setFontItalic(not state)
        
    def underline(self):
        
        state = self.text.fontUnderline()
        
        self.text.setFontUnderline(not state)
        
    def strike(self):
        
        fmt = self.text.currentCharFormat()
        
        fmt.setFontStrikeOut(not fmt.fontStrikeOut())
        
        self.text.setCurrentCharFormat(fmt)
        
    def superScript(self):
        
        fmt = self.text.currentCharFormat()
        
        align = fmt.verticalAlignment()
        
        if align == QtGui.QTextCharFormat.AlignNormal:
            
            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSuperScript)
            
        else:
            
            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)
            
        self.text.setCurrentCharFormat(fmt)
        
    def subScript(self):
        
        fmt = self.text.currentCharFormat()
        
        align = fmt.verticalAlignment()
        
        if align == QtGui.QTextCharFormat.AlignNormal:
            
            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSubScript)
            
        else:
            
            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)
            
        self.text.setCurrentCharFormat(fmt)
        
    def alignsLeft(self):
        self.text.setAlignment(Qt.AlignLeft)
        
    def alignsRight(self):
        self.text.setAlignment(Qt.AlignRight)
        
    def alignsCenter(self):
        self.text.setAlignment(Qt.AlignCenter)
        
    def alignsJustify(self):
        self.text.setAlignment(Qt.AlignJustify)
        
    def toggleToolbar(self):
        
        state = self.toolbar.isVisible()
        
        self.toolbar.setVisible(not state)
        
    def toggleFormatbar(self):
        
        state = self.formatbar.isVisible()
        
        self.formatbar.setVisible(not state)
        
    def toggleStatusbar(self):
        
        state = self.statusbar.isVisible()
        
        self.statusbar.setVisible(not state)
        
    def wordCount(self):
        
        wc = wordcount.WordCount(self)
        
        wc.getText()
        
        wc.show()
        
    def closeEvent(self, event): #Gives a popup to prevent quiting without saving
        
        reply = QtGui.QMessageBox.question(self, 'Warning', "Are you sure you want to quit? All unsaved work will be lost.", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
        
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
        
    sys.exit(app.exec_())
        
if __name__ == "__main__":
    main()
