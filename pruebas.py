from FUNCIONES_PROYECTO import *
import pandas as pd
import matplotlib.pyplot as plt

RegistrosPo = pd.read_csv('GUI/CSV_PROYECTO.csv', encoding= 'windows-1252')
RegistrosP = RegistrosPo.set_index("Correo")
estad_o = pd.read_csv('GUI/ESTADISTICAS.csv', encoding = 'windows-1252')
estad = estad_o.set_index('Correo')
email = 'jskenpo2002@gmail.com'

variable = email in RegistrosPo.Correo.values
contraE = str(RegistrosP.loc[email]['Contra'])

print(contraE)
