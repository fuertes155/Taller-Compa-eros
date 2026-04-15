import math

class Procesador:
    """Lógica de negocio: Operaciones matemáticas puras."""
    
    def suma(self, a, b): return a + b
    def resta(self, a, b): return a - b
    def multi(self, a, b): return a * b
    
    def div(self, a, b):
        # Validación para evitar división por cero
        return a / b if b != 0 else "Error: División por cero"
        
    def pot(self, a, b): return a ** b
    def raiz(self, a): return math.sqrt(a)
    def porcentaje(self, a, b): return (a * b) / 100
    def c_a_f(self, c): return (c * 9/5) + 32