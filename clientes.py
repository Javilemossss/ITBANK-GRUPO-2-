
class Direcciones:
    def __init__(self,calle,numero,ciudad,provincia,pais):
        self.calle = calle
        self.numero = numero
        self.ciudad = ciudad
        self.provincia = provincia
        self.pais = pais

class Transacciones:
        def __init__(self,estado,tipo,cupoDiarioRestante,monto,fecha,numero,saldoEnCuenta,totalTarjetasDeCreditoActualmente,totalChequerasActualmente):
            self.estado = estado
            self.tipo = tipo
            self.cupoDiarioRestante = cupoDiarioRestante
            self.monto = monto
            self.fecha = fecha
            self.numero = numero
            self.saldoEnCuenta = saldoEnCuenta
            self.CantidadTarjetas = totalTarjetasDeCreditoActualmente
            self.CantidadChequeras = totalChequerasActualmente
            self.razon = ""
            
            
class Razon:
    def __init__(self,razon):
        self.razon = razon


class Clientes:
    def __init__(self,nombre,apellido,dni,tipo):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.tipo = tipo





            
    
    
    

class Classic(Clientes):
    
    def __init__(self,nombre,apellido,dni,tipo,direcciones):
        Clientes.__init__(self, nombre, apellido, dni, tipo)
        self.retiroDiario = 10000
        self.transfereciaRecibida = 150000
        self.transacciones = []
        self.direcciones = direcciones
    
    def puede_crear_chequera(self):
        return False
    
    def puede_crear_tarjeta(self):
        return False
    
    def puede_comprar_dolar(self):
        return False
    
    
    def retiro_efectivo(self,obj):
        if obj.tipo == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
            if obj.estado == "RECHAZADA":
                if obj.saldoEnCuenta < 1:
                    print("no tiene saldo en la cuenta",obj.numero)
                    # raz = Razon("no tiene saldo en la cuenta")
                    # obj.razon = raz
                    
                
                if obj.monto > obj.cupoDiarioRestante:
                    print("se vencio su monto restante diario",obj.numero)
                    return "se vencio su monto restante diario"
                    

                
                if obj.monto > obj.saldoEnCuenta:
                    print("saldo insuficiente",obj.numero)
     
    
    def alta_tarjeta(self, obj):
        
         if obj.tipo == "ALTA_TARJETA_CREDITO":
            if obj.estado == "RECHAZADA":
                if self.puede_crear_tarjeta():
                    if obj.CantidadTarjetas == 1 :
                        print("usted no puede tener mas tarjetas",obj.numero)
                        #definir razon 
                    
                else:
                    print("esta cuenta no esta habilitada para tener una tarjeta de credito",obj.numero)
                    #definir razon                 
      
                    
    def alta_chequera(self, obj):
        
         if obj.tipo == "ALTA_CHEQUERA":
            if obj.estado == "RECHAZADA":
                if self.puede_crear_chequera():
                    if obj.CantidadChequeras == 1 :
                        print("usted no puede tener mas chequeras",obj.numero)
                        #definir razon 
                    
                else:
                    print("esta cuenta no esta habilitada para tener una chequera",obj.numero)
                    #definir razon


    def compra_dolar(self, obj):
        
         if obj.tipo == "COMPRA_DOLAR":
            if obj.estado == "RECHAZADA":
                if self.puede_comprar_dolar():
                    
                    if obj.monto > obj.saldoEnCuenta:
                        print("saldo insuficiente para completar esta accion",obj.numero)
                    
                else:
                    print("esta cuenta no esta habilitada para comprar dolares",obj.numero)
                    #definir razon
                    



class Gold(Clientes):
    
    def __init__(self,nombre,apellido,dni,tipo, direcciones):
        Clientes.__init__(self, nombre, apellido, dni, tipo)
        self.retiroDiario = 20000
        self.transfereciaRecibida = 500000
        self.transacciones = []
        self.direcciones = direcciones
    
    def puede_crear_chequera(self):
        return False
    
    def puede_crear_tarjeta(self):
        return True
    
    def puede_comprar_dolar(self):
        return True
    
    
    def retiro_efectivo(self,obj):
        if obj.tipo == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
            if obj.estado == "RECHAZADA":
                if obj.saldoEnCuenta < 1:
                    print("no tiene saldo en la cuenta",obj.numero)
                    # raz = Razon("no tiene saldo en la cuenta")
                    # obj.razon = raz
                    
                
                if obj.monto > obj.cupoDiarioRestante:
                    print("se vencio su monto restante diario",obj.numero)
                    # raz = Razon("se vencio su monto restante diario")
                    # obj.razon.append(raz)
                
                if obj.monto > obj.saldoEnCuenta:
                    print("saldo insuficiente",obj.numero)
    
    
    
    
    def alta_tarjeta(self, obj):
        
         if obj.tipo == "ALTA_TARJETA_CREDITO":
            if obj.estado == "RECHAZADA":
                if self.puede_crear_tarjeta():
                    if obj.CantidadTarjetas == 1 :
                        print("usted no puede tener mas tarjetas",obj.numero)
                        #definir razon 
                    
                else:
                    print("esta cuenta no esta habilitada para tener una tarjeta de credito",obj.numero)
                    #definir razon                
                    
    def alta_chequera(self, obj):
        
         if obj.tipo == "ALTA_CHEQUERA":
            if obj.estado == "RECHAZADA":
                if self.puede_crear_chequera():
                    if obj.CantidadChequeras == 1 :
                        print("usted no puede tener mas chequeras",obj.numero)
                        #definir razon 
                    
                else:
                    print("esta cuenta no esta habilitada para tener una chequera",obj.numero)
                    #definir razon

    def compra_dolar(self, obj):
        
         if obj.tipo == "COMPRA_DOLAR":
            if obj.estado == "RECHAZADA":
                if self.puede_comprar_dolar():
                    
                    if obj.monto > obj.saldoEnCuenta:
                        print("saldo insuficiente para completar esta accion",obj.numero)
                    
                else:
                    print("esta cuenta no esta habilitada para comprar dolares",obj.numero)
                    #definir razon


class Black(Clientes):
    
    def __init__(self,nombre,apellido,dni,tipo ,direcciones):
        Clientes.__init__(self, nombre, apellido, dni, tipo)
        self.retiroDiario = 100000
        self.transfereciaRecibida = True
        self.transacciones = []
        self.direcciones = direcciones
    
    def puede_crear_chequera(self):
        return True
    
    def puede_crear_tarjeta(self):
        return True
    
    def puede_comprar_dolar(self):
        return True