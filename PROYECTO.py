'''
hola josee
PROTOTIPO DE PROYECTO PROGRAMADO (uso de archivo csv)
Programa principal

hola carlos

'''


from FUNCIONES_PROYECTO import *
import pandas as pd

Registros = origen('CSV_PROYECTO.csv')
RegistrosP=pd.read_csv('CSV_PROYECTO.csv')
estad_o=pd.read_csv('ESTADISTICAS.csv')
estad=estad_o.set_index('Correo')
#variables


finalizar1=True

validar1=False
op1=0
op2=0



while finalizar1:
    print('''-----------BIENVENIDO A MASTER EDUCATION-------------
--------------MENÚ DE INGRESO-----------
SI NO TIENE NINGUNA SESIÓN CREADA, POR FAVOR REGISTRESE

Seleccione una opción:
1. ¿Qué es MASTER EDUCATION?
2. Iniciar sesión
3. Registrarse
4. Estadisticas
5. Salir


''')
    op1=int(input())
    if op1==1:
        print('''
--------------QUÉ ES MASTER EDUCATION---------------

Es una plataforma en la cual se pueda apoyar la enseñanza de los niños
de primero a sexto primaria, mediante una plataforma interactiva que permita
a los tutores o a los estudiantes seleccionar el tema que quieran reforzar.
El programa también cuenta con la implementación de exámenes a los estudiantes,
para evaluar el progreso durante los cursos que llevaron y así mismo llegar a
un promedio establecido para que el estudiante pueda ganar una recompensa.

Las recompensas empleadas en este programa son los tokens, estos se consiguen
mediante la realización de exámenes opcionales. Los tokens son canjeables por
puntos extras para los estudiantes, el factor de conversión es por cada 100
tokens se obtendrá un punto extra. Esto se realiza con el objetivo de dar
oportunidad a los estudiantes de conseguir puntos extra, los cuales pueden
usar a su placer.

---------------------------------------------------
''')
    elif op1== 2:
        correo=input('Por favor ingrese su correo electrónico: ')
        contra=input('Ingrese su contraseña: ')
        validar1=ingreso(Registros,correo,contra)
        if validar1 == True:
            finalizar2=True
            print('Ha ingresado exitosamente ')
            while finalizar2:
                print('''---------------------------
MENÚ DE OPCIONES
------------------------
Seleccione una opción
1. Consultar datos
2. Modificar datos
3. Ganar tokens
4. Canjear tokens
5. Salir a menú principal''')
                op2=int(input())
                
                if op2 == 1 :
                    print('--------------REGISTROS--------------')
                    select(Registros,correo)
                    print('-------------------------------------')
                elif op2 == 2:
                    print('--------------MODIFICACIÓN DE DATOS-----------')
                    ccontra=input('Ingrese su contraseña para modificar datos: ')
                    if contra == ccontra:
                        print('Los puntos extras, la cantidad de tokens y el carnet del estudiante no son modificables \n')
                        nCorreo=input('Ingrese su nuevo coreo : ')
                        nUser=input('Ingrese su nuevo usuario: ')
                        nContra=input('Ingrese su nueva contraseña: ')
                        nNombre=input('Ingrese su nuevo nombre: ')
                        nApellido=input('Ingrese su nuevo apellido: ')
                        nGrado=input('Ingrese su nuevo Grado: ')
                        update(Registros, correo, contra, nCorreo, nUser, nContra, nNombre, nApellido, nGrado)
                        print('-----------------------------------------')
                        print('Datos actualizados, se requiere un nuevo inicio de sesión')
                        save('CSV_PROYECTO.csv',Registros)
                        print('-----------------------------------------')
                        finalizar2=False
                elif op2 == 3:
                    print('-----------TOKENS MATEMÁTICAS-----------')
                    obTok(Registros,correo, estad)
                    guardar=str(input('¿desea guardar su progreso?  '  ))
                    if guardar=='si':
                        save('CSV_PROYECTO.csv',Registros)
                        print('Se a guardado con éxito')
                    print('-----------------------------------------')
                elif op2 == 4:
                    print('-----------CANJEO DE TOKENS--------------')
                    PenT(Registros, correo, estad)
                    guardar=str(input('¿desea guardar su progreso?  '  ))
                    if guardar=='si':
                        save('CSV_PROYECTO.csv',Registros)
                        print('Se a guardado con éxito')
                    print('-----------------------------------------')
                elif op2 == 5:
                    print('Ha salido exitosamente')
                    finalizar2= False
        else:
            print('Su usuario y/o contraseña son incorrectos, por favor intente de nuevo \n\n')
    elif op1 ==3:
        correo=str(input('Ingrese su correo electrónico: '))
        user=str(input('Ingrese su nombre de usuario: '))
        contra=str(input('Ingrese una cotraseña: '))
        cContra=str(input('Confirme su contraseña: '))
        if contra == cContra:
            nombre=str(input('Ingrese su nombre: '))
            apellido=str(input('Ingrese sus apellidos: '))
            carnet=str(input('Ingrese su número de carnet: '))
            grado=str(input('Ingrese el grado que está cursando actualmente '))
            insert(Registros,correo,user,contra,nombre,apellido,carnet,grado,estad)
            save('CSV_PROYECTO.csv',Registros)
        else :
            print('Las contraseñas no coinciden, intente de nuevo')
    elif op1==4:
        finalizar2=True
        while finalizar2:
            print('''--------------ESTDISTICAS-----------
SELECCIONE UNA OPCIÓN
1. Ver media de los puntos extras obtenidos en general
2. Ver cantidad de usuarios registrados
3. Ver exámenes realizados de un alumno específico
4. Ver cuántas veces ha canjeado puntos un alumno especifico
5. Comparar 5 usuarios con más exámenes hechos
6. Comparar 5 usuarios con más puntos extras
7. salir a menú principal

''')
            op2=int(input())
            if op2==1:
                media(RegistrosP)
            elif op2 == 2:
                contar(estad)
            elif op2 == 3:
                correo=input('Ingrese correo a revisar: ')
                exUsuario(estad,correo)
            elif op2== 4:
                correo=input('Ingrese correo a revisar: ')
                puntUsuario(estad,correo)
            elif op2==5:
                graficaEx(estad_o)
            elif op2==6:
                graficaP(RegistrosP)
            elif op2==7:
                print('ha salido exitosamente')
                finalizar2=False
        
    elif op1==5:
        print('ha salido exitoamente')
        finalizar1=False
            
            
                
    

