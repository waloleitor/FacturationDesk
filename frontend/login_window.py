# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(615, 479)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(180, 70, 231, 111))
        self.usernameImput = QLineEdit(self.centralwidget)
        self.usernameImput.setObjectName(u"usernameImput")
        self.usernameImput.setGeometry(QRect(210, 200, 171, 22))
        self.passwordInput = QLineEdit(self.centralwidget)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setGeometry(QRect(210, 240, 171, 22))
        self.loginButton = QPushButton(self.centralwidget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(250, 280, 81, 24))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(60, 50, 461, 331))
        self.messageLabel = QLabel(self.groupBox)
        self.messageLabel.setObjectName(u"messageLabel")
        self.messageLabel.setGeometry(QRect(90, 290, 281, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.groupBox.raise_()
        self.titleLabel.raise_()
        self.usernameImput.raise_()
        self.passwordInput.raise_()
        self.loginButton.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 615, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; text-decoration: underline; color:#ff0000;\">Facturarion-Desk</span></p></body></html>", None))
        self.usernameImput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesi\u00f3n", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"inicio_sesion", None))
        self.messageLabel.setText("")
    # retranslateUi

