--Listar la cantidad de clientes por nombre de sucursal ordenando de mayor
--a menor

select (select branch_name from sucursal where branch_id = cliente.branch_id) as NombreSuc, count() as cantidad from cliente group by branch_id

--Obtener la cantidad de empleados por cliente por sucursal en un número
--real

select (select branch_name from sucursal where branch_id = empleado.branch_id) as NombreSuc, count() as CantidadEmpleados from empleado group by branch_id



--Obtener la cantidad de tarjetas de crédito por tipo por sucursa

select sucursal.branch_name, count() as CantTarjetas, marca_tarjetas.marca from tarjeta
inner join cliente on tarjeta.customer_id = cliente.customer_id
inner join sucursal on cliente.branch_id = sucursal.branch_id 
inner join marca_tarjetas on marca_tarjetas.marca_tarjeta_ID = tarjeta.marca_tarjeta_ID 
where tipo_tarjeta ="Crédito" group by sucursal.branch_name, tarjeta.marca_tarjeta_ID


--Obtener el promedio de créditos otorgado por sucursal

select sucursal.branch_name as Sucur, avg(loan_total) as Promedio from prestamo 
inner join cliente on prestamo.customer_id = cliente.customer_id
inner join sucursal on cliente.branch_id = sucursal.branch_id 
group by sucursal.branch_id


--La información de las cuentas resulta critica para la compañía, por eso es
--necesario crear una tabla denominada “auditoria_cuenta” para guardar los
--datos movimientos, con los siguientes campos: old_id, new_id, old_balance,
--new_balance, old_iban, new_iban, old_type, new_type, user_action,
--created_at
--o Crear un trigger que después de actualizar en la tabla cuentas los
--campos balance, IBAN o tipo de cuenta registre en la tabla auditoria
--o Restar $100 a las cuentas 10,11,12,13,14

CREATE TABLE auditoria_cuenta (
old_id INTEGER not NULL,
new_id integer,
old_balance INTEGER not NULL,
new_balance INTEGER NOT NULL,
old_iban  TEXT NOT NULL,
new_iban TEXT UNIQUE not null,
old_type INTEGER not NULL,
new_type INTEGER not null,
user_action TEXT,
created_at date
)


CREATE TRIGGER Auditoria 
	AFTER UPDATE ON cuenta
	WHEN old.balance <> new.balance
		OR old.iban <> new.iban
		OR old.tipo_cuenta_ID <> new.tipo_cuenta_ID
BEGIN
	INSERT INTO auditoria_cuenta(old_id, new_id, old_balance, new_balance, old_iban, new_iban, old_type, new_type, user_action, created_at)
	VALUES
	(old.account_id, 
	new.account_id, 
	old.balance, 
	new.balance, 
	old.iban, 
	new.iban, 
	old.tipo_cuenta_ID, 
	new.tipo_cuenta_ID, 
	'UPDATE', DATETIME('NOW')
	);
	
END



UPDATE cuenta
SET 
	balance = balance - 100
WHERE 
	account_id = 10 OR 
	account_id = 11 OR
	account_id = 12 OR
	account_id = 13 OR
	account_id = 14;

	
CREATE UNIQUE INDEX index_dni ON Cliente(customer_dni)
	
CREATE TABLE Movimientos (
	mov_id INT NOT NULL,
	nro_cuenta  INT NOT NULL,
	monto INT NOT NULL,
	op_type TEXT NOT NULL,
	hora DATE NOT NULL,
	PRIMARY KEY (mov_id),
	FOREIGN KEY (nro_cuenta) REFERENCES cuenta(account_id)
);

BEGIN TRANSACTION;


UPDATE cuenta
SET balance = balance - 1000
WHERE account_id = 200;

UPDATE cuenta
SET balance = balance + 1000
WHERE account_id = 400;

INSERT INTO Movimientos (mov_id, nro_cuenta, monto, op_type, hora) VALUES
(1, 200, 1000, 'TRANSFERENCIA', DATETIME('now'));

COMMIT;
