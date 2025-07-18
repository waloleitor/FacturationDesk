from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from frontend.login_window import Ui_MainWindow
from users import USERS
import sys
#import temporal de pruebas
from frontend.forms.form_nueva_factura import FormNuevaFactura
from frontend.forms.form_consulta_facturas import FormConsultaFacturas

class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Facturation-Desk Login")

        #conexion de boton
        self.ui.loginButton.clicked.connect(self.verificar_login)

    def verificar_login(self):
        usuario=self.ui.usernameImput.text()
        clave=self.ui.passwordInput.text()

        if usuario in USERS and USERS[usuario]["password"] == clave:
            rol = USERS[usuario]["rol"]
            self.ventana_consulta = FormConsultaFacturas()
            self.ventana_consulta.show()
            self.hide()        
        #aqui abriremos el panel según el rol
        else: self.ui.messageLabel.setText("Usuario o contraseña incorrectos.")
