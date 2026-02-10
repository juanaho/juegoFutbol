# 🏆 Juego de Fútbol - Simulación Monte Carlo

Un juego interactivo de fútbol con simulación de probabilidades realistas basado en el método Monte Carlo.

## 📋 Descripción

Este proyecto simula una jugada de fútbol con 5 obstáculos progresivos que el jugador debe superar:

1. **Control del balón** (95% de éxito)
2. **Regate al primer defensa** (70% de éxito)
3. **Regate al segundo defensa** (55% de éxito)
4. **Enfrentamiento con el portero** (60% de éxito)
5. **Disparo a puerta** (75% de éxito)

## 🚀 Cómo ejecutar

### Requisitos
- Python 3.7 o superior

### Instalación y uso

```bash
# Clonar el repositorio
git clone https://github.com/juanaho/juegoFutbol.git
cd juegoFutbol

# Ejecutar el juego
python main.py
```

## 🎮 Opciones del menú

El programa ofrece dos modos:

1. **Jugar una jugada** - Intenta superar los 5 obstáculos
2. **Simulación Monte Carlo** - Ejecuta 10,000 simulaciones y muestra estadísticas

## 📁 Estructura del proyecto

```
juegoFutbol/
├── LICENSE              # Licencia Apache 2.0
├── README.md            # Este archivo
├── main.py              # Programa principal
├── probability/
│   └── obstaculos.py    # Definición de obstáculos y probabilidades
└── utils/
    └── rng.py           # Función de números aleatorios
```

## 📊 Probabilidades realistas

Las probabilidades se basan en estadísticas reales de fútbol:

| Obstáculo | Probabilidad |
|-----------|------------|
| Control del balón | 95% |
| Regate 1 | 70% |
| Regate 2 | 55% |
| Portero | 60% |
| Disparo | 75% |

**Probabilidad total de gol:** ~12.7%

## 🔧 Modificaciones

Puedes cambiar las probabilidades editando el archivo `probability/obstaculos.py`.

## 📝 Licencia

Este proyecto está bajo la licencia Apache 2.0. Ver archivo `LICENSE`.

## 👤 Autor

Juan Aho (@juanaho)
