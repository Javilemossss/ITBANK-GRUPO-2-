
class Direcciones:
    def __init__(self,calle,numero,ciudad,provincia,pais):
        self.calle = calle
        self.numero = numero
        self.ciudad = ciudad
        self.provincia = provincia
        self.pais = pais
        
    def __str__(self):
        return f" {self.calle} {self.numero} de {self.ciudad}"

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
           
            
        def array(self):
            return [
                self.numero,
                self.fecha,
                self.tipo,
                self.estado,
                self.monto,
                self.razon
            ]
            


class Clientes:
    def __init__(self,nombre,apellido,dni,tipo):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.tipo = tipo

    

class Classic(Clientes):
    
    def __init__(self,nombre,apellido,dni,tipo,direcciones):
        Clientes.__init__(self, nombre, apellido, dni, tipo)
        self.limit = 150000
        self.transacciones = []
        self.direcciones = direcciones
        self.comision = 0.01
    
    def puede_crear_chequera(self):
        return False
    
    def puede_crear_tarjeta(self):
        return False
    
    def puede_comprar_dolar(self):
        return False
    
    def saldo_negativo(self):
        return False
   
    
    def retiro_efectivo(self,obj):
        if obj.tipo == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
            if obj.estado == "RECHAZADA":
                if obj.saldoEnCuenta < 1:
                    obj.razon = "no tiene saldo en la cuenta"
                
                elif obj.monto > obj.cupoDiarioRestante:
                    obj.razon = "se vencio su cupo restante diario"

                elif obj.monto > obj.saldoEnCuenta:
                    obj.razon = "saldo insuficiente"
                
                elif self.saldo_negativo():
                    if obj.monto > obj.saldoEnCuenta:
                        nega = obj.saldoEnCuenta - obj.monto 
                        if nega < -10000:
                            obj.razon = "se supero su descubierto y no tiene saldo para esta transaccion"
     
    
    def alta_tarjeta(self, obj):
        
         if obj.tipo == "ALTA_TARJETA_CREDITO":
            if obj.estado == "RECHAZADA":
                if self.puede_crear_tarjeta():
                    if obj.CantidadTarjetas == 1 :
                        obj.razon =  "usted no puede tener mas tarjetas"
                    
                else:
                    obj.razon = "esta cuenta no esta habilitada para tener una tarjeta de credito"             
      
                    
    def alta_chequera(self, obj):
        
         if obj.tipo == "ALTA_CHEQUERA":
            if obj.estado == "RECHAZADA":
                if self.puede_crear_chequera():
                    if obj.CantidadChequeras == 1 :
                        obj.razon = "usted no puede tener mas chequeras"
                    
                else:
                    obj.razon = "esta cuenta no esta habilitada para tener una chequera"


    def compra_dolar(self, obj):
         if obj.tipo == "COMPRA_DOLAR":
            if obj.estado == "RECHAZADA":
                if self.puede_comprar_dolar():
                    if obj.monto > obj.saldoEnCuenta:
                        obj.razon = "saldo insuficiente para completar esta accion"
                    
                else:
                    obj.razon = "esta cuenta no esta habilitada para comprar dolares"
    
                    
    def transferencia_enviada(self, obj):
        if obj.tipo == "TRANSFERENCIA_ENVIADA":
            if obj.estado == "RECHAZADA":
                re = (obj.monto * self.comision) + obj.monto
                
                if obj.monto > obj.saldoEnCuenta:
                    obj.razon = "saldo insuficiente"
                
                if obj.monto == obj.saldoEnCuenta:    
                    if obj.saldoEnCuenta < re:
                        obj.razon = "su saldo no cubre la comision por transferencia"
                    
                if self.saldo_negativo():
                    if obj.monto > obj.saldoEnCuenta:
                        nega = obj.saldoEnCuenta - obj.monto
                        if nega < -10000:
                            obj.razon = "se supero su descubierto y no tiene saldo para esta transaccion"


    def transferencia_recibida(self, obj):
        if obj.tipo == "TRANSFERENCIA_RECIBIDA":
            if obj.estado == "RECHAZADA":
                if obj.monto > self.limit:
                    obj.razon = f"no puede recibir una transferencia mayor a {self.limit} sin previo aviso"
        
                    



class Gold(Clientes):
    
    def __init__(self,nombre,apellido,dni,tipo, direcciones):
        Clientes.__init__(self, nombre, apellido, dni, tipo)
        self.limit = 500000
        self.transacciones = []
        self.direcciones = direcciones
        self.comision = 0.005
    
    def puede_crear_chequera(self):
        return True
    
    def puede_crear_tarjeta(self):
        return True
    
    def puede_comprar_dolar(self):
        return True
    
    def saldo_negativo(self):
        return True
    
    def retiro_efectivo(self,obj):
        if obj.tipo == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
            if obj.estado == "RECHAZADA":
                if obj.saldoEnCuenta < 1:
                    obj.razon = "no tiene saldo en la cuenta"
                
                elif obj.monto > obj.cupoDiarioRestante:
                    obj.razon = "se vencio su cupo restante diario"

                elif obj.monto > obj.saldoEnCuenta:
                    obj.razon = "saldo insuficiente"
                
                elif self.saldo_negativo():
                    if obj.monto > obj.saldoEnCuenta:
                        nega = obj.saldoEnCuenta - obj.monto 
                        if nega < -10000:
                            obj.razon = "se supero su descubierto y no tiene saldo para esta transaccion"
    
    
    def alta_tarjeta(self, obj):
        if obj.tipo == "ALTA_TARJETA_CREDITO":
            if obj.estado == "RECHAZADA":
                if self.puede_crear_tarjeta():
                    if obj.CantidadTarjetas == 1 :
                        obj.razon =  "usted no puede tener mas tarjetas"
                    
                else:
                    obj.razon = "esta cuenta no esta habilitada para tener una tarjeta de credito"                             
    
                    
    def alta_chequera(self, obj):
         if obj.tipo == "ALTA_CHEQUERA":
            if obj.estado == "RECHAZADA":
                if self.puede_crear_chequera():
                    if obj.CantidadChequeras == 1 :
                        obj.razon = "usted no puede tener mas chequeras"
                    
                else:
                    obj.razon = "esta cuenta no esta habilitada para tener una chequera"


    def compra_dolar(self, obj):
         if obj.tipo == "COMPRA_DOLAR":
            if obj.estado == "RECHAZADA":
                if self.puede_comprar_dolar():
                    if obj.monto > obj.saldoEnCuenta:
                        obj.razon = "saldo insuficiente para completar esta accion"
                    
                else:
                    obj.razon = "esta cuenta no esta habilitada para comprar dolares"

    
                    
    def transferencia_enviada(self, obj):
        if obj.tipo == "TRANSFERENCIA_ENVIADA":
            if obj.estado == "RECHAZADA":
                re = (obj.monto * self.comision) + obj.monto
                
                if obj.monto > obj.saldoEnCuenta:
                    obj.razon = "saldo insuficiente"
                
                if obj.monto == obj.saldoEnCuenta :
                    if obj.saldoEnCuenta < re :
                        obj.razon = "su saldo no cubre la comision por transferencia"
                        
                if self.saldo_negativo():
                    if obj.monto > obj.saldoEnCuenta:
                        nega = obj.saldoEnCuenta - obj.monto
                        if nega < -10000:
                            obj.razon = "se supero su descubierto y no tiene saldo para esta transaccion"

     
    def transferencia_recibida(self, obj):
        if obj.tipo == "TRANSFERENCIA_RECIBIDA":
            if obj.estado == "RECHAZADA":
                if obj.monto > self.limit:
                    obj.razon = f"no puede recibir una transferencia mayor a {self.limit} sin previo aviso"
        
                    

class Black(Clientes):
    
    def __init__(self,nombre,apellido,dni,tipo ,direcciones):
        Clientes.__init__(self, nombre, apellido, dni, tipo)
        self.transacciones = []
        self.direcciones = direcciones
    
    def puede_crear_chequera(self):
        return True
    
    def puede_crear_tarjeta(self):
        return True
    
    def puede_comprar_dolar(self):
        return True
    
    def saldo_negativo(self):
        return True 
    
    
    def retiro_efectivo(self,obj):
        if obj.tipo == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
            if obj.estado == "RECHAZADA":
                if obj.saldoEnCuenta < 1:
                    obj.razon = "no tiene saldo en la cuenta"
                
                elif obj.monto > obj.cupoDiarioRestante:
                    obj.razon = "se vencio su cupo restante diario"

                elif obj.monto > obj.saldoEnCuenta:
                    obj.razon = "saldo insuficiente"
                
                elif self.saldo_negativo():
                    if obj.monto > obj.saldoEnCuenta:
                        nega = obj.saldoEnCuenta - obj.monto 
                        if nega < -10000:
                            obj.razon = "se supero su descubierto y no tiene saldo para esta transaccion"
    
    
    def alta_tarjeta(self, obj):
        if obj.tipo == "ALTA_TARJETA_CREDITO":
            if obj.estado == "RECHAZADA":
                if self.puede_crear_tarjeta():
                    if obj.CantidadTarjetas == 5 :
                        obj.razon =  "usted no puede tener mas tarjetas"
                    
                else:
                    obj.razon = "esta cuenta no esta habilitada para tener una tarjeta de credito"                             
    
                    
    def alta_chequera(self, obj):
         if obj.tipo == "ALTA_CHEQUERA":
            if obj.estado == "RECHAZADA":
                if self.puede_crear_chequera():
                    if obj.CantidadChequeras == 2 :
                        obj.razon = "usted no puede tener mas chequeras"
                    
                else:
                    obj.razon = "esta cuenta no esta habilitada para tener una chequera"


    def compra_dolar(self, obj):
         if obj.tipo == "COMPRA_DOLAR":
            if obj.estado == "RECHAZADA":
                if self.puede_comprar_dolar():
                    if obj.monto > obj.saldoEnCuenta:
                        obj.razon = "saldo insuficiente para completar esta accion"
                    
                else:
                    obj.razon = "esta cuenta no esta habilitada para comprar dolares"

                    
    def transferencia_enviada(self, obj):
        if obj.tipo == "TRANSFERENCIA_ENVIADA":
            if obj.estado == "RECHAZADA":
                
                if obj.monto > obj.saldoEnCuenta:
                    obj.razon = "saldo insuficiente"
                    
                if self.saldo_negativo():
                    if obj.monto > obj.saldoEnCuenta:
                        nega = obj.saldoEnCuenta - obj.monto
                        if nega < -10000:
                            obj.razon = "se supero su descubierto y no tiene saldo para esta transaccion"
                

    def transferencia_recibida(self, obj):
        if obj.tipo == "TRANSFERENCIA_RECIBIDA":
            if obj.estado == "RECHAZADA":
                pass
                # if obj.monto > self.limit:
                #     obj.razon = f"no puede recibir una transferencia mayor a {self.limit} sin previo aviso"    