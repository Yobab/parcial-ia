# Crear una lista de diccionarios con tres diccionarios
lista_diccionarios = [
    {"curso": "Inteligencia Artificial", "inscritos": 50, "aprobados": 20},
    {"curso": "Administración de Tecnologías de Información", "inscritos": 30, "aprobados": 15},
    {"curso": "Redes II", "inscritos": 35, "aprobados": 32}
]

# Imprimir la cantidad de inscritos en el tercer registro (indice 2 para el tercer diccionario, clave "inscritos")
print(lista_diccionarios[2]["inscritos"])

# Imprimir la cantidad de aprobados en el último registro (indice -1 para el último diccionario, clave "aprobados")
print(lista_diccionarios[-1]["aprobados"])

# Calcular el porcentaje de aprobados en el segundo registro (indice 1 para el segundo diccionario, clave "aprobados" y "inscritos")
porcentaje_aprobados = (lista_diccionarios[1]["aprobados"] / lista_diccionarios[1]["inscritos"]) * 100
print("El porcentaje de aprobados en el segundo registro es:", porcentaje_aprobados)
