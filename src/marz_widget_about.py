# -*- coding: utf-8 -*-
"""
Marz Workbench for FreeCAD 0.19+.
https://github.com/mnesarco/MarzWorkbench
"""

__author__       = "Frank D. Martinez. M."
__copyright__    = "Copyright 2020, Frank D. Martinez. M."
__license__      = "GPLv3"
__maintainer__   = "https://github.com/mnesarco"

import FreeCADGui as Gui
from PySide import QtGui, QtCore, QtSvg
import marz_ui as ui

class MarzAboutWindow(QtGui.QDialog):

    def __init__(self, frame = True, timeout = False):
        super().__init__(Gui.getMainWindow())
        self.frame = frame
        self.timeout = timeout
        self.initUI()

    def initUI(self):
        
        # Window
        sg = QtGui.QDesktopWidget().screenGeometry()
        screenWidth = sg.width()
        screenHeight = sg.height()
        height = 350
        width = height * 1.61803398875
        self.setGeometry((screenWidth-width)/2, (screenHeight-height)/2, width, height)
        self.setWindowTitle(ui.MARZ_WINDOW_LABEL)
        if not self.frame:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setFixedSize(self.size())
        
        # Layout
        layout = QtGui.QStackedLayout(self)
        layout.setAlignment(QtGui.Qt.AlignBottom)
        self.setLayout(layout)

        # Content
        content = QtGui.QLabel(self)
        content.setTextInteractionFlags(QtGui.Qt.TextBrowserInteraction)
        content.setOpenExternalLinks(True)
        content.setText(f"""<p>
            A FreeCAD Workbenck for Guitar design. Version {ui.MARZ_VERSION}
            <br/><a href="https://github.com/mnesarco/MarzWorkbench/" style="color: #0088AA;">https://github.com/mnesarco/MarzWorkbench</a>
            <br/>Author: {__author__}
            <br/>{__copyright__}
            <br />All Rights Reserved.
            </p>
        """)
        content.setAlignment(QtGui.Qt.AlignBottom | QtGui.Qt.AlignCenter)
        content.setStyleSheet("""
            color: #eeeeee; 
            font-size: 12px; 
            background-color: #101010;
            background: url(%s) no-repeat center top fixed;
            padding: 260px 10px 10px 10px;
        """ % ui.graphicsPath('logo.svg'))
        layout.addWidget(content)
        
        # Timer
        if self.timeout:
            QtCore.QTimer.singleShot(self.timeout, self.close)

        self.show()
       
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.close()

    def paintEvent(self, event):
        opt = QtGui.QStyleOption()
        opt.init(self)
        painter = QtGui.QPainter(self)
        self.style().drawPrimitive(QtGui.QStyle.PE_Widget, opt, painter, self)


    @classmethod
    def execute(cls, frame = True, timeout = None):
        MarzAboutWindow(frame, timeout).show()