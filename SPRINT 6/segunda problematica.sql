--crear la vista de las edades

CREATE VIEW edades (customer_id, customer_name,customer_surname,customer_DNI,branch_number,edad) as
SELECT
	customer_id,customer_name,customer_surname,customer_DNI,sucursal.branch_number,
	CAST (((julianday('now') - julianday(dob))/365.25) as INT )as edad
	FROM cliente INNER JOIN sucursal on cliente.branch_id = sucursal.branch_id

	
--corroborar que funciona la vista
	
SELECT * FROM edades


--insertar a los 5 nuevos clientes

INSERT INTO cliente(customer_name,customer_surname,customer_DNI,branch_id,dob) VALUES 
("Lois","Stout",47730534,80,"1984-07-07"),
("Hall","Mcconnell",52055464,45,"1968-04-30"),
("Hilel","Mclean",43625213,77,"1993-03-28"),
("Jin","Cooley",21207908,96,"1959-08-24"),
("Gabriel","Harmon",57063950,27,"1976-04-01")

--corroborar que se hallan insertado correctamente

SELECT * FROM cliente WHERE customer_DNI = 47730534 UNION
SELECT * FROM cliente WHERE customer_DNI = 52055464 UNION
SELECT * FROM cliente WHERE customer_DNI = 43625213 UNION
SELECT * FROM cliente WHERE customer_DNI = 21207908 UNION
SELECT * FROM cliente WHERE customer_DNI = 57063950 

--actualizar la branch_id de los clientes nuevos 

UPDATE cliente SET branch_id = 10 WHERE customer_DNI = 47730534
UPDATE cliente SET branch_id = 10 WHERE customer_DNI = 52055464
UPDATE cliente SET branch_id = 10 WHERE customer_DNI = 43625213
UPDATE cliente SET branch_id = 10 WHERE customer_DNI = 21207908
UPDATE cliente SET branch_id = 10 WHERE customer_DNI = 57063950

--eliminar el registro perteneciente a David

DELETE FROM cliente where customer_name = "David"

--corroborar que se elimine correctamente

select * FROM cliente where customer_name = "David"

--seleccionar el prestamo con mayor importe

SELECT loan_type , max(loan_total) as "max_total" FROM prestamo
