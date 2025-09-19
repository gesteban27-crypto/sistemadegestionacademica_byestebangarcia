import csv
from typing import List
from modelos import Estudiante  # Sin punto

class RepositorioCSV:
    def __init__(self, archivo: str):
        self.archivo = archivo
    
    def cargar_estudiantes(self) -> List[Estudiante]:
        estudiantes = []
        try:
            with open(self.archivo, 'r', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    estudiante = Estudiante(
                        int(row['id']),
                        row['nombre'],
                        float(row['nota'])
                    )
                    estudiantes.append(estudiante)
        except FileNotFoundError:
            pass
        return estudiantes
    
    def guardar_estudiantes(self, estudiantes: List[Estudiante]) -> None:
        with open(self.archivo, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'nombre', 'nota'])
            writer.writeheader()
            for estudiante in estudiantes:
                writer.writerow(estudiante.to_dict())
