from logica.operaciones import Procesador

def iniciar_menu():
    calc = Procesador()
    
    while True:
        print("\n--- CALCULADORA INTELIGENTE ---")
        print("1. Suma           5. Potencia")
        print("2. Resta          6. Raíz Cuadrada")
        print("3. Multiplicación 7. Porcentaje")
        print("4. División       8. Celsius -> Fahrenheit")
        print("S. Salir")
        
        op = input("\nSeleccione una opción: ").lower()
        
        if op == 's':
            print("¡Adiós!")
            break
            
        try:
            val1 = float(input("Ingrese el primer valor: "))
            
            # Operaciones que solo requieren un operando
            if op in ['6', '8']:
                res = calc.raiz(val1) if op == '6' else calc.c_a_f(val1)
            else:
                val2 = float(input("Ingrese el segundo valor: "))
                acciones = {
                    '1': calc.suma, '2': calc.resta, '3': calc.multi,
                    '4': calc.div, '5': calc.pot, '7': calc.porcentaje
                }
                if op in acciones:
                    res = acciones[op](val1, val2)
                else:
                    print("Opción no válida.")
                    continue
            
            print(f"\n>>> RESULTADO: {res}")
            
        except ValueError:
            print("Error: Ingrese números válidos.")
        except Exception as e:
            print(f"Error inesperado: {e}")