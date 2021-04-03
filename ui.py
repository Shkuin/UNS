# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1079, 614)
        Form.setStyleSheet(u"QWidget {\n"
"		background-color: #0f0f0f;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	border-radius: 3px;\n"
"	background-color: #49494a;\n"
"	color: #fcdea2;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"\n"
"	}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #baa884;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #eddbb7;\n"
"	color: #0f0f0f;\n"
"}\n"
"\n"
"\n"
"QLineEdit {\n"
"	border-radius: 3px;\n"
"	background-color: #49494a;\n"
"	width: 300px;\n"
"	height: 30px;\n"
"	color: #fcdea2;\n"
"	font-size: 20px;\n"
"	letter-space: 2px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QLineEdit:pressed {\n"
"	background-color: white;\n"
"\n"
"}\n"
"\n"
"QLabel  {\n"
"color: #fcdea2;\n"
"font-size: 20px;\n"
"text-align: center;\n"
"}")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(430, 440, 221, 41))
        self.pushButton.setStyleSheet(u"")
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(230, 150, 691, 256))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lineEdit_2 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lineEdit_2)

        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lineEdit)

        self.lineEdit_3 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.lineEdit_7)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.formLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.label_7)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_2)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 0, 81, 41))
        self.label_8.setStyleSheet(u"text-align: center;\n"
"font-size: 20px;\n"
"color: #85827d;")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(430, 50, 221, 41))
        self.pushButton_2.setStyleSheet(u"")
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 120, 991, 20))
        self.label_9.setStyleSheet(u"color: #85827d;\n"
"font-size: 15px;")
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 530, 1101, 51))
        self.label_10.setStyleSheet(u"color: #fcdea2;\n"
"font-size: 15px;\n"
"font-weight: bold;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
        self.lineEdit_2.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043b\u0438\u0441\u0442\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b\u043e\u043d\u043a\u0430 \u043d\u043e\u0432\u044b\u0445 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b\u043e\u043d\u043a\u0430 \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b\u043e\u043d\u043a\u0430 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 1", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b\u043e\u043d\u043a\u0430 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 2", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0447\u0430\u043b\u043e \u043f\u043e\u0438\u0441\u043a\u0430 (\u0441\u0442\u0440\u043e\u043a\u0430)", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043d\u0435\u0446 \u043f\u043e\u0438\u0441\u043a\u0430 (\u0441\u0442\u0440\u043e\u043a\u0430)", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u042e\u041d\u0421-\u041b\u0422", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430: ", None))
        self.label_10.setText("")
    # retranslateUi

