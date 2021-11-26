import matplotlib.pyplot as plt
import pandas
class Archivos:

    def ingreso(self, dfr1, dfr, correo, contra):
        verificar = False
        verificar2 = False
        exisC = correo in dfr1.Correo.values

        if exisC:
            print("existe el correo")
            contraE = str(dfr.loc[correo]['Contra'])
            print(contraE)
            if contraE == contra:
                print("contraeñas iguales")
                verificar = True

        if exisC == True & verificar ==  True :
            verificar2 = True

        return verificar2

    def insert(self, correo, usuario, contra, nombre, apellido, ide, grado, estado, dfe, dfr,dfr1):
        verificar = False
        # ---Pandas--
        exisC = correo in dfr1.Correo.values

        if not exisC:
            verificar = True
            try:
                dfe.loc[correo] = [usuario, 0, 0, 0, 0]
                dfe.to_csv('ESTADISTICAS.csv')
            except Exception as e :
                print("error en estadísticas", e)
            try:
                dfr.loc[correo] = [usuario, contra, nombre, apellido, ide, 0, 0, grado, estado]
                dfr.to_csv("CSV_PROYECTO.csv")
            except Exception as e:
                print('Error en agregar nuevo usuario ',e)

        # ---FinPandas---

        return verificar

class Estadisticas:
    def media(self, df):
        mediaA = df['puntE'].mean()
        print('la media de todos los puntos extras obtenidos es: ', mediaA)

    def contar(self,df):
        indices = len(df.index.tolist())
        print('actualmente hay ', indices, ' usuarios registrados')

    def exUsuario(self,df, correo):
        try:
            cont = int(df.loc[[correo], 'Examenes hechos'])
            print('el correo: ', correo, ' ha realizado ', cont, ' exámenes')
            contA = int(df.loc[[correo], 'Examenes aprovados'])
            print(' ha aprovado ', contA, ' exámenes')
            contB = int(df.loc[[correo], 'Examenes reprobados'])
            print(' ha reprovado ', contB, ' exámenes')
        except:
            print('El correo ingresado no existe')

    def puntUsuario(self,df, correo):
        try:
            cont = int(df.loc[[correo], 'No.veces de puntos canjeados'])
            print('el correo: ', correo, ' ha canjeado puntos ', cont, ' veces')
        except:
            print('El correo ingresado no existe')

    def graficaEx(self,df):
        mejorI = df.sort_values(['Examenes hechos'], ascending=True)
        mejorfixed = mejorI.tail()
        x_axis = mejorfixed['Correo']
        y_axis = mejorfixed['Examenes hechos']
        plt.bar(x_axis, y_axis)
        plt.show()

    def graficaP(self,df):
        mejorI = df.sort_values(['puntE'], ascending=True)
        mejorfixed = mejorI.tail()
        x_axis = mejorfixed['Nombre']
        y_axis = mejorfixed['puntE']
        plt.bar(x_axis, y_axis)
        plt.show()

class Examenes:
    def Mate(self, correo, dfe,dfr):
        cont = int(dfe.loc[[correo], 'Examenes hechos'])
        cont = cont + 1
        dfe.loc[[correo], 'Examenes hechos'] = cont
        dfe.to_csv('ESTADISTICAS.csv')
        print('-----------MATEMÁTICAS----------')
        print('Cada respuesta correcta vale 5 tokens, haciendo un total de 25 tokens por examen')
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        p5 = 0
        tk = 0

        p1 = int(input('Cuánto es 1 + 1? '))
        if p1 == 2:
            tk = tk + 1

        p2 = int(input('Cuánto es 5 + 5? '))
        if p2 == 10:
            tk = tk + 1

        p3 = int(input('Cuánto es 3 + 1? '))
        if p3 == 4:
            tk = tk + 1

        p4 = int(input('Cuánto es 5 + 1? '))
        if p4 == 6:
            tk = tk + 1

        p5 = int(input('Cuánto es 2 * 3? '))
        if p5 == 6:
            tk = tk + 1
        print('su puntuaje total fue de: \n', tk, '/5')

        if tk >= 3:
            print('Usted ha aprobado el exámen')
            cont = int(dfe.loc[[correo], 'Examenes aprovados'])
            cont = cont + 1
            dfe.loc[[correo], 'Examenes aprovados'] = cont
            dfe.to_csv('ESTADISTICAS.csv')
        else:
            print('Usted ha reporbado el exámen')
            cont = int(dfe.loc[[correo], 'Examenes reprobados'])
            cont = cont + 1
            dfe.loc[[correo], 'Examenes reprobados'] = cont
            dfe.to_csv('ESTADISTICAS.csv')

        tO = tk * 5
        vA = int(dfr.loc[[correo],'Tokens'])
        print('Tokens actuales: ', vA)
        print('Sus tokens obtenidos fueron: ', tO)
        nV = vA + tO
        print('Su nuevo puntuaje de tokens es de: ', nV)
        dfr.loc[[correo], 'Tokens'] = str(nV)
        dfr.to_csv('CSV_PROYECTO.csv')

    def Lenguaje(self, correo, dfe,dfr):
        cont = int(dfe.loc[[correo], 'Examenes hechos'])
        cont = cont + 1
        dfe.loc[[correo], 'Examenes hechos'] = cont
        dfe.to_csv('ESTADISTICAS.csv')
        print('-----------LENGUAJE----------')
        print('Cada respuesta correcta vale 5 tokens, haciendo un total de 25 tokens por examen')
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        p5 = 0
        tk = 0

        p1 = int(input('Seleccione la opción que sea sinonimo de la palabra TENER '))
        print("1. Presentar")
        print("2. Poseer")
        print("3. Seleccionar/n")
        if p1 == 2:
            tk = tk + 1

        p2 = int(input('En la oración: "Sofia lee un libro de cuentos" cual es el sujeto'))
        print("1. cuentos")
        print("2. lee")
        print("3. sofia/n")
        if p2 == 3:
            tk = tk + 1

        p3 = int(input('En la oración: "El chofer maneja rápido" cual es el verbo '))
        print("1. Chofer")
        print("2. El chofer")
        print("3. Maneja/n")
        if p3 == 3:
            tk = tk + 1

        p4 = int(input('Cual es el antonimo de blanco'))
        print("1. claro")
        print("2. Negro")
        print("3. Oscuro/n")
        if p4 == 2:
            tk = tk + 1

        p5 = int(input('De estas palabras "comer, correr, casa, agua, beber" cuantas son verbos '))
        if p5 == 3:
            tk = tk + 1
        print('su puntuaje total fue de: \n', tk, '/5')
        if tk >= 3:
            print('Usted ha aprobado el exámen')
            cont = int(dfe.loc[[correo], 'Examenes aprovados'])
            cont = cont + 1
            dfe.loc[[correo], 'Examenes aprovados'] = cont
            dfe.to_csv('ESTADISTICAS.csv')
        else:
            print('Usted ha reporbado el exámen')
            cont = int(dfe.loc[[correo], 'Examenes reprobados'])
            cont = cont + 1
            dfe.loc[[correo], 'Examenes reprobados'] = cont
            dfe.to_csv('ESTADISTICAS.csv')
        tO = tk * 5
        vA = int(dfr.loc[[correo], 'Tokens'])
        print('Tokens actuales: ', vA)
        print('Sus tokens obtenidos fueron: ', tO)
        nV = vA + tO
        print('Su nuevo puntuaje de tokens es de: ', nV)
        dfr.loc[[correo], 'Tokens'] = str(nV)
        dfr.to_csv('CSV_PROYECTO.csv')

    def Ingles(self, correo, dfe, dfr):
        cont = int(dfe.loc[[correo], 'Examenes hechos'])
        cont = cont + 1
        dfe.loc[[correo], 'Examenes hechos'] = cont
        dfe.to_csv('ESTADISTICAS.csv')
        print('-----------INGLES----------')
        print('Cada respuesta correcta vale 5 tokens, haciendo un total de 25 tokens por examen')
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        p5 = 0
        tk = 0

        p1 = int(input('You can climb it. Sometimes you can see snow on the top of it '))
        print("1. waterfall")
        print("2. mountain")
        print("3. cave/n")
        if p1 == 2:
            tk = tk + 1

        p2 = int(input('It´s sometimes under the ground. It´s dark inside it.'))
        print("1. cave")
        print("2. island")
        print("3. jungle/n")
        if p2 == 1:
            tk = tk + 1

        p3 = int(input('it´s very hot here and it rains every day '))
        print("1. island")
        print("2. waterfall")
        print("3. jungle/n")
        if p3 == 3:
            tk = tk + 1

        p4 = int(input('Its´s a place with sea all around it'))
        print("1. mountain")
        print("2. island")
        print("3. waterfall/n")
        if p4 == 2:
            tk = tk + 1

        p5 = int(input(
            'It can be very loud. It´s a place where water from a river comes down quickly over rocks or into a lake. '))
        print("1. jungle")
        print("2. cave")
        print("3. waterfall/n")
        if p5 == 3:
            tk = tk + 1
        print('su puntuaje total fue de: \n', tk, '/5')
        if tk >= 3:
            print('Usted ha aprobado el exámen')
            cont = int(dfe.loc[[correo], 'Examenes aprovados'])
            cont = cont + 1
            dfe.loc[[correo], 'Examenes aprovados'] = cont
            dfe.to_csv('ESTADISTICAS.csv')
        else:
            print('Usted ha reporbado el exámen')
            cont = int(dfe.loc[[correo], 'Examenes reprobados'])
            cont = cont + 1
            dfe.loc[[correo], 'Examenes reprobados'] = cont
            dfe.to_csv('ESTADISTICAS.csv')
        tO = tk * 5
        vA = int(dfr.loc[[correo], 'Tokens'])
        print('Tokens actuales: ', vA)
        print('Sus tokens obtenidos fueron: ', tO)
        nV = vA + tO
        print('Su nuevo puntuaje de tokens es de: ', nV)
        dfr.loc[[correo], 'Tokens'] = str(nV)
        dfr.to_csv('CSV_PROYECTO.csv')

    def sociales(self, correo, dfe, dfr):
        cont = int(dfe.loc[[correo], 'Examenes hechos'])
        cont = cont + 1
        dfe.loc[[correo], 'Examenes hechos'] = cont
        dfe.to_csv('ESTADISTICAS.csv')
        print('-----------SOCIALES----------')
        print('Cada respuesta correcta vale 5 tokens, haciendo un total de 25 tokens por examen')
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        p5 = 0
        tk = 0

        p1 = int(input('el _____ de septiembre se celebra la independencia de Guatemala'))
        if p1 == 15:
            tk = tk + 1

        p2 = int(input('Quién conquistó américa?.'))
        print("1. Leo Messi")
        print("2. Cristobal Colón")
        print("3. Giamattei/n")
        if p2 == 2:
            tk = tk + 1

        p3 = int(input('Sociales es la formación _______'))
        print("1. cultural")
        print("2. personal")
        print("3. Ciudadana/n")
        if p3 == 3:
            tk = tk + 1

        p4 = int(input('Quién ya no pertenece a Guatemala'))
        print("1. Petén")
        print("2. Belice")
        print("3. Izabal/n")
        if p4 == 2:
            tk = tk + 1

        p5 = int(input('Que mito se ha descubierto sobre un supuesto guerrero'))
        print("1. El Quetzal")
        print("2. Conquista")
        print("3. Tecún Human/n")
        if p5 == 3:
            tk = tk + 1
        print('su puntuaje total fue de: \n', tk, '/5')
        if tk >= 3:
            print('Usted ha aprobado el exámen')
            cont = int(dfe.loc[[correo], 'Examenes aprovados'])
            cont = cont + 1
            dfe.loc[[correo], 'Examenes aprovados'] = cont
            dfe.to_csv('ESTADISTICAS.csv')
        else:
            print('Usted ha reporbado el exámen')
            cont = int(dfe.loc[[correo], 'Examenes reprobados'])
            cont = cont + 1
            dfe.loc[[correo], 'Examenes reprobados'] = cont
            dfe.to_csv('ESTADISTICAS.csv')
        tO = tk * 5
        vA = int(dfr.loc[[correo], 'Tokens'])
        print('Tokens actuales: ', vA)
        print('Sus tokens obtenidos fueron: ', tO)
        nV = vA + tO
        print('Su nuevo puntuaje de tokens es de: ', nV)
        dfr.loc[[correo], 'Tokens'] = str(nV)
        dfr.to_csv('CSV_PROYECTO.csv')

    def Artes(self, correo, dfe , dfr):
        cont = int(dfe.loc[[correo], 'Examenes hechos'])
        cont = cont + 1
        dfe.loc[[correo], 'Examenes hechos'] = cont
        dfe.to_csv('ESTADISTICAS.csv')
        print('-----------ARTES----------')
        print('Cada respuesta correcta vale 5 tokens, haciendo un total de 25 tokens por examen')
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        p5 = 0
        tk = 0

        p1 = int(input('Cuantos años tardó Leonardo da Vinci en pintar la mona lisa'))
        if p1 == 4:
            tk = tk + 1

        p2 = int(input('Quién de estos fue un artista muy enfermo'))
        print("1. picasso")
        print("2. Beethoven")
        print("3. Frida Kahlo/n")
        if p2 == 2:
            tk = tk + 1

        p3 = int(input('. ¿cómo es conocidad la mujer de ‘La joven de la perla’ de Johannes Vermeer?'))
        print("1. cultural")
        print("2. reina")
        print("3. Mona Lisa Holandesa/n")
        if p3 == 3:
            tk = tk + 1

        p4 = int(input('la pintura más cara que se ha vendido en la historia'))
        print("1. Interchange de Willem de Kooning")
        print("2. La mona lisa")
        print("3. El grito/n")
        if p4 == 2:
            tk = tk + 1

        p5 = int(input('La losa de mármol que utilizó Miguel Ángel para crear el famoso ‘David’ es ______'))
        print("1. Protegida")
        print("2. Original")
        print("3. Reciclada/n")
        if p5 == 3:
            tk = tk + 1
        print('su puntuaje total fue de: \n', tk, '/5')
        if tk >= 3:
            print('Usted ha aprobado el exámen')
            cont = int(dfe.loc[[correo], 'Examenes aprovados'])
            cont = cont + 1
            dfe.loc[[correo], 'Examenes aprovados'] = cont
            dfe.to_csv('ESTADISTICAS.csv')
        else:
            print('Usted ha reporbado el exámen')
            cont = int(dfe.loc[[correo], 'Examenes reprobados'])
            cont = cont + 1
            dfe.loc[[correo], 'Examenes reprobados'] = cont
            dfe.to_csv('ESTADISTICAS.csv')
        tO = tk * 5
        vA = int(dfr.loc[[correo], 'Tokens'])
        print('Tokens actuales: ', vA)
        print('Sus tokens obtenidos fueron: ', tO)
        nV = vA + tO
        print('Su nuevo puntuaje de tokens es de: ', nV)
        dfr.loc[[correo], 'Tokens'] = str(nV)
        dfr.to_csv('CSV_PROYECTO.csv')

    def obTok(self, correo, dfe ,dfr):
        RealizarExamen = True
        while RealizarExamen == True:
            print('-----------EXAMEN POR ASIGNATURA----------')
            print('1. Matemática')
            print('2. Lenguaje')
            print('3. Ingles')
            print('4. Sociales')
            print('5. Artes')
            print('6. Salir')
            opcion = int(input("Ingrese su opción: "))
            if opcion == 1:
                self.Mate(correo, dfe, dfr)
            if opcion == 2:
                self.Lenguaje(correo, dfe, dfr)
            if opcion == 3:
                self.Ingles(correo, dfe, dfr)
            if opcion == 4:
                self.sociales(correo, dfe, dfr)
            if opcion == 5:
                self.Artes(correo, dfe, dfr)
            if opcion == 6:
                RealizarExamen = False
