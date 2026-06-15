# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ApphssnjF.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QSpinBox, QTabWidget,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(490, 403)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_exactCount = QLabel(Form)
        self.label_exactCount.setObjectName(u"label_exactCount")

        self.gridLayout.addWidget(self.label_exactCount, 2, 1, 1, 1)

        self.progressBar_capacity = QProgressBar(Form)
        self.progressBar_capacity.setObjectName(u"progressBar_capacity")
        self.progressBar_capacity.setValue(24)

        self.gridLayout.addWidget(self.progressBar_capacity, 2, 2, 1, 1)

        self.label_capacity = QLabel(Form)
        self.label_capacity.setObjectName(u"label_capacity")

        self.gridLayout.addWidget(self.label_capacity, 2, 0, 1, 1)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setDocumentMode(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.formLayout = QFormLayout(self.tab)
        self.formLayout.setObjectName(u"formLayout")
        self.label_noOfSpots = QLabel(self.tab)
        self.label_noOfSpots.setObjectName(u"label_noOfSpots")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_noOfSpots)

        self.spin_noOfSpots = QSpinBox(self.tab)
        self.spin_noOfSpots.setObjectName(u"spin_noOfSpots")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spin_noOfSpots)

        self.label_treeTypes = QLabel(self.tab)
        self.label_treeTypes.setObjectName(u"label_treeTypes")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_treeTypes)

        self.comboBox_treeTypes = QComboBox(self.tab)
        self.comboBox_treeTypes.addItem("")
        self.comboBox_treeTypes.addItem("")
        self.comboBox_treeTypes.addItem("")
        self.comboBox_treeTypes.setObjectName(u"comboBox_treeTypes")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox_treeTypes)

        self.pushButton_saveConfig = QPushButton(self.tab)
        self.pushButton_saveConfig.setObjectName(u"pushButton_saveConfig")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.pushButton_saveConfig)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line = QFrame(self.tab_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 2)

        self.pushButton_enter = QPushButton(self.tab_2)
        self.pushButton_enter.setObjectName(u"pushButton_enter")

        self.gridLayout_2.addWidget(self.pushButton_enter, 2, 0, 1, 1)

        self.label_message = QLabel(self.tab_2)
        self.label_message.setObjectName(u"label_message")

        self.gridLayout_2.addWidget(self.label_message, 3, 0, 1, 2)

        self.lineEdit_enterRegNo = QLineEdit(self.tab_2)
        self.lineEdit_enterRegNo.setObjectName(u"lineEdit_enterRegNo")

        self.gridLayout_2.addWidget(self.lineEdit_enterRegNo, 0, 1, 1, 1)

        self.pushButton_leave = QPushButton(self.tab_2)
        self.pushButton_leave.setObjectName(u"pushButton_leave")

        self.gridLayout_2.addWidget(self.pushButton_leave, 2, 1, 1, 1)

        self.label_enterRegNo = QLabel(self.tab_2)
        self.label_enterRegNo.setObjectName(u"label_enterRegNo")

        self.gridLayout_2.addWidget(self.label_enterRegNo, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 4, 0, 1, 1)

        self.pushButton_1 = QPushButton(self.tab_2)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.gridLayout_2.addWidget(self.pushButton_1, 4, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 3)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_exactCount.setText(QCoreApplication.translate("Form", u"5/10", None))
        self.label_capacity.setText(QCoreApplication.translate("Form", u"Current Occupancy:", None))
        self.label_noOfSpots.setText(QCoreApplication.translate("Form", u"Enter the number of parking spots:", None))
        self.label_treeTypes.setText(QCoreApplication.translate("Form", u"Choose Tree type:", None))
        self.comboBox_treeTypes.setItemText(0, QCoreApplication.translate("Form", u"Binary Search Tree", None))
        self.comboBox_treeTypes.setItemText(1, QCoreApplication.translate("Form", u"AVL Tree", None))


        self.pushButton_saveConfig.setText(QCoreApplication.translate("Form", u"Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Tab 1", None))
        self.pushButton_enter.setText(QCoreApplication.translate("Form", u"I'd like to find a spot to park", None))
        self.label_message.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton_leave.setText(QCoreApplication.translate("Form", u"I'm leaving", None))
        self.label_enterRegNo.setText(QCoreApplication.translate("Form", u"Enter your vehicle Reg.No: ", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Print Receipt", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Tab 2", None))
    # retranslateUi

