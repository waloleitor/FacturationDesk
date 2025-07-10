# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nueva_factura.ui'
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
    QDoubleSpinBox, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(467, 443)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 451, 411))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.fechaFacturaInput = QDateEdit(self.formLayoutWidget)
        self.fechaFacturaInput.setObjectName(u"fechaFacturaInput")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.fechaFacturaInput)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.numeroFacturaInput = QLineEdit(self.formLayoutWidget)
        self.numeroFacturaInput.setObjectName(u"numeroFacturaInput")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.numeroFacturaInput)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.clienteInput = QLineEdit(self.formLayoutWidget)
        self.clienteInput.setObjectName(u"clienteInput")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.clienteInput)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.rutaInput = QLineEdit(self.formLayoutWidget)
        self.rutaInput.setObjectName(u"rutaInput")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.rutaInput)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.precioInput = QDoubleSpinBox(self.formLayoutWidget)
        self.precioInput.setObjectName(u"precioInput")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.precioInput)

        self.cargarPdfButton = QPushButton(self.formLayoutWidget)
        self.cargarPdfButton.setObjectName(u"cargarPdfButton")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.cargarPdfButton)

        self.cobradaCheck = QCheckBox(self.formLayoutWidget)
        self.cobradaCheck.setObjectName(u"cobradaCheck")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.cobradaCheck)

        self.rechazadaCheck = QCheckBox(self.formLayoutWidget)
        self.rechazadaCheck.setObjectName(u"rechazadaCheck")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.rechazadaCheck)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.metodoCobroInput = QComboBox(self.formLayoutWidget)
        self.metodoCobroInput.addItem("")
        self.metodoCobroInput.addItem("")
        self.metodoCobroInput.addItem("")
        self.metodoCobroInput.addItem("")
        self.metodoCobroInput.setObjectName(u"metodoCobroInput")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.metodoCobroInput)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.fechaCobroInput = QDateEdit(self.formLayoutWidget)
        self.fechaCobroInput.setObjectName(u"fechaCobroInput")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.fechaCobroInput)

        self.entregadaCheck = QCheckBox(self.formLayoutWidget)
        self.entregadaCheck.setObjectName(u"entregadaCheck")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.FieldRole, self.entregadaCheck)

        self.fechaEntregaInput = QDateEdit(self.formLayoutWidget)
        self.fechaEntregaInput.setObjectName(u"fechaEntregaInput")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.FieldRole, self.fechaEntregaInput)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.guardarFacturaButton = QPushButton(self.formLayoutWidget)
        self.guardarFacturaButton.setObjectName(u"guardarFacturaButton")

        self.formLayout.setWidget(12, QFormLayout.ItemRole.FieldRole, self.guardarFacturaButton)

        self.statusLabel = QLabel(self.formLayoutWidget)
        self.statusLabel.setObjectName(u"statusLabel")

        self.formLayout.setWidget(13, QFormLayout.ItemRole.SpanningRole, self.statusLabel)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Fecha de factura", None))
#if QT_CONFIG(tooltip)
        self.fechaFacturaInput.setToolTip(QCoreApplication.translate("Form", u"Fecha de la factura", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"N\u00famero de factura", None))
#if QT_CONFIG(tooltip)
        self.numeroFacturaInput.setToolTip(QCoreApplication.translate("Form", u"C\u00f3digo \u00fanico de la factura", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"Cliente", None))
#if QT_CONFIG(tooltip)
        self.clienteInput.setToolTip(QCoreApplication.translate("Form", u"Nombre del cliente", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Form", u"Ruta", None))
#if QT_CONFIG(tooltip)
        self.rutaInput.setToolTip(QCoreApplication.translate("Form", u"Ruta de reparto", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Form", u"Precio", None))
#if QT_CONFIG(tooltip)
        self.precioInput.setToolTip(QCoreApplication.translate("Form", u"precio decimal, m\u00ednimo 0", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cargarPdfButton.setToolTip(QCoreApplication.translate("Form", u"Cargar y abrir PDF", None))
#endif // QT_CONFIG(tooltip)
        self.cargarPdfButton.setText(QCoreApplication.translate("Form", u"Cargar PDF", None))
        self.cobradaCheck.setText(QCoreApplication.translate("Form", u"Cobrada", None))
        self.rechazadaCheck.setText(QCoreApplication.translate("Form", u"Rechazada", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"M\u00e9todo de pago", None))
        self.metodoCobroInput.setItemText(0, QCoreApplication.translate("Form", u"Tarjeta", None))
        self.metodoCobroInput.setItemText(1, QCoreApplication.translate("Form", u"Efectivo", None))
        self.metodoCobroInput.setItemText(2, QCoreApplication.translate("Form", u"Transferencia", None))
        self.metodoCobroInput.setItemText(3, QCoreApplication.translate("Form", u"Otros", None))

#if QT_CONFIG(tooltip)
        self.metodoCobroInput.setToolTip(QCoreApplication.translate("Form", u"M\u00e9todo de cobro", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("Form", u"Fecha de cobro", None))
        self.entregadaCheck.setText(QCoreApplication.translate("Form", u"Entregada a PPCR", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Fecha de entrega", None))
        self.guardarFacturaButton.setText(QCoreApplication.translate("Form", u"Guardar factura", None))
        self.statusLabel.setText("")
    # retranslateUi

