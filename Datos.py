import matplotlib.pyplot as plt
class Datos:

    def origen(archivo):
        registros = open(archivo, 'r')
        cont = registros.read()
        registros.close()

        lista = cont.split("\n")
        new_list = []

        for registro in lista[1:]:
            dicc_personas = {}

            partes = registro.split(",")

            dicc_personas["Correo"] = partes[0]
            dicc_personas["Usuario"] = partes[1]
            dicc_personas["Contra"] = partes[2]
            dicc_personas["Nombre"] = partes[3]
            dicc_personas["Apellido"] = partes[4]
            dicc_personas["ID"] = partes[5]
            dicc_personas["puntE"] = partes[6]
            dicc_personas["Tokens"] = partes[7]
            dicc_personas["Grado"] = partes[8]

            new_list.append(dicc_personas)

        return new_list

    def ingreso(personas, correo, contra):
        verificar = False
        for user in personas:
            if user['Correo'] == correo and user['Contra'] == contra:
                verificar = True
        return verificar

    def insert(personas, correo, usuario, contra, nombre, apellido, ide, grado, df):
        verificar = False
        # ---Pandas--
        df.loc[correo] = [usuario, 0, 0, 0, 0]
        df.to_csv('ESTADISTICAS.csv')
        # ---FinPandas---
        for user in personas:
            if user['Correo'] == correo:
                verificar = True
        if verificar == True:
            print('El correo ingresado correo ya existe')
        else:
            valorAgregado = {"Correo": correo, "Usuario": usuario, "Contra": contra, "Nombre": nombre,
                             "Apellido": apellido, "ID": ide, "puntE": '0', "Tokens": '0', "Grado": grado}
            personas.append(valorAgregado)
        return verificar

    def save(archivo, personas):
        cont = "Correo,Usuario,Contra,Nombre,Apellido,ID,puntE,Tokens,Grado"
        for user in personas:
            cont = cont + "\n" + str(user["Correo"]) + "," + str(user["Usuario"]) + "," + str(
                user["Contra"]) + "," + str(user["Nombre"]) + "," + str(user["Apellido"]) + "," + str(
                user["ID"]) + "," + str(user["puntE"]) + "," + str(user["Tokens"]) + "," + str(user["Grado"])

        registros = open(archivo, 'w')
        registros.write(cont)
        registros.close()

    def update(personas, correo, contra, nCorreo, nUsuario, nContra, nNombre, nApellido, nGrado):
        verificar = False  # Hasta no var la user, no creer.
        for user in personas:
            if user["Correo"] == correo and user["Contra"] == contra:
                existia = True
                user["Correo"] = nCorreo
                user["Usuario"] = nUsuario
                user["Contra"] = nContra
                user["Nombre"] = nNombre
                user["Apellido"] = nApellido
                user["Grado"] = nGrado

        resul = 0
        if (verificar == False):
            resul = -1
        else:
            resul = 1

        return resul

    def PenT(personas, correo, df):
        cont = int(df.loc[[correo], 'No.veces de puntos canjeados'])
        cont = cont + 1
        df.loc[[correo], 'No.veces de puntos canjeados'] = cont
        df.to_csv('ESTADISTICAS.csv')
        for user in personas:
            if user['Correo'] == correo:
                Conversion = 100
                puntosT = 0.0
                puntosTk = float(user['Tokens'])
                puntosT = puntosTk / Conversion
                print('Tiene ', puntosT, ' puntos en forma de tokens')
                op = input(' ¿desea canjearlos?')
                if op == 'si':
                    pA = float(user['puntE'])
                    nPuntos = pA + puntosT
                    user['puntE'] = nPuntos
                    user['Tokens'] = 0
                    print('Sus puntos totales son de: ', nPuntos)
                    print('Sus tokens actuales son de: ' + str(user['Tokens']))

class Estadisticas:
    def media(df):
        mediaA = df['puntE'].mean()
        print('la media de todos los puntos extras obtenidos es: ', mediaA)

    def contar(df):
        indices = len(df.index.tolist())
        print('actualmente hay ', indices, ' usuarios registrados')

    def exUsuario(df, correo):
        try:
            cont = int(df.loc[[correo], 'Examenes hechos'])
            print('el correo: ', correo, ' ha realizado ', cont, ' exámenes')
            contA = int(df.loc[[correo], 'Examenes aprovados'])
            print(' ha aprovado ', contA, ' exámenes')
            contB = int(df.loc[[correo], 'Examenes reprobados'])
            print(' ha reprovado ', contB, ' exámenes')
        except:
            print('El correo ingresado no existe')

    def puntUsuario(df, correo):
        try:
            cont = int(df.loc[[correo], 'No.veces de puntos canjeados'])
            print('el correo: ', correo, ' ha canjeado puntos ', cont, ' veces')
        except:
            print('El correo ingresado no existe')

    def graficaEx(df):
        mejorI = df.sort_values(['Examenes hechos'], ascending=True)
        mejorfixed = mejorI.tail()
        x_axis = mejorfixed['Correo']
        y_axis = mejorfixed['Examenes hechos']
        plt.bar(x_axis, y_axis)
        plt.show()

    def graficaP(df):
        mejorI = df.sort_values(['puntE'], ascending=True)
        mejorfixed = mejorI.tail()
        x_axis = mejorfixed['Nombre']
        y_axis = mejorfixed['puntE']
        plt.bar(x_axis, y_axis)
        plt.show()