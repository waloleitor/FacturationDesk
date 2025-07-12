from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from frontend.forms.impresion_facturas import Ui_Form
from backend.database import SessionLocal
from backend.models import Factura
from datetime import date


class FormImpresionFacturas(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Imprimir facturas entregadas")

        self.ui.buscarButton.clicked.connect(self.consultar_facturas)
        self.ui.imprimirButton.clicked.connect(self.imprimir_resultados)

    def consultar_facturas(self):
        session = SessionLocal()
        try:
            query = session.query(Factura)

            if self.ui.usarFechaDesdeCheck.isChecked():
                desde = self.ui.fechaDesdeInput.date().toPython()
                query = query.filter(Factura.fecha_factura >= desde)

            if self.ui.usarFechaHastaCheck.isChecked():
                hasta = self.ui.fechaHastaInput.date().toPython()
                query = query.filter(Factura.fecha_factura <= hasta)

            if self.ui.numeroFacturaInput.text():
                query = query.filter(Factura.numero_factura.like(f"%{self.ui.numeroFacturaInput.text()}%"))

            if self.ui.clienteInput.text():
                query = query.filter(Factura.cliente.like(f"%{self.ui.clienteInput.text()}%"))

            if self.ui.rutaInput.text():
                query = query.filter(Factura.ruta.like(f"%{self.ui.rutaInput.text()}%"))

            if self.ui.soloEntregadasCheck.isChecked():
                query = query.filter(Factura.entregada_ppcr == True)

            if self.ui.soloRechazadasCheck.isChecked():
                query = query.filter(Factura.rechazada == True)

            if self.ui.soloCobradasCheck.isChecked():
                query = query.filter(Factura.cobrada == True)

            if self.ui.soloPendientesCheck.isChecked():
                query = query.filter(Factura.cobrada == False, Factura.rechazada == False)

            resultados = query.all()
            texto = ""

            for f in resultados:
                texto += f"{f.fecha_factura} | {f.numero_factura} | {f.cliente} | {f.ruta} | {f.precio}€\n"

            if not resultados:
                texto = "No se encontraron facturas con esos filtros."

            self.ui.resultadoText.setPlainText(texto)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error: {str(e)}")
        finally:
            session.close()

    def imprimir_resultados(self):
        QMessageBox.information(self, "Imprimir", "Aquí se implementará la exportación a PDF o impresión directa más adelante.")
