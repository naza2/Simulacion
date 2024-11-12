def cargar_casetas(conexion):
    consulta = """
    SELECT id_observacion, caseta, fecha, hora_inicio, hora_fin, clientes_totales, tiempo_promedio_atencion 
    FROM observaciones_caseta;
    """
    cursor = conexion.cursor()
    cursor.execute(consulta)
    casetas = cursor.fetchall()
    cursor.close()
    return casetas

def cargar_encuestas(conexion):
    consulta = """
    SELECT semestre, frecuencia_compra, horario_preferido, horas_libres, caseta_preferida, factor_influencia, 
           tiempo_espera_dispuesto, presupuesto, experiencia_general, experiencia_filas, espera_promedio_filas 
    FROM encuestas_estudiantes;
    """
    cursor = conexion.cursor()
    cursor.execute(consulta)
    encuestas = cursor.fetchall()
    cursor.close()
    return encuestas
