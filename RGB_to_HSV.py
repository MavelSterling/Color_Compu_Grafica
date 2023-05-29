def RGBtoHSV(r, g, b):
    
    r= r/255
    g= g/255
    b= b/255
    
    max_rgb = max(r, g, b)
    min_rgb = min(r, g, b)
    v = max_rgb

    if min_rgb == max_rgb:
        return 0.0, 0.0, round(v, 5)

    s = round((max_rgb - min_rgb) / max_rgb, 5)
    rc = round((max_rgb - r) / (max_rgb - min_rgb), 5)
    gc = round((max_rgb - g) / (max_rgb - min_rgb), 5)
    bc = round((max_rgb - b) / (max_rgb - min_rgb), 5)

    if r == max_rgb:
        h = round(bc - gc, 5)
    elif g == max_rgb:
        h = round(2.0 + rc - bc, 5)
    else:
        h = round(4.0 + gc - rc, 5)

    h = round((h / 6.0) % 1.0, 5)

    return h, s, v



# Definir los valores RGB del punto 1. a.
red = 12 
green = 12 
blue = 12 

# Llamar a la función RGBtoHSV
h, s, v = RGBtoHSV(red, green, blue)

# Imprimir los resultados
print("Valores de RGB:", red, green, blue)
print("Valores de HSV:", h, s, v)
