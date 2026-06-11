import os
import sys
import numpy as np
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# --- IMPORTACIÓN DIRECTA DEL MOTOR MATEMÁTICO ---
# La lógica matemática se ejecuta aquí adentro, liberando por completo al dashboard.
from motor_de_simulacion.motor_simulacion import Motor
from motor_de_simulacion.seir_sei.seir import DatosSimulacionHumanos
from motor_de_simulacion.seir_sei.sei import DatosSimulacionVector
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

# =====================================================================
# 1. COMPONENTES DE LIENZOS MATPLOTLIB (CYBERPUNK DINÁMICOS)
# =====================================================================


class MapaCanvas(QWebEngineView):
    """Lienzo para la visualización del mapa de la simulación."""

    def __init__(self):
        super().__init__()
        self.setUrl(QUrl("http://localhost:4000"))


class MiniGraficaCanvas(FigureCanvas):
    """Lienzo individual de alta eficiencia para las 7 minigráficas de los lados."""

    def __init__(self, titulo, color_linea, color_relleno):
        self.figura = Figure(figsize=(2.5, 2.0), facecolor="#111519")
        self.ax = self.figura.add_subplot(111, facecolor="#111519")
        super().__init__(self.figura)

        self.titulo = titulo
        self.color_linea = color_linea
        self.color_relleno = color_relleno
        self.figura.subplots_adjust(left=0.22, right=0.92, top=0.82, bottom=0.25)

    def redibujar_curva(self, x, y, indice_activo, dia_activo):
        """Limpia el estado anterior y grafica la curva exacta calculada con los datos del usuario."""
        self.ax.clear()
        self.ax.grid(True, color="#222b35", alpha=0.6, linestyle="--")
        self.ax.plot(x, y, color=self.color_linea, linewidth=1.8)
        self.ax.fill_between(x, y, color=self.color_relleno, alpha=0.18)

        valor_actual = int(y[indice_activo])
        self.ax.set_title(
            f"{self.titulo} | Val: {valor_actual:,}",
            color="#00f0ff",
            fontsize=8,
            family="monospace",
            loc="left",
            pad=4,
        )

        self.ax.set_xlabel(
            "Días", color="#687582", fontsize=7, family="monospace", labelpad=1
        )
        self.ax.set_ylabel(
            "Cant.", color="#687582", fontsize=7, family="monospace", labelpad=1
        )
        self.ax.tick_params(colors="#687582", labelsize=7)

        for spine in self.ax.spines.values():
            spine.set_color("#222b35")

        # Cursor temporal vertical síncrono
        self.ax.axvline(
            x=dia_activo, color="#00f0ff", linestyle="--", linewidth=1.2, zorder=5
        )
        self.draw_idle()


class GraficaCentralCanvas(FigureCanvas):
    """Lienzo del Monitor Maestro de Línea de Tiempo Interactivo Central."""

    def __init__(self, callback_mouse):
        self.figura = Figure(figsize=(5.0, 2.5), facecolor="#161a1e")
        self.ax = self.figura.add_subplot(111, facecolor="#161a1e")
        super().__init__(self.figura)

        self.callback_mouse = callback_mouse
        self.figura.subplots_adjust(left=0.15, right=0.95, top=0.85, bottom=0.20)
        self.dias = []

        # Escucha física de eventos del mouse sobre el lienzo de dibujo
        self.mpl_connect("motion_notify_event", self.detectar_arrastre)
        self.mpl_connect("button_press_event", self.detectar_arrastre)

    def graficar_tendencia_maestra(self, dias, infectados_humanos):
        """Construye la gráfica principal de infectados humanos generados por el usuario."""
        self.dias = dias
        self.ax.clear()
        self.ax.grid(True, color="#2e3842", alpha=0.5, linestyle="--")

        self.ax.plot(dias, infectados_humanos, color="#39ff14", linewidth=2.2)
        self.ax.fill_between(dias, infectados_humanos, color="#39ff14", alpha=0.12)

        self.ax.set_title(
            "CONTROL MAESTRO TEMPORAL (DESLIZA EL MOUSE SOBRE EL GRÁFICO)",
            color="#00f0ff",
            fontsize=9,
            fontweight="bold",
            pad=8,
        )
        self.ax.set_xlabel(
            "Eje de Tiempo Simulado (Días)",
            color="#a0aab5",
            fontsize=8,
            family="monospace",
        )
        self.ax.set_ylabel(
            "Infectados Humanos", color="#a0aab5", fontsize=8, family="monospace"
        )

        for label in self.ax.get_xticklabels() + self.ax.get_yticklabels():
            label.set_family("monospace")

        self.linea_guia = self.ax.axvline(
            x=dias[0], color="#00f0ff", linewidth=2, alpha=0.8
        )
        self.draw()

    def mover_linea_guia(self, dia):
        """Desplaza la barra vertical neón siguiendo la coordenada x del cursor."""
        if hasattr(self, "linea_guia"):
            self.linea_guia.set_xdata([dia, dia])
            self.draw_idle()

    def detectar_arrastre(self, event):
        """Calcula el índice exacto del día en base a la posición del mouse del usuario."""
        if not event.inaxes or len(self.dias) == 0:
            return
        if event.button == 1 or event.name == "motion_notify_event":
            x_mouse = event.xdata
            indice = (np.abs(np.array(self.dias) - x_mouse)).argmin()
            dia_seleccionado = self.dias[indice]
            # Dispara la actualización interna de todos los contadores de la pantalla
            self.callback_mouse(dia_seleccionado, indice)


# =====================================================================
# 2. PANEL CONTENEDOR VISUAL TRICOLOR (VISTA PRINCIPAL)
# =====================================================================


class VistaGraficas(QWidget):
    """PANTALLA 3: Renderizador y procesador interactivo de curvas simuladas."""

    def __init__(self):
        super().__init__()
        layout_pantalla = QHBoxLayout(self)
        layout_pantalla.setContentsMargins(10, 10, 10, 10)
        layout_pantalla.setSpacing(12)

        # Repositorios locales en memoria (Inician vacíos de fábrica)
        self.dias_x = []
        self.datos_h = {}
        self.datos_v = {}

        # --- SUB-COLUMNA IZQUIERDA: HUMANOS (SEIR) ---
        self.col_izquierda = QVBoxLayout()
        self.col_izquierda.setSpacing(8)
        self.mini_graficas_h = {
            "S": MiniGraficaCanvas("HUMANOS SUSCEPTIBLES (Sh)", "#0066ff", "#0066ff"),
            "E": MiniGraficaCanvas("HUMANOS EXPUESTOS (Eh)", "#ff9500", "#ff9500"),
            "I": MiniGraficaCanvas("HUMANOS INFECTADOS (Ih)", "#ff3b30", "#ff3b30"),
            "R": MiniGraficaCanvas("HUMANOS RECUPERADOS (Rh)", "#34c759", "#34c759"),
            "M": MiniGraficaCanvas("HUMANOS MUERTOS (Mh)", "#a2a2a7", "#a2a2a7"),
        }
        lbl_tit_h = QLabel("SISTEMA HUMANO (SEIR)")
        lbl_tit_h.setStyleSheet("color: #00f0ff; font-weight: bold; font-size: 11px;")
        self.col_izquierda.addWidget(lbl_tit_h)
        for canvas in self.mini_graficas_h.values():
            tarjeta = QWidget()
            tarjeta.setStyleSheet(
                "background-color: #111519; border: 1px solid #1a232c; border-radius: 6px;"
            )
            ly = QVBoxLayout(tarjeta)
            ly.setContentsMargins(2, 2, 2, 2)
            ly.addWidget(canvas)
            self.col_izquierda.addWidget(tarjeta)

        # --- SUB-COLUMNA CENTRAL: CONTROL TEMPORAL Y MONITORES ---
        self.col_central = QVBoxLayout()
        self.col_central.setSpacing(10)

        # Marcador Digital de Días
        self.tarjeta_contador = QWidget()
        self.tarjeta_contador.setStyleSheet(
            "background-color: #111519; border: 1px solid #00f0ff; border-radius: 6px;"
        )
        ly_cont = QVBoxLayout(self.tarjeta_contador)
        lbl_c_tit = QLabel("DÍAS TRANSCURRIDOS")
        lbl_c_tit.setAlignment(Qt.AlignCenter)
        lbl_c_tit.setStyleSheet(
            "color: #687582; font-size: 10px; font-weight: bold; letter-spacing: 1px;"
        )
        self.lbl_dias_num = QLabel("0")
        self.lbl_dias_num.setAlignment(Qt.AlignCenter)
        self.lbl_dias_num.setStyleSheet(
            "color: #00f0ff; font-family: 'Consolas'; font-size: 32px; font-weight: bold;"
        )
        ly_cont.addWidget(lbl_c_tit)
        ly_cont.addWidget(self.lbl_dias_num)
        self.col_central.addWidget(self.tarjeta_contador)

        # Panel de Lecturas Numéricas Digitales Instantáneas
        self.tarjeta_info = QWidget()
        self.tarjeta_info.setStyleSheet(
            "background-color: #111519; border: 1px solid #1a232c; border-radius: 6px;"
        )
        grid_info = QGridLayout(self.tarjeta_info)
        self.lbl_pob_h = QLabel("Carga inicial pendiente...")
        self.lbl_est_h = QLabel("")
        self.lbl_cen_v = QLabel("")
        self.lbl_status = QLabel("")
        for lbl in [self.lbl_pob_h, self.lbl_est_h, self.lbl_cen_v]:
            lbl.setStyleSheet(
                "font-family: 'Consolas'; color: #cbd5e1; font-size: 11px; line-height: 16px;"
            )
        grid_info.addWidget(self.lbl_pob_h, 0, 0)
        grid_info.addWidget(self.lbl_est_h, 0, 1)
        grid_info.addWidget(self.lbl_cen_v, 1, 0)
        grid_info.addWidget(self.lbl_status, 1, 1)
        self.col_central.addWidget(self.tarjeta_info)

        # Canvas Maestro Central
        self.canvas_central = GraficaCentralCanvas(
            callback_mouse=self.sincronizar_movimiento_interfaces
        )
        tarjeta_canvas = QWidget()
        tarjeta_canvas.setStyleSheet(
            "background-color: #161a1e; border: 1px solid #1a232c; border-radius: 6px;"
        )
        ly_can = QVBoxLayout(tarjeta_canvas)
        ly_can.setContentsMargins(4, 4, 4, 4)
        ly_can.addWidget(self.canvas_central)
        self.col_central.addWidget(tarjeta_canvas)

        self.col_derecha = QVBoxLayout()
        self.col_derecha.setSpacing(8)
        self.mini_graficas_v = {
            "S": MiniGraficaCanvas("MOSQUITOS SUSCEPTIBLES (Sv)", "#00e5ff", "#00e5ff"),
            "E": MiniGraficaCanvas("MOSQUITOS EXPUESTOS (Ev)", "#d055ff", "#d055ff"),
            "I": MiniGraficaCanvas("MOSQUITOS INFECTADOS (Iv)", "#ff2244", "#ff2244"),
            "M": MapaCanvas(),
        }
        lbl_tit_v = QLabel("SISTEMA VECTORIAL (SEI)")
        lbl_tit_v.setStyleSheet("color: #00f0ff; font-weight: bold; font-size: 11px;")
        self.col_derecha.addWidget(lbl_tit_v)
        for canvas in self.mini_graficas_v.values():
            tarjeta = QWidget()
            tarjeta.setStyleSheet(
                "background-color: #111519; border: 1px solid #1a232c; border-radius: 6px;"
            )
            ly = QVBoxLayout(tarjeta)
            ly.setContentsMargins(2, 2, 2, 2)
            ly.addWidget(canvas)
            self.col_derecha.addWidget(tarjeta)
        self.col_derecha.addStretch()

        layout_pantalla.addLayout(self.col_izquierda, stretch=26)
        layout_pantalla.addLayout(self.col_central, stretch=48)
        layout_pantalla.addLayout(self.col_derecha, stretch=26)

    def recibir_y_procesar_simulacion(self, config_humanos, config_vectores):
        """PROCESADOR CIENTÍFICO: Toma las entradas puras del usuario de forma directa,

        alimenta las ecuaciones matemáticas y compila el resultado final.
        """
        # 1. Instanciar los modelos de datos clínicos usando los inputs exactos digitados
        datos_h = DatosSimulacionHumanos(
            tasa_picaduras=config_humanos["tasa_picaduras"],
            tasa_transmision=config_humanos["tasa_transmision"],
            tasa_incubacion=config_humanos["tasa_incubacion"],
            tasa_recuperacion=config_humanos["tasa_recuperacion"],
            tasa_muerte_h=config_humanos["tasa_muerte_h"],
        )

        datos_v = DatosSimulacionVector(
            tasa_picaduras=config_vectores["tasa_picaduras"],
            tasa_transmision=config_vectores["tasa_transmision"],
            tasa_incubacion=config_vectores["tasa_incubacion"],
            tasa_nacimiento_vector=config_vectores["tasa_nacimiento_v"],
            tasa_muerte_vector=config_vectores["tasa_muerte_v"],
        )

        motor = Motor(
            humanos_poblacion=config_humanos["poblacion_inicial"],
            infectados_humanos=config_humanos["infectados_inicial"],
            datos_simulacion_humanos=datos_h,
            vector_poblacion=config_vectores["poblacion_inicial"],
            infectados_vectores=config_vectores["infectados_inicial"],
            datos_simulacion_vector=datos_v,
        )
        motor.iniciar_simulacion()
        lista_de_dias = motor.lista_de_dias

        # 3. Mapear y desestructurar las matrices de curvas resultantes
        self.dias_x = [nodo["dia"] for nodo in lista_de_dias]
        self.datos_h = {
            "S": [nodo["humano"]["susceptibles"] for nodo in lista_de_dias],
            "E": [nodo["humano"]["expuestos"] for nodo in lista_de_dias],
            "I": [nodo["humano"]["infectados"] for nodo in lista_de_dias],
            "R": [nodo["humano"]["recuperados"] for nodo in lista_de_dias],
            "M": [nodo["humano"]["muertos"] for nodo in lista_de_dias],
        }
        self.datos_v = {
            "S": [nodo["vector"]["susceptibles"] for nodo in lista_de_dias],
            "E": [nodo["vector"]["expuestos"] for nodo in lista_de_dias],
            "I": [nodo["vector"]["infectados"] for nodo in lista_de_dias],
        }

        # 4. Renderizar la tendencia principal e inicializar en el día cero
        self.canvas_central.graficar_tendencia_maestra(self.dias_x, self.datos_h["I"])
        self.sincronizar_movimiento_interfaces(self.dias_x[0], 0)

    def sincronizar_movimiento_interfaces(self, dia_seleccionado, indice):
        """INTERACTIVIDAD SÍNCRONA: Mueve los cursores y actualiza las lecturas digitales."""
        if not self.datos_h:
            return

        self.lbl_dias_num.setText(f"{int(dia_seleccionado)}")

        sh, eh, ih, rh, mh = (
            self.datos_h["S"][indice],
            self.datos_h["E"][indice],
            self.datos_h["I"][indice],
            self.datos_h["R"][indice],
            self.datos_h["M"][indice],
        )
        sv, ev, iv = (
            self.datos_v["S"][indice],
            self.datos_v["E"][indice],
            self.datos_v["I"][indice],
        )

        # Actualizar textos del monitor central
        self.lbl_pob_h.setText(
            f"HUMANOS VIVOS\n» Susc: {int(sh):<5}\n» Recu: {int(rh):<5}"
        )
        self.lbl_est_h.setText(
            f"CASOS ACTIVOS\n» Infec: {int(ih):<4}\n» Muert: {int(mh):<4}"
        )
        self.lbl_cen_v.setText(
            f"POB. VECTORES\n» Susc: {int(sv):<5}\n» Infec: {int(iv):<5}"
        )

        if ih < 1 and iv < 1:
            self.lbl_status.setText("ESTADO:\n[BROTE EXTINTO]")
            self.lbl_status.setStyleSheet(
                "color: #34c759; font-weight: bold; font-size: 11px;"
            )
        else:
            self.lbl_status.setText("ESTADO:\n[BROTE CRÍTICO]")
            self.lbl_status.setStyleSheet(
                "color: #ff3b30; font-weight: bold; font-size: 11px;"
            )

        # Redibujar sincrónicamente el cursor temporal en las 7 minigráficas
        for clave, canvas in self.mini_graficas_h.items():
            canvas.redibujar_curva(
                self.dias_x, self.datos_h[clave], indice, dia_seleccionado
            )
        for clave, canvas in self.mini_graficas_v.items():
            if isinstance(canvas, MiniGraficaCanvas):
                canvas.redibujar_curva(
                    self.dias_x, self.datos_v[clave], indice, dia_seleccionado
                )

        # Mover la línea vertical guía de la gráfica principal
        self.canvas_central.mover_linea_guia(dia_seleccionado)
