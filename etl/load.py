from operator import index
import sys

sys.path.append('.')

import pandas as pd
import helpers as hlp

def clientes(file):
    actual = hlp.actual(strategy='archive')
    target = f'./data-ouput/Clientes.csv'
    file.to_csv(target, index=False, sep=',', encoding='utf-8')

def compras(file, outliers=False):
    actual = hlp.actual(strategy='archive')
    if outliers == False:
        target = f'./data-ouput/Compras.csv'
        file.to_csv(target, index=False, sep=',', encoding='utf-8')
    else:
        target = f'./data-ouput/ComprasOutliers.csv'
        file.to_csv(target, index=False, sep=',', encoding='utf-8')

def gastos(file, outliers=False):
    actual = hlp.actual(strategy='archive')
    if outliers == False:
        target = f'./data-ouput/Gastos.csv'
        file.to_csv(target, index=False, sep=',', encoding='utf-8')
    else:
        target = f'./data-ouput/GastosOutliers.csv'
        file.to_csv(target, index=False, sep=',', encoding='utf-8')

def localidades(file):
    actual = hlp.actual(strategy='archive')
    target = f'./data-ouput/Localidades.csv'
    file.to_csv(target, index=False, sep=',', encoding='utf-8')

def proveedores(file):
    actual = hlp.actual(strategy='archive')
    target = f'./data-ouput/Proveedores.csv'
    file.to_csv(target, index=False, sep=',', encoding='utf-8')

def sucursales(file):
    actual = hlp.actual(strategy='archive')
    target = f'./data-ouput/Sucursales.csv'
    file.to_csv(target, index=False, sep=',', encoding='utf-8')

def ventas(file, outliers=False):
    actual = hlp.actual(strategy='archive')
    if outliers == False:
        target = f'./data-ouput/Ventas.csv'
        file.to_csv(target, index=False, sep=',', encoding='utf-8')
    else:
        target = f'./data-ouput/VentasOutliers.csv'
        file.to_csv(target, index=False, sep=',', encoding='utf-8')
