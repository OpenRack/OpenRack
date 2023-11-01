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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QFrame,
    QHeaderView, QListView, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QWidget)
import icons_rc

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        if not Preferences.objectName():
            Preferences.setObjectName(u"Preferences")
        Preferences.resize(869, 629)
        self.tabWidget = QTabWidget(Preferences)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 851, 611))
        self.tabWidget.setMinimumSize(QSize(851, 0))
        self.tabWidget.setTabPosition(QTabWidget.East)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(32, 32))
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
        self.Preferences_Libraries_FolderAdd.setFocusPolicy(Qt.NoFocus)
        self.Preferences_Libraries_FolderAdd.setCheckable(False)
        self.Preferences_Libraries_FolderAdd.setAutoRepeat(False)
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
        self.Preferences_Libraries_ListView = QListView(self.Preferences_LibrariesSettingsFrame)
        self.Preferences_Libraries_ListView.setObjectName(u"Preferences_Libraries_ListView")
        self.Preferences_Libraries_ListView.setGeometry(QRect(0, 0, 551, 171))
        icon = QIcon()
        icon.addFile(u":/standardicons/fugue-icons-3.5.6/icons/book-brown.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab, icon, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame = QFrame(self.tab_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 781, 611))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 781, 611))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(150)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        icon1 = QIcon()
        icon1.addFile(u":/standardicons/fugue-icons-3.5.6/icons/script.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon1, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.frame_2 = QFrame(self.tab_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 10, 811, 351))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.Preferences_Advanced_Restore_DB = QPushButton(self.frame_2)
        self.Preferences_Advanced_Restore_DB.setObjectName(u"Preferences_Advanced_Restore_DB")
        self.Preferences_Advanced_Restore_DB.setGeometry(QRect(10, 300, 131, 31))
        self.Preferences_Advanced_Backup_DB = QPushButton(self.frame_2)
        self.Preferences_Advanced_Backup_DB.setObjectName(u"Preferences_Advanced_Backup_DB")
        self.Preferences_Advanced_Backup_DB.setGeometry(QRect(140, 300, 131, 31))
        self.Preferences_Advanced_Write_ComicInfo = QCheckBox(self.frame_2)
        self.Preferences_Advanced_Write_ComicInfo.setObjectName(u"Preferences_Advanced_Write_ComicInfo")
        self.Preferences_Advanced_Write_ComicInfo.setGeometry(QRect(10, 10, 801, 31))
        self.Preferences_Advanced_Auto_Write = QCheckBox(self.frame_2)
        self.Preferences_Advanced_Auto_Write.setObjectName(u"Preferences_Advanced_Auto_Write")
        self.Preferences_Advanced_Auto_Write.setGeometry(QRect(10, 50, 801, 31))
        self.Preferences_Advanced_Auto_Write.setTristate(False)
        icon2 = QIcon()
        icon2.addFile(u":/standardicons/fugue-icons-3.5.6/icons/gear--plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon2, "")

        self.retranslateUi(Preferences)
        self.Preferences_Libraries_FolderAdd.pressed.connect(Preferences.addfolder)
        self.Preferences_Libraries_RemovePath.pressed.connect(Preferences.removefolder)
        self.Preferences_Advanced_Auto_Write.toggled.connect(Preferences.auto_write_to_db)
        self.Preferences_Advanced_Write_ComicInfo.toggled.connect(Preferences.write_comicinfo)
        self.Preferences_Advanced_Backup_DB.pressed.connect(Preferences.backup_db)
        self.Preferences_Advanced_Restore_DB.pressed.connect(Preferences.restore_db)

        self.tabWidget.setCurrentIndex(2)
        self.Preferences_Libraries_FolderAdd.setDefault(False)


        QMetaObject.connectSlotsByName(Preferences)
    # setupUi

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(QCoreApplication.translate("Preferences", u"Form", None))
        self.Preferences_Libraries_RemoveMissing.setText(QCoreApplication.translate("Preferences", u"Automatically remove missing files from database on scan", None))
        self.Preferences_Libraries_ManualScan.setText(QCoreApplication.translate("Preferences", u"Scan", None))
        self.Preferences_Libraries_FolderAdd.setText(QCoreApplication.translate("Preferences", u"Add Folder", None))
        self.Preferences_Libraries_ChangePath.setText(QCoreApplication.translate("Preferences", u"Change Path", None))
        self.Preferences_Libraries_RemovePath.setText(QCoreApplication.translate("Preferences", u"Remove", None))
        self.Preferences_Libraries_OpenPath.setText(QCoreApplication.translate("Preferences", u"Open Path", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Preferences", u"Script", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Preferences", u"Author", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Preferences", u"Description", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "")
        self.Preferences_Advanced_Restore_DB.setText(QCoreApplication.translate("Preferences", u"Restore Database", None))
        self.Preferences_Advanced_Backup_DB.setText(QCoreApplication.translate("Preferences", u"Backup Database", None))
        self.Preferences_Advanced_Write_ComicInfo.setText(QCoreApplication.translate("Preferences", u"Write info to ComicInfo.xml", None))
        self.Preferences_Advanced_Auto_Write.setText(QCoreApplication.translate("Preferences", u"Update info automatically", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), "")
    # retranslateUi

