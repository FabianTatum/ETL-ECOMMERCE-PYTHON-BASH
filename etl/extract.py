import sys
import glob

sys.path.append(".")

def clientes():
    files = glob.glob('./data-input/Cli*.csv')
    return files

def compras():
    files = glob.glob('./data-input/Com*.csv')
    return files

def gastos():
    files = glob.glob('./data-input/Gas*.csv')
    return files

def localidades():
    files = glob.glob('./data-input/Loc*.csv')
    return files

def proveedores():
    files = glob.glob('./data-input/Pro*.csv')
    return files

def sucursales():
    files = glob.glob('./data-input/Suc*.csv')
    return files

def ventas():
    files = glob.glob('./data-input/Ven*.csv')
    return files