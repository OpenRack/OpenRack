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
from PySide6.QtWidgets import (QApplication, QHeaderView, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QStatusBar, QTabWidget, QTableView, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1828, 881)
        self.action_Open = QAction(MainWindow)
        self.action_Open.setObjectName(u"action_Open")
        icon = QIcon()
        icon.addFile(u":/standardicons/fugue-icons-3.5.6/icons/book-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Open.setIcon(icon)
        self.actionScan_Library = QAction(MainWindow)
        self.actionScan_Library.setObjectName(u"actionScan_Library")
        icon1 = QIcon()
        icon1.addFile(u":/standardicons/fugue-icons-3.5.6/icons/radar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionScan_Library.setIcon(icon1)
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        icon2 = QIcon()
        icon2.addFile(u":/standardicons/fugue-icons-3.5.6/icons/wrench-screwdriver.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPreferences.setIcon(icon2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1821, 831))
        self.library_tab = QWidget()
        self.library_tab.setObjectName(u"library_tab")
        self.tableView = QTableView(self.library_tab)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(280, 0, 1541, 801))
        self.listWidget = QListWidget(self.library_tab)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 0, 281, 791))
        icon3 = QIcon()
        icon3.addFile(u":/standardicons/fugue-icons-3.5.6/icons/books-stack.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.library_tab, icon3, "")
        self.folder_tab = QWidget()
        self.folder_tab.setObjectName(u"folder_tab")
        icon4 = QIcon()
        icon4.addFile(u":/standardicons/fugue-icons-3.5.6/icons/folder-tree.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.folder_tab, icon4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1828, 22))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_Edit = QMenu(self.menubar)
        self.menu_Edit.setObjectName(u"menu_Edit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.actionScan_Library)
        self.menu_Edit.addAction(self.actionPreferences)

        self.retranslateUi(MainWindow)
        self.actionPreferences.triggered.connect(MainWindow.openpreferences)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_Open.setText(QCoreApplication.translate("MainWindow", u"&Open...", None))
        self.actionScan_Library.setText(QCoreApplication.translate("MainWindow", u"Scan Library", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.library_tab), QCoreApplication.translate("MainWindow", u"Library", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.folder_tab), QCoreApplication.translate("MainWindow", u"Folders", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menu_Edit.setTitle(QCoreApplication.translate("MainWindow", u"&Edit", None))
    # retranslateUi

