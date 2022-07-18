
import json
import sys
from clientes import *
obj_json= sys.argv[1]

list_tran = []

#accedo al json que lo paso como parametro con sys
with open(obj_json,'r')as archivo:
    datos_json = json.load(archivo)
    print('archivo leido con exito')
    print("")

#guardo las direcciones adentro de un objeto
direc = Direcciones(datos_json['direccion']['calle'], 
                    datos_json['direccion']['numero'], 
                    datos_json['direccion']['ciudad'], 
                    datos_json['direccion']['provincia'], 
                    datos_json['direccion']['pais'])


#dependiendo del tipo de cliente creo un obj u otro
if datos_json['tipo'] == 'CLASSIC':
    user = Classic(datos_json['nombre'], datos_json['apellido'], datos_json['dni'], datos_json['tipo'], direc)    

if datos_json['tipo'] == 'GOLD':
    user = Gold(datos_json['nombre'], datos_json['apellido'], datos_json['dni'], datos_json['tipo'], direc)

if datos_json['tipo'] == 'BLACK':
    user = Black(datos_json['nombre'], datos_json['apellido'], datos_json['dni'], datos_json['tipo'], direc)

#creo el obj que tiene las transacciones y los guardo adentro de un parametro que es una lista
for i in datos_json['transacciones']:
    tra = Transacciones(
        i['estado'], 
        i['tipo'], 
        i['cupoDiarioRestante'], 
        i['monto'], 
        i['fecha'],
        i['numero'],
        i['saldoEnCuenta'], 
        i['totalTarjetasDeCreditoActualmente'], 
        i['totalChequerasActualmente'])


    user.transacciones.append(tra)


for i in user.transacciones:
    user.retiro_efectivo(i)
    print("razon ", user.retiro_efectivo(i))
    user.alta_tarjeta(i)
    user.alta_chequera(i)
    user.compra_dolar(i)











# for i in user.transacciones:

#     # print(i.tipo)
#     # print("")
    







# class ALTA_TARJETA_CREDITO:
    
#     def LTA_TARJETA_CREDITO():
#         if puede_crear_tarjeta():
#             if i['tipo'] == 'ALTA_TARJETA_CREDITO' and i['estado'] != 'ACEPTADA' and i['totalTarjetasDeCreditoActualmente'] == 0 :
#                 print("usted ya tiene una tarjeta de credito")
                
#         else:
#             print("tu tipo de cuenta no es apta para este tipo de transacciones")