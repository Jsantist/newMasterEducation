import pandas as pd
import matplotlib.pyplot as plt


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
        dicc_personas["Estado"] = partes[9]
        
        
        new_list.append(dicc_personas)

    return new_list

def select(personas,correo):
    for user in personas:
        if user['Correo']==correo:
            print('Sus datos son : ')
            print('correo: '+user['Correo'])
            print('Usuario: '+user['Usuario'])
            print('Contraseña: '+user['Contra'])
            print('Su nombre: '+user['Nombre'])
            print('Sus apellidos: '+user['Apellido'])
            print('No. carnet: '+user['ID'])
            print('Puntos extras acumulados: '+str(user['puntE']))
            print('Tokens obtenidos: '+str(user['Tokens']))
            print('Grado actualmente cursando : '+user['Grado'])
            print('Usted tiene el estado de:'+user['Estado'] )
            
            
def ingreso(personas,correo,contra):
    verificar=False
    for user in personas:
        if user['Correo']==correo and user['Contra']==contra:
            verificar=True
    return verificar

def insert(personas,correo,usuario,contra,nombre,apellido,ide,grado,estado,df):
    verificar=False
    #---Pandas--
    df.loc[correo]=[usuario,0,0,0,0]
    df.to_csv('ESTADISTICAS.csv')
    #---FinPandas---
    for user in personas:
        if user['Correo']==correo :
            verificar=True
    if verificar==True:
        print('El correo ingresado correo ya existe')
    else:
        valorAgregado = {"Correo" : correo, "Usuario" : usuario, "Contra" : contra, "Nombre" : nombre, "Apellido" :apellido , "ID":ide,"puntE":'0',"Tokens":'0',"Grado":grado,"Estado":estado}
        personas.append(valorAgregado)
    return verificar


def Mate(personas,correo,df):
    cont=int(df.loc[[correo],'Examenes hechos'])
    cont= cont +1
    df.loc[[correo],'Examenes hechos']=cont
    df.to_csv('ESTADISTICAS.csv')
    print('-----------MATEMÁTICAS----------')
    print('Cada respuesta correcta vale 5 tokens, haciendo un total de 25 tokens por examen')
    p1=0
    p2=0
    p3=0
    p4=0
    p5=0
    tk=0
    
    
    p1=int(input('Cuánto es 1 + 1? '))
    if p1==2:
        tk=tk+1
        
    p2=int(input('Cuánto es 5 + 5? '))
    if p2==10:
        tk=tk+1
        
    p3=int(input('Cuánto es 3 + 1? '))
    if p3==4:
        tk=tk+1
        
    p4=int(input('Cuánto es 5 + 1? '))
    if p4==6:
        tk=tk+1
        
    p5=int(input('Cuánto es 2 * 3? '))
    if p5==6:
        tk=tk+1
    print('su puntuaje total fue de: \n',tk,'/5')
    if tk>=3:
        print('Usted ha aprobado el exámen')
        cont=int(df.loc[[correo],'Examenes aprovados'])
        cont= cont +1
        df.loc[[correo],'Examenes aprovados']=cont
        df.to_csv('ESTADISTICAS.csv')
    else:
        print('Usted ha reporbado el exámen')
        cont=int(df.loc[[correo],'Examenes reprobados'])
        cont= cont +1
        df.loc[[correo],'Examenes reprobados']=cont
        df.to_csv('ESTADISTICAS.csv')
    tO=tk*5 
    
    for user in personas:
        if user['Correo']==correo :
            vA= int(user['Tokens'])
            print('Tokens actuales: ', vA)
            print('Sus tokens obtenidos fueron: ',tO)
            nV = vA + tO
            print('Su nuevo puntuaje de tokens es de: ', nV)
            
            user['Tokens']=str(nV)
            
            
def Lenguaje(personas,correo,df):
    cont=int(df.loc[[correo],'Examenes hechos'])
    cont= cont +1
    df.loc[[correo],'Examenes hechos']=cont
    df.to_csv('ESTADISTICAS.csv')
    print('-----------LENGUAJE----------')
    print('Cada respuesta correcta vale 5 tokens, haciendo un total de 25 tokens por examen')
    p1=0
    p2=0
    p3=0
    p4=0
    p5=0
    tk=0
    
    
    p1=int(input('Seleccione la opción que sea sinonimo de la palabra TENER '))
    print("1. Presentar")
    print("2. Poseer")
    print("3. Seleccionar/n")
    if p1==2:
        tk=tk+1
        
    p2=int(input('En la oración: "Sofia lee un libro de cuentos" cual es el sujeto'))
    print("1. cuentos")
    print("2. lee")
    print("3. sofia/n")
    if p2==3:
        tk=tk+1
        
    p3=int(input('En la oración: "El chofer maneja rápido" cual es el verbo '))
    print("1. Chofer")
    print("2. El chofer")
    print("3. Maneja/n")
    if p3==3:
        tk=tk+1
        
    p4=int(input('Cual es el antonimo de blanco'))
    print("1. claro")
    print("2. Negro")
    print("3. Oscuro/n")
    if p4==2:
        tk=tk+1
        
    p5=int(input('De estas palabras "comer, correr, casa, agua, beber" cuantas son verbos '))
    if p5==3:
        tk=tk+1
    print('su puntuaje total fue de: \n',tk,'/5')
    if tk>=3:
        print('Usted ha aprobado el exámen')
        cont=int(df.loc[[correo],'Examenes aprovados'])
        cont= cont +1
        df.loc[[correo],'Examenes aprovados']=cont
        df.to_csv('ESTADISTICAS.csv')
    else:
        print('Usted ha reporbado el exámen')
        cont=int(df.loc[[correo],'Examenes reprobados'])
        cont= cont +1
        df.loc[[correo],'Examenes reprobados']=cont
        df.to_csv('ESTADISTICAS.csv')
    tO=tk*5 
    
    for user in personas:
        if user['Correo']==correo :
            vA= int(user['Tokens'])
            print('Tokens actuales: ', vA)
            print('Sus tokens obtenidos fueron: ',tO)
            nV = vA + tO
            print('Su nuevo puntuaje de tokens es de: ', nV)
            
            user['Tokens']=str(nV)
    
def Ingles (personas,correo,df):
    cont=int(df.loc[[correo],'Examenes hechos'])
    cont= cont +1
    df.loc[[correo],'Examenes hechos']=cont
    df.to_csv('ESTADISTICAS.csv')
    print('-----------INGLES----------')
    print('Cada respuesta correcta vale 5 tokens, haciendo un total de 25 tokens por examen')
    p1=0
    p2=0
    p3=0
    p4=0
    p5=0
    tk=0
    
    
    p1=int(input('You can climb it. Sometimes you can see snow on the top of it '))
    print("1. waterfall")
    print("2. mountain")
    print("3. cave/n")
    if p1==2:
        tk=tk+1
        
    p2=int(input('It´s sometimes under the ground. It´s dark inside it.'))
    print("1. cave")
    print("2. island")
    print("3. jungle/n")
    if p2==1:
        tk=tk+1
        
    p3=int(input('it´s very hot here and it rains every day '))
    print("1. island")
    print("2. waterfall")
    print("3. jungle/n")
    if p3==3:
        tk=tk+1
        
    p4=int(input('Its´s a place with sea all around it'))
    print("1. mountain")
    print("2. island")
    print("3. waterfall/n")
    if p4==2:
        tk=tk+1
        
    p5=int(input('It can be very loud. It´s a place where water from a river comes down quickly over rocks or into a lake. '))
    print("1. jungle")
    print("2. cave")
    print("3. waterfall/n")
    if p5==3:
        tk=tk+1
    print('su puntuaje total fue de: \n',tk,'/5')
    if tk>=3:
        print('Usted ha aprobado el exámen')
        cont=int(df.loc[[correo],'Examenes aprovados'])
        cont= cont +1
        df.loc[[correo],'Examenes aprovados']=cont
        df.to_csv('ESTADISTICAS.csv')
    else:
        print('Usted ha reporbado el exámen')
        cont=int(df.loc[[correo],'Examenes reprobados'])
        cont= cont +1
        df.loc[[correo],'Examenes reprobados']=cont
        df.to_csv('ESTADISTICAS.csv')
    tO=tk*5 
    
    for user in personas:
        if user['Correo']==correo :
            vA= int(user['Tokens'])
            print('Tokens actuales: ', vA)
            print('Sus tokens obtenidos fueron: ',tO)
            nV = vA + tO
            print('Su nuevo puntuaje de tokens es de: ', nV)
            
            user['Tokens']=str(nV)
            
def sociales(personas,correo,df):
    cont=int(df.loc[[correo],'Examenes hechos'])
    cont= cont +1
    df.loc[[correo],'Examenes hechos']=cont
    df.to_csv('ESTADISTICAS.csv')
    print('-----------SOCIALES----------')
    print('Cada respuesta correcta vale 5 tokens, haciendo un total de 25 tokens por examen')
    p1=0
    p2=0
    p3=0
    p4=0
    p5=0
    tk=0
    
    
    p1=int(input('el _____ de septiembre se celebra la independencia de Guatemala'))
    if p1==15:
        tk=tk+1
        
    p2=int(input('Quién conquistó américa?.'))
    print("1. Leo Messi")
    print("2. Cristobal Colón")
    print("3. Giamattei/n")
    if p2==2:
        tk=tk+1
        
    p3=int(input('Sociales es la formación _______'))
    print("1. cultural")
    print("2. personal")
    print("3. Ciudadana/n")
    if p3==3:
        tk=tk+1
        
    p4=int(input('Quién ya no pertenece a Guatemala'))
    print("1. Petén")
    print("2. Belice")
    print("3. Izabal/n")
    if p4==2:
        tk=tk+1
        
    p5=int(input('Que mito se ha descubierto sobre un supuesto guerrero'))
    print("1. El Quetzal")
    print("2. Conquista")
    print("3. Tecún Human/n")
    if p5==3:
        tk=tk+1
    print('su puntuaje total fue de: \n',tk,'/5')
    if tk>=3:
        print('Usted ha aprobado el exámen')
        cont=int(df.loc[[correo],'Examenes aprovados'])
        cont= cont +1
        df.loc[[correo],'Examenes aprovados']=cont
        df.to_csv('ESTADISTICAS.csv')
    else:
        print('Usted ha reporbado el exámen')
        cont=int(df.loc[[correo],'Examenes reprobados'])
        cont= cont +1
        df.loc[[correo],'Examenes reprobados']=cont
        df.to_csv('ESTADISTICAS.csv')
    tO=tk*5 
    
    for user in personas:
        if user['Correo']==correo :
            vA= int(user['Tokens'])
            print('Tokens actuales: ', vA)
            print('Sus tokens obtenidos fueron: ',tO)
            nV = vA + tO
            print('Su nuevo puntuaje de tokens es de: ', nV)
            
            user['Tokens']=str(nV)
            
            
def Artes(personas,correo,df):
    cont=int(df.loc[[correo],'Examenes hechos'])
    cont= cont +1
    df.loc[[correo],'Examenes hechos']=cont
    df.to_csv('ESTADISTICAS.csv')
    print('-----------ARTES----------')
    print('Cada respuesta correcta vale 5 tokens, haciendo un total de 25 tokens por examen')
    p1=0
    p2=0
    p3=0
    p4=0
    p5=0
    tk=0
    
    
    p1=int(input('Cuantos años tardó Leonardo da Vinci en pintar la mona lisa'))
    if p1==4:
        tk=tk+1
        
    p2=int(input('Quién de estos fue un artista muy enfermo'))
    print("1. picasso")
    print("2. Beethoven")
    print("3. Frida Kahlo/n")
    if p2==2:
        tk=tk+1
        
    p3=int(input('. ¿cómo es conocidad la mujer de ‘La joven de la perla’ de Johannes Vermeer?'))
    print("1. cultural")
    print("2. reina")
    print("3. Mona Lisa Holandesa/n")
    if p3==3:
        tk=tk+1
        
    p4=int(input('la pintura más cara que se ha vendido en la historia'))
    print("1. Interchange de Willem de Kooning")
    print("2. La mona lisa")
    print("3. El grito/n")
    if p4==2:
        tk=tk+1
        
    p5=int(input('La losa de mármol que utilizó Miguel Ángel para crear el famoso ‘David’ es ______'))
    print("1. Protegida")
    print("2. Original")
    print("3. Reciclada/n")
    if p5==3:
        tk=tk+1
    print('su puntuaje total fue de: \n',tk,'/5')
    if tk>=3:
        print('Usted ha aprobado el exámen')
        cont=int(df.loc[[correo],'Examenes aprovados'])
        cont= cont +1
        df.loc[[correo],'Examenes aprovados']=cont
        df.to_csv('ESTADISTICAS.csv')
    else:
        print('Usted ha reporbado el exámen')
        cont=int(df.loc[[correo],'Examenes reprobados'])
        cont= cont +1
        df.loc[[correo],'Examenes reprobados']=cont
        df.to_csv('ESTADISTICAS.csv')
    tO=tk*5
    vA = int(dfr.loc[[correo], 'Tokens'])
    print('Tokens actuales: ', vA)
    print('Sus tokens obtenidos fueron: ', tO)
    nV = vA + tO
    print('Su nuevo puntuaje de tokens es de: ', nV)
    dfr.loc[[correo], 'Tokens'] = str(nV)
    dfr.to_csv('CSV_PROYECTO.csv')
    
    

def obTok(personas,correo,df):
    
    cont=int(df.loc[[correo],'Examenes hechos'])
    cont= cont +1
    df.loc[[correo],'Examenes hechos']=cont
    df.to_csv('ESTADISTICAS.csv')
    RealizarExamen = True
    while RealizarExamen == True :
        print('-----------EXAMEN POR ASIGNATURA----------')
        print('1. Matemática')
        print('2. Lenguaje')
        print('3. Ingles')
        print('4. Sociales')
        print('5. Artes')
        print('6. Salir')
        opcion = int(input("Ingrese su opción: "))
        if opcion == 1:
            Mate(personas,correo,df)
        if opcion == 2:
            Lenguaje(personas,correo,df)
        if opcion == 3:
            Ingles(personas,correo,df)
        if opcion == 4:
            sociales(personas,correo,df)
        if opcion == 5:
            Artes(personas,correo,df)
        if opcion == 6:
            RealizarExamen = False
            
            
        

        
            
def save(archivo, personas):
    cont = "Correo,Usuario,Contra,Nombre,Apellido,ID,puntE,Tokens,Grado,Estado"
    for user in personas:
        cont = cont + "\n" + str(user["Correo"]) + "," + str(user["Usuario"]) + "," + str(user["Contra"]) + "," + str(user["Nombre"]) + "," + str(user["Apellido"]) + "," + str(user["ID"]) + "," + str(user["puntE"]) + "," + str(user["Tokens"]) + "," + str(user["Grado"]) + "," + str(user["Estado"])
    
    registros = open(archivo, 'w')
    registros.write(cont)
    registros.close()
    
def update(personas, correo, contra, nCorreo, nUsuario, nContra, nNombre, nApellido, nGrado):
    verificar = False #Hasta no var la user, no creer.
    for user in personas:
        if user["Correo"] == correo and user["Contra"] == contra : 
            existia = True
            user["Correo"]=nCorreo
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
    cont=int(df.loc[[correo],'No.veces de puntos canjeados'])
    cont= cont +1
    df.loc[[correo],'No.veces de puntos canjeados']=cont
    df.to_csv('ESTADISTICAS.csv')
    for user in personas:
        if user['Correo']==correo :
            Conversion=100
            puntosT=0.0
            puntosTk= float(user['Tokens'])
            puntosT = puntosTk/Conversion
            print('Tiene ', puntosT,' puntos en forma de tokens')
            op=input(' ¿desea canjearlos?')
            if op == 'si':
                pA=float(user['puntE'])
                nPuntos= pA + puntosT
                user['puntE']=nPuntos
                user['Tokens']=0
                print('Sus puntos totales son de: ',nPuntos)
                print('Sus tokens actuales son de: '+str(user['Tokens']))

def media(df):
    mediaA=df['puntE'].mean()
    print('la media de todos los puntos extras obtenidos es: ', mediaA)
def contar(df):
    indices=len(df.index.tolist())
    print('actualmente hay ',indices,' usuarios registrados')
def exUsuario(df,correo):
    try:
        cont=int(df.loc[[correo],'Examenes hechos'])
        print('el correo: ',correo,' ha realizado ',cont,' exámenes')
        contA=int(df.loc[[correo],'Examenes aprovados'])
        print(' ha aprovado ',contA,' exámenes')
        contB=int(df.loc[[correo],'Examenes reprobados'])
        print(' ha reprovado ',contB,' exámenes')
    except:
        print('El correo ingresado no existe')
def puntUsuario(df,correo):
    try:
        cont=int(df.loc[[correo],'No.veces de puntos canjeados'])
        print('el correo: ',correo,' ha canjeado puntos ',cont,' veces')
    except:
        print('El correo ingresado no existe')
def graficaEx(df):
    mejorI=df.sort_values(['Examenes hechos'], ascending = True)
    mejorfixed=mejorI.tail()
    x_axis=mejorfixed['Correo']
    y_axis=mejorfixed['Examenes hechos']
    plt.bar(x_axis,y_axis)
    plt.show()
def graficaP(df):
    mejorI=df.sort_values(['puntE'], ascending = True)
    mejorfixed=mejorI.tail()
    x_axis=mejorfixed['Nombre']
    y_axis=mejorfixed['puntE']
    plt.bar(x_axis,y_axis)
    plt.show()
    

    
    
            
            