# -*- coding: utf-8 -*-
##-----------------------------------------------##
#Operador de datos epectro radiometro#
#Universidad Del Valle#
#Curso de Teledeteccion Espacial#
#Presentado a: Cesar Edwin Garcia#
#Taller N2, Rutina Python#
#Creado por: Ramiro Andrés Bastidas Copete#
# Codigo: 1327989
##-----------------------------------------------##
#Importante para el uso de la rutina#
#Pasos:
#Abrir Prompt#
#Ejecutar el comando: pip install easygui #
#Al terminar de instalar ejecutar el comando: spyder #
#Abrir este codigo y ejecutar#
##-----------------------------------------------##

#librerias importadas#
import os #Operaciones con carpetas, archivos y directorios#
import numpy as np #Operaciones matematicas#
import easygui as eg #Intefaz grafica simple#
import os.path #Uso de rutas#
from os import scandir, getcwd #Escanear y obtener directorios#
from os.path import abspath #I have no idea#
from collections import defaultdict


##-----------------------------------------------##
#Definicion de funciones#
#Nombre de los archivos en la carpeta#
#Crea una lista con las rutas absolutas de cada archivo#
def ruta_ab(ruta = getcwd()):
    return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]

#Encontrar tipo elemento#
def encontrar(cadena,contenido):
    if(cadena.find(contenido) == -1):
        return "false"
    elif(cadena.find(contenido) != -1):
        return "true"
##-----------------------------------------------##
#Funciones de los indices a calcular#
def ndvi (NIR,RED):
    n=((NIR-RED)/(NIR+RED))
    return(n)

def savi (NIR,RED,L):
    s=((NIR-RED)/((NIR+RED+L)*(1+L)))
    return(s)

def evi (NIR,RED,BLUE):
    e=((2.5)*((NIR-RED)/((NIR+6*RED-7.5*BLUE)+1)))
    return(e)

def mcari (NIR,RED,GREEN):
    m=((NIR-RED)-(0.2*(NIR-GREEN))*(NIR/RED))
    return(m)

def gci (REDEDGE,GREEN):
    g=((REDEDGE/GREEN)-1)
    return(g)
    
def psri(RED,BLUE,NIR):
    p=((RED-BLUE)/NIR)
    return(p)

##-----------------------------------------------##
#Interfaz para buscar carpeta de archivos "Seleccionar el archivo sacadade: https://pypi.org/project/easygui/#description"#
nombres_carpeta = eg.diropenbox(msg="Abrir archivos:",
                           title="Control: diropenbox",
                           default='/C:/Users')
  
eg.msgbox(nombres_carpeta, "diropenbox", ok_button="Continuar")
extension = ["*.py","*.pyc","*.txt","*.TRM"]

##-----------------------------------------------##
#Crear una lista con todos los archivos .TRM dentro de la carpeta#
ruta_archivos =ruta_ab (nombres_carpeta)

##-----------------------------------------------##
#Crear una lista con la ruta absoluta del primer elemento#        
list_elemento1=[]
for i in ruta_archivos:
    r = encontrar(i, "AMARILLA")
    if (r == "true"):
        list_elemento1.append(i)

lista_elemento1 = []
clave=[]
valor=[]

#Abrir y re-escribir todos los archivos pertenecientes al elemento1#
for h in  list_elemento1:
    lines = open(h).readlines()
    open(h, 'w').writelines(lines[2:-1])
    registros_elemento1 = open(h).read()
    work= registros_elemento1.split()
    lista_elemento1.append(work)

#Lista de claves y valores de todos los archivos del elemento 1#
for i in lista_elemento1:
    for j in range(0,len(i)):
        if j%2==0:
            clave.append(i[j])
        else:
            valor.append(i[j])

#Diccionario del Elemento1#
aux = defaultdict(list)
for index, item in enumerate(clave):
    aux[item].append(valor[index])
result = {item: indexs for item, indexs in aux.items() if len(indexs) > 1}

##-----------------------------------------------##
#Creacion de bandas para uso de las funciones de los indices#   

##-----------------------------------------------##
#Obteniendo los valores de la banda 1#
valores_banda1=[]
for k in result:
    if(float(k)>=430 and float(k)<=450):
        valores_banda1.append(result[k])

matriz_b1=np.array(valores_banda1)

g1=[]
for i in range(0,matriz_b1.shape[0]):
    for j in range(0,matriz_b1.shape[1]):
        g1.append(float(valores_banda1[i][j]))

      
ULBLUE=np.mean(g1)
print("El valor de la banda UltraAzul es:", ULBLUE)
 
##-----------------------------------------------##
#Obteniendo los valores de la banda 2#
valores_banda2=[]
for k in result:
    if(float(k)>=450 and float(k)<=520):
        valores_banda2.append(result[k])

matriz_b2=np.array(valores_banda2)

g2=[]
for i in range(0,matriz_b2.shape[0]):
    for j in range(0,matriz_b2.shape[1]):
        g2.append(float(valores_banda2[i][j]))

      
BLUE=np.mean(g2)
print("El valor de la banda Azul es:", BLUE)

##-----------------------------------------------##
#Obteniendo los valores de la banda 3#
valores_banda3=[]
for k in result:
    if(float(k)>=540 and float(k)<=570):
        valores_banda3.append(result[k])

matriz_b3=np.array(valores_banda3)

g3=[]
for i in range(0,matriz_b3.shape[0]):
    for j in range(0,matriz_b3.shape[1]):
        g3.append(float(valores_banda3[i][j]))

      
GREEN=np.mean(g3)
print("El valor de la banda Verde es:", GREEN)

##-----------------------------------------------##
#Obteniendo los valores de la banda 4#
valores_banda4=[]
for k in result:
    if(float(k)>=650 and float(k)<=680):
        valores_banda4.append(result[k])

matriz_b4=np.array(valores_banda4)

g4=[]
for i in range(0,matriz_b4.shape[0]):
    for j in range(0,matriz_b4.shape[1]):
        g4.append(float(valores_banda4[i][j]))

      
RED=np.mean(g4)
print("El valor de la banda Roja es:", RED)

##-----------------------------------------------##
#Obteniendo los valores de la banda 5#
valores_banda5=[]
for k in result:
    if(float(k)>=690 and float(k)<=710):
        valores_banda5.append(result[k])

matriz_b5=np.array(valores_banda5)
g5=[]
for i in range(0,matriz_b5.shape[0]):
    for j in range(0,matriz_b5.shape[1]):
        g5.append(float(valores_banda5[i][j]))

      
NIR1=np.mean(g5)
print("El valor de la banda Infraroja es:", NIR1)

##-----------------------------------------------##
valores_banda9=[]
for k in result:
    if(float(k)>=930 and float(k)<=950):
        valores_banda9.append(result[k])

matriz_b9=np.array(valores_banda9)
g9=[]
for i in range(0,matriz_b9.shape[0]):
    for j in range(0,matriz_b9.shape[1]):
        g9.append(float(valores_banda9[i][j]))

      
REDEDGE=np.mean(g9)
print("El valor de la banda Infraroja es:", REDEDGE)

##-----------------------------------------------##
#Calculo de indices para el elemento 1#

indice_ndvi_elemento1=ndvi(NIR1,RED)
print("El valor del NDVI para el elmento1 es:", indice_ndvi_elemento1)

indice_savi_elemento1=savi(NIR1,RED,0.5)
print("El valor del SAVI para el elmento1 es:", indice_savi_elemento1)

indice_evi_elemento1=evi(NIR1,RED,BLUE)
print("El valor del EVI para el elmento1 es:", indice_evi_elemento1)

indice_mcari_elemento1=mcari(NIR1,RED,GREEN)
print("El valor de MCARI para el elmento1 es:",indice_mcari_elemento1)

indice_gci_elemento1= gci(REDEDGE,GREEN)
print("El valor de GCI para el elmento1 es:",indice_gci_elemento1)

indice_psri_elemento1= psri(RED,BLUE,NIR1)
print("El valor de PSRI para el elmento1 es:",indice_psri_elemento1)









