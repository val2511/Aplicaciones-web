def aplicar_impuesto(tasa_iva, precios):

    for i in range(len(precios)):
        precios[i] = precios[i] + precios[i] * tasa_iva


iva = 0.19
precios = [100, 200, 300]

print("Antes:", precios)

aplicar_impuesto(iva, precios)

print("Después:", precios)
