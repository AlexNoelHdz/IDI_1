# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 08:20:10 2021

@author: Alejandro Hernandez
"""
import pandas as pd
#Jalar la información de un archivo
df = pd.read_excel('datosPE.xlsx', sheet_name = 'Hoja1')

# - El vector de IMC
df_IMC = df['Peso']/df['Estatura']**2
# - La media de los pesos y la media de las estaturas
media_pesos = df['Peso'].mean()
media_estatura = df['Estatura'].mean()

#Ejemplo indexar

# - El ID de la persona de mayor peso, de la persona de menor estatura
mayor_peso = df[max(df['Peso'])]['ID Persona']
# - El vector de los ID de las personas con IMC>=28

# Todos los resultados se ponen en una variable y se imprimen.
