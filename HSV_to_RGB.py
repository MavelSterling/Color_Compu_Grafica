def hsv_to_rgb(h, s, v):
    # Asegurar que los valores de H, S y V estén en el rango correcto
    h = max(0, min(360, h))
    s = max(0, min(1, s))
    v = max(0, min(1, v))

    # Calcular el valor de C (Chroma)
    c = v * s

    # Calcular el valor de X
    x = c * (1 - abs((h / 60) % 2 - 1))

    # Calcular los valores de m (valor mínimo) y rgb_base (componentes de RGB sin ajuste)
    m = v - c
    if h < 60:
        rgb_base = (c, x, 0)
    elif h < 120:
        rgb_base = (x, c, 0)
    elif h < 180:
        rgb_base = (0, c, x)
    elif h < 240:
        rgb_base = (0, x, c)
    elif h < 300:
        rgb_base = (x, 0, c)
    else:
        rgb_base = (c, 0, x)

    # Ajustar los componentes de RGB con el valor mínimo (m)
    r, g, b = (rgb_base[0] + m, rgb_base[1] + m, rgb_base[2] + m)

    # Asegurar que los valores de R, G y B estén en el rango correcto (0 a 1)
    r = max(0, min(1, r))
    g = max(0, min(1, g))
    b = max(0, min(1, b))

    # Escalar los valores de R, G y B al rango de 0 a 255 y convertir a enteros
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)

    # Devolver los valores de R, G y B como resultado de la conversión
    return r, g, b


# Definir los valores HSV del punto 1 b.
h = 212
s = 0.94
v = 0.78431

# Llamar a la función hsv_a_rgb
r, g, b = hsv_to_rgb(h, s, v)

# Imprimir los resultados
print("Valores de HSV:", h, s, v)
print("Valores de RGB:", r, g, b)
