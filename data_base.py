
from models_clases.virus import Virus
from models_clases.simulacion import Simulacion
import sqlite3
#we
class DataBase():
    def __init__(self, nombre_db = "Simulador.db"):
        self.conexion = sqlite3.connect(nombre_db)
        self.conexion.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.conexion.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        self.cursor.execute( """CREATE TABLE IF NOT EXISTS simulacion(
            id_simulacion INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_virus TEXT, 
            poblacion INTEGER,
            cant_contagio_inicial INTEGER,
            area_km2 REAL, 
            tipo_transmision TEXT, 
            probabilidad_contagio REAL,
            tasa_letalidad REAL,
            tiempo_recuperacion INTEGER,
            capacidad_hospitalaria INTEGER)""")
        
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS dia_simulacion(
            id_dia INTEGER PRIMARY KEY AUTOINCREMENT,
            id_simulacion INTEGER,
            numero_dia INTEGER,
            sanos INTEGER,
            infectados INTEGER,
            recuperados INTEGER,
            fallecidos INTEGER,
            pacientes_en_espera INTEGER,
            FOREIGN KEY (id_simulacion) REFERENCES simulacion(id_simulacion)ON DELETE CASCADE)""")
        
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS paciente_hospital(
            id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
            id_simulacion INTEGER,
            dia_ingreso_cola INTEGER,
            dia_atencion INTEGER,
            estado_final TEXT, 
            FOREIGN KEY (id_simulacion) REFERENCES simulacion(id_simulacion) ON DELETE CASCADE)""")
        
        self.conexion.commit()

 #_____________CRUD SIMULACION_______________________________
    def insertar_simulacion(self, virus_obj, simulacion_obj):
        query = """INSERT INTO simulacion (
            nombre_virus, poblacion, cant_contagio_inicial, area_km2, tipo_transmision, 
            probabilidad_contagio, tasa_letalidad, tiempo_recuperacion, capacidad_hospitalaria
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        
        valores = (
            virus_obj.nombre, 
            simulacion_obj.poblacion_total,
            simulacion_obj.cant_contagio_inicial,
            simulacion_obj.area_km2, 
            virus_obj.tipo_transmision,
            virus_obj.probabilidad_contagio,
            virus_obj.tasa_letalidad,
            virus_obj.tiempo_recuperacion, 
            simulacion_obj.capacidad_hospitalaria
        )
        
        self.cursor.execute(query, valores)
        self.conexion.commit()
        return self.cursor.lastrowid 

    def ver_una_simulacion(self, id_simulacion):
        query = "SELECT * FROM simulacion WHERE id_simulacion = ?"
        self.cursor.execute(query, (id_simulacion,))
        return self.cursor.fetchone()
    
    def obtener_todas_las_simulaciones(self):
        query = "SELECT id_simulacion, nombre_virus, poblacion FROM simulacion ORDER BY id_simulacion DESC"
        self.cursor.execute(query)
        return self.cursor.fetchall()
  
    def actualizar_simulacion(self, id_simulacion, nombre, poblacion, cant_inicial, area, transmision, probabilidad, tasa_let, tiempo_rec, capacidad):
       
        query = """UPDATE simulacion SET 
            nombre_virus = ?, 
            poblacion = ?, 
            cant_contagio_inicial = ?,
            area_km2 = ?, 
            tipo_transmision = ?, 
            probabilidad_contagio = ?, 
            tasa_letalidad = ?, 
            tiempo_recuperacion = ?, 
            capacidad_hospitalaria = ?
            WHERE id_simulacion = ?"""
        
        valores = (nombre, poblacion, cant_inicial, area, transmision, probabilidad, tasa_let, tiempo_rec, capacidad, id_simulacion)
        
        self.cursor.execute(query, valores)
        self.conexion.commit()
        return self.cursor.rowcount > 0  
    
    def borrar_simulacion(self, id_simulacion):

        query = "DELETE FROM simulacion WHERE id_simulacion = ?"
        self.cursor.execute(query, (id_simulacion,))
        self.conexion.commit()


    #_____________________CRUD dia_simulacion_______________

    def insertar_dia(self, id_simulacion, dia_dict):
     
        query = """INSERT INTO dia_simulacion (
            id_simulacion, numero_dia, sanos, infectados, 
            recuperados, fallecidos, pacientes_en_espera
        ) VALUES (?, ?, ?, ?, ?, ?, ?)"""
        
        valores = (
            id_simulacion,
            dia_dict['numero_dia'],
            dia_dict['sanos'],
            dia_dict['infectados'],
            dia_dict['recuperados'],
            dia_dict['fallecidos'],
            dia_dict['espera']
        )
        
        self.cursor.execute(query, valores)
        self.conexion.commit()

    def ver_resumen_dia_simulacion(self, id_simulacion):

        query = "SELECT * FROM dia_simulacion WHERE id_simulacion = ? ORDER BY numero_dia ASC"
        self.cursor.execute(query, (id_simulacion,))
        return self.cursor.fetchall()
    
    
    #___________________CRUD paciente_hospital_______________


    def insertar_paciente_final(self, id_simulacion, paciente):
        query = """INSERT INTO paciente_hospital (
            id_simulacion, dia_ingreso_cola, dia_atencion, estado_final
        ) VALUES (?, ?, ?, ?)"""
        
        valores = (
            id_simulacion,
            paciente.dia_ingreso_cola,
            paciente.dia_atencion,
            paciente.estado
        )
        
        self.cursor.execute(query, valores)
        self.conexion.commit()
        

    def ver_fila_paciente(self, id_simulacion):

        query = "SELECT * FROM paciente_hospital WHERE id_simulacion = ? ORDER BY dia_ingreso_cola ASC"
        self.cursor.execute(query, (id_simulacion,))
        return self.cursor.fetchall()