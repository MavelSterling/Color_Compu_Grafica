def hls_to_rgb(h, l, s):
    # Asegurar que los valores de H, L y S estén en el rango correcto
    h = max(0, min(360, h))
    l = max(0, min(1, l))
    s = max(0, min(1, s))
    
    print(f"Paso 1: H = {h}, L = {l}, S = {s}")


    if s == 0:
        # Tono de gris, asignar R, G y B como L multiplicada por 255
        r = g = b = int(l * 255)
        print("Tono es gris. Se le asigna R, G y B como:", r)
    else:
        # Calcular los valores temporales
        c = (1 - abs(2 * l - 1)) * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = l - c / 2
        print(f"Paso 2: Valores temporales C = {c}, X = {x}, m = {m}")

        # Determinar en qué rango de H se encuentra para calcular los valores de R, G y B
        if 0 <= h < 60:
            r, g, b = c, x, 0
        elif 60 <= h < 120:
            r, g, b = x, c, 0
        elif 120 <= h < 180:
            r, g, b = 0, c, x
        elif 180 <= h < 240:
            r, g, b = 0, x, c
        elif 240 <= h < 300:
            r, g, b = x, 0, c
        else:  # 300 <= h < 360
            r, g, b = c, 0, x
        print(f"Paso 3: Valores de R, G y B ={r,g,b}")

        # Se ajustan los valores de R, G y B sumando m a cada componente
        r = int((r + m) * 255)
        g = int((g + m) * 255)
        b = int((b + m) * 255)
        print(f"Paso 4: Valores de R, G y B ajustados ={r,g,b}")

    # Se verifican que los valores de R, G y B estén en el rango correcto (0 a 255)
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    print(f"Paso 5: R = {r}, G = {g}, B = {b}")
    return r, g, b


# Definir los valores HSV del punto 2 b.
h = 88
l = 0.5980
s = 1

# Llamar a la función hls_to_rgb
r, g, b = hls_to_rgb(h, l, s)

# Imprimir los resultados
print("Valores de HLS:", h, l, s)
print("Valores de RGB:", r, g, b)