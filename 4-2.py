def generar_reporte(titulo, *secciones):

    print(titulo)

    for seccion in secciones:
        print(seccion)


basicas = ("Introducción", "Resultados")

extras = ["Conclusión", "Recomendaciones"]


generar_reporte(
    "Mi reporte",
    *basicas,
    *extras
)
