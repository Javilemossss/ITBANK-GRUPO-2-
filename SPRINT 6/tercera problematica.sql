
--seleccionar las cuentas con saldo negativo

SELECT * FROM cuenta WHERE balance < 0

--Seleccionar el nombre, apellido y edad de los clientes que tengan en el apellido la letra Z.
--PRIMERO CREAMOS LA VISTA DE LAS edades

CREATE VIEW edades (customer_id, customer_name,customer_surname,customer_DNI,branch_number,edad) as
SELECT
	customer_id,customer_name,customer_surname,customer_DNI,sucursal.branch_number,
	CAST (((julianday('now') - julianday(dob))/365.25) as INT )as edad
	FROM cliente INNER JOIN sucursal on cliente.branch_id = sucursal.branch_id
	
SELECT customer_name, customer_surname,edad FROM edades WHERE customer_surname like '%z%'

--Seleccionar el nombre, apellido, edad y nombre de sucursal de las personas cuyo nombre sea “Brendan” 
--y el resultado ordenarlo por nombre de sucursal


SELECT cli.customer_name, cli.customer_surname,edades.edad, suc.branch_name FROM cliente as cli
INNER join edades on cli.customer_id = edades.customer_id
INNER join sucursal as suc on cli.branch_id = suc.branch_id
WHERE cli.customer_name = 'Brendan' ORDER by suc.branch_name 

--Seleccionar de la tabla de préstamos, los préstamos con un importe mayor a $80.000 y los préstamos prendarios utilizando la unión de tablas/consultas 
--(recordar que en las bases de datos la moneda se guarda como integer, en este caso con 2 centavos)
--primero crear vista para guardar los importes con centavos
select * from prestamo
select count() from prestamo where loan_type="PRENDARIO" and loan_total > 80000
select * from loan_total


-- Seleccionar los prestamos cuyo importe sea mayor que el importe medio de todos los prestamos
Select * from prestamo where loan_total > (select avg(loan_total) as promedio FROM PRESTAMO )

--Contar la cantidad de clientes menores a 50 años

SELECT count(*)FROM edades WHERE edad > 50

--Seleccionar las primeras 5 cuentas con saldo mayor a 8.000$
SELECT * FROM cuenta WHERE balance > 8000 LIMIT 0,5
 
--Seleccionar los préstamos que tengan fecha en abril, junio y agosto, ordenándolos por importe
SELECT * FROM prestamo WHERE loan_date like '%-04-%' UNION
SELECT * from prestamo WHERE loan_date like '%-06-%' UNION
SELECT * from prestamo WHERE loan_date like '%-08-%' ORDER BY loan_total

--Obtener el importe total de los prestamos agrupados por tipo de préstamos.
--Por cada tipo de préstamo de la tabla préstamo, calcular la suma de sus importes.
--Renombrar la columna como loan_total_accu

SELECT sum(loan_total) as loan_total_accu,loan_type FROM prestamo
GROUP BY loan_type
