import sys
import os
import folium
import json
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMessageBox
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtCore import QUrl


# 1. SOLUCIÓN DE RENDERIZADO: Desactiva GPU e ignora errores de certificados SSL
os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-gpu --ignore-certificate-errors"

def generar_mapa_offline_2():
    with open('GeoJson/clipping_boundary.geojson', 'r', encoding='utf-8') as f:
        datos_geojson = json.load(f)

    lat, lon = 11.70466667, -70.19933333
    mapa = folium.Map(
        location=[lat, lon],
        zoom_start=14
    )

    folium.GeoJson(
        datos_geojson,
        name='puntofijo',
        style_function=lambda x:{
            'fillColor': '#228b22',  # Color de relleno
            'color': 'black',  # Color del borde
            'weight': 1,  # Grosor del borde
            'fillOpacity': 0.5  # Transparencia
        }
    ).add_to(mapa)
    ruta_temp = os.path.join(os.getcwd(), "mapa_punto_fijo88.html")
    mapa.save(ruta_temp)
    return ruta_temp

def generar_mapa_offline():
    lat, lon = 11.70466667, -70.19933333
    mapa = folium.Map(
        location=[lat, lon],
        zoom_start=14
    )
    folium.GeoJson("clipping_boundary.geojson", name="Punto Fijo").add_to(mapa)
    ruta_temp = os.path.join(os.getcwd(), "puntoFijo1.html")
    mapa.save(ruta_temp)
    return ruta_temp

def generar_mapa_seguro():
    """Crea el mapa y devuelve la ruta absoluta del archivo."""
    try:
        # Coordenadas de prueba (Ciudad de México)
        lat, lon = 11.70466667, -70.19933333
        mapa = folium.Map(
            location=[lat, lon],
            zoom_start=14,
            tiles="OpenStreetMap"  # Usamos el estándar
        )

        folium.Marker(
            [lat, lon],
            popup="<b>Zócalo CDMX</b>",
            tooltip="Click para ver"
        ).add_to(mapa)

        # Guardar con ruta absoluta clara
        ruta_temp = os.path.join(os.getcwd(), "mapa_interactivo.html")
        mapa.save(ruta_temp)
        return ruta_temp
    except Exception as e:
        print(f"Error al generar Folium: {e}")
        return None

class VisorMapa(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visor de Mapas Folium + QtWebEngine")
        self.resize(900, 700)

        # Layout principal
        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 50, 50, 50)  # Mapa a pantalla completa

        # Crear el navegador
        self.browser = QWebEngineView()
        self.browser.setMaximumSize(600, 700)

        # 2. CONFIGURACIÓN DE SEGURIDAD: Permitir acceso a contenido remoto (JS de Leaflet)
        settings = self.browser.settings()
        settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        settings.setAttribute(QWebEngineSettings.ErrorPageEnabled, True)
        settings.setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)

        # 3. CARGA DEL ARCHIVO
        ruta = generar_mapa_offline_2()

        if ruta and os.path.exists(ruta):
            print(f"Cargando mapa desde: {ruta}")
            # Importante: Usar QUrl.fromLocalFile para que Chromium entienda la ruta
            self.browser.load(QUrl.fromLocalFile(ruta))
        else:
            QMessageBox.critical(self, "Error", "No se pudo crear o encontrar el archivo HTML del mapa.")

        # Conectar evento de carga para saber si falló algo
        self.browser.loadFinished.connect(self.verificar_carga)

        layout.addWidget(self.browser)

    def verificar_carga(self, success):
        if success:
            print("¡Mapa renderizado con éxito!")
        else:
            print("Error: El motor web no pudo renderizar el HTML.")
            QMessageBox.warning(self, "Error de Renderizado",
                                "El archivo cargó pero no se puede mostrar. Revisa tu conexión a internet.")


if __name__ == "__main__":
    # La aplicación debe crearse después de configurar las variables de entorno de arriba
    app = QApplication(sys.argv)

    ventana = VisorMapa()
    ventana.show()

    sys.exit(app.exec())
