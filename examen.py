import random

def asignar_sueldo(empleados):
    trabajadores = ["juan perez”,”maria garcia”,”carlos lopez”,”ana martinez”,”pedro rodriguez”,”laura hernandez”,”miguel sanchez”,”isabel gomez”,”francisco diaz”,”elena Fernandez","pepe"]
    print(empleados)
    print("")
    nombre = input("ingrese el nombre del trabajador: ").lower()
    if nombre in trabajadores:
        sueldados = []
        empleados = []
        sueldados.append(nombre)
        sueldo = random.randint(350000,2500000)
        print("encontrado")
        sueldados.append(sueldo)
        empleados.append(sueldados)
       
    else:
        print("no encontrado")
        
        
    

def descuentos_mensuales(empleados,sueldo,nombre):
  if not empleados:
     print("aun no hay empleados")



  else:
    for sueldados in empleados:
        sueldados.get(sueldo)
        descsalud = sueldo * 0.07
        descafp = sueldo * 0.12
        print("")
        print("nombre empleado:     desc salud:         desc afp")
        print("")
        print("")
        print(f"{sueldados[nombre]},     {descsalud},       {descafp}")

           

    
def clasificar_sueldos(empleados,sueldo,nombre):
   if sueldo:
    for sueldados in empleados:
     sueldados.get(sueldo)
     if sueldo < 800000:
       for sueldados in empleados:
        print("sueldos menores a $800.000")
        print("")
        print("trabajador:          sueldo")
        print("")
        print("")
        print(f"nombre: {nombre},      sueldo: {trabajadores[0]}   ")
        print("")
        print("")
     elif sueldo in range(800000,2000000):
       for trabajadores in empleados:
           print("sueldos entre $800.000 y $2.000.000")
           print("")
           print("trabajador:          sueldo")
           print("")
           print("")
           print(f"nombre: {sueldados[0]},      sueldo: {sueldados[0]}   ")
     elif sueldo > 2000000:
       for sueldados in empleados:
           print("sueldos mayores a $2.000.000")
           print("")
           print("trabajador:          sueldo")
           print("")
           print("")
           print(f"nombre: {sueldados[0]},      sueldo: {sueldados[0]}   ")
     
     else: 
        print("no hay empleados ingresados")

def mostrar_estadisticas(empleados):
    pass
        
    
    
    











































lista = []


while True:
    print("menu de oficina")
    print("")
    print("1: asignar sueldo aleatorio")
    print("2: clasificar sueldos")
    print("3: ver estadisticas")
    print("4: reporte de sueldos")
    print("5: imprimir csv")
    print("6: salir del programa")
    
    opc = int(input("ingrese una opcion: "))

    if opc == 1:
        asignar_sueldo(lista)

    if opc == 2:
        clasificar_sueldos(lista)
    
    if opc == 3: 
        sueldo(lista)