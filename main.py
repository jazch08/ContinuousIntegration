from datetime import datetime, timedelta

class Libro:
    def __init__(self, titulo, autor, cantidad_disponible):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_disponible = cantidad_disponible

class Prestamo:
    def __init__(self, libro, cantidad):
        self.libro = libro
        self.cantidad = cantidad
        self.fecha_prestamo = datetime.now()
        self.fecha_vencimiento = self.fecha_prestamo + timedelta(days=14)  # 14 días de préstamo

    def calcular_cargos_mora(self):
        fecha_actual = datetime.now()
        if fecha_actual > self.fecha_vencimiento:
            dias_vencidos = (fecha_actual - self.fecha_vencimiento).days
            cargo_mora = dias_vencidos * 1  # $1 de cargo por día de retraso
            return cargo_mora
        return 0

class SistemaBiblioteca:
    def __init__(self):
        self.catalogo = [
            Libro("Cien años de soledad", "Gabriel García Márquez", 5),
            Libro("El nombre del viento", "Patrick Rothfuss", 3),
            # Agregar más libros al catálogo
        ]
        self.prestamos = []

    def mostrar_catalogo(self):
        print("Catálogo de libros disponibles:")
        for libro in self.catalogo:
            print(f"Título: {libro.titulo}, Autor: {libro.autor}, Disponibles: {libro.cantidad_disponible}")

    def realizar_prestamo(self):
        cantidad_total_prestada = 0

        print("Catálogo de libros disponibles:")
        for libro in self.catalogo:
            print(f"Título: {libro.titulo}, Autor: {libro.autor}, Disponibles: {libro.cantidad_disponible}")

        while cantidad_total_prestada < 10:
            titulo = input("Ingrese el título del libro que desea llevar en préstamo (o 'fin' para finalizar): ")

            if titulo.lower() == "fin":
                break

            libro_seleccionado = None
            for libro in self.catalogo:
                if libro.titulo.lower() == titulo.lower():
                    libro_seleccionado = libro
                    break

            if libro_seleccionado and libro_seleccionado.cantidad_disponible > 0:
                cantidad = int(input("Ingrese la cantidad de ejemplares que desea llevar en préstamo: "))
                if 0 < cantidad <= libro_seleccionado.cantidad_disponible and cantidad_total_prestada + cantidad <= 10:
                    libro_seleccionado.cantidad_disponible -= cantidad
                    cantidad_total_prestada += cantidad
                    print(f"¡Préstamo de '{libro_seleccionado.titulo}' realizado con éxito!")
                else:
                    print("La cantidad ingresada es inválida o excede el límite de disponibilidad o de libros a prestar.")
            else:
                print("El libro ingresado no está disponible en el catálogo o no quedan ejemplares.")

        print("Ha alcanzado el límite máximo de libros prestados o ha finalizado el proceso de préstamo.")
