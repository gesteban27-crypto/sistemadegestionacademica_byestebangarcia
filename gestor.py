from typing import List, Optional
from modelos import Estudiante

class GestorEstudiantes:
    def __init__(self):
        self.estudiantes: List[Estudiante] = []
        self._ultimo_id = 0
    
    def agregar_estudiante(self, nombre: str, nota: float) -> Estudiante:
        """Agrega un nuevo estudiante y retorna el objeto creado."""
        self._ultimo_id += 1
        estudiante = Estudiante(self._ultimo_id, nombre, nota)
        self.estudiantes.append(estudiante)
        return estudiante
    
    def buscar_por_id(self, id: int) -> Optional[Estudiante]:
        """Busca un estudiante por su ID."""
        return next((e for e in self.estudiantes if e.id == id), None)
    
    def editar_nota(self, id: int, nueva_nota: float) -> bool:
        """Edita la nota de un estudiante. Retorna True si se realizó el cambio."""
        estudiante = self.buscar_por_id(id)
        if estudiante:
            estudiante.nota = nueva_nota
            return True
        return False
    
    def eliminar_estudiante(self, id: int) -> bool:
        """Elimina un estudiante por su ID. Retorna True si se eliminó."""
        estudiante = self.buscar_por_id(id)
        if estudiante:
            self.estudiantes.remove(estudiante)
            return True
        return False
    
    def calcular_estadisticas(self):
        """Calcula estadísticas básicas de las notas."""
        if not self.estudiantes:
            return {"promedio": 0, "max": 0, "min": 0}
        
        notas = [e.nota for e in self.estudiantes]
        return {
            "promedio": sum(notas) / len(notas),
            "max": max(notas),
            "min": min(notas)
        }
    
    def obtener_distribucion(self):
        """Calcula la distribución de notas por rangos."""
        total = len(self.estudiantes)
        if total == 0:
            return {"0-59": 0, "60-79": 0, "80-100": 0}
        
        rangos = {
            "0-59": len([e for e in self.estudiantes if 0 <= e.nota < 60]),
            "60-79": len([e for e in self.estudiantes if 60 <= e.nota < 80]),
            "80-100": len([e for e in self.estudiantes if 80 <= e.nota <= 100])
        }
        
        return {k: (v/total)*100 for k, v in rangos.items()}