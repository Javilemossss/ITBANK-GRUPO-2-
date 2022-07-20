
import json
import sys
import os
from clientes import *

try:
    obj_json= sys.argv[1]
except IndexError:
    print("ERROR NO SE ENCUENTRA EL ARCHIVO .json")
    exit()


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

#creo el obj que tiene las transacciones y los guardo adentro de un atributo que es una lista
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
    user.alta_tarjeta(i)
    user.alta_chequera(i)
    user.compra_dolar(i)
    user.transferencia_enviada(i)
    user.transferencia_recibida(i)
    
for i in user.transacciones:
    print("numero",i.numero ,i.estado , i.tipo ,"saldo:",i.saldoEnCuenta,"monto:", i.monto, "cupodiario:" , i.cupoDiarioRestante , "RAZON:",i.razon, i.fecha)



columna=''
for i in user.transacciones:
    columna+= '<tr>'
    for n in i.array():
        columna+= f'<td> {n} </td>'
    columna += '</td>'



import codecs
with codecs.open ('archivo.html', 'w','utf-8') as html_file:
        
    html_content= f"""
 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css"
    rel="stylesheet"
    integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor"
    crossorigin="anonymous"/>
    <title>Reporte Transacciones</title>
</head>
<body style="background-color:rgba(182, 177, 182, 0.50)">
    <div class="container" >
        <div class="card" style="background-color: rgba(173, 216, 230, 0.3);">
            <div class="row justify-content-center" id="titulo" style="font-size: 30px; padding: 30px;">Reporte de Transacciones</div>
            <div class="row">
                <div class="col-md-12 mx-auto" style="padding: 30px;">
                    <div class="card-header">
                        <h1 style="font-size: 20px">Cliente: {user.nombre, user.apellido, user.dni, user.tipo}</h1>
                    </div>
                    <table class="table table-responsive">
                        <thead>
                        <tr>
                            <th scope="col">Numero</th>
                            <th scope="col">Fecha</th>
                            <th scope="col">Tipo</th>
                            <th scope="col">Estado</th>
                            <th scope="col">Monto</th>
                            <th scope="col">Razon</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            {columna}
                        </tr>
                                
                                
                        </tbody>
                    </table>
                </div>
                        
                                
            </div>
        </div>
    </div>
</body>
</html>
    """

    html_file.write(html_content)

html_file.close()

file = codecs.open("archivo.html", 'r', "utf-8")
print(file.read())


print(user.direcciones)



# <ul class="list-group">
                    #     <li class="list-group-item"> DNI: {user.dni} </li>
                    #     <li class="list-group-item"> Direccion: "direccion" </li>
                    # </ul>

