from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QPushButton, 
                             QSpinBox, QDoubleSpinBox, QGridLayout, QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class TarjetaFormulario(QFrame):
    """Contenedor visual con bordes redondeados para agrupar los campos de entrada."""
    def __init__(self, titulo, color_borde="#ff9500"):
        super().__init__()
        self.setStyleSheet(f"""
            QFrame {{
                background-color: #111519;
                border: 1px solid {color_borde};
                border-radius: 8px;
            }}
            QLabel {{
                color: #cbd5e1;
                font-size: 12px;
                border: none;
                background: transparent;
            }}
        """)
        self.layout_grid = QGridLayout(self)
        self.layout_grid.setContentsMargins(15, 15, 15, 15)
        self.layout_grid.setSpacing(12)
        
        lbl_titulo = QLabel(titulo.upper())
        lbl_titulo.setFont(QFont("Segoe UI", 10, QFont.Bold))
        lbl_titulo.setStyleSheet(f"color: {color_borde}; letter-spacing: 1px; border: none; background: transparent;")
        self.layout_grid.addWidget(lbl_titulo, 0, 0, 1, 2)


class VistaFormulario(QWidget):
    """PANTALLA 2: Formulario de Configuración de Parámetros del Modelo Matemático."""
    def __init__(self, callback_iniciar=None):
        super().__init__()
        self.callback_iniciar = callback_iniciar
        
        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(20, 20, 20, 20)
        layout_principal.setSpacing(18)
        
        lbl_titulo_pantalla = QLabel("CONFIGURACIÓN DE PARÁMETROS INICIALES DE SIMULACIÓN")
        lbl_titulo_pantalla.setFont(QFont("Segoe UI", 14, QFont.Bold))
        lbl_titulo_pantalla.setStyleSheet("color: #ff9500; letter-spacing: 1px;")
        layout_principal.addWidget(lbl_titulo_pantalla)
        
        style_spinners = """
            QSpinBox, QDoubleSpinBox {
                background-color: #0b0e11;
                color: #00f0ff;
                border: 3px solid #1a232c;
                border-radius: 6px;
                padding: 6px;
                min-width: 120px;
                font-weight: bold;
            }
            QSpinBox:focus, QDoubleSpinBox:focus {
                border: 1px solid #00f0ff;
            }
        """
        
        # --- TARJETA 1: VARIABLES POBLACIÓN HUMANA ---
        tarjeta_humanos = TarjetaFormulario("Variables Población Humana", color_borde="#0066ff")
        
        lbl_pob_h = QLabel("Población Humana Total de la Zona (Establecida):")
        lbl_pob_h_val = QLabel("10,450 hab.")
        lbl_pob_h_val.setStyleSheet("color: #ffffff; font-weight: bold; font-size: 12px; background: transparent;")
        
        lbl_inf_h = QLabel("Cantidad Inicial de Personas Infectadas:")
        self.spn_inf_h = QSpinBox()
        self.spn_inf_h.setRange(0, 5000)
        self.spn_inf_h.setValue(10)
        self.spn_inf_h.setStyleSheet(style_spinners)
        
        tarjeta_humanos.layout_grid.addWidget(lbl_pob_h, 1, 0)
        tarjeta_humanos.layout_grid.addWidget(lbl_pob_h_val, 1, 1, Qt.AlignLeft)
        tarjeta_humanos.layout_grid.addWidget(lbl_inf_h, 2, 0)
        tarjeta_humanos.layout_grid.addWidget(self.spn_inf_h, 2, 1)
        layout_principal.addWidget(tarjeta_humanos)
        
        # --- TARJETA 2: VARIABLES POBLACIÓN VECTORIAL ---
        tarjeta_vectores = TarjetaFormulario("Variables Población Vectorial (Mosquitos)", color_borde="#ff3b30")
        
        lbl_pob_v = QLabel("Cantidad Total de Mosquitos Estimados:")
        self.spn_pob_v = QSpinBox()
        self.spn_pob_v.setRange(10, 100000)
        self.spn_pob_v.setValue(2500)
        self.spn_pob_v.setStyleSheet(style_spinners)
        
        lbl_inf_v = QLabel("Cantidad Inicial de Mosquitos Infectados:")
        self.spn_inf_v = QSpinBox()
        self.spn_inf_v.setRange(0, 10000)
        self.spn_inf_v.setValue(50)
        self.spn_inf_v.setStyleSheet(style_spinners)
        
        
        tarjeta_vectores.layout_grid.addWidget(lbl_pob_v, 1, 0)
        tarjeta_vectores.layout_grid.addWidget(self.spn_pob_v, 1, 1)
        tarjeta_vectores.layout_grid.addWidget(lbl_inf_v, 2, 0)
        tarjeta_vectores.layout_grid.addWidget(self.spn_inf_v, 2, 1)
        layout_principal.addWidget(tarjeta_vectores)
        
        # --- TARJETA 3: TASAS CLÍNICAS Y BIOLÓGICAS ---
        tarjeta_tasas = TarjetaFormulario("Tasas Clínicas y Biológicas", color_borde="#34c759")
        
        lbl_tasa_rec = QLabel("Tasa de Recuperación Humana Diaria (Rango 0.01 - 0.50):")
        self.spn_tasa_rec = QDoubleSpinBox()
        self.spn_tasa_rec.setRange(0.01, 0.50)
        self.spn_tasa_rec.setSingleStep(0.01)
        self.spn_tasa_rec.setValue(0.14)
        self.spn_tasa_rec.setDecimals(2)
        self.spn_tasa_rec.setStyleSheet(style_spinners)
    
        lbl_tasa_trans = QLabel("Tasa de transmisión Humana Diaria (Rango 0.20 - 0.40):")
        self.spn_tasa_trans = QDoubleSpinBox()
        self.spn_tasa_trans.setRange(0.20, 0.4000)
        self.spn_tasa_trans.setSingleStep(0.2000)
        self.spn_tasa_trans.setValue(0.20)
        self.spn_tasa_trans.setDecimals(2)
        self.spn_tasa_trans.setStyleSheet(style_spinners)
        
        lbl_tasa_mor = QLabel("Tasa de Mortalidad Humana por Dengue (Rango 0.10 - 0.20):")
        self.spn_tasa_mor = QDoubleSpinBox()
        self.spn_tasa_mor.setRange(0.10, 0.2000)
        self.spn_tasa_mor.setSingleStep(0.0005)
        self.spn_tasa_mor.setValue(0.0002)
        self.spn_tasa_mor.setDecimals(2)
        self.spn_tasa_mor.setStyleSheet(style_spinners)
        
        lbl_tasa_trans_v = QLabel("Tasa de Transmisión del Vector (Rango 0.01 - 0.15):")
        self.spn_tasa_trans_v = QDoubleSpinBox()
        self.spn_tasa_trans_v.setSingleStep(0.0005)
        self.spn_tasa_trans_v.setRange(0.01, 0.1500)
        self.spn_tasa_trans_v.setValue(0.0001)
        self.spn_tasa_trans_v.setDecimals(2)
        self.spn_tasa_trans_v.setStyleSheet(style_spinners)
        
        tarjeta_tasas.layout_grid.addWidget(lbl_tasa_rec, 1, 0)
        tarjeta_tasas.layout_grid.addWidget(self.spn_tasa_rec, 1, 1)
        tarjeta_tasas.layout_grid.addWidget(lbl_tasa_trans, 2, 0)
        tarjeta_tasas.layout_grid.addWidget(self.spn_tasa_trans, 2, 1)
        tarjeta_tasas.layout_grid.addWidget(lbl_tasa_mor, 3, 0)
        tarjeta_tasas.layout_grid.addWidget(self.spn_tasa_mor, 3, 1)
        tarjeta_tasas.layout_grid.addWidget(lbl_tasa_trans_v, 4, 0)
        tarjeta_tasas.layout_grid.addWidget(self.spn_tasa_trans_v, 4, 1)
        layout_principal.addWidget(tarjeta_tasas)
        
        layout_principal.addStretch()
        
        # --- BOTÓN DE COMPILACIÓN E INICIO ---
        self.btn_compilar = QPushButton("COMPILAR E INICIAR SIMULACIÓN ACTIVADA")
        self.btn_compilar.setFont(QFont("Segoe UI", 10, QFont.Bold))
        self.btn_compilar.setCursor(Qt.PointingHandCursor)
        self.btn_compilar.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #ff9500;
                border: 2px solid #ff9500;
                border-radius: 6px;
                padding: 12px;
                letter-spacing: 1px;
            }
            QPushButton:hover {
                background-color: #ff9500;
                color: #0b0e11;
            }
            QPushButton:pressed {
                background-color: #cc7700;
            }
        """)
        
        
        self.btn_compilar.clicked.connect(self.recopilar_y_transmitir_valores)
        layout_principal.addWidget(self.btn_compilar)

    def recopilar_y_transmitir_valores(self):
        """Toma exclusivamente los datos que el usuario ha ingresado en la interfaz

        y los envía empaquetados hacia el dashboard principal mediante el callback.
        """
        datos_humanos = {
            "poblacion_inicial": 10450,
            "infectados_inicial": self.spn_inf_h.value(),
            "tasa_recuperacion": self.spn_tasa_rec.value(),
            "tasa_muerte_h": self.spn_tasa_mor.value(),
            "tasa_picaduras": 0.3,
            "tasa_transmision": self.spn_tasa_trans.value(),
            "tasa_incubacion": 0.2
        }
        
        datos_vectores = {
            "poblacion_inicial": self.spn_pob_v.value(),
            "infectados_inicial": self.spn_inf_v.value(),
            "tasa_picaduras": 0.3,
            "tasa_transmision": self.spn_tasa_trans_v.value(),
            "tasa_incubacion": 0.2,
            "tasa_nacimiento_v": 0.08,
            "tasa_muerte_v": 0.10
        }
        
        # Si el Dashboard nos configuró un puente, le enviamos los datos inmediatamente
        if self.callback_iniciar:
            self.callback_iniciar(datos_humanos, datos_vectores)