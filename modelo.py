def entrenar_modelo(estudiantes, casetas):
    for estudiante in estudiantes:
        caseta_elegida = estudiante.elegir_caseta(casetas)
        if caseta_elegida:
            caseta_elegida.atender_estudiante(estudiante)
            print(f"{estudiante} ha elegido la {caseta_elegida.nombre}")
