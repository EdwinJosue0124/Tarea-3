import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

titanic_pdf = pd.read_csv("D:\Documentos\Cursos\Ciencia de datos\Tarea 3\lista_titanic.csv")


#input() lo utilicé para hacer pausas y avanzar cuando se presione el teclado

def limpieza():
    lista_titacnic = pd.read_csv('d:\Ciencia de Datos\EVA_03\Titanic.csv')
    lista_titacnic = lista_titacnic.drop(['Edad','Cabina','Bote de Rescate','Cuerpo', 'Destino'], axis=1)
    lista_titacnic.to_csv('D:\Documentos\Cursos\Ciencia de datos\Tarea 3\lista_titanic.csv')
    print(lista_titacnic, " \n")


def busqueda():
    ticket=str(input('Ingrese el ticket del o los pasajeros: '))
    t_ticket=titanic_pdf['Ticket'] == ticket
    busqueda_ticket=titanic_pdf[t_ticket]
    print(busqueda_ticket, " \n")


def grafica_p():
    estado=titanic_pdf.groupby('Sobrevivió')['Clase'].count()
    print(estado)
    y=np.np.array([estado[0], estado[1]])

    estados=['Cantidad de Muertos', 'Cantidad de Vivos']  

    plt.pie(y, labels= estados, autopct="%0.1f %%", shadow= True)
    plt.legend(title ="Grafica de sobrevivientes del titanic")
    plt.show()


def grafica_b():
    eje_x = ['1','2','3']
    eje_y = titanic_pdf.groupby('Clase')['Sobrevivió'].count()
    print(eje_x)
    print(eje_y)

    y=np.array([eje_y[1],eje_y[2], eje_y[3]])

    plt.bar(eje_x,y)

    plt.ylabel('Cantidad de sobrevivientes')

    plt.xlabel('Clases')

    plt.show()

def costo_ticket():
    tarifa_ticket = titanic_pdf['Tarifa']

    print('Tarifa maxima: ', titanic_pdf.max())
    print('Tarifa minima: ', titanic_pdf.min())


menu="""
1 - Limpieza de datos.
2 - Busqueda de usuarios por ticket.
3 - Grafica de personas fallecidad.
4 - Grafica de personas sobrevivientes por clase.
5 - Saber los costos de los tickers.
6 - Salir
Elige una opcion: """
opcion = input(menu)

if opcion == '1':
    limpieza()
elif opcion == '2':
    busqueda()
elif opcion == '3':
    grafica_p()
elif opcion == '4':
    grafica_b()
elif opcion == '5':
    costo_ticket()
elif opcion == '6':
   exit()
else:
    print('Ingrese una opcion correcta')
    
    os.system("cls") #Limpieza de pantalla
  