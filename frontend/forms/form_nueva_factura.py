from PySide6.QtWidgets import QWidget, QFileDialog
from frontend.forms.nueva_factura import Ui_Form
from backend.database import SessionLocal
from backend.models import Factura, MetodoCobro
from datetime import date

class FormNuevaFactura(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Nueva factura")

        #conectar boton de guardar
        self.ui.guardarFacturaButton.clicked.connect(self.guardar_factura)

        #PDF seleccionado
        self.pdf_path =""

    def cargar_pdf(self):
        archivo, _ = QFileDialog.getOpenFileName(self, "Selecciona el PDF", "", "PDF Files (*.pdf)" )
        if archivo: 
            self.pdf_path = archivo
            self.ui.statusLabel.setText(f"PDF cargado: {archivo}")

    def guardar_factura(self):
        session = SessionLocal()

        try:
            factura = Factura(
                fecha_factura=self.ui.fechaFacturaInput.date().toPython(),
                numero_factura=self.ui.numeroFacturaInput.text(),
                cliente=self.ui.clienteInput.text(),
                ruta=self.ui.rutaInput.text(),
                precio=self.ui.precioInput.value(),
                pdf_path=self.pdf_path,

                cobrada=self.ui.cobradaCheck.isChecked(),
                rechazada=self.ui.rechazadaCheck.isChecked(),
                metodo_cobro=MetodoCobro[self.ui.metodoCobroInput.currentText().lower()],
                fecha_cobro=self.ui.fechaCobroInput.date().toPython() if self.ui.cobradaCheck.isChecked() else None,

                entregada_ppcr=self.ui.entregadaCheck.isChecked(),
                fecha_entrega=self.ui.fechaEntregaInput.date().toPython() if self.ui.entregadaCheck.isChecked() else None,

                creada_por="admin" #mantener mientras testeo
            )

            session.add(factura)
            session.commit()
            self.ui.statusLabel.setText("Factura guardada con éxito!!")

        except Exception as e:
            self.ui.statusLabel.setText(f"Error!: {str(e)}")

        finally:
            session.close()