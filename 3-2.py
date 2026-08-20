def auditar_evento(nivel, *etiquetas, **datos):

    print("Nivel:", nivel)
    print("Etiquetas:", etiquetas)
    print("Datos:", datos)


auditar_evento(
    "ERROR",
    "seguridad",
    "auth",
    usuario="admin",
    intento=3
)
