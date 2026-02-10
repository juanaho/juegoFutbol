from probability.obstaculos import obtener_obstaculos
import os

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def jugar_una_jugada():
    """Simula una jugada individual."""
    limpiar_pantalla()
    print("=" * 50)
    print("⚽ JUEGA UNA JUGADA DE FÚTBOL ⚽")
    print("=" * 50)
    print()
    
    obstaculos = obtener_obstaculos()
    gol = True
    obstaculos_superados = 0
    
    for i, obstaculo in enumerate(obstaculos, 1):
        print(f"Obstáculo {i}: {obstaculo}")
        
        if obstaculo.intentar_superar():
            print(f"✅ ¡Superado!")
            obstaculos_superados += 1
        else:
            print(f"❌ ¡Falló!")
            gol = False
            break
        print()
    
    print("=" * 50)
    if gol:
        print("🎉 ¡¡¡GOL!!! 🎉")
    else:
        print(f"⚠️ La jugada se interrumpió en el obstáculo {obstaculos_superados + 1}")
    print("=" * 50)
    print()
    input("Presiona Enter para continuar...")

def simulacion_monte_carlo():
    """Ejecuta una simulación Monte Carlo de 10,000 jugadas."""
    limpiar_pantalla()
    print("=" * 50)
    print("📊 SIMULACIÓN MONTE CARLO (10,000 simulaciones)")
    print("=" * 50)
    print()
    
    NUM_SIMULACIONES = 10000
    obstaculos = obtener_obstaculos()
    goles = 0
    resultados_por_obstaculo = [0] * len(obstaculos)
    
    for _ in range(NUM_SIMULACIONES):
        for i, obstaculo in enumerate(obstaculos):
            if obstaculo.intentar_superar():
                resultados_por_obstaculo[i] += 1
            else:
                break
        else:
            goles += 1
    
    print(f"Total de simulaciones: {NUM_SIMULACIONES}")
    print(f"Total de goles: {goles}")
    print(f"Porcentaje de éxito: {(goles / NUM_SIMULACIONES) * 100:.2f}%")
    print()
    
    print("Obstáculos superados:")
    for i, obstaculo in enumerate(obstaculos):
        superados = resultados_por_obstaculo[i]
        porcentaje = (superados / NUM_SIMULACIONES) * 100
        print(f"{i+1}. {obstaculo.nombre}: {superados:,} veces ({porcentaje:.2f}%)")
    
    print()
    print("=" * 50)
    input("Presiona Enter para continuar...")

def menu_principal():
    """Menú principal del programa."""
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("🏆 JUEGO DE FÚTBOL - SIMULACIÓN MONTE CARLO 🏆")
        print("=" * 50)
        print()
        print("1. Jugar una jugada")
        print("2. Simulación Monte Carlo")
        print("3. Salir")
        print()
        
        opcion = input("Elige una opción (1-3): ").strip()
        
        if opcion == "1":
            jugar_una_jugada()
        elif opcion == "2":
            simulacion_monte_carlo()
        elif opcion == "3":
            limpiar_pantalla()
            print("¡Hasta luego! ⚽")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
