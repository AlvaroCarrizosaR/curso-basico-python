# Declaramos una variable
calificacion = int(input("¿Introduce tu calificacion de la AZ-900? "))

# Preguntamos si la califación es menor a 700
if calificacion < 700:
    print("Reprobaste") # Si es menor a 700, muestra esto
elif calificacion == 700:
    print("Panzaso")
elif calificacion > 1000:
    print("Mientes!!! No puedes sacar mas de mil")
else: # Si no se cumple el if anterior, pasa por esta linea
    print("Pasaste") # Se ejecuta si ninguno de los if se cumple

# Verificador de mayoria de edad
edad = int(input("Introduce tu edad: "))

if edad >= 18 and edad <= 100:
    print("Bienvenid@ al mamitas")
elif edad > 100:
    print("Si vienes acompañad@ de tus abuelitos, si te podemos fiar")
elif edad < 0:
    print("Ni que fueras viajer@ del tiempo")
else:
    print("No puedes llevarte esos cigarros")

# En python no existe el Switch
