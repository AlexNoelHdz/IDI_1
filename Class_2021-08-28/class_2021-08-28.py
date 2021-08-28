# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 08:20:10 2021

@author: Alejandro Hernandez
"""
import pandas as pd

#Jalar la información de un archivo
df = pd.read_excel('datosPE.xlsx', sheet_name = 'Hoja1')

# - El vector de IMC
series_IMC = (df['Peso']/df['Estatura']**2)
df_IMC = pd.concat([df['ID Persona'], series_IMC], axis=1)

# - La media de los pesos y la media de las estaturas
media_pesos = df['Peso'].mean()
media_estatura = df['Estatura'].mean()

# - El ID de la persona de mayor peso, de la persona de menor estatura
mayor_peso = df[df['Peso'] == max(df['Peso'])]['ID Persona']
menor_estatura = df[df['Estatura'] == min(df['Estatura'])]['ID Persona']

# - El vector de los ID de las personas con IMC>=28
IMC_mayor_o_igual_28 = df_IMC[df_IMC[0] >= 28]['ID Persona']
# Todos los resultados se ponen en una variable y se imprimen.
print(f"Vector IMC: \n{df_IMC}")
print(f"Media de los pesos: {media_pesos}")
print(f"Media de las estaturas: {media_estatura}")
print(f"Id Persona Mayor Peso: {mayor_peso}")
print(f"Id Persona Menor Estatura: {menor_estatura}")
print(f"Id personas IMC Mayor o Igual a 28: {IMC_mayor_o_igual_28}")
