# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QColumnView, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1857, 1022)
        self.action_Open = QAction(MainWindow)
        self.action_Open.setObjectName(u"action_Open")
        self.action_About = QAction(MainWindow)
        self.action_About.setObjectName(u"action_About")
        self.actionNews = QAction(MainWindow)
        self.actionNews.setObjectName(u"actionNews")
        self.actionOpenRack_Forum = QAction(MainWindow)
        self.actionOpenRack_Forum.setObjectName(u"actionOpenRack_Forum")
        self.actionOpenRack_Website = QAction(MainWindow)
        self.actionOpenRack_Website.setObjectName(u"actionOpenRack_Website")
        self.actionDocs = QAction(MainWindow)
        self.actionDocs.setObjectName(u"actionDocs")
        self.actionSupport_OpenRack = QAction(MainWindow)
        self.actionSupport_OpenRack.setObjectName(u"actionSupport_OpenRack")
        self.actionScan_Library = QAction(MainWindow)
        self.actionScan_Library.setObjectName(u"actionScan_Library")
        icon = QIcon()
        iconThemeName = u"emblem-documents"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.actionScan_Library.setIcon(icon)
        self.actionScan_Library.setMenuRole(QAction.TextHeuristicRole)
        self.actionWrite_Metadata = QAction(MainWindow)
        self.actionWrite_Metadata.setObjectName(u"actionWrite_Metadata")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.columnView = QColumnView(self.centralwidget)
        self.columnView.setObjectName(u"columnView")
        self.columnView.setGeometry(QRect(210, 0, 1641, 971))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1857, 21))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_Edit = QMenu(self.menubar)
        self.menu_Edit.setObjectName(u"menu_Edit")
        self.menu_Tools = QMenu(self.menubar)
        self.menu_Tools.setObjectName(u"menu_Tools")
        self.menu_Display = QMenu(self.menubar)
        self.menu_Display.setObjectName(u"menu_Display")
        self.menu_View = QMenu(self.menubar)
        self.menu_View.setObjectName(u"menu_View")
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Tools.menuAction())
        self.menubar.addAction(self.menu_Display.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menu_File.addAction(self.action_Open)
        self.menu_Edit.addAction(self.actionPreferences)
        self.menu_Tools.addAction(self.actionScan_Library)
        self.menu_Tools.addAction(self.actionWrite_Metadata)
        self.menu_Help.addAction(self.action_About)
        self.menu_Help.addAction(self.actionNews)
        self.menu_Help.addAction(self.actionOpenRack_Forum)
        self.menu_Help.addAction(self.actionOpenRack_Website)
        self.menu_Help.addAction(self.actionDocs)
        self.menu_Help.addAction(self.actionSupport_OpenRack)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_Open.setText(QCoreApplication.translate("MainWindow", u"&Open...", None))
        self.action_About.setText(QCoreApplication.translate("MainWindow", u"&About", None))
        self.actionNews.setText(QCoreApplication.translate("MainWindow", u"News", None))
        self.actionOpenRack_Forum.setText(QCoreApplication.translate("MainWindow", u"OpenRack Forum", None))
        self.actionOpenRack_Website.setText(QCoreApplication.translate("MainWindow", u"OpenRack Website", None))
        self.actionDocs.setText(QCoreApplication.translate("MainWindow", u"Docs", None))
        self.actionSupport_OpenRack.setText(QCoreApplication.translate("MainWindow", u"Support OpenRack", None))
        self.actionScan_Library.setText(QCoreApplication.translate("MainWindow", u"Scan Library", None))
        self.actionWrite_Metadata.setText(QCoreApplication.translate("MainWindow", u"Write Metadata", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menu_Edit.setTitle(QCoreApplication.translate("MainWindow", u"&Edit", None))
        self.menu_Tools.setTitle(QCoreApplication.translate("MainWindow", u"&Tools", None))
        self.menu_Display.setTitle(QCoreApplication.translate("MainWindow", u"&Display", None))
        self.menu_View.setTitle(QCoreApplication.translate("MainWindow", u"&View", None))
        self.menu_Help.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
    # retranslateUi

