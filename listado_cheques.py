import sys

print("")
print("_______________LISTADO DE CHEQUES_______________")
print("")

dni=False
salida=False
cantidad=False
cheque=False
tipo_cheque=False
estado_cheque=False
fecha_origen=False
fecha_pago=False

cont=0

"""ESTABLECEMOS PARAMETROS MINIMOS"""

if len(sys.argv) >=3 and len(sys.argv) <=5:
    cantidad=True
    print("cantidad valida de parametros")

    """COMENZAMOS LA VALIDACIÓN DE LOS PARAMETROS"""

    try:
        """PARAMETRO DNI"""
        sys.argv[1]=int(sys.argv[1])
        
        if type(sys.argv[1]) == int:
            print("el dni tiene parametros numericos, CORRECTO")
            
            
            eldni=str(sys.argv[1])
            
            if len(eldni) == 8:
                print("el dni tiene 8 caracteres, CORRECTO")
                dni=True
            else:
                print("ERROR")
                print("ERROR EL DNI NO TIENE 8 CARACTERES")
                print("ERROR")
            
                         
    except ValueError:
        print("ERROR")
        print("ERROR EL DNI NO ES un numero")
        print("ERROR")
        exit()
        
    
    """PARAMETRO TIPO DE SALIDA"""
        
    if sys.argv[2] == 'pantalla':
        salida=True
        print("la salida es pantalla correcto")
        
    elif sys.argv[2] == 'csv':
        salida=True
        print("la salida es csv, CORRECTO")
        
    else:
        print("ERROR")
        print("ERROR EL PARAMETRO ES INCORRECTO")
        print("ERROR")
    
    
    """PARAMETRO TIPO DE CHEQUE"""
    
    if sys.argv[3] == 'emitido':
        tipo_cheque=True
        print("el cheque esta emitido, CORRECTO")
        
    elif sys.argv[3] == 'depositado':
        tipo_cheque=True
        print("el cheque esta depositado, CORRECTO")
        
    else:
        print("ERROR")
        print("ERROR EL PARAMETRO DE TIPO DE CHEQUE ES INCORRECTO")
        print("ERROR")
    

    """PARAMETRO DE ESTADO DE CHEQUE"""

    if sys.argv[4]=='pendiente':
        estado_cheque=True
        print("el cheque esta pendiente, CORRECTO")

    elif sys.argv[4]=='aprobado':
        estado_cheque=True
        print("el cheque esta aprobado, CORRECTO")
    
    elif sys.argv[4]=='rechazado':
        estado_cheque=True
        print("el cheque esta rechazado, CORRECTO")

    else:
        print("ERROR")
        print("ERROR EL PARAMETRO DE ESTADO DE CHEQUE ES INCORRECTO")
        print("ERROR")

    """PARARAMETRO DE FECHA"""

    
    
    
    
    if cantidad and dni and salida and tipo_cheque:
        
        cheque=True
        print("LOS PARAMETROS OBLIGATORIOS SON CORRECTOS")
    else:
        print("ERROR")
        print("ERROR AH FALLADO EN ALGUN PARAMETRO")
        print("ERROR")
    
    
else:
    print("ERROR")
    print("ERROR CANTIDAD INVALIDA DE PARAMETROS")
    print("ERROR")


