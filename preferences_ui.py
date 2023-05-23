# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QTabWidget,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(864, 641)
        self.actionPreferences_Libraries_FolderAdd = QAction(Form)
        self.actionPreferences_Libraries_FolderAdd.setObjectName(u"actionPreferences_Libraries_FolderAdd")
        self.actionPreferences_Libraries_FolderAdd.setMenuRole(QAction.TextHeuristicRole)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 851, 611))
        self.tabWidget.setMinimumSize(QSize(851, 0))
        self.tabWidget.setTabPosition(QTabWidget.East)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(64, 64))
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setLayoutDirection(Qt.LeftToRight)
        self.Preferences_LibrariesSettingsFrame = QFrame(self.tab)
        self.Preferences_LibrariesSettingsFrame.setObjectName(u"Preferences_LibrariesSettingsFrame")
        self.Preferences_LibrariesSettingsFrame.setEnabled(True)
        self.Preferences_LibrariesSettingsFrame.setGeometry(QRect(10, 0, 831, 591))
        self.Preferences_LibrariesSettingsFrame.setLayoutDirection(Qt.LeftToRight)
        self.Preferences_LibrariesSettingsFrame.setFrameShape(QFrame.StyledPanel)
        self.Preferences_LibrariesSettingsFrame.setFrameShadow(QFrame.Raised)
        self.Preferences_Libraries_RemoveMissing = QCheckBox(self.Preferences_LibrariesSettingsFrame)
        self.Preferences_Libraries_RemoveMissing.setObjectName(u"Preferences_Libraries_RemoveMissing")
        self.Preferences_Libraries_RemoveMissing.setGeometry(QRect(10, 170, 641, 41))
        self.Preferences_Libraries_ManualScan = QPushButton(self.Preferences_LibrariesSettingsFrame)
        self.Preferences_Libraries_ManualScan.setObjectName(u"Preferences_Libraries_ManualScan")
        self.Preferences_Libraries_ManualScan.setGeometry(QRect(10, 210, 75, 24))
        self.Preferences_Libraries_FolderAdd = QPushButton(self.Preferences_LibrariesSettingsFrame)
        self.Preferences_Libraries_FolderAdd.setObjectName(u"Preferences_Libraries_FolderAdd")
        self.Preferences_Libraries_FolderAdd.setGeometry(QRect(560, 10, 75, 24))
        self.Preferences_Libraries_FolderAdd.setAutoDefault(False)
        self.Preferences_Libraries_FolderAdd.setFlat(False)
        self.Preferences_Libraries_ChangePath = QPushButton(self.Preferences_LibrariesSettingsFrame)
        self.Preferences_Libraries_ChangePath.setObjectName(u"Preferences_Libraries_ChangePath")
        self.Preferences_Libraries_ChangePath.setGeometry(QRect(560, 40, 75, 24))
        self.Preferences_Libraries_RemovePath = QPushButton(self.Preferences_LibrariesSettingsFrame)
        self.Preferences_Libraries_RemovePath.setObjectName(u"Preferences_Libraries_RemovePath")
        self.Preferences_Libraries_RemovePath.setGeometry(QRect(560, 70, 75, 24))
        self.Preferences_Libraries_OpenPath = QPushButton(self.Preferences_LibrariesSettingsFrame)
        self.Preferences_Libraries_OpenPath.setObjectName(u"Preferences_Libraries_OpenPath")
        self.Preferences_Libraries_OpenPath.setGeometry(QRect(560, 100, 75, 24))
        self.Preferences_Libraries_ListDisplay = QListWidget(self.Preferences_LibrariesSettingsFrame)
        self.Preferences_Libraries_ListDisplay.setObjectName(u"Preferences_Libraries_ListDisplay")
        self.Preferences_Libraries_ListDisplay.setGeometry(QRect(10, 10, 531, 141))
        icon = QIcon()
        icon.addFile(u"../../../../Downloads/22222222.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab, icon, "")

        self.retranslateUi(Form)
        self.Preferences_Libraries_FolderAdd.clicked.connect(Form.addfolder)

        self.tabWidget.setCurrentIndex(0)
        self.Preferences_Libraries_FolderAdd.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.actionPreferences_Libraries_FolderAdd.setText(QCoreApplication.translate("Form", u"Preferences_Libraries_FolderAdd", None))
        self.Preferences_Libraries_RemoveMissing.setText(QCoreApplication.translate("Form", u"Automatically remove missing files from database on scan", None))
        self.Preferences_Libraries_ManualScan.setText(QCoreApplication.translate("Form", u"Scan", None))
        self.Preferences_Libraries_FolderAdd.setText(QCoreApplication.translate("Form", u"Add Folder", None))
        self.Preferences_Libraries_ChangePath.setText(QCoreApplication.translate("Form", u"Change Path", None))
        self.Preferences_Libraries_RemovePath.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.Preferences_Libraries_OpenPath.setText(QCoreApplication.translate("Form", u"Open Path", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "")
    # retranslateUi

