from datetime import datetime, timedelta
from main import Libro, Prestamo

def test_calcular_cargos_mora_sin_retraso():
    libro = Libro("Cien años de soledad", "Gabriel García Márquez", 5)
    prestamo = Prestamo(libro, 2)
    assert prestamo.calcular_cargos_mora() == 0

def test_calcular_cargos_mora_con_retraso():
    libro = Libro("El nombre del viento", "Patrick Rothfuss", 3)
    prestamo = Prestamo(libro, 1)
    
    # Cambiar la fecha de vencimiento del préstamo a 3 días antes de la fecha actual
    fecha_vencimiento = datetime.now() - timedelta(days=3)
    prestamo.fecha_vencimiento = fecha_vencimiento
    
    # Calcular cargos por mora considerando un retraso de 3 días
    assert prestamo.calcular_cargos_mora() == 3

def test_calcular_cargos_mora_con_fecha_actual_antes_de_vencimiento():
    libro = Libro("Prueba de libro", "Autor de prueba", 2)
    prestamo = Prestamo(libro, 1)
    
    # Cambiar la fecha de vencimiento del préstamo a 5 días después de la fecha actual
    fecha_vencimiento = datetime.now() + timedelta(days=5)
    prestamo.fecha_vencimiento = fecha_vencimiento
    
    # La fecha actual es antes de la fecha de vencimiento, por lo tanto no hay cargos por mora
    assert prestamo.calcular_cargos_mora() == 0
