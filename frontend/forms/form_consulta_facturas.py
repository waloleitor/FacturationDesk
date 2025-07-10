from PySide6.QtWidgets import QWidget, QTableWidgetItem
from frontend.forms.consulta_facturas import Ui_Form
from backend.database import SessionLocal
from backend.models import Factura, MetodoCobro
from datetime import date

class FormConsultaFacturas(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Consulta de Facturas")

        # Conectar botón de consultar
        self.ui.consultarButton.clicked.connect(self.consultar_facturas)

        # Configurar tabla
        self.ui.tablaResultados.setColumnCount(6)
        self.ui.tablaResultados.setHorizontalHeaderLabels([
            "Nº Factura", "Cliente", "Ruta", "Precio", "Cobrada", "Fecha"
        ])

    def consultar_facturas(self):
        session = SessionLocal()
        query = session.query(Factura)

        # Filtros del formulario
        numero = self.ui.numeroFacturaInput.text()
        cliente = self.ui.clienteInput.text()
        ruta = self.ui.rutaInput.text()
        metodo = self.ui.metodoCobroCombo.currentText().lower()
        desde = self.ui.fechaDesdeInput.date().toPython()
        hasta = self.ui.fechaHastaInput.date().toPython()

        # Aplicar filtros solo si el usuario los usa
        if numero.strip():
            query = query.filter(Factura.numero_factura.contains(numero.strip()))
        if cliente.strip():
            query = query.filter(Factura.cliente.contains(cliente.strip()))
        if ruta.strip():
            query = query.filter(Factura.ruta.contains(ruta.strip()))
        if self.ui.filtroCobradaCheck.isChecked():
            query = query.filter(Factura.cobrada == True)
        if self.ui.filtroRechazadaCheck.isChecked():
            query = query.filter(Factura.rechazada == True)
        if metodo != "todos":
            query = query.filter(Factura.metodo_cobro == MetodoCobro[metodo])
        if self.ui.usarFechaDesdeCheck.isChecked():
            query = query.filter(Factura.fecha_factura >= desde)
        if self.ui.usarFechaHastaCheck.isChecked():
            query = query.filter(Factura.fecha_factura <= hasta)

        resultados = query.all()
        self.ui.tablaResultados.setRowCount(len(resultados))

        for fila, factura in enumerate(resultados):
            self.ui.tablaResultados.setItem(fila, 0, QTableWidgetItem(factura.numero_factura))
            self.ui.tablaResultados.setItem(fila, 1, QTableWidgetItem(factura.cliente))
            self.ui.tablaResultados.setItem(fila, 2, QTableWidgetItem(factura.ruta))
            self.ui.tablaResultados.setItem(fila, 3, QTableWidgetItem(f"{factura.precio:.2f} €"))
            self.ui.tablaResultados.setItem(fila, 4, QTableWidgetItem("Sí" if factura.cobrada else "No"))
            self.ui.tablaResultados.setItem(fila, 5, QTableWidgetItem(str(factura.fecha_factura)))

        session.close()
