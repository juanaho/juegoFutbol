import random

def random_event(prob):
    """
    Evalúa si un evento ocurre basado en una probabilidad.
    
    Args:
        prob (float): Probabilidad del evento (0.0 a 1.0)
    
    Returns:
        bool: True si el evento ocurre, False si no
    """
    return random.random() < prob
