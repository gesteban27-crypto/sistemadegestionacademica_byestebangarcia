from gestor import GestorEstudiantes
from repositorio import RepositorioCSV

class InterfazConsola:
    def __init__(self):
        self.gestor = GestorEstudiantes()
        self.repositorio = RepositorioCSV('estudiantes.csv')
        self.cargar_datos()
    
    def cargar_datos(self):
        estudiantes = self.repositorio.cargar_estudiantes()
        self.gestor.estudiantes = estudiantes
        if estudiantes:
            self.gestor._ultimo_id = max(e.id for e in estudiantes)

    def registrar_estudiante(self):
        try:
            nombre = input("\nIngrese el nombre del estudiante: ")
            if not nombre.strip():
                print("Error: El nombre no puede estar vacío")
                return
            
            nota = float(input("Ingrese la nota del estudiante (0-100): "))
            if not 0 <= nota <= 100:
                print("Error: La nota debe estar entre 0 y 100")
                return
                
            estudiante = self.gestor.agregar_estudiante(nombre, nota)
            print(f"\nEstudiante registrado exitosamente:")
            print(estudiante)
            input("\nPresione Enter para continuar...")
            
        except ValueError:
            print("Error: La nota debe ser un número válido")
            input("\nPresione Enter para continuar...")
    
    def mostrar_estudiantes(self):
        if not self.gestor.estudiantes:
            print("\nNo hay estudiantes registrados")
        else:
            print("\nLista de estudiantes:")
            for estudiante in self.gestor.estudiantes:
                print(estudiante)
        input("\nPresione Enter para continuar...")
    
    def editar_nota(self):
        try:
            id = int(input("\nIngrese el ID del estudiante: "))
            nueva_nota = float(input("Ingrese la nueva nota (0-100): "))
            
            if self.gestor.editar_nota(id, nueva_nota):
                print("Nota actualizada exitosamente")
            else:
                print("Estudiante no encontrado")
            
        except ValueError:
            print("Error: Ingrese valores numéricos válidos")
        input("\nPresione Enter para continuar...")
    
    def eliminar_estudiante(self):
        try:
            id = int(input("\nIngrese el ID del estudiante a eliminar: "))
            if self.gestor.eliminar_estudiante(id):
                print("Estudiante eliminado exitosamente")
            else:
                print("Estudiante no encontrado")
        except ValueError:
            print("Error: ID inválido")
        input("\nPresione Enter para continuar...")
    
    def mostrar_estadisticas(self):
        stats = self.gestor.calcular_estadisticas()
        print("\nEstadísticas:")
        print(f"Promedio: {stats['promedio']:.2f}")
        print(f"Nota máxima: {stats['max']}")
        print(f"Nota mínima: {stats['min']}")
        input("\nPresione Enter para continuar...")
    
    def mostrar_distribucion(self):
        dist = self.gestor.obtener_distribucion()
        print("\nDistribución de notas:")
        for rango, porcentaje in dist.items():
            print(f"{rango}: {porcentaje:.2f}%")
        input("\nPresione Enter para continuar...")
    
    def mostrar_menu(self):
        print("\n=== Sistema de Gestión Académica ===")
        print("1. Registrar estudiante")
        print("2. Ver estudiantes")
        print("3. Editar nota")
        print("4. Eliminar estudiante")
        print("5. Ver estadísticas")
        print("6. Ver distribución")
        print("0. Salir")
        
    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                self.registrar_estudiante()
            elif opcion == "2":
                self.mostrar_estudiantes()
            elif opcion == "3":
                self.editar_nota()
            elif opcion == "4":
                self.eliminar_estudiante()
            elif opcion == "5":
                self.mostrar_estadisticas()
            elif opcion == "6":
                self.mostrar_distribucion()
            elif opcion == "0":
                self.repositorio.guardar_estudiantes(self.gestor.estudiantes)
                print("\n¡Hasta luego!")
                break
            else:
                print("\nOpción no válida")
                input("\nPresione Enter para continuar...")