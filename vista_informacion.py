from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class TarjetaInformativa(QFrame):
    """Componente personalizado para crear contenedores estilizados (Tarjetas)."""
    def __init__(self, titulo, contenido, color_borde="#1a232c"):
        super().__init__()
        self.setStyleSheet(f"""
            QFrame {{
                background-color: #111519;
                border: 1px solid {color_borde};
                border-radius: 8px;
            }}
        """)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(8)
        
        lbl_titulo = QLabel(titulo.upper())
        lbl_titulo.setFont(QFont("Segoe UI", 10, QFont.Bold))
        lbl_titulo.setStyleSheet(f"color: {color_borde}; letter-spacing: 1px; border: none; background: transparent;")
        
        lbl_contenido = QLabel(contenido)
        lbl_contenido.setFont(QFont("Segoe UI", 10))
        lbl_contenido.setStyleSheet("color: #cbd5e1; border: none; background: transparent;")
        lbl_contenido.setWordWrap(True)
        
        layout.addWidget(lbl_titulo)
        layout.addWidget(lbl_contenido)


class VistaInformacion(QWidget):
    """PANTALLA 1: Reporte Geográfico e Histórico de la Zona de Estudio."""
    def __init__(self):
        super().__init__()
        
        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(20, 20, 20, 20)
        layout_principal.setSpacing(15)
        
        lbl_comunidad = QLabel("ZONA DE ESTUDIO: COMUNIDAD ANTIGUO AEROPUERTO")
        lbl_comunidad.setFont(QFont("Segoe UI", 16, QFont.Bold))
        lbl_comunidad.setStyleSheet("color: #00f0ff; letter-spacing: 1px;")
        layout_principal.addWidget(lbl_comunidad)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")
        
        contenedor_scroll = QWidget()
        contenedor_scroll.setStyleSheet("background-color: transparent;")
        layout_scroll = QVBoxLayout(contenedor_scroll)
        layout_scroll.setContentsMargins(0, 0, 5, 0)
        layout_scroll.setSpacing(15)
        
        # --- 1. TARJETA: ORIGEN HISTÓRICO ---
        txt_origen = (
            "Se dice que en este espacio, conocido tradicionalmente como 'campo espinoso' "
            "frente a Caja de Agua, funcionó un campo de aviación construido por iniciativa "
            "de Luis Roncalojo a mediados de los años 40."
        )
        tarjeta_origen = TarjetaInformativa("Origen del Nombre", txt_origen, color_borde="#a0aab5")
        layout_scroll.addWidget(tarjeta_origen)
        
        # --- 2. TARJETA: UBICACIÓN Y DEMOGRAFÍA ---
        txt_ubicacion = (
            "La urbanización 'Cerro Atravesado', mejor conocida como Antiguo Aeropuerto, "
            "se encuentra ubicada en la Parroquia Norte, Municipio Carirubana, Estado Falcón.\n\n"
            "» Censo Demográfico Actual: ~10.450 habitantes.\n"
            "» Distribución Territorial: Dividido en al menos 6 sub-sectores principales."
        )
        tarjeta_ubicacion = TarjetaInformativa("Ubicación y Datos Generales", txt_ubicacion, color_borde="#0066ff")
        layout_scroll.addWidget(tarjeta_ubicacion)
        
        # --- 3. TARJETA: LÍMITES GEOGRÁFICOS ---
        txt_limites = (
            "• Norte: Sector Ezequiel Zamora y La Chinita Arriba.\n"
            "• Sur: Sector Caja de Agua y la Urb. Ramón Luis Polanco.\n"
            "• Este: Parcelamiento Antiguo Aeropuerto y El Milagro.\n"
            "• Oeste: Santa Rosalía 1 y 3."
        )
        tarjeta_limites = TarjetaInformativa("Límites Geográficos", txt_limites, color_borde="#34c759")
        layout_scroll.addWidget(tarjeta_limites)
        
        # --- 4. TARJETA: FÍSICAS Y AMBIENTALES ---
        txt_ambiente = (
            "• Clima: Seco, característico de gran parte de la península, con pocas precipitaciones, "
            "días soleados y algunos nublados.\n\n"
            "• Vegetación: Predomina la vegetación xerófila propia como los cujíes; sin embargo, en áreas planificadas "
            "como la avenida principal, se han adaptado árboles y arbustos que no son nativos.\n\n"
            "• Fauna: Asociada al bioma desértico inferior, es escasa y se limita a pequeños animales "
            "como lagartijas, palomas, ciempiés, saltamontes, cucarachas, moscas, zancudos y mariposas."
        )
        tarjeta_ambiente = TarjetaInformativa("Características Físicas y Ambientales", txt_ambiente, color_borde="#ff9500")
        layout_scroll.addWidget(tarjeta_ambiente)
        
        # --- 5. TARJETA: ALERTA SANITARIA (VECTOR) ---
        txt_salud = (
            "Dueño de las condiciones climáticas y de almacenamiento de agua locales, el mosquito "
            "Aedes aegypti encuentra facilidades para establecer criaderos urbanos. Este vector es el "
            "principal transmisor de enfermedades infectocontagiosas como el Dengue, Zika y Chikungunya.\n\n"
            "Recomendación del sistema epidemiológico: Evitar el almacenamiento de agua estancada en "
            "recipientes abiertos, sellar herméticamente tanques/pipas y eliminar recipientes en desuso."
        )
        tarjeta_salud = TarjetaInformativa("Nota sobre Salud Pública: El Mosquito Aedes aegypti", txt_salud, color_borde="#ff3b30")
        layout_scroll.addWidget(tarjeta_salud)
        
        scroll.setWidget(contenedor_scroll)
        layout_principal.addWidget(scroll)