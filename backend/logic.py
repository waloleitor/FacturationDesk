from backend.database import SessionLocal
from backend.models import Factura, MetodoCobro
from datetime import date

def crear_factura_demo():
    session = SessionLocal()

    factura = Factura(
        fecha_factura=date(2024, 7, 10),
        numero_factura="17034448",
        cliente="Cliente de prueba",
        ruta="MA2",
        precio=155.75,
        pdf_path="facturas/factura17034448.pdf",
        cobrada=True,
        rechazada=False,
        metodo_cobro=MetodoCobro.transferencia,
        fecha_cobro=date(2024, 7, 11),
        entregada_ppcr=True,
        fecha_entrega=date(2024, 7, 11),
        creada_por="admin"
    )

    session.add(factura)
    session.commit()
    session.close()

    print("Factura de prueba guardada con éxito!")