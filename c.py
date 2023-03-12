import pandas as pd

# Leer el archivo nombres.csv
df = pd.read_csv("nombres.csv")

# ¿Hay mujeres llamadas Jules, Nery?
mujeres_jules = df[(df["name"] == "Jules") & (df["sex"] == "F")]
mujeres_nery = df[(df["name"] == "Nery") & (df["sex"] == "F")]
print(
    f"Hay {len(mujeres_jules)} mujeres llamadas Jules y {len(mujeres_nery)} mujeres llamadas Nery."
)

# ¿Cuál es la cantidad de mujeres llamadas Nery en el estado de CA y NJ nacidas después de 1950?
mujeres_nery_ca_nj = df[
    (df["name"] == "Nery")
    & (df["sex"] == "F")
    & (df["year"] > 1950)
    & ((df["state"] == "CA") | (df["state"] == "NJ"))
]
print(
    f"Hay {mujeres_nery_ca_nj['quantity'].sum()} mujeres llamadas Nery en los estados de CA y NJ nacidas después de 1950."
)

# ¿Cuál es la cantidad promedio de hombres llamados Mary nacidos después de 1989?
hombres_mary = df[(df["name"] == "Mary") & (df["sex"] == "M") & (df["year"] > 1989)]
promedio_hombres_mary = hombres_mary["quantity"].mean()
print(
    f"La cantidad promedio de hombres llamados Mary nacidos después de 1989 es {promedio_hombres_mary}."
)

# ¿Cuáles son los tres estados donde hay más mujeres llamadas Nery y Alex?
mujeres_nery_alex = df[(df["name"].isin(["Nery", "Alex"])) & (df["sex"] == "F")]
estados_con_mas_mujeres = (
    mujeres_nery_alex.groupby("state")["quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)
print(
    f"Los tres estados donde hay más mujeres llamadas Nery y Alex son:\n{estados_con_mas_mujeres}"
)
