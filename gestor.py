from typing import List, Optional
from modelos import Estudiante

class GestorEstudiantes:
    def __init__(self):
        self.estudiantes: List[Estudiante] = []
        self._ultimo_id = 0
    
    def agregar_estudiante(self, nombre: str, nota: float) -> Estudiante:
        self._ultimo_id += 1
        estudiante = Estudiante(self._ultimo_id, nombre, nota)
        self.estudiantes.append(estudiante)
        return estudiante
    
    def buscar_por_id(self, id: int) -> Optional[Estudiante]:
        return next((e for e in self.estudiantes if e.id == id), None)
    
    def editar_nota(self, id: int, nueva_nota: float) -> bool:
        estudiante = self.buscar_por_id(id)
        if estudiante:
            estudiante.nota = nueva_nota
            return True
        return False
    
    def eliminar_estudiante(self, id: int) -> bool:
        estudiante = self.buscar_por_id(id)
        if estudiante:
            self.estudiantes.remove(estudiante)
            return True
        return False
    
    def calcular_estadisticas(self):
        if not self.estudiantes:
            return {"promedio": 0, "max": 0, "min": 0}
        
        notas = [e.nota for e in self.estudiantes]
        return {
            "promedio": sum(notas) / len(notas),
            "max": max(notas),
            "min": min(notas)
        }
    
    def obtener_distribucion(self):
        total = len(self.estudiantes)
        if total == 0:
            return {"0-59": 0, "60-79": 0, "80-100": 0}
        
        rangos = {
            "0-59": len([e for e in self.estudiantes if 0 <= e.nota < 60]),
            "60-79": len([e for e in self.estudiantes if 60 <= e.nota < 80]),
            "80-100": len([e for e in self.estudiantes if 80 <= e.nota <= 100])
        }
        
        return {k: (v/total)*100 for k, v in rangos.items()}

    def obtener_estudiantes_ordenados(self, criterio='nombre'):
        """Retorna lista de estudiantes ordenada por nombre o nota."""
        if criterio == 'nombre':
            return sorted(self.estudiantes, key=lambda e: e.nombre)
        elif criterio == 'nota':
            return sorted(self.estudiantes, key=lambda e: e.nota, reverse=True)
        return self.estudiantes

    def clasificar_estudiantes(self, umbral=60):
        """Clasifica estudiantes como aprobados o reprobados."""
        aprobados = [e for e in self.estudiantes if e.nota >= umbral]
        reprobados = [e for e in self.estudiantes if e.nota < umbral]
        return {
            'aprobados': aprobados,
            'reprobados': reprobados
        }

    def buscar_por_nombre(self, nombre):
        """Busca estudiantes por nombre exacto o inicial."""
        nombre = nombre.lower()
        return [e for e in self.estudiantes 
                if e.nombre.lower().startswith(nombre)]