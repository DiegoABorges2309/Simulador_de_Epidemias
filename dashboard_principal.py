import sys
import os

# --- CONFIGURACIÓN DE RUTAS AUTOMÁTICAS ---
ruta_raiz = os.path.dirname(os.path.abspath(__file__))
ruta_motor = os.path.join(ruta_raiz, "motor_de_simulacion")
if ruta_raiz not in sys.path:
    sys.path.insert(0, ruta_raiz)
if ruta_motor not in sys.path:
    sys.path.insert(0, ruta_motor)

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QStackedWidget,
    QLabel,
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QFont

# Importación de los componentes modulares de las pantallas
from vista_informacion import VistaInformacion
from vista_formulario import VistaFormulario
from vista_graficas import VistaGraficas
from servidor_local.servidor_local import iniciar_servidor, cerrar_servidor


class DashboardPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulador Dengue Engine - Tablero Maestro")
        self.setGeometry(40, 40, 1420, 860)

        # Paleta de color ultra oscuro de fondo de pantalla para resaltar el contenedor central
        self.setStyleSheet("QMainWindow { background-color: #0b0e11; }")

        # Layout horizontal global (Barra lateral izquierda y contenedor dinámico derecho)
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        self.layout_global = QHBoxLayout(widget_central)
        self.layout_global.setContentsMargins(12, 12, 12, 12)
        self.layout_global.setSpacing(15)

        # Repositorios globales de datos (Inician completamente limpios)
        self.lista_dias = []
        self.datos_h = {}
        self.datos_v = {}

        # Inicializar los dos componentes maestros de la interfaz
        self.construir_sidebar_lateral()
        self.construir_contenedor_central()

    def construir_sidebar_lateral(self):
        """Genera la barra de navegación lateral izquierda optimizada para tus iconos reales."""
        self.sidebar = QWidget()
        self.sidebar.setStyleSheet("""
            QWidget {
                background-color: #e2e8f0; 
                border-radius: 12px;
            }
            QPushButton {
                background-color: transparent;
                border: 2px solid transparent;
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #cbd5e1;
                border: 2px solid #00f0ff;
            }
            QPushButton:checked {
                background-color: #ffffff;
                border: 2px solid #00f0ff;
            }
        """)
        layout_sidebar = QVBoxLayout(self.sidebar)
        layout_sidebar.setContentsMargins(8, 30, 8, 30)
        layout_sidebar.setSpacing(25)

        # Espaciador decorativo superior
        self.lbl_logo = QLabel()
        self.lbl_logo.setStyleSheet("background: transparent;")
        layout_sidebar.addWidget(self.lbl_logo)

        # --- OBTENER RUTA BASE DEL PROYECTO PARA EVITAR ERRORES DE CARGA ---
        dir_actual = os.path.dirname(os.path.abspath(__file__))

        # Definición exacta de las rutas según tus archivos reales (.png y .jpg)
        ruta_documento = os.path.join(dir_actual, "iconos", "documento.png")
        ruta_mosquito = os.path.join(
            dir_actual, "iconos", "mosquito1.png"
        )  # <-- Corregido a .jpg
        ruta_play = os.path.join(
            dir_actual, "iconos", "play.png"
        )  # <-- Corregido a .jpg

        # --- BOTONES DE CONTROL CON TUS ICONOS REALES ---
        self.btn_info = QPushButton()
        self.btn_info.setIcon(QIcon(ruta_documento))
        self.btn_info.setIconSize(QSize(35, 35))
        self.btn_info.setCheckable(True)

        self.btn_datos = QPushButton()
        self.btn_datos.setIcon(QIcon(ruta_mosquito))
        self.btn_datos.setIconSize(QSize(35, 35))
        self.btn_datos.setCheckable(True)

        self.btn_play = QPushButton()
        self.btn_play.setIcon(QIcon(ruta_play))
        self.btn_play.setIconSize(QSize(35, 35))
        self.btn_play.setCheckable(True)

        self.grupo_botones = [self.btn_info, self.btn_datos, self.btn_play]

        layout_sidebar.addWidget(self.btn_info)
        layout_sidebar.addWidget(self.btn_datos)
        layout_sidebar.addWidget(self.btn_play)
        layout_sidebar.addStretch()

        # Enlaces de eventos clic para alternar las pantallas
        self.btn_info.clicked.connect(lambda: self.cambiar_pantalla(0, self.btn_info))
        self.btn_datos.clicked.connect(lambda: self.cambiar_pantalla(1, self.btn_datos))
        self.btn_play.clicked.connect(lambda: self.cambiar_pantalla(2, self.btn_play))

        self.layout_global.addWidget(self.sidebar, stretch=6)

    def construir_contenedor_central(self):
        """Configura el apilador de pantallas dinámico."""
        self.pantallas_sistema = QStackedWidget()
        self.pantallas_sistema.setStyleSheet("""
            QStackedWidget {
                background-color: #0e1216;
                border: 1px solid #1a232c;
                border-radius: 12px;
            }
        """)

        self.vista_info = VistaInformacion()
        # Cambia esta línea para que apunte a ejecutar_procesamiento_matematico
        self.vista_form = VistaFormulario(
            callback_iniciar=self.ejecutar_procesamiento_matematico
        )
        self.vista_graficas = VistaGraficas()

        # Acoplar las pantallas al mazo indexado del QStackedWidget
        self.pantallas_sistema.addWidget(self.vista_info)  # Índice 0
        self.pantallas_sistema.addWidget(self.vista_form)  # Índice 1
        self.pantallas_sistema.addWidget(self.vista_graficas)  # Índice 2

        # --- MENSAJE LIMPIO DE BIENVENIDA INICIAL ---
        # Removido cualquier cálculo previo. Arranca con una presentación minimalista
        self.pantalla_bienvenida = QWidget()
        layout_bienvenida = QVBoxLayout(self.pantalla_bienvenida)

        lbl_saludo = QLabel("¡Bienvenido!\n¿Listo para iniciar tu próxima simulación?")
        lbl_saludo.setAlignment(Qt.AlignCenter)
        lbl_saludo.setFont(QFont("Segoe UI", 18, QFont.Bold))
        lbl_saludo.setStyleSheet(
            "color: #00f0ff; line-height: 40px; letter-spacing: 1px;"
        )

        lbl_instruccion = QLabel(
            "Selecciona un icono en el panel lateral izquierdo para comenzar."
        )
        lbl_instruccion.setAlignment(Qt.AlignCenter)
        lbl_instruccion.setFont(QFont("Segoe UI", 11))
        lbl_instruccion.setStyleSheet("color: #687582;")

        layout_bienvenida.addStretch()
        layout_bienvenida.addWidget(lbl_saludo)
        layout_bienvenida.addSpacing(10)
        layout_bienvenida.addWidget(lbl_instruccion)
        layout_bienvenida.addStretch()

        # Añadir la pantalla neutra como índice 3 y fijarla por defecto
        self.pantallas_sistema.addWidget(self.pantalla_bienvenida)  # Índice 3

        # Inicializar el software mostrando el mensaje limpio sin iluminar ningún botón lateral aún
        self.pantallas_sistema.setCurrentIndex(3)
        for btn in self.grupo_botones:
            btn.setChecked(False)

        self.layout_global.addWidget(self.pantallas_sistema, stretch=94)

    def cambiar_pantalla(self, indice, boton_presionado):
        """Intercambia la vista en pantalla y resalta la selección del usuario."""
        self.pantallas_sistema.setCurrentIndex(indice)
        for btn in self.grupo_botones:
            btn.setChecked(False)
        boton_presionado.setChecked(True)

    def ejecutar_procesamiento_matematico(self, config_humanos, config_vectores):
        """Recibe los diccionarios del formulario, activa el procesador matemático
        en la vista de gráficas y redirige la pantalla al Monitor Central.
        """
        # 1. Pasar los datos calculados a la pestaña de gráficos
        self.vista_graficas.recibir_y_procesar_simulacion(
            config_humanos, config_vectores
        )

        # 2. Forzar el cambio automático de pestaña hacia la Vista de Gráficas (Índice 2)
        # Pasamos el botón de reproducir (btn_play) para que visualmente se resalte la selección
        self.cambiar_pantalla(2, self.btn_play)

    def evento_sincronizacion_lineal(self, dia_seleccionado, indice):
        """Controlador de movimiento de cursor interactivo para Matplotlib."""
        pass


if __name__ == "__main__":
    iniciar_servidor()  # Iniciar el servidor local para servir los archivos necesarios
    app = QApplication(sys.argv)
    dashboard = DashboardPrincipal()
    dashboard.show()
    sys.exit(app.exec_())
