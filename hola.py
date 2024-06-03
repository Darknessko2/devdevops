from datetime import datetime
try:
    fecha_input = input("Ingresa la fecha con el siguiente formato dia/mes/anyo: ")
    formato = "%d/%m/%Y"

    fecha = datetime.strptime(fecha_input,formato)
    
    print(f'el dia es {fecha.day}, el mes es {fecha.month} y el anio es {fecha.year}')
except:
    print('Fecha no valida')



    