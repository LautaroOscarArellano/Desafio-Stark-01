
from data import *
flag_salida=True

def mostrar_menu():
    print("""
    *** Menu de opciones *** 
    A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
    B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F

    C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
    D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
    E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género Mx
    F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
    G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
    H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
    I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)

    J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con No Tiene).

    M. Listar todos los superhéroes agrupados por color de ojos.
    N. Listar todos los superhéroes agrupados por color de pelo.
    O. Listar todos los superhéroes agrupados por tipo de inteligencia
    Para salir escriba "salir"
    """)
    opcion = input("  ")
    return opcion 



#check 26/4/2023
def copiar_lista_origen(copia:list)->list:
    copia_lista=list()
    for item in copia:
        copia_lista.append(item.copy())
    return copia_lista

def parseo(lista:list , key :str)->None:
    for numerico in lista:
        numerico[key]=float(numerico[key])  

def pasar_mayuscula(lista:list , key: str)->None:
    for color in lista:
        color[key]=color[key].capitalize()


flag_salida=True
flag_masculino_alto=False
flag_femenino_alto=False
flag_masculino_bajo=False
flag_femenino_bajo=False
flag_promedio_masculino=False
flag_promedio_femenino=False




#   A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
#   B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M   
def buscar_datos(lista:list ,key:str , valor:str)->list:
    lista_hombres=list()
    for elemento in lista:
        if(elemento[key]==valor):
            lista_hombres.append(elemento)
    return lista_hombres

def filtrar_por_nombre (lista:list , key :str)->list:
    lista_filtrada=list()
    for nombre in lista:
        lista_filtrada.append(nombre[key])
    return lista_filtrada
    

#filtrar por xxx
def filtrar_por_altura(lista:list , key_nombre:str ,key_altura:float,palanca:bool)->str:
    mas_alto=lista[0]
    for altura in lista:
        if(palanca):
            if(mas_alto[key_altura]<altura[key_altura]):
                mas_alto=altura
        elif(mas_alto[key_altura]>altura[key_altura]):
                mas_alto=altura
        
    return mas_alto[key_nombre]

def sacar_promedio(lista:list , key_altura)->float:
    sumatoria=0
    contador=0
    for elemento in lista:
        sumatoria+=elemento[key_altura]
        contador+=1
    promedio=sumatoria / contador
    return promedio
    

#muestra la lista de datos
def mostrar_datos(lista:list)->None:
        for elemento in lista:
            print(elemento)

def mostrar(a:str,b:str,c:str,d:str,e:float,f:float)->None:
    print(f"""Tabla de valores
            superhéroe más alto de género M {a}
            superhéroe más alto de género F {b}                                       
            superhéroe más bajo de género M {c}
            superhéroe más bajo de género F {d}
            altura promedio de los superhéroes de género M {e:0.2f}
            altura promedio de los superhéroes de género F {f:0.2f}
            """)
def indicadores(a,b,c,d,e,f):
    print(f"""Tabla de valore
            superhéroe más alto de género M {a}
            superhéroe más alto de género F {b}                                       
            superhéroe más bajo de género M {c}
            superhéroe más bajo de género F {d}
            altura promedio de los superhéroes de género M {e:0.2f}
            altura promedio de los superhéroes de género F {f:0.2f}
            """)


#J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
def color_ojos(lista_heroes:list,key_color_ojos:str)->None:
    colores=[]
    for heroe in lista_heroes:
        if not esta_en_lista(colores , heroe[key_color_ojos]):
            colores.append(heroe[key_color_ojos])

    for elemento in colores:
        i=0
        print("\Cantidad color de ojos " , elemento )
        for nombre in lista_heroes:
            if(nombre[key_color_ojos]==elemento):
                i+=1
        print(f"cantidad de heroes que tienen ese pelo : {i}")
#K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
def color_pelos(lista_heroes:list,key_color_pelo:str)->None:
    color_pelos=[]
    for heroe in lista_heroes:
        if not esta_en_lista(color_pelos , heroe[key_color_pelo]):
            color_pelos.append(heroe[key_color_pelo])

    for elemento in color_pelos:
        i=0
        print("\Cantidad color de pelo " , elemento)
        for nombre in lista_heroes:
            if(nombre[key_color_pelo]==elemento):
                i+=1
        print(f"{i} ")

#L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con No Tiene).
def tipo_inteligencia(lista_heroes:list,key_tipo_inteligecia:str)->None:
    lista_inteligencia=[]
    for heroe in lista_heroes:
        if not esta_en_lista(lista_inteligencia , heroe[key_tipo_inteligecia]):
            lista_inteligencia.append(heroe[key_tipo_inteligecia])

    #print(lista_inteligencia, "<<<<<<<<<<")
    for elemento in lista_inteligencia:
        i=0
        print(f"\n--------------\n\Cantidad tipo Inteligencia {elemento} \n--------------")
        for nombre in lista_heroes:
            if(nombre[key_tipo_inteligecia]==""):
                print(f"No tiene")
            elif(nombre[key_tipo_inteligecia]==elemento):
                i+=1
        print(f"{i}")

#M. Listar todos los superhéroes agrupados por color de ojos.
def agruacion_ojos(lista_heroes : list , key_color_ojos:str , key_nombre:str)->None:
    lista_color_ojos=[]
    for heroe in lista_heroes:
        if not esta_en_lista(lista_color_ojos , heroe[key_color_ojos]):
            lista_color_ojos.append(heroe[key_color_ojos])

    #print(lista_inteligencia, "<<<<<<<<<<")
    for elemento in lista_color_ojos:
        print(f"\n--------------\nLista de heroes agrupados por color de Ojo {elemento}\n--------------")
        for nombre in lista_heroes:
            if(nombre[key_color_ojos]==elemento):
                print(f"{nombre[key_nombre]} ")

#N. Listar todos los superhéroes agrupados por color de pelo.
def mostar_agrupados_por_color_pelo(lista : list , key_color_pelo:str , key_nombre:str)->None:
    agrupacion_color_pelo=[]
    for heroe in lista:
        if not esta_en_lista(agrupacion_color_pelo , heroe[key_color_pelo]):
            agrupacion_color_pelo.append(heroe[key_color_pelo])

    #print(lista_inteligencia, "<<<<<<<<<<")
    for elemento in agrupacion_color_pelo:
        print(f"\n--------------\nLista de heroes agrupados por color de Ojo {elemento}\n--------------")
        for nombre in lista:
            if(nombre[key_color_pelo]==elemento):
                print(f"{nombre[key_nombre]} ")

#O. Listar todos los superhéroes agrupados por tipo de inteligencia
def mostar_agrupados_por_inteligencia(lista : list , key_inteligencia:str , key_nombre:str)->None:
    agrupacion_color_pelo=[]
    for heroe in lista:
        if not esta_en_lista(agrupacion_color_pelo , heroe[key_inteligencia]):
            agrupacion_color_pelo.append(heroe[key_inteligencia])

    #print(lista_inteligencia, "<<<<<<<<<<")
    for elemento in agrupacion_color_pelo:
        print(f"\n--------------\nLista de heroes agrupados  por tipo de inteligencia {elemento}\n--------------")
        for nombre in lista:
            if(nombre[key_inteligencia]==elemento):
                print(f"{nombre[key_nombre]} ")


#sub funcion de la de arriba
def esta_en_lista (lista:list , color_ojos:str)->list:
    esta=False
    for elemento in lista:
        if(elemento == color_ojos):
            esta=True
            break
    return esta
            








