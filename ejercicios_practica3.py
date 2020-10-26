#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


def ej1():
    # Ejercicios de práctica numérica

    # Comparadores
    # Ingrese dos números cualesquiera y realice las sigueintes
    # comparaciones entre ellos
    
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))



    # Compare cual de los dos números es mayor
    # Imprima en pantalla según corresponda
    if 9 > 12:
        print('9=', 9, 'es mayor a 12=', 12)
    else:
        print('12=', 12, 'es mayor a 9=', 9) 

    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso
    if 9 > 0:
        print('9 es positivo')
    elif 9 < 0:
        print('9 es negativo')
    else:
        print('9 es 0')
    # Verifique si el numero_1 es mayor a 0 y menor a 100
    # Imprima en pantalla si se cumple o no la condición
    if 9 > 0:
        print('9=', 9, 'es mayor a 0=', 0)
    if 9 < 100:
        print('9=', 9, 'es menor a 100=', 100)

        
    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2
    # Imprima en pantalla si se cumple o no la condición
    if (numero_1 < 10) or (numero_2 < -2):
        print('se cumple una condicion al menos')
    else: 
        print('no cumple ninguna condicion')




def ej2():
    # Ejemplos variables de texto

    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas
    texto_1 = str(input('Ingrese la primera palabra:\n'))

    texto_2 = str(input('Ingrese la segunda palabra:\n'))

    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda
    if (texto_1 > texto_2):
        print('texto_1 es mayor a texto_2')
    else:
        print('texto_2 no es mayor a texto_1')

    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda
    if len(texto_1) > len(texto_2): 
        print('texto_1 tiene mayor cantidad de letras que el texto_2')
    else:
        print('texto_2 no tiene mayor cantidad de letras que el texto_1')
    

    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda
    if (texto_1[0] > texto_2[0]):
        print('la primera letra de primera palabra es mayor a primer letra de segunda palabra')

    copia_texto_1 = texto_1  # Copia de la variable texto_1

    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda

    if copia_texto_1 == texto_1:
        print('copia_texto_1 es igual a texto_1')
    else:
        print('copia_texto_1 es diferente a texto_1')

    
    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda

    if (copia_texto_1 != texto_2):
        print('la copia_texto_1 es distinta a texto_2')
    else:
        print('la copia_texto_1 es igual a texto_2')


def ej3():
    # Ejercicios de práctica numérica

    # Condicionales anidados
    numero_1 = 7
    numero_2 = -2

    # Verifique si el numero_1 es mayor a 5
    #   --> En caso afirmativo, verifique si el numero_2
    #       es positivo
    #       --> En caso afirmativo imprima en pantalla "Resp=1"
    #       --> En caso negativo imprima en pantalla   "Resp=2"
    #  --> En caso negativo (numero_1 no es mayor a 5)
    #      verifique si el numero_2 es mayor a 5
    #       --> En caso afirmativo imprima en pantalla "Resp=3"
    #       --> En caso negativo imprima en pantalla "Resp=4"
    if (numero_1 > 5):
        if (numero_2 > 0):
            print('Resp=1')
    else:
            print('Resp=2')
    if (numero_2 > 5):
            print('Resp=3')
    else:
            print('Resp=4')

    

    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    puntaje = 70

    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F

    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados


def ej4():
    # Ejemplos variables de texto

    texto_1 = '5'
    texto_2 = '7'

    # Verifique cual cual de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda

    if len(texto_1) > len(texto_2)
        print('texto_1 es mayor a texto_2')
        

    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)
    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda

    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    #ej4()
