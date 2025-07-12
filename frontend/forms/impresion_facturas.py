# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_impresion_facturas.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QFormLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_FormImpresionFacturas(object):
    def setupUi(self, FormImpresionFacturas):
        if not FormImpresionFacturas.objectName():
            FormImpresionFacturas.setObjectName(u"FormImpresionFacturas")
        FormImpresionFacturas.resize(818, 432)
        self.formLayoutWidget = QWidget(FormImpresionFacturas)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 801, 741))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.numeroFacturaInput = QLineEdit(self.formLayoutWidget)
        self.numeroFacturaInput.setObjectName(u"numeroFacturaInput")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.numeroFacturaInput)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.clienteInput = QLineEdit(self.formLayoutWidget)
        self.clienteInput.setObjectName(u"clienteInput")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.clienteInput)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.rutaInput = QLineEdit(self.formLayoutWidget)
        self.rutaInput.setObjectName(u"rutaInput")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.rutaInput)

        self.usarFechaDesdeCheck = QCheckBox(self.formLayoutWidget)
        self.usarFechaDesdeCheck.setObjectName(u"usarFechaDesdeCheck")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.usarFechaDesdeCheck)

        self.fechaDesdeInput = QDateEdit(self.formLayoutWidget)
        self.fechaDesdeInput.setObjectName(u"fechaDesdeInput")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.fechaDesdeInput)

        self.usarFechaHastaCheck = QCheckBox(self.formLayoutWidget)
        self.usarFechaHastaCheck.setObjectName(u"usarFechaHastaCheck")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.usarFechaHastaCheck)

        self.fechaHastaInput = QDateEdit(self.formLayoutWidget)
        self.fechaHastaInput.setObjectName(u"fechaHastaInput")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.fechaHastaInput)

        self.soloEntregadasCheck = QCheckBox(self.formLayoutWidget)
        self.soloEntregadasCheck.setObjectName(u"soloEntregadasCheck")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.soloEntregadasCheck)

        self.soloRechazadasCheck = QCheckBox(self.formLayoutWidget)
        self.soloRechazadasCheck.setObjectName(u"soloRechazadasCheck")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.soloRechazadasCheck)

        self.soloCobradasCheck = QCheckBox(self.formLayoutWidget)
        self.soloCobradasCheck.setObjectName(u"soloCobradasCheck")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.soloCobradasCheck)

        self.soloPendientesCheck = QCheckBox(self.formLayoutWidget)
        self.soloPendientesCheck.setObjectName(u"soloPendientesCheck")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.soloPendientesCheck)

        self.tablaResultados = QTableWidget(self.formLayoutWidget)
        self.tablaResultados.setObjectName(u"tablaResultados")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.SpanningRole, self.tablaResultados)

        self.imprimirButton = QPushButton(self.formLayoutWidget)
        self.imprimirButton.setObjectName(u"imprimirButton")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.SpanningRole, self.imprimirButton)


        self.retranslateUi(FormImpresionFacturas)

        QMetaObject.connectSlotsByName(FormImpresionFacturas)
    # setupUi

    def retranslateUi(self, FormImpresionFacturas):
        FormImpresionFacturas.setWindowTitle(QCoreApplication.translate("FormImpresionFacturas", u"Imprimir Facturas", None))
        self.label.setText(QCoreApplication.translate("FormImpresionFacturas", u"N\u00famero factura", None))
        self.label_2.setText(QCoreApplication.translate("FormImpresionFacturas", u"Cliente", None))
        self.label_3.setText(QCoreApplication.translate("FormImpresionFacturas", u"Ruta", None))
        self.usarFechaDesdeCheck.setText(QCoreApplication.translate("FormImpresionFacturas", u"Fecha desde", None))
        self.usarFechaHastaCheck.setText(QCoreApplication.translate("FormImpresionFacturas", u"Fecha hasta", None))
        self.soloEntregadasCheck.setText(QCoreApplication.translate("FormImpresionFacturas", u"Entregada PPCR", None))
        self.soloRechazadasCheck.setText(QCoreApplication.translate("FormImpresionFacturas", u"Rechazadas", None))
        self.soloCobradasCheck.setText(QCoreApplication.translate("FormImpresionFacturas", u"Cobradas", None))
        self.soloPendientesCheck.setText(QCoreApplication.translate("FormImpresionFacturas", u"Pendientes de cobro", None))
        self.imprimirButton.setText(QCoreApplication.translate("FormImpresionFacturas", u"Imprimir facturas filtradas", None))
    # retranslateUi

