import sys
import os
from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl


class Pro(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)
        self.box = QVBoxLayout()
        self.ventana_web = QWebEngineView()
        self.box.addWidget(self.ventana_web)
        self.setLayout(self.box)

        ruta_archivo = os.path.abspath("eppaaa.html")
        self.ventana_web.load(QUrl.fromLocalFile(ruta_archivo))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pro = Pro()
    pro.show()
    app.exec()
