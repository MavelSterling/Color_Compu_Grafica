def rgb_to_cmy(r, g, b):
    # Asegurar que los valores de R, G y B estén en el rango correcto (0 a 255)
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    print(f"Paso 1: R = {r}, G = {g}, B = {b}")

    # Normalizar los valores de R, G y B al rango de 0 a 1
    r = round(r / 255, 5)
    g = round(g / 255, 5)
    b = round(b / 255, 5)
    print(f"Paso 2: Se normaliza los valores R = {r}, G = {g}, B = {b}")

    # Calcular los valores de C, M y Y 
    c = round(1 - r, 5)
    m = round(1 - g, 5)
    y = round(1 - b, 5)
    print(f"Paso 3: Los valores C= {c}, M = {m}, Y = {y}")

    # Asegurar que los valores de C, M y Y estén en el rango correcto (0 a 1)
    c = max(0, min(1, c))
    m = max(0, min(1, m))
    y = max(0, min(1, y))
    print(f"Paso 4: Los valores C= {c}, M = {m}, Y = {y}")

    # Retornar los valores de C, M y Y 
    return c, m, y

# Definir los valores RGB del punto 3. a.
R = 160
G = 255
B = 50 

# Llamar a la función rgb_to_cmy
c, m, y = rgb_to_cmy(R, G, B)

# Imprimir los resultados
print("Valores de RGB:", R, G, B)
print("Valores de CMY:", c, m, y)