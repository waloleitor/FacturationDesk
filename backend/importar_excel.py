import openpyxl
from backend.database import SessionLocal
from backend.models import Factura, MetodoCobro
from datetime import datetime

def importar_facturas_desde_excel(ruta_archivo):
    wb = openpyxl.load_workbook(ruta_archivo)
    hoja = wb.active
    session = SessionLocal()

    filas_importadas = 0

    try:
        for fila in hoja.iter_rows(min_row=2, values_only=True):
            (
                fecha_factura,
                numero_factura,
                cliente,
                ruta,
                precio,
                cobrada,
                rechazada,
                metodo_cobro,
                fecha_cobro,
                entregada_ppcr,
                fecha_entrega,
                pdf_path,
                creada_por
            ) = fila

            factura = Factura(
                fecha_factura = fecha_factura.date() if isinstance(fecha_factura, datetime) else datetime.strptime(str(fecha_factura).split()[0], "%Y-%m-%d").date(),
                numero_factura=numero_factura,
                cliente=cliente,
                ruta=ruta,
                precio=float(precio),
                cobrada=bool(cobrada),
                rechazada=bool(rechazada),
                metodo_cobro=MetodoCobro[metodo_cobro.lower()],
                fecha_cobro = datetime.strptime(str(fecha_cobro).split()[0], "%Y-%m-%d").date() if fecha_cobro else None,
                entregada_ppcr=bool(entregada_ppcr),
                fecha_entrega = datetime.strptime(str(fecha_entrega).split()[0], "%Y-%m-%d").date() if fecha_entrega else None,
                pdf_path=pdf_path,
                creada_por=creada_por or "importador"
            )

            session.add(factura)
            filas_importadas += 1

        session.commit()
        print(f"✅ Importadas {filas_importadas} facturas correctamente.")
    except Exception as e:
        print(f"❌ Error al importar: {e}")
    finally:
        session.close()
