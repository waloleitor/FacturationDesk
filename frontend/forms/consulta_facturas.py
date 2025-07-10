# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'consulta_facturas.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFormLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(760, 422)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 741, 401))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(14, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.numeroFacturaInput = QLineEdit(self.formLayoutWidget)
        self.numeroFacturaInput.setObjectName(u"numeroFacturaInput")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.numeroFacturaInput)

        self.clienteInput = QLineEdit(self.formLayoutWidget)
        self.clienteInput.setObjectName(u"clienteInput")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.clienteInput)

        self.rutaInput = QLineEdit(self.formLayoutWidget)
        self.rutaInput.setObjectName(u"rutaInput")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.rutaInput)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.filtroCobradaCheck = QCheckBox(self.formLayoutWidget)
        self.filtroCobradaCheck.setObjectName(u"filtroCobradaCheck")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.filtroCobradaCheck)

        self.metodoCobroCombo = QComboBox(self.formLayoutWidget)
        self.metodoCobroCombo.addItem("")
        self.metodoCobroCombo.addItem("")
        self.metodoCobroCombo.addItem("")
        self.metodoCobroCombo.addItem("")
        self.metodoCobroCombo.addItem("")
        self.metodoCobroCombo.setObjectName(u"metodoCobroCombo")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.metodoCobroCombo)

        self.filtroRechazadaCheck = QCheckBox(self.formLayoutWidget)
        self.filtroRechazadaCheck.setObjectName(u"filtroRechazadaCheck")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.filtroRechazadaCheck)

        self.fechaDesdeInput = QDateEdit(self.formLayoutWidget)
        self.fechaDesdeInput.setObjectName(u"fechaDesdeInput")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.fechaDesdeInput)

        self.fechaHastaInput = QDateEdit(self.formLayoutWidget)
        self.fechaHastaInput.setObjectName(u"fechaHastaInput")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.FieldRole, self.fechaHastaInput)

        self.consultarButton = QPushButton(self.formLayoutWidget)
        self.consultarButton.setObjectName(u"consultarButton")

        self.formLayout.setWidget(12, QFormLayout.ItemRole.SpanningRole, self.consultarButton)

        self.tablaResultados = QTableWidget(self.formLayoutWidget)
        self.tablaResultados.setObjectName(u"tablaResultados")

        self.formLayout.setWidget(14, QFormLayout.ItemRole.FieldRole, self.tablaResultados)

        self.usarFechaDesdeCheck = QCheckBox(self.formLayoutWidget)
        self.usarFechaDesdeCheck.setObjectName(u"usarFechaDesdeCheck")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.usarFechaDesdeCheck)

        self.usarFechaHastaCheck = QCheckBox(self.formLayoutWidget)
        self.usarFechaHastaCheck.setObjectName(u"usarFechaHastaCheck")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.FieldRole, self.usarFechaHastaCheck)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"N\u00famero de factura", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Cliente", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Ruta", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"M\u00e9todo de cobro", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Fecha factura desde", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Fecha factura hasta", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Resultado", None))
#if QT_CONFIG(tooltip)
        self.numeroFacturaInput.setToolTip(QCoreApplication.translate("Form", u"N\u00famero de factura", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.clienteInput.setToolTip(QCoreApplication.translate("Form", u"Cliente", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.rutaInput.setToolTip(QCoreApplication.translate("Form", u"Ej: MA2", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText("")
        self.filtroCobradaCheck.setText(QCoreApplication.translate("Form", u"Cobrado", None))
        self.metodoCobroCombo.setItemText(0, QCoreApplication.translate("Form", u"Todos", None))
        self.metodoCobroCombo.setItemText(1, QCoreApplication.translate("Form", u"Tarjeta", None))
        self.metodoCobroCombo.setItemText(2, QCoreApplication.translate("Form", u"Efectivo", None))
        self.metodoCobroCombo.setItemText(3, QCoreApplication.translate("Form", u"Transferencia", None))
        self.metodoCobroCombo.setItemText(4, QCoreApplication.translate("Form", u"Otros", None))

        self.filtroRechazadaCheck.setText(QCoreApplication.translate("Form", u"Rechazado", None))
#if QT_CONFIG(tooltip)
        self.consultarButton.setToolTip(QCoreApplication.translate("Form", u"Comenzar consulta", None))
#endif // QT_CONFIG(tooltip)
        self.consultarButton.setText(QCoreApplication.translate("Form", u"Consultar", None))
        self.usarFechaDesdeCheck.setText(QCoreApplication.translate("Form", u"Filtrar desde esta fecha", None))
        self.usarFechaHastaCheck.setText(QCoreApplication.translate("Form", u"Filtrar hasta esta fecha", None))
    # retranslateUi

