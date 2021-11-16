from FUNCIONES_PROYECTO import *
import pandas as pd
import matplotlib.pyplot as plt

Registros = origen('CSV_PROYECTO.csv')
RegistrosP=pd.read_csv('CSV_PROYECTO.csv')
estad_o=pd.read_csv('ESTADISTICAS.csv')
estad=estad_o.set_index('Correo')

indices=len(estad.index.tolist())

media=RegistrosP['puntE'].mean()

print(media)
