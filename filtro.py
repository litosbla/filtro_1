import json
import os
def error(msg):
    print("\t!!!!!! Error: ",msg.upper(),end=" ")
    input("\t @Digite cualquier tecla para continuar")

def leer_nombre(msg):
    while True: # numero de horas 
        try:
            nombre_agregar= input(msg)
            if  nombre_agregar.isalpha():
                return nombre_agregar
            error("Valor invalido")
            continue
        except ValueError:
            error("Valor invalido")
            continue
def leer_id(msg):
    while True: # id
        try:
            id_agregar=int(input(msg))
            if id_agregar>0:
                return id_agregar
                
            error("Valor negativo")
            continue
                    
        except ValueError:
            error("Valor invalido")
            continue
def leer_documento(msg):
    while True: # id
        try:
            id_agregar=int(input(msg))
            if id_agregar>0:
                return id_agregar
                
            error("Valor negativo")
            continue
                    
        except ValueError:
            error("Valor invalido")
            continue

def leer_nota(msg):
    while True: # numero de horas 
        try:
            nota_agregar= float(input(msg))
            if  nota_agregar>0 and nota_agregar<= 5:
                return nota_agregar
            error("Valor invalido")
            continue
        except ValueError:
            error("valor invalido")
            continue
def validar_otro_ciclo(msg):
    while True:
        try:
            y=input(msg)
            if y.lower() == "si":
                return True
            if y.lower() == "no":
                return False
            print("!@ valor invalido")
        except ValueError:
            print("!@ valor invalido")
            continue
def menu():
    while True:
        try:
            print("="*30)
            print("\tSISTEMA GESTOR DE LIBROS")
            print("\t1- Mostrar en pantalla todos los manuales\n\t2- Crear un nuevo manual\n\t3- Modificar los manuales\n\t4- Eliminar\n\t5- Generar datos.txt\n\t6- Salir")
            print("="*30)
            op=int(input("\t>> escoja una opción (1-6)"))
            
            if op <1 or op >8:
                error("!@ Valor invalido")
                continue
            return op
        except ValueError:
            error("!@ Valor invalido")
            continue
def verificar_en_lista(msg,lista):
    while True:
        num=leer_id(msg)
        if num in lista:
            return num
        print("\tError, numero invalido, solo se permite",end=" ")
        [print(i,end=" ") for i in lista]
        input("\t @Digite cualquier tecla para continuar")
        continue
def fun_temas():
    lista=[]

    while True:
        titulo=leer_nombre("\tDigite un tema: ").lower().capitalize()
        
        if len(lista)!=0 and titulo in [lista[i]["titulo"]for i in range(len(lista))]:
            error(f"el tema {titulo} ya se encuentra agregado, por favor digite otro")
            continue
        clasificacion=verificar_en_lista("\tDigite la clasificiacion: (solo se admite 1, 2, y 3) ",[1,2,3])
        dato={
            "titulo":titulo,
            "clasificacion":clasificacion
        }
        lista.append(dato)

        if validar_otro_ciclo("\t@Desea ingresar otro tema ? (si|no) "):
            continue
        
        return lista
          
def crear_datos():
    general=leer_json()
    print(" "*15,f"\n\tregistrar un nuevo manual \n"," "*15)
    while True: 
        nombre_manual=leer_nombre(f"\tDigite el nombre del manual: ").capitalize()
        
        if nombre_manual in [key for key,value in general["manuales"].items()]:
            error("Nombre de manual ya existente")
            continue
        autor=leer_nombre(f"\tDigite el autor: ")
        paginas=str(leer_documento(f"\tDigite las paginas: "))
        temas=fun_temas()
        #definitiva= (nota1+nota2+nota3)/3
        datos={
                "autor":autor,
                "paginas":paginas,
               
                "temas":temas
                
            }
        general["manuales"][nombre_manual]=datos
        

        
        
        if validar_otro_ciclo("\t@¿Quiere seguir agregando otro manual? (si|no) "):
            print(" "*15,f"\n\tregistrar un nuevo manual \n"," "*15)
            continue
        subir_json(general)
        os.system("clear")
        break


def Actualizar(general,v):

    autor=leer_nombre(f"\tDigite el autor: ")
    paginas=str(leer_documento(f"\tDigite las paginas: "))
    if v!=0:
        temas=general["manuales"][v]["temas"]
        if len(temas)==0:
            temas=fun_temas()
        else:
            if validar_otro_ciclo(f"\tParece que tienes algunos temas para {v}, deseas modificarlos tambien? (si/no) "):
                temas=fun_temas()
    else:
        temas=fun_temas()

    datos={

            "autor":autor,
            "paginas":paginas,
            
            "temas":temas
            
        }
    
    return datos



def modificar_datos():
    general= leer_json()
    while True:
        lista=[key for key,value in general["manuales"].items()]
        tuplas=[(i+1,f"{manual}") for i,manual in enumerate(general["manuales"].keys())]
        [print(f"\t{j} --> {manual}")for j,manual in tuplas]
       
    
        codigo=leer_id("Digite el indice del manual que quiere modificar ")-1
            
           
        if codigo < 0 or codigo >len(lista):
            error("Manual inexistente")
            continue

        datos_agregar=Actualizar(general,lista[codigo])
        
        general["manuales"][lista[codigo]]=datos_agregar
        
        
        if validar_otro_ciclo("\t@Desea modificar otro manual? (si|no) "):
            continue
        
        subir_json(general)
        os.system("clear")
        break

def eliminar_manual():
    general=leer_json()
    while True:
        [print(f"\t{i+1} --> {manual}")for i,manual in enumerate(general["manuales"].keys())]
        lista=[key for key,value in general["manuales"].items()]
        codigo=leer_id("\tDigite el indice del manual que quiere borrar ")-1
        if codigo < 0 or codigo >len(lista):
            error("Manual inexistente")
            continue
        
        del general["manuales"][lista[codigo]]

        if validar_otro_ciclo("\t@Desea eliminar otro manual? (si|no)"):
            continue
        
        subir_json(general)
        os.system("clear")
        break
def mostrar_tem(i,elemento):
    print(f"\tPara el tema # {i+1}")
    [print(f"\t{key}={value}") for key,value in elemento.items()]     
def eliminar_temas():
    general=leer_json()
    print("\tPrimero es necesario saber en cual Manual quiere eliminar el tema")
    while True:
        [print(f"\t{i+1} --> {manual}")for i,manual in enumerate(general["manuales"].keys())]
        lista=[key for key,value in general["manuales"].items()]
        codigo=leer_id("\tDigite el indice del manual donde quiere borrar el tema ")-1
        if codigo < 0 or codigo >len(lista):
            error("Manual inexistente")
            continue
        break
    while True:
        [mostrar_tem(i,elemento) for i,elemento in enumerate(general["manuales"][lista[codigo]]["temas"])]
        lista_1=general["manuales"][lista[codigo]]["temas"]
        if len(lista_1)==0:
            error("Parece que no hay ningun tema, agrega uno para poder continuar")
            break
        
        codigo_1=leer_id("\tDigite el indice del tema que quiere borrar ")-1
        
        if len(lista_1)==1:
            print("hola")
            if codigo_1==0:

                general["manuales"][lista[codigo]]["temas"]=[]
                print("\tNo hay más temas para eliminar")
                input("\tDigite cualquier tecla para continuar")
                subir_json(general)
                os.system("clear")
                break
                
                
            else:
                error("\tTema inexistente")
                continue
        else:
            if codigo_1 < 0 or codigo_1 >len(lista_1):
                error("Tema inexistente")
                continue
            else:
                general["manuales"][lista[codigo]]["temas"].pop(codigo_1)
                subir_json(general)

        
        if validar_otro_ciclo("\t@Desea eliminar otro tema? (si|no)"):
            continue
        subir_json(general)
        os.system("clear")
        break
def eliminar_datos():
    while True:
        print("\t1. Eliminar manual\n\t2. Eliminar tema")
        num=leer_id("\tDigite la opcion que quiere realizar")
        if num >0 and num <=2:
            break
        error("opcion invalida")
        continue
    if num ==1:
        eliminar_manual()
    if num ==2:
        eliminar_temas()
def mostrar_todos():
    general=leer_json()
    [mostrar_dic(i,manual,dic_manual)for i,(manual, dic_manual) in enumerate(general["manuales"].items())]
  
    
def mostrar_dic(i,manual,dic_manual):
    print(" "*15,f"\n {i+1}  Manual {manual} \n"," "*15)
    [print(f"\t{key} = {value} ") if key !="temas" else mostrar_lista(value)
      for key,value in dic_manual.items()]

def mostrar_lista(lista):
    print("\t","."*10)
    print("\tTemas: ")
    print("\t","."*10)
    [[print(f"\t{k}--->{v}") if k!="titulo"else print(f"\tTema {i}\n\t{k}--->{v}")for k,v in dic.items()] for i,dic  in enumerate(lista)]


def leer_json():
    with open("manuales.json","r") as file:
        data=json.load(file)
    return data
def subir_json(data):
    with open("manuales.json","w") as file:
        json.dump(data,file,indent=4)



def generar_datos_txt():
    contador={}
    general=leer_json()
    for key in general["manuales"].keys():
        contador[key]={}
        for dic in general["manuales"][key]["temas"]:
            if dic["clasificacion"]==1:
                try:
                    contador[key]["Temas Basicos"]+=1
                except:
                    contador[key]["Temas Basicos"]=1
            if dic["clasificacion"]==2:
                try:
                    contador[key]["Temas intermedios"]+=1
                except:
                    contador[key]["Temas intermedios"]=1
            if dic["clasificacion"]==3:
                try:
                    contador[key]["Temas avanzados"]+=1
                except:
                    contador[key]["Temas avanzados"]=1
    
    lista_agregar=[]
    for llaves,dic in contador.items():
        lista_agregar.append(f"\nManual {llaves}:\n")
        for k,v in dic.items(): 
            lista_agregar.append(f"\t{k}: {v}\n")
    
    with open("datos.txt","w") as file:
        file.write("".join(lista_agregar))
    print("Ya se genero un archivo llamado datos.txt que tiene el informe de los temas por manual")
    input("Digite cualquier tecla para continuar")
    os.system("clear")





def main():
    
    while True:
       
        op=menu()
        if op ==1:
            mostrar_todos()
            input("\tDigite cualquier tecla para continuar")
            os.system("clear")
        elif op==2:
            crear_datos()
        elif op==3:
            modificar_datos()
        elif op==4:
            eliminar_datos()
        elif op==5:
            generar_datos_txt()
        elif op==6:
            os.system("clear")
            print("hasta luego")
            break
        
        
main()  