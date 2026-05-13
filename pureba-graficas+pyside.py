from PySide6.QtWidgets import QWidget, QApplication, QFrame, QVBoxLayout, QPushButton
from PySide6.QtCore import QTimer
import matplotlib.pyplot as plt
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanva

import sys

def grafica(_canva):
    dias = ["l", "m", 'm', 'j', 'v']
    datos = [0, 1, 2, 3, 4]

    _canva.axes.plot(dias, datos, marker='o', linestyle='-', color='b')
    _canva.axes.set_title("prueba")
    _canva.axes.set_ylabel("dias")
    _canva.axes.set_xlabel("datos")

    _canva.axes.grid(True)

class Grafica(FigureCanva):
    def __init__(self, parent=None, width=500, height=300, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(Grafica, self).__init__(fig)

class GraficasPrograma(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Programas de graficas")
        self.setGeometry(0,0,50,35)

        boton = QPushButton()
        boton.clicked.connect(self.actualizar)
        frame_grafica = QFrame()
        frame_grafica.setStyleSheet("background-color: rgb(255, 0, 0);")

        layout = QVBoxLayout()
        layout.addWidget(frame_grafica)
        self.setLayout(layout)

        self.tiempo = QTimer()
        self.tiempo.setInterval(500)
        self.tiempo.timeout.connect(self.actualizar)
        self.tiempo.start()
        self.canva = Grafica(frame_grafica)
        grafica(self.canva)

        layout.addWidget(self.canva)
        layout.addWidget(boton)

    def actualizar(self):
        self.axes = self.canva.axes
        self.axes.cla()

        # Datos aleatorios
        x = list(range(10))
        y = [random.randint(0, 100) for _ in x]

        # Dibujamos con un estilo más limpio
        self.axes.plot(x, y, 'r-o', label="Muestreo Dinámico")
        self.axes.set_title("Monitor de Datos en Tiempo Real")
        self.axes.set_xlabel("Intervalo")
        self.axes.set_ylabel("Valor")
        self.axes.grid(True, linestyle='--', alpha=0.6)
        self.axes.legend()

        # ¡Importante! Refrescar el lienzo
        self.canva.draw()

