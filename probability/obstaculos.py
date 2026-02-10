from utils.rng import random_event

class Obstaculo:
    """Clase que representa un obstáculo en la jugada de fútbol."""
    
    def __init__(self, nombre, probabilidad):
        self.nombre = nombre
        self.probabilidad = probabilidad
    
    def intentar_superar(self):
        """Intenta superar el obstáculo basado en su probabilidad."""
        return random_event(self.probabilidad)
    
    def __str__(self):
        return f"{self.nombre} ({self.probabilidad * 100:.0f}%)"


# Definición de los 5 obstáculos con probabilidades realistas
OBSTACULOS = [
    Obstaculo("Control del balón", 0.95),
    Obstaculo("Regate al primer defensa", 0.70),
    Obstaculo("Regate al segundo defensa", 0.55),
    Obstaculo("Enfrentamiento con el portero", 0.60),
    Obstaculo("Disparo a puerta", 0.75),
]

def obtener_obstaculos():
    """Retorna la lista de obstáculos."""
    return OBSTACULOS
