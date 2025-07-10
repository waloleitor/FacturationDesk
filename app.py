from PySide6.QtWidgets import QApplication
from frontend.main_window import LoginApp
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = LoginApp()
    ventana.show()
    sys.exit(app.exec())
