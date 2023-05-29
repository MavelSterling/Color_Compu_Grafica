def rgb_to_hsv(r, g, b):
    # Asegurar que los valores de R, G y B estén en el rango(0 a 255)
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))

    # Normalizar los valores de R, G y B al rango de 0 a 1
    r = round(r / 255, 5)
    g = round(g / 255, 5)
    b = round(b / 255, 5)

    # Calcular el valor máximo y el valor mínimo de las componentes R, G y B
    max_val = max(r, g, b)
    min_val = min(r, g, b)

    # Calcular el valor de V (luminosidad) como max_val
    v = max_val

    # Si max_val es igual a 0, asignar H y S como 0 y retornar el resultado
    if max_val == 0:
        return 0, 0, v

    # Calcular el valor de S (saturación)
    s = round((max_val - min_val) / max_val, 5)

    # Si max_val es igual a min_val, asignar H como 0 y retornar el resultado
    if max_val == min_val:
        return 0, s, v

    # Calcular el valor de C (intensidad cromática)
    c = round(max_val - min_val, 5)

    # Determinar qué componente es el mayor para calcular el ángulo de H
    if max_val == r:
        h = round(((g - b) / c) % 6, 5)
    elif max_val == g:
        h = round(((b - r) / c) + 2, 5)
    else:
        h = round(((r - g) / c) + 4, 5)

    # Calcular el valor de H como H * 60
    h = round(h * 60, 5)

    # Si H es menor que 0, entonces se suma 360 a H
    if h < 0:
        h += 360

    # Retornar los valores de H, S y V como resultado de la conversión
    return h, s, v

# Definir los valores RGB del punto 1. a.
R = 12 
G = 12 
B = 12 

# Llamar a la función rgb_to_hsv
h, s, v = rgb_to_hsv(R, G, B)

# Imprimir los resultados
print("Valores de RGB:", R, G, B)
print("Valores de HSV:", h, s, v)
