# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 14:32:18 2021

@author: Alejandro Hernandez
"""
import pandas as pd
# Primero lea la hoja vt en un Dataframe vt y sobre este:
vt = pd.read_excel('datosCT.xlsx', sheet_name='vt', index_col=0)
vt.columns
# Suponga que ha habido un olvido y no se tomó en cuenta un Ingreso mensual de $1000 en todos los meses. 
# Modifique el DataFrame para aumentar en $1000 los ingresos de cada mes.
vt['Ingreso'] = vt['Ingreso']+1000
# Agregue una columna Utilidad (Ingreso - Gasto).
vt['Utilidad'] = vt['Ingreso'] - vt['Gasto']
# Encuentre el promedio de Gasto en los meses en los que la Utilidad fue negativa.
promedio_GASTOS_utilidad_negativa = (vt[vt['Utilidad'] < 0]['Gasto']).mean()
# Encuentre los ingresos totales del año.
ingresos_anio = sum(vt['Ingreso'])
# Encuentre la lista de los meses en los que la Utilidad fue positiva.
meses_utilidad_positiva = (vt[vt['Utilidad'] > 0])

# Ahora lea la hoja 8c, que representa las distancias en kilómetros entre una serie de ciudades, 
#en un Dataframe cd y sobre este:
cd = pd.read_excel('datosCT.xlsx', sheet_name='8c', index_col=0)
# Convierta todos los valores a millas (km/1.609)
cd.iloc[:,1:] = cd.iloc[:,1:] / 1.609
# Genere una serie llamada gdl con las distancias a partir de Guadalajara a todas las ciudades.
gdl = cd['GDL']
# Encuentre la lista de las ciudades que están a más de 1000 millas de Guadalajara.
diez_millas_de_GDL = gdl[gdl > 1000]
