import pandas as pd
import numpy as np

datos_alturas = ["1.82", "1.55", "1.67", "1.69", "1.67", "1.82", "1.75", "1.74", "1.66", "1.73", "1.70", "1.74", 
                 "1.66", "1.62", "1.75", "1.65", "1.74", "1.90", "1.67", "1.50", "1.71", "1.74", "1.77", "1.65", 
                 "1.54", "1.78", "1.64", "1.69"]

alturas = [float(h) for h in datos_alturas]
df = pd.DataFrame({'Altura': alturas})

max_altura = df['Altura'].max()
min_altura = df['Altura'].min()
rango = max_altura - min_altura


num_clases = round(1 + 3.3 * np.log10(len(df)))


ancho_clase = rango / num_clases


limites_inferiores = [min_altura + i * ancho_clase for i in range(num_clases)]
limites_superiores = [lim_inf + ancho_clase for lim_inf in limites_inferiores]


marcas_clase = [(lim_inf + lim_sup) / 2 for lim_inf, lim_sup in zip(limites_inferiores, limites_superiores)]


frec_absoluta = [0] * num_clases


for altura in alturas:
    for i in range(num_clases):
        if limites_inferiores[i] <= altura < limites_superiores[i]:
            frec_absoluta[i] += 1


total_datos = len(df)
frec_relativa = [(f / total_datos) * 100 for f in frec_absoluta]


tabla = pd.DataFrame({
    'Límite Inferior': limites_inferiores,
    'Límite Superior': limites_superiores,
    'Marca de Clase': marcas_clase,
    'Frec. Absoluta': frec_absoluta,
    'Frec. Relativa (%)': frec_relativa
})


print("Tabla de Distribución de Frecuencias:")
print(tabla)
