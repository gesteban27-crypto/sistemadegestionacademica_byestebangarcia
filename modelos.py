from dataclasses import dataclass
from typing import Dict

@dataclass
class Estudiante:
    """Clase que representa a un estudiante con sus atributos básicos."""
    
    _id: int
    _nombre: str
    _nota: float
    
    def __post_init__(self):
        self.nota = self._nota  # Validación al crear instancia
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def nombre(self) -> str:
        return self._nombre
        
    @property
    def nota(self) -> float:
        return self._nota
    
    @nota.setter
    def nota(self, valor: float) -> None:
        if not isinstance(valor, (int, float)):
            raise ValueError("La nota debe ser un número")
        if not 0 <= valor <= 100:
            raise ValueError("La nota debe estar entre 0 y 100")
        self._nota = float(valor)
    
    def __str__(self) -> str:
        return f"ID: {self._id} | Nombre: {self._nombre} | Nota: {self._nota}"
    
    def to_dict(self) -> Dict:
        return {
            "id": self._id,
            "nombre": self._nombre,
            "nota": self._nota
        }