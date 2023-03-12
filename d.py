import pandas as pd

# Escribir un programa que genere un DataFreme con los datos de la siguiente tabla:
data = {
    "Mes": [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
    ],
    "Ventas": [
        30500,
        35600,
        28300,
        33900,
        45000,
        18600,
        38740,
        35000,
        28950,
        17505,
        36540,
        44444,
    ],
    "Gastos": [
        22000,
        23400,
        18100,
        20700,
        42500,
        12000,
        21450,
        18900,
        17850,
        8500,
        21500,
        25600,
    ],
}

df = pd.DataFrame(data)

print(df)


# Escribir una función que reciba un DataFrame con el formato del ejercicio anterior y devuelva el balance total en los meses indicados
def calcular_balance(df, mes_inicio, mes_fin):
    # Obtener el índice de los meses de inicio y fin
    indice_inicio = df[df["Mes"] == mes_inicio].index[0]
    indice_fin = df[df["Mes"] == mes_fin].index[0]
    # Obtener las ventas y gastos en el rango de meses especificado
    ventas = df.loc[indice_inicio:indice_fin, "Ventas"].sum()
    gastos = df.loc[indice_inicio:indice_fin, "Gastos"].sum()
    # Calcular el balance y devolverlo
    balance = ventas - gastos
    return balance


balance_trimestral = calcular_balance(df, "Enero", "Marzo")
print(f"El balance total en el primer trimestre es {balance_trimestral}")

# Escribir una función que exporte el DataFrame y el resultado de lo solicitado en este item.
def exportar_datos(df, mes_inicio, mes_fin):
    # Calcular el balance total en el rango de meses especificado
    balance = calcular_balance(df, mes_inicio, mes_fin)

    # Crear un nuevo dataframe con los resultados
    resultado = pd.DataFrame(
        {"Balance": [balance], "Mes de inicio": [mes_inicio], "Mes de fin": [mes_fin]}
    )

    # Crear un escritor de Excel
    writer = pd.ExcelWriter("datos_exportados.xlsx", engine="xlsxwriter")

    # Exportar el dataframe original a la hoja 'Datos'
    df.to_excel(writer, sheet_name="Datos", index=False)

    # Exportar el dataframe con los resultados a la hoja 'Resultado'
    resultado.to_excel(writer, sheet_name="Resultado", index=False)

    # Guardar y cerrar el archivo
    writer.save()


exportar_datos(df, "Enero", "Marzo")
