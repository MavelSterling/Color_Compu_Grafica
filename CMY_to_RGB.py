def cmy_to_rgb(c, m, y):
    # Asegurar que los valores de C, M y Y estén en el rango correcto (0 a 1)
    c = max(0, min(1, c))
    m = max(0, min(1, m))
    y = max(0, min(1, y))
    print(f"Paso 1: Los valores C= {c}, M = {m}, Y = {y}")

    # Calcular los valores de R, G y B
    r = 1 - c
    g = 1 - m
    b = 1 - y
    print(f"Paso 2: R = {r}, G = {g}, B = {b}")

    # Asegurar que los valores de R, G y B estén en el rango correcto (0 a 255)
    r = max(0, min(255, int(r * 255)))
    g = max(0, min(255, int(g * 255)))
    b = max(0, min(255, int(b * 255)))
    print(f"Paso 3: R = {r}, G = {g}, B = {b}")


    # Retornar los valores de R, G y B como resultado de la conversión
    return r, g, b

# Definir los valores CMY del punto 3 b.
h = 88
l = 0.5980
s = 1

# Llamar a la función hls_to_rgb
r, g, b = hls_to_rgb(h, l, s)

# Imprimir los resultados
print("Valores de HLS:", h, l, s)
print("Valores de RGB:", r, g, b)