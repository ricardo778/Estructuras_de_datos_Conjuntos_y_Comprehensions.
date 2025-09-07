# Tengo una lista de temperaturas en Celsius
celsius = [0, 10, 20, 30, 40]

# Convierto cada temperatura a Fahrenheit usando la fórmula
fahrenheit = [(9/5) * temp + 32 for temp in celsius]

# Muestro las temperaturas convertidas
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]