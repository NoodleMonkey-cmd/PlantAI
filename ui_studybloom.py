# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Beta.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 560)
        MainWindow.setMinimumSize(QSize(800, 560))
        MainWindow.setMaximumSize(QSize(800, 560))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.SideMenu = QFrame(self.centralwidget)
        self.SideMenu.setObjectName(u"SideMenu")
        self.SideMenu.setGeometry(QRect(0, 30, 110, 531))
        self.SideMenu.setStyleSheet(u"   QFrame {\n"
"    background-color: rgb(28, 28, 30);\n"
"}")
        self.SideMenu.setFrameShape(QFrame.Shape.StyledPanel)
        self.SideMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.Button_Setting = QPushButton(self.SideMenu)
        self.Button_Setting.setObjectName(u"Button_Setting")
        self.Button_Setting.setGeometry(QRect(14, 200, 81, 81))
        self.Button_Setting.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 18px;\n"
"}")
        self.Button_Setting.setIconSize(QSize(20, 20))
        self.Button_Summary = QPushButton(self.SideMenu)
        self.Button_Summary.setObjectName(u"Button_Summary")
        self.Button_Summary.setGeometry(QRect(14, 20, 81, 81))
        self.Button_Summary.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(80, 130, 80, 25);\n"
"    border: 1px solid rgb(110, 190, 110);\n"
"    border-radius: 18px;\n"
"    color: rgb(150, 220, 140);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(100, 180, 100, 35);\n"
"    border: 1px solid rgb(140, 220, 130);\n"
"}")
        self.Button_Summary.setIconSize(QSize(35, 35))
        self.Label_SummaryIcon = QLabel(self.SideMenu)
        self.Label_SummaryIcon.setObjectName(u"Label_SummaryIcon")
        self.Label_SummaryIcon.setGeometry(QRect(39, 35, 31, 31))
        self.Label_SummaryIcon.setStyleSheet(u"QLabel {\n"
"    color: rgb(130, 200, 120);\n"
"}")
        self.Label_SummaryIcon.setPixmap(QPixmap(u"Modules/Assets/Icon/summaryv2.svg"))
        self.Label_SummaryIcon.setScaledContents(True)
        self.Label_SettingsIcon = QLabel(self.SideMenu)
        self.Label_SettingsIcon.setObjectName(u"Label_SettingsIcon")
        self.Label_SettingsIcon.setGeometry(QRect(38, 215, 31, 31))
        self.Label_SettingsIcon.setPixmap(QPixmap(u"Modules/Assets/Icon/cogv3.svg"))
        self.Label_SettingsIcon.setScaledContents(True)
        self.Label_SettingsText = QLabel(self.SideMenu)
        self.Label_SettingsText.setObjectName(u"Label_SettingsText")
        self.Label_SettingsText.setGeometry(QRect(33, 250, 51, 16))
        self.Label_SettingsText.setStyleSheet(u"QLabel {\n"
"    color: rgb(95, 95, 95);\n"
"}")
        self.Label_SummaryText_2 = QLabel(self.SideMenu)
        self.Label_SummaryText_2.setObjectName(u"Label_SummaryText_2")
        self.Label_SummaryText_2.setGeometry(QRect(30, 70, 51, 16))
        self.Label_SummaryText_2.setStyleSheet(u"QLabel {\n"
"    color: rgb(130, 200, 120);\n"
"}")
        self.Button_Study = QPushButton(self.SideMenu)
        self.Button_Study.setObjectName(u"Button_Study")
        self.Button_Study.setGeometry(QRect(14, 110, 81, 81))
        self.Button_Study.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 18px;\n"
"}")
        self.Button_Study.setIconSize(QSize(20, 20))
        self.Label_StudyIcon = QLabel(self.SideMenu)
        self.Label_StudyIcon.setObjectName(u"Label_StudyIcon")
        self.Label_StudyIcon.setGeometry(QRect(38, 127, 31, 31))
        self.Label_StudyIcon.setPixmap(QPixmap(u"Modules/Assets/Icon/bookopenv2.svg"))
        self.Label_StudyIcon.setScaledContents(True)
        self.Label_StudyText = QLabel(self.SideMenu)
        self.Label_StudyText.setObjectName(u"Label_StudyText")
        self.Label_StudyText.setGeometry(QRect(39, 160, 51, 16))
        self.Label_StudyText.setStyleSheet(u"QLabel {\n"
"    color: rgb(95, 95, 95);\n"
"}")
        self.TopFrane = QFrame(self.centralwidget)
        self.TopFrane.setObjectName(u"TopFrane")
        self.TopFrane.setGeometry(QRect(0, 0, 811, 41))
        self.TopFrane.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(28, 28, 33);\n"
"    border-bottom: 1px solid rgb(50, 52, 55);\n"
"}")
        self.TopFrane.setFrameShape(QFrame.Shape.StyledPanel)
        self.TopFrane.setFrameShadow(QFrame.Shadow.Raised)
        self.Label_Leaf = QLabel(self.TopFrane)
        self.Label_Leaf.setObjectName(u"Label_Leaf")
        self.Label_Leaf.setGeometry(QRect(10, 10, 21, 21))
        self.Label_Leaf.setPixmap(QPixmap(u"Modules/Assets/Icon/leafy-green.svg"))
        self.Label_Leaf.setScaledContents(True)
        self.Label_StudyBloom = QLabel(self.TopFrane)
        self.Label_StudyBloom.setObjectName(u"Label_StudyBloom")
        self.Label_StudyBloom.setGeometry(QRect(38, 12, 71, 16))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(10)
        font.setKerning(False)
        self.Label_StudyBloom.setFont(font)
        self.Label_StudyBloom.setStyleSheet(u"QLabel {\n"
"    color: rgb(165, 165, 170);\n"
"    font-family: \"Inter\";\n"
"    font-size: 10pt;\n"
"}")
        self.Button_Minimize = QPushButton(self.TopFrane)
        self.Button_Minimize.setObjectName(u"Button_Minimize")
        self.Button_Minimize.setGeometry(QRect(695, 5, 31, 31))
        icon = QIcon()
        icon.addFile(u"Modules/Assets/Icon/minus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Minimize.setIcon(icon)
        self.Buttom_Maximize = QPushButton(self.TopFrane)
        self.Buttom_Maximize.setObjectName(u"Buttom_Maximize")
        self.Buttom_Maximize.setGeometry(QRect(730, 5, 31, 31))
        icon1 = QIcon()
        icon1.addFile(u"Modules/Assets/Icon/expand.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Buttom_Maximize.setIcon(icon1)
        self.Buttom_Close = QPushButton(self.TopFrane)
        self.Buttom_Close.setObjectName(u"Buttom_Close")
        self.Buttom_Close.setGeometry(QRect(765, 5, 31, 31))
        self.Buttom_Close.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: rgb(196, 43, 28);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"Modules/Assets/Icon/x.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Buttom_Close.setIcon(icon2)
        self.MainMenu = QFrame(self.centralwidget)
        self.MainMenu.setObjectName(u"MainMenu")
        self.MainMenu.setGeometry(QRect(110, 40, 691, 531))
        self.MainMenu.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(28, 28, 29);\n"
"	border:none;\n"
"}")
        self.MainMenu.setFrameShape(QFrame.Shape.StyledPanel)
        self.MainMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedWidget = QStackedWidget(self.MainMenu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 671, 511))
        self.Page_Settings = QWidget()
        self.Page_Settings.setObjectName(u"Page_Settings")
        self.MainFrame_2 = QFrame(self.Page_Settings)
        self.MainFrame_2.setObjectName(u"MainFrame_2")
        self.MainFrame_2.setGeometry(QRect(9, 4, 655, 501))
        self.MainFrame_2.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(28, 28, 30);\n"
"}")
        self.MainFrame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.MainFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.Label_Welcome_5 = QLabel(self.MainFrame_2)
        self.Label_Welcome_5.setObjectName(u"Label_Welcome_5")
        self.Label_Welcome_5.setGeometry(QRect(14, 10, 351, 41))
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(20)
        font1.setWeight(QFont.Weight.DemiBold)
        font1.setItalic(False)
        self.Label_Welcome_5.setFont(font1)
        self.Label_Welcome_5.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 20pt;\n"
"    font-weight: 550;\n"
"    color: rgb(240, 240, 240);\n"
"}")
        self.Label_SummaryText_3 = QLabel(self.MainFrame_2)
        self.Label_SummaryText_3.setObjectName(u"Label_SummaryText_3")
        self.Label_SummaryText_3.setGeometry(QRect(11, 35, 401, 51))
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.Label_SummaryText_3.setFont(font2)
        self.Label_SummaryText_3.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 8pt;\n"
"    font-weight: 400;\n"
"    color: rgb(135, 135, 145);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Frame_Profile = QFrame(self.MainFrame_2)
        self.Frame_Profile.setObjectName(u"Frame_Profile")
        self.Frame_Profile.setGeometry(QRect(10, 80, 621, 101))
        self.Frame_Profile.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(31, 32, 35);\n"
"    border: 1px solid rgb(55, 57, 61);\n"
"    border-radius: 14px;\n"
"}")
        self.Frame_Profile.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_Profile.setFrameShadow(QFrame.Shadow.Raised)
        self.CircularBackground_4 = QFrame(self.Frame_Profile)
        self.CircularBackground_4.setObjectName(u"CircularBackground_4")
        self.CircularBackground_4.setGeometry(QRect(10, 10, 30, 30))
        self.CircularBackground_4.setMinimumSize(QSize(30, 30))
        self.CircularBackground_4.setMaximumSize(QSize(30, 30))
        self.CircularBackground_4.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(45, 55, 43);\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"}")
        self.CircularBackground_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.CircularBackground_4.setFrameShadow(QFrame.Shadow.Raised)
        self.Label_UserProfileIcon = QLabel(self.CircularBackground_4)
        self.Label_UserProfileIcon.setObjectName(u"Label_UserProfileIcon")
        self.Label_UserProfileIcon.setGeometry(QRect(4, 5, 21, 21))
        self.Label_UserProfileIcon.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 25pt;\n"
"    font-weight: 700;\n"
"    color: rgb(118, 190, 112);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_UserProfileIcon.setPixmap(QPixmap(u"Modules/Assets/Icon/user.svg"))
        self.Label_UserProfileIcon.setScaledContents(True)
        self.label = QLabel(self.Frame_Profile)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 17, 91, 16))
        self.label.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 12pt;\n"
"    font-weight: 500;\n"
"    color: rgb(137, 205, 101);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.line = QFrame(self.Frame_Profile)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 45, 601, 1))
        self.line.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(52, 54, 58);\n"
"    border: none;\n"
"    max-height: 1px;\n"
"}")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.Label_SummaryText_4 = QLabel(self.Frame_Profile)
        self.Label_SummaryText_4.setObjectName(u"Label_SummaryText_4")
        self.Label_SummaryText_4.setGeometry(QRect(15, 47, 401, 51))
        font3 = QFont()
        font3.setFamilies([u"Inter"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        self.Label_SummaryText_4.setFont(font3)
        self.Label_SummaryText_4.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 10pt;\n"
"    font-weight: 400;\n"
"    color: rgb(135, 135, 145);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Entry_Name = QLineEdit(self.Frame_Profile)
        self.Entry_Name.setObjectName(u"Entry_Name")
        self.Entry_Name.setGeometry(QRect(490, 60, 113, 26))
        self.Entry_Name.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(25, 26, 28);\n"
"    border: 1px solid rgb(58, 60, 64);\n"
"    border-radius: 8px;\n"
"\n"
"    color: rgb(225, 225, 230);\n"
"\n"
"    font-family: \"Inter\";\n"
"    font-size: 10pt;\n"
"\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid rgb(137, 205, 101);\n"
"}")
        self.Frame_Profile_2 = QFrame(self.MainFrame_2)
        self.Frame_Profile_2.setObjectName(u"Frame_Profile_2")
        self.Frame_Profile_2.setGeometry(QRect(10, 190, 621, 291))
        self.Frame_Profile_2.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(31, 32, 35);\n"
"    border: 1px solid rgb(55, 57, 61);\n"
"    border-radius: 14px;\n"
"}")
        self.Frame_Profile_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_Profile_2.setFrameShadow(QFrame.Shadow.Raised)
        self.line_2 = QFrame(self.Frame_Profile_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 43, 601, 1))
        self.line_2.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(52, 54, 58);\n"
"    border: none;\n"
"    max-height: 1px;\n"
"}")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.CircularBackground_5 = QFrame(self.Frame_Profile_2)
        self.CircularBackground_5.setObjectName(u"CircularBackground_5")
        self.CircularBackground_5.setGeometry(QRect(10, 8, 30, 30))
        self.CircularBackground_5.setMinimumSize(QSize(30, 30))
        self.CircularBackground_5.setMaximumSize(QSize(30, 30))
        self.CircularBackground_5.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(45, 55, 43);\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"}")
        self.CircularBackground_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.CircularBackground_5.setFrameShadow(QFrame.Shadow.Raised)
        self.Label_UserProfileIcon_2 = QLabel(self.CircularBackground_5)
        self.Label_UserProfileIcon_2.setObjectName(u"Label_UserProfileIcon_2")
        self.Label_UserProfileIcon_2.setGeometry(QRect(4, 5, 21, 21))
        self.Label_UserProfileIcon_2.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 25pt;\n"
"    font-weight: 700;\n"
"    color: rgb(118, 190, 112);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_UserProfileIcon_2.setPixmap(QPixmap(u"Modules/Assets/Icon/leaf.svg"))
        self.Label_UserProfileIcon_2.setScaledContents(True)
        self.Label_SectiontwoTitle = QLabel(self.Frame_Profile_2)
        self.Label_SectiontwoTitle.setObjectName(u"Label_SectiontwoTitle")
        self.Label_SectiontwoTitle.setGeometry(QRect(50, 15, 91, 16))
        self.Label_SectiontwoTitle.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 12pt;\n"
"    font-weight: 500;\n"
"    color: rgb(137, 205, 101);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_SummaryText_5 = QLabel(self.Frame_Profile_2)
        self.Label_SummaryText_5.setObjectName(u"Label_SummaryText_5")
        self.Label_SummaryText_5.setGeometry(QRect(15, 45, 401, 51))
        self.Label_SummaryText_5.setFont(font3)
        self.Label_SummaryText_5.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 10pt;\n"
"    font-weight: 400;\n"
"    color: rgb(135, 135, 145);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_SummaryText_6 = QLabel(self.Frame_Profile_2)
        self.Label_SummaryText_6.setObjectName(u"Label_SummaryText_6")
        self.Label_SummaryText_6.setGeometry(QRect(15, 80, 401, 51))
        self.Label_SummaryText_6.setFont(font3)
        self.Label_SummaryText_6.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 10pt;\n"
"    font-weight: 400;\n"
"    color: rgb(135, 135, 145);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_SummaryText_7 = QLabel(self.Frame_Profile_2)
        self.Label_SummaryText_7.setObjectName(u"Label_SummaryText_7")
        self.Label_SummaryText_7.setGeometry(QRect(15, 150, 401, 51))
        self.Label_SummaryText_7.setFont(font3)
        self.Label_SummaryText_7.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 10pt;\n"
"    font-weight: 400;\n"
"    color: rgb(135, 135, 145);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_SummaryText_8 = QLabel(self.Frame_Profile_2)
        self.Label_SummaryText_8.setObjectName(u"Label_SummaryText_8")
        self.Label_SummaryText_8.setGeometry(QRect(15, 115, 401, 51))
        self.Label_SummaryText_8.setFont(font3)
        self.Label_SummaryText_8.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 10pt;\n"
"    font-weight: 400;\n"
"    color: rgb(135, 135, 145);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.CheckBox_ShowDesktopPlant = QCheckBox(self.Frame_Profile_2)
        self.CheckBox_ShowDesktopPlant.setObjectName(u"CheckBox_ShowDesktopPlant")
        self.CheckBox_ShowDesktopPlant.setGeometry(QRect(560, 60, 84, 24))
        self.CheckBox_ShowDesktopPlant.setStyleSheet(u"QCheckBox {\n"
"    spacing: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 44px;\n"
"    height: 24px;\n"
"    border-radius: 12px;\n"
"\n"
"    background-color: rgb(65, 67, 72);\n"
"    border: none;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: rgb(137, 205, 101);\n"
"}")
        self.CheckBox_ShowDesktopPlant.setChecked(False)
        self.CheckBox_AlwaysOnTop = QCheckBox(self.Frame_Profile_2)
        self.CheckBox_AlwaysOnTop.setObjectName(u"CheckBox_AlwaysOnTop")
        self.CheckBox_AlwaysOnTop.setGeometry(QRect(560, 95, 84, 24))
        self.CheckBox_AlwaysOnTop.setStyleSheet(u"QCheckBox {\n"
"    spacing: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 44px;\n"
"    height: 24px;\n"
"    border-radius: 12px;\n"
"\n"
"    background-color: rgb(65, 67, 72);\n"
"    border: none;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: rgb(137, 205, 101);\n"
"}")
        self.CheckBox_RememberPlantPosition = QCheckBox(self.Frame_Profile_2)
        self.CheckBox_RememberPlantPosition.setObjectName(u"CheckBox_RememberPlantPosition")
        self.CheckBox_RememberPlantPosition.setGeometry(QRect(560, 130, 84, 24))
        self.CheckBox_RememberPlantPosition.setStyleSheet(u"QCheckBox {\n"
"    spacing: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 44px;\n"
"    height: 24px;\n"
"    border-radius: 12px;\n"
"\n"
"    background-color: rgb(65, 67, 72);\n"
"    border: none;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: rgb(137, 205, 101);\n"
"}")
        self.DropdownMenu_PlantSize = QComboBox(self.Frame_Profile_2)
        self.DropdownMenu_PlantSize.addItem("")
        self.DropdownMenu_PlantSize.addItem("")
        self.DropdownMenu_PlantSize.addItem("")
        self.DropdownMenu_PlantSize.setObjectName(u"DropdownMenu_PlantSize")
        self.DropdownMenu_PlantSize.setGeometry(QRect(515, 165, 89, 26))
        self.DropdownMenu_PlantSize.setStyleSheet(u"QComboBox {\n"
"    background-color: rgb(25, 26, 28);\n"
"    border: 1px solid rgb(58, 60, 64);\n"
"    border-radius: 8px;\n"
"\n"
"    color: rgb(225, 225, 230);\n"
"\n"
"    font-family: \"Inter\";\n"
"    font-size: 10pt;\n"
"\n"
"    padding: 6px 10px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid rgb(90, 95, 100);\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid rgb(137, 205, 101);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(31, 32, 35);\n"
"    color: rgb(225, 225, 230);\n"
"\n"
"    border: 1px solid rgb(58, 60, 64);\n"
"    selection-background-color: rgb(55, 72, 52);\n"
"    selection-color: rgb(240, 240, 240);\n"
"}")
        self.stackedWidget.addWidget(self.Page_Settings)
        self.Page_Summary = QWidget()
        self.Page_Summary.setObjectName(u"Page_Summary")
        self.MainFrame = QFrame(self.Page_Summary)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setGeometry(QRect(9, 4, 655, 501))
        self.MainFrame.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(28, 28, 30);\n"
"}")
        self.MainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.Label_Welcome = QLabel(self.MainFrame)
        self.Label_Welcome.setObjectName(u"Label_Welcome")
        self.Label_Welcome.setGeometry(QRect(7, 10, 351, 41))
        font4 = QFont()
        font4.setFamilies([u"Inter"])
        font4.setPointSize(20)
        font4.setBold(True)
        font4.setItalic(False)
        self.Label_Welcome.setFont(font4)
        self.Label_Welcome.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 20pt;\n"
"    font-weight: 700;\n"
"    color: rgb(240, 240, 240);\n"
"}")
        self.Label_SummaryText = QLabel(self.MainFrame)
        self.Label_SummaryText.setObjectName(u"Label_SummaryText")
        self.Label_SummaryText.setGeometry(QRect(11, 35, 401, 51))
        self.Label_SummaryText.setFont(font2)
        self.Label_SummaryText.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 8pt;\n"
"    font-weight: 400;\n"
"    color: rgb(135, 135, 145);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Frame_TodayStudyTime = QFrame(self.MainFrame)
        self.Frame_TodayStudyTime.setObjectName(u"Frame_TodayStudyTime")
        self.Frame_TodayStudyTime.setGeometry(QRect(10, 80, 151, 81))
        self.Frame_TodayStudyTime.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(36, 37, 40);\n"
"\n"
"    border: 1px solid rgb(62, 64, 68);\n"
"    border-radius: 18px;\n"
"}")
        self.Frame_TodayStudyTime.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_TodayStudyTime.setFrameShadow(QFrame.Shadow.Raised)
        self.Label_Subtext = QLabel(self.Frame_TodayStudyTime)
        self.Label_Subtext.setObjectName(u"Label_Subtext")
        self.Label_Subtext.setGeometry(QRect(10, 10, 141, 16))
        self.Label_Subtext.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 8pt;\n"
"    font-weight: 500;\n"
"    color: rgb(145, 145, 155);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_StudyTimeValue = QLabel(self.Frame_TodayStudyTime)
        self.Label_StudyTimeValue.setObjectName(u"Label_StudyTimeValue")
        self.Label_StudyTimeValue.setGeometry(QRect(10, 30, 151, 31))
        self.Label_StudyTimeValue.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 25pt;\n"
"    font-weight: 700;\n"
"    color: rgb(145, 201, 112);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_StudyTimeIcon = QLabel(self.Frame_TodayStudyTime)
        self.Label_StudyTimeIcon.setObjectName(u"Label_StudyTimeIcon")
        self.Label_StudyTimeIcon.setGeometry(QRect(115, 8, 21, 21))
        self.Label_StudyTimeIcon.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 8pt;\n"
"    font-weight: 500;\n"
"    color: rgb(145, 145, 155);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_StudyTimeIcon.setPixmap(QPixmap(u"Modules/Assets/Icon/clock.svg"))
        self.Label_StudyTimeIcon.setScaledContents(True)
        self.Frame_PointsEarnedToday = QFrame(self.MainFrame)
        self.Frame_PointsEarnedToday.setObjectName(u"Frame_PointsEarnedToday")
        self.Frame_PointsEarnedToday.setGeometry(QRect(170, 80, 151, 81))
        self.Frame_PointsEarnedToday.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(35, 36, 39);\n"
"\n"
"    border: 1px solid rgb(58, 60, 64);\n"
"    border-radius: 16px;\n"
"}")
        self.Frame_PointsEarnedToday.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_PointsEarnedToday.setFrameShadow(QFrame.Shadow.Raised)
        self.Label_SubText_2 = QLabel(self.Frame_PointsEarnedToday)
        self.Label_SubText_2.setObjectName(u"Label_SubText_2")
        self.Label_SubText_2.setGeometry(QRect(10, 10, 141, 16))
        self.Label_SubText_2.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 8pt;\n"
"    font-weight: 500;\n"
"    color: rgb(145, 145, 155);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_PointsEarnedValue = QLabel(self.Frame_PointsEarnedToday)
        self.Label_PointsEarnedValue.setObjectName(u"Label_PointsEarnedValue")
        self.Label_PointsEarnedValue.setGeometry(QRect(10, 30, 151, 31))
        self.Label_PointsEarnedValue.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 25pt;\n"
"    font-weight: 700;\n"
"    color: rgb(145, 201, 112);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_PointImage = QLabel(self.Frame_PointsEarnedToday)
        self.Label_PointImage.setObjectName(u"Label_PointImage")
        self.Label_PointImage.setGeometry(QRect(115, 8, 21, 21))
        self.Label_PointImage.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 8pt;\n"
"    font-weight: 500;\n"
"    color: rgb(145, 145, 155);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_PointImage.setPixmap(QPixmap(u"Modules/Assets/Icon/star.svg"))
        self.Label_PointImage.setScaledContents(True)
        self.Frame_CurrentStreak = QFrame(self.MainFrame)
        self.Frame_CurrentStreak.setObjectName(u"Frame_CurrentStreak")
        self.Frame_CurrentStreak.setGeometry(QRect(330, 80, 151, 81))
        self.Frame_CurrentStreak.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(35, 36, 39);\n"
"\n"
"    border: 1px solid rgb(58, 60, 64);\n"
"    border-radius: 16px;\n"
"}")
        self.Frame_CurrentStreak.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_CurrentStreak.setFrameShadow(QFrame.Shadow.Raised)
        self.Label_SubText_3 = QLabel(self.Frame_CurrentStreak)
        self.Label_SubText_3.setObjectName(u"Label_SubText_3")
        self.Label_SubText_3.setGeometry(QRect(10, 10, 141, 16))
        self.Label_SubText_3.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 8pt;\n"
"    font-weight: 500;\n"
"    color: rgb(145, 145, 155);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_CurrentStreakValue = QLabel(self.Frame_CurrentStreak)
        self.Label_CurrentStreakValue.setObjectName(u"Label_CurrentStreakValue")
        self.Label_CurrentStreakValue.setGeometry(QRect(10, 30, 151, 31))
        self.Label_CurrentStreakValue.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 25pt;\n"
"    font-weight: 700;\n"
"    color: rgb(145, 201, 112);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_PointImage_2 = QLabel(self.Frame_CurrentStreak)
        self.Label_PointImage_2.setObjectName(u"Label_PointImage_2")
        self.Label_PointImage_2.setGeometry(QRect(115, 8, 21, 21))
        self.Label_PointImage_2.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 8pt;\n"
"    font-weight: 500;\n"
"    color: rgb(145, 145, 155);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_PointImage_2.setPixmap(QPixmap(u"Modules/Assets/Icon/flame.svg"))
        self.Label_PointImage_2.setScaledContents(True)
        self.Frame_SessionToday = QFrame(self.MainFrame)
        self.Frame_SessionToday.setObjectName(u"Frame_SessionToday")
        self.Frame_SessionToday.setGeometry(QRect(490, 80, 151, 81))
        self.Frame_SessionToday.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(35, 36, 39);\n"
"\n"
"    border: 1px solid rgb(58, 60, 64);\n"
"    border-radius: 16px;\n"
"}")
        self.Frame_SessionToday.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_SessionToday.setFrameShadow(QFrame.Shadow.Raised)
        self.Label_SubText_4 = QLabel(self.Frame_SessionToday)
        self.Label_SubText_4.setObjectName(u"Label_SubText_4")
        self.Label_SubText_4.setGeometry(QRect(10, 10, 141, 16))
        self.Label_SubText_4.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 8pt;\n"
"    font-weight: 500;\n"
"    color: rgb(145, 145, 155);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_SessionTodayValue = QLabel(self.Frame_SessionToday)
        self.Label_SessionTodayValue.setObjectName(u"Label_SessionTodayValue")
        self.Label_SessionTodayValue.setGeometry(QRect(10, 30, 151, 31))
        self.Label_SessionTodayValue.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 25pt;\n"
"    font-weight: 700;\n"
"    color: rgb(118, 190, 112);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_PointImage_3 = QLabel(self.Frame_SessionToday)
        self.Label_PointImage_3.setObjectName(u"Label_PointImage_3")
        self.Label_PointImage_3.setGeometry(QRect(115, 8, 21, 21))
        self.Label_PointImage_3.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 8pt;\n"
"    font-weight: 500;\n"
"    color: rgb(145, 145, 155);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_PointImage_3.setPixmap(QPixmap(u"Modules/Assets/Icon/notepad-text.svg"))
        self.Label_PointImage_3.setScaledContents(True)
        self.Frame_FavoriteSubject = QFrame(self.MainFrame)
        self.Frame_FavoriteSubject.setObjectName(u"Frame_FavoriteSubject")
        self.Frame_FavoriteSubject.setGeometry(QRect(10, 170, 191, 311))
        self.Frame_FavoriteSubject.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(35, 36, 39);\n"
"\n"
"    border: 1px solid rgb(58, 60, 64);\n"
"    border-radius: 16px;\n"
"}")
        self.Frame_FavoriteSubject.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_FavoriteSubject.setFrameShadow(QFrame.Shadow.Raised)
        self.Label_SubText_9 = QLabel(self.Frame_FavoriteSubject)
        self.Label_SubText_9.setObjectName(u"Label_SubText_9")
        self.Label_SubText_9.setGeometry(QRect(50, 120, 141, 16))
        self.Label_SubText_9.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 8pt;\n"
"    font-weight: 500;\n"
"    color: rgb(145, 145, 155);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.CircularBackground = QFrame(self.Frame_FavoriteSubject)
        self.CircularBackground.setObjectName(u"CircularBackground")
        self.CircularBackground.setGeometry(QRect(50, 20, 80, 80))
        self.CircularBackground.setMinimumSize(QSize(80, 80))
        self.CircularBackground.setMaximumSize(QSize(80, 80))
        self.CircularBackground.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(45, 55, 43);\n"
"    border: none;\n"
"    border-radius: 40px;\n"
"}")
        self.CircularBackground.setFrameShape(QFrame.Shape.StyledPanel)
        self.CircularBackground.setFrameShadow(QFrame.Shadow.Raised)
        self.Label_CurrentStreakValue_8 = QLabel(self.CircularBackground)
        self.Label_CurrentStreakValue_8.setObjectName(u"Label_CurrentStreakValue_8")
        self.Label_CurrentStreakValue_8.setGeometry(QRect(22, 23, 35, 35))
        self.Label_CurrentStreakValue_8.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 25pt;\n"
"    font-weight: 700;\n"
"    color: rgb(118, 190, 112);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_CurrentStreakValue_8.setPixmap(QPixmap(u"Modules/Assets/Icon/book-open-text.svg"))
        self.Label_CurrentStreakValue_8.setScaledContents(True)
        self.Label_Welcome_2 = QLabel(self.Frame_FavoriteSubject)
        self.Label_Welcome_2.setObjectName(u"Label_Welcome_2")
        self.Label_Welcome_2.setEnabled(True)
        self.Label_Welcome_2.setGeometry(QRect(30, 130, 121, 41))
        font5 = QFont()
        font5.setFamilies([u"Inter"])
        font5.setPointSize(14)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setKerning(True)
        self.Label_Welcome_2.setFont(font5)
        self.Label_Welcome_2.setAutoFillBackground(False)
        self.Label_Welcome_2.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"\n"
"    font-family: \"Inter\";\n"
"    font-size: 14pt;\n"
"    font-weight: 700;\n"
"    color: rgb(240, 240, 240);\n"
"}")
        self.Framel_CurrentFlowerStage = QFrame(self.MainFrame)
        self.Framel_CurrentFlowerStage.setObjectName(u"Framel_CurrentFlowerStage")
        self.Framel_CurrentFlowerStage.setGeometry(QRect(210, 170, 221, 311))
        self.Framel_CurrentFlowerStage.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(35, 36, 39);\n"
"\n"
"    border: 1px solid rgb(58, 60, 64);\n"
"    border-radius: 16px;\n"
"}")
        self.Framel_CurrentFlowerStage.setFrameShape(QFrame.Shape.StyledPanel)
        self.Framel_CurrentFlowerStage.setFrameShadow(QFrame.Shadow.Raised)
        self.Label_SubText_11 = QLabel(self.Framel_CurrentFlowerStage)
        self.Label_SubText_11.setObjectName(u"Label_SubText_11")
        self.Label_SubText_11.setGeometry(QRect(60, 120, 141, 16))
        self.Label_SubText_11.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 8pt;\n"
"    font-weight: 500;\n"
"    color: rgb(145, 145, 155);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.CircularBackground_2 = QFrame(self.Framel_CurrentFlowerStage)
        self.CircularBackground_2.setObjectName(u"CircularBackground_2")
        self.CircularBackground_2.setGeometry(QRect(70, 20, 80, 80))
        self.CircularBackground_2.setMinimumSize(QSize(80, 80))
        self.CircularBackground_2.setMaximumSize(QSize(80, 80))
        self.CircularBackground_2.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(45, 55, 43);\n"
"    border: none;\n"
"    border-radius: 40px;\n"
"}")
        self.CircularBackground_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.CircularBackground_2.setFrameShadow(QFrame.Shadow.Raised)
        self.Label_CurrentStreakValue_9 = QLabel(self.CircularBackground_2)
        self.Label_CurrentStreakValue_9.setObjectName(u"Label_CurrentStreakValue_9")
        self.Label_CurrentStreakValue_9.setGeometry(QRect(18, 18, 41, 41))
        self.Label_CurrentStreakValue_9.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 25pt;\n"
"    font-weight: 700;\n"
"    color: rgb(118, 190, 112);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_CurrentStreakValue_9.setPixmap(QPixmap(u"Modules/Assets/Icon/sprout.svg"))
        self.Label_CurrentStreakValue_9.setScaledContents(True)
        self.Label_Welcome_3 = QLabel(self.Framel_CurrentFlowerStage)
        self.Label_Welcome_3.setObjectName(u"Label_Welcome_3")
        self.Label_Welcome_3.setEnabled(True)
        self.Label_Welcome_3.setGeometry(QRect(20, 130, 181, 41))
        self.Label_Welcome_3.setFont(font5)
        self.Label_Welcome_3.setAutoFillBackground(False)
        self.Label_Welcome_3.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"\n"
"    font-family: \"Inter\";\n"
"    font-size: 14pt;\n"
"    font-weight: 700;\n"
"    color: rgb(240, 240, 240);\n"
"}")
        self.Label_Welcome_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Frame_RecentSession = QFrame(self.MainFrame)
        self.Frame_RecentSession.setObjectName(u"Frame_RecentSession")
        self.Frame_RecentSession.setGeometry(QRect(440, 170, 201, 311))
        self.Frame_RecentSession.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(35, 36, 39);\n"
"\n"
"    border: 1px solid rgb(58, 60, 64);\n"
"    border-radius: 16px;\n"
"}")
        self.Frame_RecentSession.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_RecentSession.setFrameShadow(QFrame.Shadow.Raised)
        self.Label_SubText_13 = QLabel(self.Frame_RecentSession)
        self.Label_SubText_13.setObjectName(u"Label_SubText_13")
        self.Label_SubText_13.setGeometry(QRect(63, 120, 141, 16))
        self.Label_SubText_13.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 8pt;\n"
"    font-weight: 500;\n"
"    color: rgb(145, 145, 155);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.CircularBackground_3 = QFrame(self.Frame_RecentSession)
        self.CircularBackground_3.setObjectName(u"CircularBackground_3")
        self.CircularBackground_3.setGeometry(QRect(60, 20, 80, 80))
        self.CircularBackground_3.setMinimumSize(QSize(80, 80))
        self.CircularBackground_3.setMaximumSize(QSize(80, 80))
        self.CircularBackground_3.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(45, 55, 43);\n"
"    border: none;\n"
"    border-radius: 40px;\n"
"}")
        self.CircularBackground_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.CircularBackground_3.setFrameShadow(QFrame.Shadow.Raised)
        self.Label_CurrentStreakValue_10 = QLabel(self.CircularBackground_3)
        self.Label_CurrentStreakValue_10.setObjectName(u"Label_CurrentStreakValue_10")
        self.Label_CurrentStreakValue_10.setGeometry(QRect(18, 18, 41, 41))
        self.Label_CurrentStreakValue_10.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 25pt;\n"
"    font-weight: 700;\n"
"    color: rgb(118, 190, 112);\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_CurrentStreakValue_10.setPixmap(QPixmap(u"Modules/Assets/Icon/clipboard-clock.svg"))
        self.Label_CurrentStreakValue_10.setScaledContents(True)
        self.Label_Welcome_4 = QLabel(self.Frame_RecentSession)
        self.Label_Welcome_4.setObjectName(u"Label_Welcome_4")
        self.Label_Welcome_4.setEnabled(True)
        self.Label_Welcome_4.setGeometry(QRect(8, 130, 181, 41))
        self.Label_Welcome_4.setFont(font5)
        self.Label_Welcome_4.setAutoFillBackground(False)
        self.Label_Welcome_4.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"\n"
"    font-family: \"Inter\";\n"
"    font-size: 14pt;\n"
"    font-weight: 700;\n"
"    color: rgb(240, 240, 240);\n"
"}")
        self.Label_Welcome_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.Page_Summary)
        self.Page_Study = QWidget()
        self.Page_Study.setObjectName(u"Page_Study")
        self.MainFrame_3 = QFrame(self.Page_Study)
        self.MainFrame_3.setObjectName(u"MainFrame_3")
        self.MainFrame_3.setGeometry(QRect(9, 4, 655, 501))
        self.MainFrame_3.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(28, 28, 30);\n"
"}")
        self.MainFrame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.MainFrame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.Label_Sub = QLabel(self.MainFrame_3)
        self.Label_Sub.setObjectName(u"Label_Sub")
        self.Label_Sub.setGeometry(QRect(11, 10, 351, 41))
        self.Label_Sub.setFont(font1)
        self.Label_Sub.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 20pt;\n"
"    font-weight: 550;\n"
"    color: rgb(240, 240, 240);\n"
"}")
        self.Label_StudyLabel = QLabel(self.MainFrame_3)
        self.Label_StudyLabel.setObjectName(u"Label_StudyLabel")
        self.Label_StudyLabel.setGeometry(QRect(11, 35, 401, 51))
        self.Label_StudyLabel.setFont(font2)
        self.Label_StudyLabel.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 8pt;\n"
"    font-weight: 400;\n"
"    color: rgb(135, 135, 145);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Frame_StudySession = QFrame(self.MainFrame_3)
        self.Frame_StudySession.setObjectName(u"Frame_StudySession")
        self.Frame_StudySession.setGeometry(QRect(10, 80, 281, 181))
        self.Frame_StudySession.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(27, 29, 34);\n"
"    border: 1px solid rgb(45, 48, 55);\n"
"    border-radius: 14px;\n"
"}")
        self.Frame_StudySession.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_StudySession.setFrameShadow(QFrame.Shadow.Raised)
        self.label_SessionSetupIcon = QLabel(self.Frame_StudySession)
        self.label_SessionSetupIcon.setObjectName(u"label_SessionSetupIcon")
        self.label_SessionSetupIcon.setGeometry(QRect(10, 10, 21, 21))
        self.label_SessionSetupIcon.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.label_SessionSetupIcon.setPixmap(QPixmap(u"Modules/Assets/Icon/sliders-horizontal.svg"))
        self.label_SessionSetupIcon.setScaledContents(True)
        self.label_SessionSetupText = QLabel(self.Frame_StudySession)
        self.label_SessionSetupText.setObjectName(u"label_SessionSetupText")
        self.label_SessionSetupText.setGeometry(QRect(39, 12, 121, 16))
        self.label_SessionSetupText.setStyleSheet(u"QLabel {\n"
"	color: rgb(137, 205, 101);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.line_7 = QFrame(self.Frame_StudySession)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(10, 38, 259, 1))
        self.line_7.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(52, 54, 58);\n"
"    border: none;\n"
"    max-height: 1px;\n"
"}")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)
        self.Label_StudyLabel_2 = QLabel(self.Frame_StudySession)
        self.Label_StudyLabel_2.setObjectName(u"Label_StudyLabel_2")
        self.Label_StudyLabel_2.setGeometry(QRect(11, 30, 401, 51))
        self.Label_StudyLabel_2.setFont(font2)
        self.Label_StudyLabel_2.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 8pt;\n"
"    font-weight: 400;\n"
"    color: rgb(135, 135, 145);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.comboBox_subject = QComboBox(self.Frame_StudySession)
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.setObjectName(u"comboBox_subject")
        self.comboBox_subject.setGeometry(QRect(10, 70, 211, 26))
        self.comboBox_subject.setStyleSheet(u"QComboBox {\n"
"    background-color: rgb(25, 26, 28);\n"
"    border: 1px solid rgb(58, 60, 64);\n"
"    border-radius: 8px;\n"
"\n"
"    color: rgb(225, 225, 230);\n"
"\n"
"    font-family: \"Inter\";\n"
"    font-size: 10pt;\n"
"\n"
"    padding: 6px 10px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid rgb(90, 95, 100);\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid rgb(137, 205, 101);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(31, 32, 35);\n"
"    color: rgb(225, 225, 230);\n"
"\n"
"    border: 1px solid rgb(58, 60, 64);\n"
"    selection-background-color: rgb(55, 72, 52);\n"
"    selection-color: rgb(240, 240, 240);\n"
"}")
        self.Label_StudyLabel_3 = QLabel(self.Frame_StudySession)
        self.Label_StudyLabel_3.setObjectName(u"Label_StudyLabel_3")
        self.Label_StudyLabel_3.setGeometry(QRect(11, 90, 401, 51))
        self.Label_StudyLabel_3.setFont(font2)
        self.Label_StudyLabel_3.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 8pt;\n"
"    font-weight: 400;\n"
"    color: rgb(135, 135, 145);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Lineedit_SessionLength = QLineEdit(self.Frame_StudySession)
        self.Lineedit_SessionLength.setObjectName(u"Lineedit_SessionLength")
        self.Lineedit_SessionLength.setGeometry(QRect(10, 130, 211, 26))
        self.Lineedit_SessionLength.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(25, 26, 28);\n"
"    border: 1px solid rgb(58, 60, 64);\n"
"    border-radius: 8px;\n"
"\n"
"    color: rgb(225, 225, 230);\n"
"\n"
"    font-family: \"Inter\";\n"
"    font-size: 10pt;\n"
"\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid rgb(137, 205, 101);\n"
"}")
        self.Frame_Timer = QFrame(self.MainFrame_3)
        self.Frame_Timer.setObjectName(u"Frame_Timer")
        self.Frame_Timer.setGeometry(QRect(310, 80, 321, 321))
        self.Frame_Timer.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(27, 29, 34);\n"
"    border: 1px solid rgb(45, 48, 55);\n"
"    border-radius: 14px;\n"
"}")
        self.Frame_Timer.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_Timer.setFrameShadow(QFrame.Shadow.Raised)
        self.label_SessionSetupIcon_3 = QLabel(self.Frame_Timer)
        self.label_SessionSetupIcon_3.setObjectName(u"label_SessionSetupIcon_3")
        self.label_SessionSetupIcon_3.setGeometry(QRect(10, 10, 21, 21))
        self.label_SessionSetupIcon_3.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.label_SessionSetupIcon_3.setPixmap(QPixmap(u"Modules/Assets/Icon/clipboard-clock.svg"))
        self.label_SessionSetupIcon_3.setScaledContents(True)
        self.label_SessionSetupText_3 = QLabel(self.Frame_Timer)
        self.label_SessionSetupText_3.setObjectName(u"label_SessionSetupText_3")
        self.label_SessionSetupText_3.setGeometry(QRect(39, 12, 121, 16))
        self.label_SessionSetupText_3.setStyleSheet(u"QLabel {\n"
"	color: rgb(137, 205, 101);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_Hour = QLabel(self.Frame_Timer)
        self.Label_Hour.setObjectName(u"Label_Hour")
        self.Label_Hour.setGeometry(QRect(45, 30, 351, 81))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(48)
        font6.setBold(False)
        font6.setItalic(False)
        self.Label_Hour.setFont(font6)
        self.Label_Hour.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_Minute = QLabel(self.Frame_Timer)
        self.Label_Minute.setObjectName(u"Label_Minute")
        self.Label_Minute.setGeometry(QRect(125, 30, 351, 81))
        self.Label_Minute.setFont(font6)
        self.Label_Minute.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_Second = QLabel(self.Frame_Timer)
        self.Label_Second.setObjectName(u"Label_Second")
        self.Label_Second.setGeometry(QRect(205, 30, 351, 81))
        self.Label_Second.setFont(font6)
        self.Label_Second.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_SmallTimeLimit = QLabel(self.Frame_Timer)
        self.Label_SmallTimeLimit.setObjectName(u"Label_SmallTimeLimit")
        self.Label_SmallTimeLimit.setGeometry(QRect(120, 115, 83, 20))
        self.Label_SmallTimeLimit.setMinimumSize(QSize(83, 20))
        self.Label_SmallTimeLimit.setMaximumSize(QSize(83, 20))
        font7 = QFont()
        font7.setFamilies([u"Inter"])
        font7.setPointSize(10)
        font7.setWeight(QFont.Medium)
        font7.setItalic(False)
        self.Label_SmallTimeLimit.setFont(font7)
        self.Label_SmallTimeLimit.setStyleSheet(u"QLabel {\n"
"    background-color: rgb(42, 55, 40);\n"
"    color: rgb(137, 205, 101);\n"
"\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"\n"
"    font-family: \"Inter\";\n"
"    font-size: 10pt;\n"
"    font-weight: 500;\n"
"\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.Label_SmallTimeLimit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Button_StartSession = QPushButton(self.Frame_Timer)
        self.Button_StartSession.setObjectName(u"Button_StartSession")
        self.Button_StartSession.setGeometry(QRect(35, 149, 261, 51))
        self.Button_StartSession.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(137, 205, 101);\n"
"    color: rgb(20, 24, 20);\n"
"\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"\n"
"    font-family: \"Inter\";\n"
"    font-size: 11pt;\n"
"    font-weight: 600;\n"
"\n"
"    padding: 10px 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(151, 218, 114);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(118, 183, 84);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(65, 72, 63);\n"
"    color: rgb(125, 130, 123);\n"
"}")
        self.Label_StartSessionIcon = QLabel(self.Frame_Timer)
        self.Label_StartSessionIcon.setObjectName(u"Label_StartSessionIcon")
        self.Label_StartSessionIcon.setGeometry(QRect(100, 160, 31, 31))
        self.Label_StartSessionIcon.setStyleSheet(u"QLabel {\n"
"	border: None;\n"
"	background-color: transparent;\n"
"}")
        self.Label_StartSessionIcon.setPixmap(QPixmap(u"Modules/Assets/Icon/play.svg"))
        self.Button_RestartSession = QPushButton(self.Frame_Timer)
        self.Button_RestartSession.setObjectName(u"Button_RestartSession")
        self.Button_RestartSession.setGeometry(QRect(50, 210, 231, 41))
        self.Button_RestartSession.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(27, 29, 34);\n"
"    color: rgb(170, 173, 184);\n"
"\n"
"    border: 1px solid rgb(55, 58, 64);\n"
"    border-radius: 10px;\n"
"\n"
"    font-family: \"Inter\";\n"
"    font-size: 11pt;\n"
"    font-weight: 500;\n"
"\n"
"    padding: 10px 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(34, 37, 42);\n"
"    color: rgb(225, 227, 232);\n"
"    border: 1px solid rgb(75, 79, 86);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 24, 28);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: rgb(90, 93, 100);\n"
"    border: 1px solid rgb(45, 47, 52);\n"
"}")
        self.Label_RestartSessionIcon = QLabel(self.Frame_Timer)
        self.Label_RestartSessionIcon.setObjectName(u"Label_RestartSessionIcon")
        self.Label_RestartSessionIcon.setGeometry(QRect(120, 220, 41, 21))
        self.Label_RestartSessionIcon.setStyleSheet(u"QLabel {\n"
"	border: None;\n"
"	background-color: transparent;\n"
"}")
        self.Label_RestartSessionIcon.setPixmap(QPixmap(u"Modules/Assets/Icon/rotate-ccw2.svg"))
        self.Button_RestartSession_2 = QPushButton(self.Frame_Timer)
        self.Button_RestartSession_2.setObjectName(u"Button_RestartSession_2")
        self.Button_RestartSession_2.setGeometry(QRect(70, 260, 191, 41))
        self.Button_RestartSession_2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(205, 82, 82);\n"
"    color: rgb(255, 245, 245);\n"
"\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"\n"
"    font-family: \"Inter\";\n"
"    font-size: 11pt;\n"
"    font-weight: 600;\n"
"\n"
"    padding: 10px 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(220, 95, 95);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(175, 65, 65);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(75, 55, 55);\n"
"    color: rgb(135, 115, 115);\n"
"}")
        self.Label_RestartSessionIcon_2 = QLabel(self.Frame_Timer)
        self.Label_RestartSessionIcon_2.setObjectName(u"Label_RestartSessionIcon_2")
        self.Label_RestartSessionIcon_2.setGeometry(QRect(125, 271, 41, 21))
        self.Label_RestartSessionIcon_2.setStyleSheet(u"QLabel {\n"
"	border: None;\n"
"	background-color: transparent;\n"
"}")
        self.Label_RestartSessionIcon_2.setPixmap(QPixmap(u"Modules/Assets/Icon/octagon-x.svg"))
        self.Frame_SessionOverview = QFrame(self.MainFrame_3)
        self.Frame_SessionOverview.setObjectName(u"Frame_SessionOverview")
        self.Frame_SessionOverview.setGeometry(QRect(10, 280, 281, 201))
        self.Frame_SessionOverview.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(27, 29, 34);\n"
"    border: 1px solid rgb(45, 48, 55);\n"
"    border-radius: 14px;\n"
"}")
        self.Frame_SessionOverview.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_SessionOverview.setFrameShadow(QFrame.Shadow.Raised)
        self.label_SessionSetupText_5 = QLabel(self.Frame_SessionOverview)
        self.label_SessionSetupText_5.setObjectName(u"label_SessionSetupText_5")
        self.label_SessionSetupText_5.setGeometry(QRect(39, 12, 121, 16))
        self.label_SessionSetupText_5.setStyleSheet(u"QLabel {\n"
"	color: rgb(137, 205, 101);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.line_10 = QFrame(self.Frame_SessionOverview)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(10, 38, 259, 1))
        self.line_10.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(52, 54, 58);\n"
"    border: none;\n"
"    max-height: 1px;\n"
"}")
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_SessionSetupIcon_5 = QLabel(self.Frame_SessionOverview)
        self.label_SessionSetupIcon_5.setObjectName(u"label_SessionSetupIcon_5")
        self.label_SessionSetupIcon_5.setGeometry(QRect(10, 10, 21, 21))
        self.label_SessionSetupIcon_5.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.label_SessionSetupIcon_5.setPixmap(QPixmap(u"Modules/Assets/Icon/folder-kanban.svg"))
        self.label_SessionSetupIcon_5.setScaledContents(True)
        self.Label_StudyLabel_8 = QLabel(self.Frame_SessionOverview)
        self.Label_StudyLabel_8.setObjectName(u"Label_StudyLabel_8")
        self.Label_StudyLabel_8.setGeometry(QRect(10, 30, 401, 51))
        self.Label_StudyLabel_8.setFont(font3)
        self.Label_StudyLabel_8.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 10pt;\n"
"    font-weight: 400;\n"
"    color: rgb(135, 135, 145);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_StudyLabel_9 = QLabel(self.Frame_SessionOverview)
        self.Label_StudyLabel_9.setObjectName(u"Label_StudyLabel_9")
        self.Label_StudyLabel_9.setGeometry(QRect(10, 60, 401, 51))
        self.Label_StudyLabel_9.setFont(font3)
        self.Label_StudyLabel_9.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 10pt;\n"
"    font-weight: 400;\n"
"    color: rgb(135, 135, 145);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_StudyLabel_10 = QLabel(self.Frame_SessionOverview)
        self.Label_StudyLabel_10.setObjectName(u"Label_StudyLabel_10")
        self.Label_StudyLabel_10.setGeometry(QRect(10, 90, 401, 51))
        self.Label_StudyLabel_10.setFont(font3)
        self.Label_StudyLabel_10.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 10pt;\n"
"    font-weight: 400;\n"
"    color: rgb(135, 135, 145);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_StudyLabel_11 = QLabel(self.Frame_SessionOverview)
        self.Label_StudyLabel_11.setObjectName(u"Label_StudyLabel_11")
        self.Label_StudyLabel_11.setGeometry(QRect(10, 120, 401, 51))
        self.Label_StudyLabel_11.setFont(font3)
        self.Label_StudyLabel_11.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 10pt;\n"
"    font-weight: 400;\n"
"    color: rgb(135, 135, 145);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_StartSessionIcon_2 = QLabel(self.Frame_SessionOverview)
        self.Label_StartSessionIcon_2.setObjectName(u"Label_StartSessionIcon_2")
        self.Label_StartSessionIcon_2.setGeometry(QRect(190, 51, 10, 10))
        self.Label_StartSessionIcon_2.setStyleSheet(u"QLabel {\n"
"	border: None;\n"
"	background-color: transparent;\n"
"}")
        self.Label_StartSessionIcon_2.setPixmap(QPixmap(u"Modules/Assets/Icon/circle-check.svg"))
        self.Label_StartSessionIcon_2.setScaledContents(True)
        self.Label_StudyLabel_12 = QLabel(self.Frame_SessionOverview)
        self.Label_StudyLabel_12.setObjectName(u"Label_StudyLabel_12")
        self.Label_StudyLabel_12.setGeometry(QRect(205, 30, 401, 51))
        self.Label_StudyLabel_12.setFont(font2)
        self.Label_StudyLabel_12.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 8pt;\n"
"    font-weight: 400;\n"
"    color: rgb(135, 135, 145);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_StudyLabel_13 = QLabel(self.Frame_SessionOverview)
        self.Label_StudyLabel_13.setObjectName(u"Label_StudyLabel_13")
        self.Label_StudyLabel_13.setGeometry(QRect(240, 60, 401, 51))
        self.Label_StudyLabel_13.setFont(font2)
        self.Label_StudyLabel_13.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 8pt;\n"
"    font-weight: 400;\n"
"    color: rgb(135, 135, 145);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_StudyLabel_14 = QLabel(self.Frame_SessionOverview)
        self.Label_StudyLabel_14.setObjectName(u"Label_StudyLabel_14")
        self.Label_StudyLabel_14.setGeometry(QRect(220, 90, 401, 51))
        self.Label_StudyLabel_14.setFont(font2)
        self.Label_StudyLabel_14.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 8pt;\n"
"    font-weight: 400;\n"
"    color: rgb(135, 135, 145);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_StudyLabel_15 = QLabel(self.Frame_SessionOverview)
        self.Label_StudyLabel_15.setObjectName(u"Label_StudyLabel_15")
        self.Label_StudyLabel_15.setGeometry(QRect(250, 120, 401, 51))
        self.Label_StudyLabel_15.setFont(font2)
        self.Label_StudyLabel_15.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 8pt;\n"
"    font-weight: 400;\n"
"    color: rgb(135, 135, 145);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.Label_StartSessionIcon_3 = QLabel(self.Frame_SessionOverview)
        self.Label_StartSessionIcon_3.setObjectName(u"Label_StartSessionIcon_3")
        self.Label_StartSessionIcon_3.setGeometry(QRect(260, 141, 10, 10))
        self.Label_StartSessionIcon_3.setStyleSheet(u"QLabel {\n"
"	border: None;\n"
"	background-color: transparent;\n"
"}")
        self.Label_StartSessionIcon_3.setPixmap(QPixmap(u"Modules/Assets/Icon/broccoli.svg"))
        self.Label_StartSessionIcon_3.setScaledContents(True)
        self.stackedWidget.addWidget(self.Page_Study)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Button_Setting.setText("")
        self.Button_Summary.setText("")
        self.Label_SummaryIcon.setText("")
        self.Label_SettingsIcon.setText("")
        self.Label_SettingsText.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.Label_SummaryText_2.setText(QCoreApplication.translate("MainWindow", u"Summary", None))
        self.Button_Study.setText("")
        self.Label_StudyIcon.setText("")
        self.Label_StudyText.setText(QCoreApplication.translate("MainWindow", u"Study", None))
        self.Label_Leaf.setText("")
        self.Label_StudyBloom.setText(QCoreApplication.translate("MainWindow", u"StudyBloom", None))
        self.Button_Minimize.setText("")
        self.Buttom_Maximize.setText("")
        self.Buttom_Close.setText("")
        self.Label_Welcome_5.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.Label_SummaryText_3.setText(QCoreApplication.translate("MainWindow", u"Customize your StudyBloom experience", None))
        self.Label_UserProfileIcon.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.Label_SummaryText_4.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.Entry_Name.setText("")
        self.Label_UserProfileIcon_2.setText("")
        self.Label_SectiontwoTitle.setText(QCoreApplication.translate("MainWindow", u"Plant & Pet", None))
        self.Label_SummaryText_5.setText(QCoreApplication.translate("MainWindow", u"Show Desktop Plant", None))
        self.Label_SummaryText_6.setText(QCoreApplication.translate("MainWindow", u"Always On Top", None))
        self.Label_SummaryText_7.setText(QCoreApplication.translate("MainWindow", u"Plant Size", None))
        self.Label_SummaryText_8.setText(QCoreApplication.translate("MainWindow", u"Remember Plant Position", None))
        self.CheckBox_ShowDesktopPlant.setText("")
        self.CheckBox_AlwaysOnTop.setText("")
        self.CheckBox_RememberPlantPosition.setText("")
        self.DropdownMenu_PlantSize.setItemText(0, QCoreApplication.translate("MainWindow", u"Small", None))
        self.DropdownMenu_PlantSize.setItemText(1, QCoreApplication.translate("MainWindow", u"Medium", None))
        self.DropdownMenu_PlantSize.setItemText(2, QCoreApplication.translate("MainWindow", u"Large", None))

        self.Label_Welcome.setText(QCoreApplication.translate("MainWindow", u"Welcome, Jake", None))
        self.Label_SummaryText.setText(QCoreApplication.translate("MainWindow", u"Here's your study summary for today", None))
        self.Label_Subtext.setText(QCoreApplication.translate("MainWindow", u"Today's Study Time", None))
        self.Label_StudyTimeValue.setText(QCoreApplication.translate("MainWindow", u"2h 14", None))
        self.Label_StudyTimeIcon.setText("")
        self.Label_SubText_2.setText(QCoreApplication.translate("MainWindow", u"Points Earned Today", None))
        self.Label_PointsEarnedValue.setText(QCoreApplication.translate("MainWindow", u"300", None))
        self.Label_PointImage.setText("")
        self.Label_SubText_3.setText(QCoreApplication.translate("MainWindow", u"Current Streak", None))
        self.Label_CurrentStreakValue.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.Label_PointImage_2.setText("")
        self.Label_SubText_4.setText(QCoreApplication.translate("MainWindow", u"Sessions Today", None))
        self.Label_SessionTodayValue.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Label_PointImage_3.setText("")
        self.Label_SubText_9.setText(QCoreApplication.translate("MainWindow", u"Favorite Subject", None))
        self.Label_CurrentStreakValue_8.setText("")
        self.Label_Welcome_2.setText(QCoreApplication.translate("MainWindow", u"Mathematics", None))
        self.Label_SubText_11.setText(QCoreApplication.translate("MainWindow", u"Current Plant Stage", None))
        self.Label_CurrentStreakValue_9.setText("")
        self.Label_Welcome_3.setText(QCoreApplication.translate("MainWindow", u"Flowering Plant", None))
        self.Label_SubText_13.setText(QCoreApplication.translate("MainWindow", u"Recent Session", None))
        self.Label_CurrentStreakValue_10.setText("")
        self.Label_Welcome_4.setText(QCoreApplication.translate("MainWindow", u"Physics", None))
        self.Label_Sub.setText(QCoreApplication.translate("MainWindow", u"Study", None))
        self.Label_StudyLabel.setText(QCoreApplication.translate("MainWindow", u"Focus, grow, and bloom.", None))
        self.label_SessionSetupIcon.setText("")
        self.label_SessionSetupText.setText(QCoreApplication.translate("MainWindow", u"Session Setup", None))
        self.Label_StudyLabel_2.setText(QCoreApplication.translate("MainWindow", u"Subject:", None))
        self.comboBox_subject.setItemText(0, QCoreApplication.translate("MainWindow", u"Mathematics", None))
        self.comboBox_subject.setItemText(1, QCoreApplication.translate("MainWindow", u"Physics ", None))
        self.comboBox_subject.setItemText(2, QCoreApplication.translate("MainWindow", u"Chemistry", None))
        self.comboBox_subject.setItemText(3, QCoreApplication.translate("MainWindow", u"Language", None))
        self.comboBox_subject.setItemText(4, QCoreApplication.translate("MainWindow", u"Geography", None))
        self.comboBox_subject.setItemText(5, QCoreApplication.translate("MainWindow", u"History", None))
        self.comboBox_subject.setItemText(6, QCoreApplication.translate("MainWindow", u"Computer Science", None))

        self.Label_StudyLabel_3.setText(QCoreApplication.translate("MainWindow", u"Session Length:", None))
        self.Lineedit_SessionLength.setText("")
        self.label_SessionSetupIcon_3.setText("")
        self.label_SessionSetupText_3.setText(QCoreApplication.translate("MainWindow", u"Timer", None))
        self.Label_Hour.setText(QCoreApplication.translate("MainWindow", u"00:", None))
        self.Label_Minute.setText(QCoreApplication.translate("MainWindow", u"00:", None))
        self.Label_Second.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.Label_SmallTimeLimit.setText(QCoreApplication.translate("MainWindow", u"25 minutes", None))
        self.Button_StartSession.setText(QCoreApplication.translate("MainWindow", u"      Start Session", None))
        self.Label_StartSessionIcon.setText("")
        self.Button_RestartSession.setText(QCoreApplication.translate("MainWindow", u"   Restart", None))
        self.Label_RestartSessionIcon.setText("")
        self.Button_RestartSession_2.setText(QCoreApplication.translate("MainWindow", u"  Stop", None))
        self.Label_RestartSessionIcon_2.setText("")
        self.label_SessionSetupText_5.setText(QCoreApplication.translate("MainWindow", u"Session Overview", None))
        self.label_SessionSetupIcon_5.setText("")
        self.Label_StudyLabel_8.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.Label_StudyLabel_9.setText(QCoreApplication.translate("MainWindow", u"Focus Time Today", None))
        self.Label_StudyLabel_10.setText(QCoreApplication.translate("MainWindow", u"Sessions Today", None))
        self.Label_StudyLabel_11.setText(QCoreApplication.translate("MainWindow", u"Total Points Earned Today", None))
        self.Label_StartSessionIcon_2.setText("")
        self.Label_StudyLabel_12.setText(QCoreApplication.translate("MainWindow", u"Not studying", None))
        self.Label_StudyLabel_13.setText(QCoreApplication.translate("MainWindow", u"0 min", None))
        self.Label_StudyLabel_14.setText(QCoreApplication.translate("MainWindow", u"0 sessions", None))
        self.Label_StudyLabel_15.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Label_StartSessionIcon_3.setText("")
    # retranslateUi

