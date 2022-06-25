import sys

sys.path.append('.')

import helpers as hlp
from etl import extract
from etl import transform
from etl import load

print('----EXTRACTING PHASE INITIALIZED----')

hlp.log('Extract Clientes')
files_clientes =  extract.clientes()
hlp.log(f'Number of files extracted: {len(files_clientes)}')

hlp.log(f'Extract Compra')
files_compras = extract.compras()
hlp.log(f'Number of Extracted files: {len(files_compras)}')

hlp.log(f'Extract Gasto')
files_gastos = extract.gastos()
hlp.log(f'Number of Extracted files: {len(files_gastos)}')

hlp.log(f'Extract Localidades')
files_localidades = extract.localidades()
hlp.log(f'Number of Extracted files: {len(files_localidades)}')

hlp.log(f'Extract Proveedores')
files_proveedores = extract.proveedores()
hlp.log(f'Number of Extracted files: {len(files_proveedores)}')

hlp.log(f'Extract Sucursales')
files_sucursales = extract.sucursales()
hlp.log(f'Number of Extracted files: {len(files_sucursales)}')

hlp.log(f'Extract Venta')
files_ventas = extract.ventas()
hlp.log(f'Number of Extracted files: {len(files_ventas)}')

print('----EXTRACTED PHASE COMPLETED------')

print('----TRANSFORM PHASE INITIALIZED-------')

flag_clientes = False
data_clientes = None
if len(files_clientes) > 0:
    data_clientes = transform.clientes(files_clientes)
    flag_clientes = True
    hlp.log(f'Transform files Clientes completed')

flag_compras = False
data_compras = None
outliers_compras = None
if len(files_compras) > 0:
    data_compras, outliers_compras = transform.compras(files_compras)
    flag_compras = True
    hlp.log(f'Transform files Compras completed')

flag_gastos = False
data_gastos = None
outliers_gastos = None
if len(files_gastos) > 0:
    data_gastos, outliers_gastos = transform.gastos(files_gastos)
    flag_gastos = True
    hlp.log(f'Transform files Gastos completed')

flag_localidades = False
data_localidades = None
if len(files_localidades) > 0:
    data_localidades = transform.localidades(files_localidades)
    flag_localidades = True
    hlp.log(f'Transform files Localidades completed')

flag_proveedores = False
data_proveedores = None
if len(files_proveedores) > 0:
    data_proveedores = transform.proveedores(files_proveedores)
    flag_proveedores = True
    hlp.log(f'Transform files Proveedores completed')

flag_sucursales = False
data_sucursales = None
if len(files_sucursales) > 0:
    data_sucursales = transform.sucursales(files_sucursales)
    flag_sucursales = True
    hlp.log(f'Transform files Sucursales completed')

flag_ventas = False
data_ventas = None
outliers_ventas = None
if len(files_ventas) > 0:
    data_ventas, outliers_ventas = transform.ventas(files_ventas)
    flag_ventas = True
    hlp.log(f'Transform files Ventas completed')

print('-----TRANSFORM PHASE COMPLETED--------')

print('-----LOAD PHASE INITIALIZED------')

if flag_clientes:
    load.clientes(data_clientes)
    hlp.log(f'Load data in csv Clientes')

if flag_compras:
    load.compras(data_compras)
    load.compras(outliers_compras, outliers=True)
    hlp.log(f'Load data in csv Compras')

if flag_gastos:
    load.gastos(data_gastos)
    load.gastos(outliers_gastos, outliers=True)
    hlp.log(f'Load data in csv Gastos')

if flag_localidades:
    load.localidades(data_localidades)
    hlp.log(f'Load data in csv Localidades')

if flag_proveedores:
    load.proveedores(data_proveedores)
    hlp.log(f'Load data in csv Proveedores')

if flag_sucursales:
    load.sucursales(data_sucursales)
    hlp.log(f'Load data in csv Sucursales')

if flag_ventas:
    load.ventas(data_ventas)
    load.ventas(outliers_ventas, outliers=True)
    hlp.log(f'Load data in csv Ventas')

print('-----LOAD PHASE COMPLETED-----')