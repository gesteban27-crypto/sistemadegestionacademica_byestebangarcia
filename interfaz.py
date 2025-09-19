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
    
    def mostrar_estudiantes_ordenados(self):
        print("\n1. Ordenar por nombre")
        print("2. Ordenar por nota")
        opcion = input("Seleccione criterio de ordenamiento: ")
        
        criterio = 'nombre' if opcion == '1' else 'nota'
        estudiantes = self.gestor.obtener_estudiantes_ordenados(criterio)
        
        print("\nLista de estudiantes ordenada:")
        for estudiante in estudiantes:
            print(estudiante)
        input("\nPresione Enter para continuar...")

    def buscar_estudiantes(self):
        nombre = input("\nIngrese nombre o inicial a buscar: ")
        estudiantes = self.gestor.buscar_por_nombre(nombre)
        
        if estudiantes:
            print("\nEstudiantes encontrados:")
            for estudiante in estudiantes:
                print(estudiante)
        else:
            print("\nNo se encontraron estudiantes")
        input("\nPresione Enter para continuar...")
    
    def editar_nota(self):
        try:
            id = int(input("\nIngrese el ID del estudiante: "))
            nueva_nota = float(input("Ingrese la nueva nota: "))
            
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
    
    def mostrar_clasificacion(self):
        try:
            umbral = float(input("\nIngrese nota mínima de aprobación (0-100): "))
            clasificacion = self.gestor.clasificar_estudiantes(umbral)
            
            print("\nEstudiantes Aprobados:")
            for estudiante in clasificacion['aprobados']:
                print(estudiante)
            
            print("\nEstudiantes Reprobados:")
            for estudiante in clasificacion['reprobados']:
                print(estudiante)
        except ValueError:
            print("Error: Ingrese un valor numérico válido")
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
        print("3. Ver estudiantes ordenados")
        print("4. Buscar estudiantes")
        print("5. Editar nota")
        print("6. Eliminar estudiante")
        print("7. Ver estadísticas")
        print("8. Ver clasificación")
        print("9. Ver distribución")
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
                self.mostrar_estudiantes_ordenados()
            elif opcion == "4":
                self.buscar_estudiantes()
            elif opcion == "5":
                self.editar_nota()
            elif opcion == "6":
                self.eliminar_estudiante()
            elif opcion == "7":
                self.mostrar_estadisticas()
            elif opcion == "8":
                self.mostrar_clasificacion()
            elif opcion == "9":
                self.mostrar_distribucion()
            elif opcion == "0":
                self.repositorio.guardar_estudiantes(self.gestor.estudiantes)
                print("\n¡Hasta luego!")
                break
            else:
                print("\nOpción no válida")
                input("\nPresione Enter para continuar...")
