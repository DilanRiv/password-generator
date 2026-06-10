# Generador de contraseñas
# Autor: DHREEN
# Descripción: genera contraseñas aleatorias con letras, números y símbolos

                                                                                  ## CONTRASEÑAS ##


import random
import string   
contras = []                            

def generar_contras(opci):
       caracteres = string.ascii_letters + string.digits + string.punctuation
       contraseña = ""
       for i in range (opci):
          contraseña += random.choice(caracteres)
          
       print(contraseña)
       contras.append(contraseña)
def mostrar_contras(contras):
   if contras: 
         print("Contraseñas generadas: ")
         for i, item in enumerate(contras,1):
             print(i,item)
   else:
           print("NO HAY CONTRASEÑAS GENERADAS")

   
while True :
    

    opciones = input("ELIJA UNA DE LAS OPCIONES : \n1.CREAR CONTRASEÑA \n2.CONTRASEÑAS GENERADAS \n3.SALIR \n").strip().lower()

    
    if opciones == "1" or opciones == "contraseña" : 
       
      try:
       opci = int(input("Elija la longitud de la contraseña\n"))
      except ValueError:
          print("tiene que introducir numeros por fa")
      else :
       
       generar_contras(opci)

    elif opciones == "2" or opciones == "mostrar" :
       
      mostrar_contras(contras)
      
    elif opciones == "3" or opciones == "salir" :
         print("CHAITO¡¡")
         break
    else :
        print ("SOLO MARQUE LAS OPCIONES MOSTRADAS")
      