def rgb_to_hls(r, g, b):
    # Asegurar que los valores de R, G y B estén en el rango correcto (0 a 255)
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    print(f"Paso 1: R = {r}, G = {g}, B = {b}")


    # Normalizar los valores de R, G y B al rango de 0 a 1
    r = round(r / 255, 5)
    g = round(g / 255, 5)
    b = round(b / 255, 5)
    print(f"Paso 2: R = {r}, G = {g}, B = {b}")

    # Calcular el valor máximo y el valor mínimo de los componentes R, G y B
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    print(f"Paso 3: máximo = {max_val}, mínimo = {min_val}")


    # Calcular el valor de L (luminosidad) como (max_val + min_val) / 2
    l = round((max_val + min_val) / 2, 5)
    print(f"Paso 4: luminosidad = {l}")


    # Si max_val es igual a min_val, asignar H y S como 0 y retornar el resultado
    if max_val == min_val:
        return 0, l, 0

    # Calcular el valor de S (saturación)
    if l <= 0.5:
        s = round((max_val - min_val) / (max_val + min_val), 5)
    else:
        s = round((max_val - min_val) / (2 - max_val - min_val), 5)
    
    print(f"Paso 5: saturación = {s}")

    # Determinar qué componente es el mayor para calcular el ángulo de H
    if max_val == r:
        h = round(((g - b) / (max_val - min_val)) % 6, 5)
    elif max_val == g:
        h = round(((b - r) / (max_val - min_val)) + 2, 5)
    else:
        h = round(((r - g) / (max_val - min_val)) + 4, 5)

    # Calcular el valor de H como H * 60
    h = round(h * 60, 5)
    print(f"Paso 6: h = {h}")


    # Si H es menor que 0, sumar 360 a H
    if h < 0:
        h += 360

    # Retornar los valores de H, L y S como resultado de la conversión
    return h, l, s

# Definir los valores RGB del punto 1. a.
R = 160
G = 255
B = 50 

# Llamar a la función rgb_to_hls
h, s, v = rgb_to_hls(R, G, B)

# Imprimir los resultados
print("Valores de RGB:", R, G, B)
print("Valores de HSV:", h, s, v)
