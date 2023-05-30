
from data import*
from funciones import *
import os 


flag_c=False
flag_d=False

cargar_lista=copiar_lista_origen(lista_heroes)#raro
parseo(cargar_lista,"altura")
pasar_mayuscula(cargar_lista , "color_ojos") #check



while (flag_salida==True):
    os.system("cls")
    match(mostrar_menu().upper()):

        case "A":
            nombre=buscar_datos(cargar_lista ,"genero","M")
            filtro=filtrar_por_nombre(nombre , "nombre" )
            mostrar_datos(filtro)
            flag_c=True
   

        case "B":
            nombre_f=buscar_datos(cargar_lista ,"genero","F")
            filtro_f=filtrar_por_nombre(nombre_f , "nombre" )
            mostrar_datos(filtro_f)
            flag_d=True

        case "C":
            if(flag_c):
                alto_m=filtrar_por_altura(nombre,"nombre","altura",True)
                print(f"el mas alto m es {alto_m} ")
            else:
                print("No cargaste A ")
        case "D":
            if(flag_d):
                alto_f=filtrar_por_altura(nombre_f,"nombre","altura",True)
                print(f"el mas alto f es {alto_f} ")
            else:
                print("No cargaste B ")

        case "E":
            bajo_m=filtrar_por_altura(nombre,"nombre","altura",False)
            print(f"El mas bajo es {bajo_m}")

        case "F":
            bajo_f=filtrar_por_altura(nombre_f,"nombre","altura",False)
            print(f"El mas bajo es {bajo_f}")

        case "G":
            prom_masculino=sacar_promedio(nombre,"altura")
            print(f" El promdio de los masculinos es {prom_masculino}")

        case "H":
            prom_femenino=sacar_promedio(nombre_f,"altura")
            print(f" El promedio de los femeninos es {prom_femenino}")

        case "I":
            if(flag_c == True):
                mostrar(alto_m,alto_f,bajo_m,bajo_f,prom_masculino,prom_femenino )
            else:
                print("Faltan poner datos ")
        case "J":
            color_ojos(cargar_lista,"color_ojos")
        case "K":
            color_pelos(cargar_lista,"color_pelo")
        case "L":
            tipo_inteligencia(cargar_lista,"inteligencia")
        case "M":
            agruacion_ojos(cargar_lista , "color_ojos" , "nombre")
        case "N":
            mostar_agrupados_por_color_pelo(cargar_lista,"color_pelo","nombre")
        case "O":
            mostar_agrupados_por_inteligencia(cargar_lista ,"inteligencia" ,"nombre")
            

        case "SALIR":
            opcion=input("Esta seguro? s/n :>").lower()
            if(opcion=="s"):
                print("Que tenga un lindo viaje♪♪♪")
                break
        case _:
            print("Opcion innesistente ")
    os.system("pause")    
