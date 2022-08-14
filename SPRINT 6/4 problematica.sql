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

