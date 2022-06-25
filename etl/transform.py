import pandas as pd
import helpers as hlp

def clientes(files):
    data_clientes = pd.DataFrame(columns=['Cliente_id', 'Provincia', 'Nombres', 'Domicilio', 'Telefono', 'Edad', 'Localidad', 'Longitud', 'Latitud'])
    for f in files:
        df = pd.read_csv(f, delimiter=';')
        # TODO  Borrar columnas innecesarias
        df.drop('col10', axis=1, inplace=True)
        # TODO: Renombrar columnas
        name_columns = {
            'ID' : 'Cliente_id',
            'Nombre_y_Apellido': 'Nombres',
            'X': 'Longitud',
            'Y': 'Latitud'
        }
        df.rename(columns=name_columns, inplace=True)
        # TODO: Imputar valores faltantes
        df['Provincia'].fillna('Sin Datos', inplace=True)
        df['Nombres'].fillna('Sin Datos', inplace=True)
        df['Domicilio'].fillna('Sin Datos', inplace=True)
        df['Localidad'].fillna('Sin Datos', inplace=True)
        df['Telefono'].fillna('Sin Datos', inplace=True)
        # TODO: Nomalizar datos a letra capital
        Cap = lambda x : x.title()
        df['Provincia'] = df['Provincia'].map(Cap)
        df['Nombres'] = df['Nombres'].map(Cap)
        df['Domicilio'] = df['Domicilio'].map(Cap)
        df['Localidad'] = df['Localidad'].map(Cap)
        # TODO: Cambiar tipos de dato
        rep = lambda x : x.replace(',', '.')
        df['Latitud'] = df['Latitud'].astype(str, copy=True, errors='raise')
        df['Latitud'] = df['Latitud'].map(rep)
        df['Latitud'] = df['Latitud'].astype(float, copy=True, errors='raise')
        df['Longitud'] = df['Longitud'].astype(str, copy=True, errors='raise')
        df['Longitud'] = df['Longitud'].map(rep)
        df['Longitud'] = df['Longitud'].astype(float, copy=True, errors='raise')
        # TODO: Imputar valores nulos
        df['Longitud'] = df['Longitud'].fillna(0)
        df['Latitud'] = df['Latitud'].fillna(0)   
        # TODO: Anexar a unico dataset
        data_clientes = pd.concat([data_clientes, df], ignore_index=True)
    # TODO: Registar valores
    num_data = data_clientes.shape[0]
    hlp.log(f'Total values: {num_data}')
    return data_clientes

def compras(files):
    data_compras = pd.DataFrame(columns=['Compra_id', 'Fecha', 'Producto_id', 'Proveedor_id', 'Cantidad', 'Precio'])
    outliers_compras = pd.DataFrame(columns=['Compra_id', 'Fecha', 'Producto_id', 'Proveedor_id', 'Cantidad', 'Precio'])
    for f in files:
        df = pd.read_csv(f)
        # TODO: Borrar columnas inncesesarias
        drop_columns = ['Fecha_Año', 'Fecha_Mes', 'Fecha_Periodo']
        df.drop(columns=drop_columns, inplace=True)
        # TODO: Renombrar columnas
        name_columns = {
            'IdCompra': 'Compra_id',
            'IdProducto': 'Producto_id',
            'IdProveedor': 'Proveedor_id'
        }
        df.rename(columns=name_columns, inplace=True)
        # TODO: Organizar columnas
        df = df.reindex(columns=['Compra_id', 'Fecha', 'Producto_id', 'Proveedor_id', 'Cantidad', 'Precio'])
        # TODO: Cambiar tipo de dato de las columnas
        df['Fecha'] = pd.to_datetime(df['Fecha'])
        # TODO: Imputar valores nulos
        df['Precio'] = df['Precio'].fillna(0)
        # TODO: Deteccion de outliers
        df_clean, df_outliers_cantidad, minlim, maxlim = hlp.SigmaOutliers(df, 'Cantidad')
        df_clean, df_outliers_precio, minlim, maxlim = hlp.IQROutliers(df_clean, 'Precio')
        # TODO: Almacenar todos los outliers en un dataframe
        outliers = pd.merge(df_outliers_cantidad, df_outliers_precio, how='outer')
        # TODO: Anexar valores a datasets
        data_compras = pd.concat([data_compras, df_clean], ignore_index=True)
        outliers_compras = pd.concat([outliers_compras, outliers], ignore_index=True)
    # TODO: Registar valores
    num_valid =  df_clean.shape[0]
    num_outliers = outliers.shape[0]
    hlp.log(f'Total Valid values: {num_valid}')
    hlp.log(f'Total Outliers values: {num_outliers}')
    return data_compras, outliers_compras

def gastos(files):
    data_gastos = pd.DataFrame(columns=['Gasto_id', 'Fecha', 'Sucursal_id', 'TipoGasto_id', 'Monto'])
    outliers_gastos = pd.DataFrame(columns=['Gasto_id', 'Fecha', 'Sucursal_id', 'TipoGasto_id', 'Monto'])
    for f in files:
        df = pd.read_csv(f)
        # TODO: Renombrar columnas 
        rename_columns = {
            'IdGasto': 'Gasto_id',
            'IdSucursal': 'Sucursal_id',
            'IdTipoGasto': 'TipoGasto_id'
        }
        df.rename(columns=rename_columns, inplace=True)
        # TODO: Cambiar tipo de dato
        df['Fecha'] = pd.to_datetime(df['Fecha'])
        # TODO: Organizar columnas
        df = df.reindex(columns=['Gasto_id', 'Fecha', 'Sucursal_id', 'TipoGasto_id', 'Monto'])
        # TODO: Detección de outliers
        df_clean, outliers, _, _ = hlp.IQROutliers(df, 'Monto')
        # TODO: Agregar registros en uno solo
        data_gastos = pd.concat([data_gastos, df_clean], ignore_index=True)
        outliers_gastos = pd.concat([outliers_gastos, outliers], ignore_index=True)
    # TODO: Numero de registros
    num_data = data_gastos.shape[0]
    num_outliers = outliers_gastos.shape[0]
    hlp.log(f'Total valid values: {num_data}')
    hlp.log(f'Total outliers values: {num_outliers}')
    return data_gastos, outliers_gastos

def localidades(files):
    data_localidades = pd.DataFrame(columns=['Codigo_Censal', 'Localidad', 'Municipio', 'Departamento', 'Provincia', 'Longitud', 'Latitud'])
    for f in files:
        df = pd.read_csv(f)
        # TODO: Borrar columnas inncesarias
        df.drop(columns=['categoria', 'departamento_id', 'fuente', 'localidad_censal_id'], inplace=True)
        df.drop(columns=['municipio_id', 'nombre', 'provincia_id'], inplace=True)
        # TODO: Renombrar columnnas
        rename_columns = {
            'centroide_lat': 'Latitud',
            'centroide_lon': 'Longitud',
            'departamento_nombre': 'Departamento',
            'id': 'Codigo_Censal',
            'localidad_censal_nombre': 'Localidad',
            'municipio_nombre': 'Municipio',
            'provincia_nombre': 'Provincia'
        }
        df.rename(columns=rename_columns, inplace=True)
        # TODO: Organizar columnas
        df = df.reindex(columns=['Codigo_Censal', 'Localidad', 'Municipio', 'Departamento', 'Provincia', 'Longitud', 'Latitud'])
        # TODO: Imputar valores nulos
        df['Municipio'] = df['Municipio'].fillna('Sin Dato')
        df['Departamento'] = df['Departamento'].fillna('Sin Dato')
        # TODO: Agregar a un dataframe universal
        data_localidades = pd.concat([data_localidades, df], ignore_index=True)
    # TODO: Registrar valores
    num_data = data_localidades.shape[0]
    hlp.log(f'Total values: {num_data}')
    return data_localidades
        
def proveedores(files):
    data_proveedores = pd.DataFrame(columns=['Proveedor_id', 'Nombres','Direccion', 'Localidad', 'Provincia'])
    for f in files:
        df = pd.read_csv(f, encoding='latin-1')

        # TODO: Renombrar columnas
        rename_columns = {
            'IDProveedor': 'Proveedor_id',
            'Nombre': 'Nombres',
            'Address': 'Direccion',
            'City': 'Localidad',
            'State': 'Provincia'
        }
        df.rename(columns=rename_columns, inplace=True)
        # TODO: Eliminar columnas innecesarias
        df.drop(columns=['departamen', 'Country'], axis=1, inplace=True)
        # TODO: Imputación de valores faltantes
        df['Nombres'] = df['Nombres'].fillna('Sin Dato')
        # TODO: Normalizar columnas en letra capital
        Cap = lambda x : x.title()
        df['Direccion'] = df['Direccion'].map(Cap)
        df['Localidad'] = df['Localidad'].map(Cap)
        df['Provincia'] = df['Provincia'].map(Cap)
        # TODO: Anexar a un unico dataframe
        data_proveedores = pd.concat([data_proveedores, df], ignore_index=True)
    # TODO: Registrar cantidad de valores
    num_data = data_proveedores.shape[0]
    hlp.log(f'Total values: {num_data}')
    return data_proveedores

def sucursales(files):
    data_sucursales = pd.DataFrame(columns=['Sucursal_id', 'Sucursal', 'Direccion', 'Localidad', 'Provincia', 'Latitud', 'Longitud'])
    for f in files:
        df = pd.read_csv(f, delimiter=';')
        # TODO: Normalización de Nombres
        df["Localidad"] = [str(x).replace('Ã³',"ó") for x in df["Localidad"]]
        df["Localidad"] = [str(x).replace('Ã',"í") for x in df["Localidad"]]
        df["Localidad"] = [str(x).replace('Tucumí¡n',"Tucumán") for x in df["Localidad"]]
        df.loc[df['Localidad'].str.contains('Buenos'), 'Localidad'] = 'CABA'
        df.loc[df['Localidad'].str.startswith('Cap'), 'Localidad'] = 'CABA'
        df.loc[df['Localidad'].str.endswith('oba'), 'Localidad'] = 'Córdoba'
        df["Provincia"] = [str(x).replace('Ã³',"ó") for x in df["Provincia"]]
        df["Provincia"] = [str(x).replace('Ã­',"í") for x in df["Provincia"]]
        df["Provincia"] = [str(x).replace('TucumÃ¡n',"Tucumán") for x in df["Provincia"]]
        df.loc[df['Provincia'].str.contains('B.'), 'Provincia'] = 'Buenos Aires'
        df.loc[df['Provincia'].str.endswith('oba'), 'Provincia'] = 'Córdoba'
        df["Sucursal"] = [str(x).replace('Ã³',"ó") for x in df["Sucursal"]]
        df["Sucursal"] = [str(x).replace('Ã¡',"á") for x in df["Sucursal"]]
        # TODO: Renombrar columnas
        rename_columns = {
            'ID': 'Sucursal_id'
        }
        df.rename(columns=rename_columns, inplace=True)
        # TODO: Cambiar tipos de datos
        rep = lambda x : x.replace(',', '.')
        df['Latitud'] = df['Latitud'].map(rep)
        df['Latitud'] = df['Latitud'].astype(float, copy=True, errors='raise')
        df['Longitud'] = df['Longitud'].map(rep)
        df['Longitud'] = df['Longitud'].astype(float, copy=True, errors='raise')
        # TODO: Normalizar en letra capital
        Cap = lambda x : x.title()
        df['Localidad'] = df['Localidad'].map(Cap)
        # TODO: Agregar al dataframe principal
        data_sucursales = pd.concat([data_sucursales, df], ignore_index=True)
    # TODO: Registro del total de valores
    num_data = data_sucursales.shape[0]
    hlp.log(f'Total values: {num_data}')
    return data_sucursales

def ventas(files):
    data_ventas = pd.DataFrame(columns=['Venta_id', 'Fecha', 'Fecha_Entrega', 'Canal_id', 'Cliente_id', 'Sucursal_id', 'Empleado_id', 'Producto_id', 'Precio', 'Cantidad'])
    outliers_ventas = pd.DataFrame(columns=['Venta_id', 'Fecha', 'Fecha_Entrega', 'Canal_id', 'Cliente_id', 'Sucursal_id', 'Empleado_id', 'Producto_id', 'Precio', 'Cantidad'])
    for f in files:
        df = pd.read_csv(f)
        # TODO: Renombrar columnas
        rename_columns = {
            'IdVenta': 'Venta_id',
            'IdCanal': 'Canal_id',
            'IdCliente': 'Cliente_id',
            'IdSucursal': 'Sucursal_id',
            'IdEmpleado': 'Empleado_id',
            'IdProducto': 'Producto_id'
        }
        df.rename(columns=rename_columns, inplace=True)
        # TODO: Imputación de valures nulos
        df['Precio'] = df['Precio'].fillna(0)
        df['Cantidad'] = df['Cantidad'].fillna(0)
        # TODO: Normalización de fechas
        df['Fecha'] = pd.to_datetime(df['Fecha'])
        df['Fecha_Entrega'] = pd.to_datetime(df['Fecha_Entrega'])
        # TODO: Detección de Outliers
        df_clean, outliers_cantidad, _, _ = hlp.SigmaOutliers(df, 'Cantidad')
        df_clean, outliers_precio, _, _ = hlp.IQROutliers(df_clean, 'Precio')
        # TODO: Almacenar outliers en un solo archivo
        outliers = pd.merge(outliers_precio, outliers_cantidad, how='outer')
        # TODO: Almacenar datos en un solo dataframe
        data_ventas = pd.concat([data_ventas, df_clean], ignore_index=True)
        outliers_ventas = pd.concat([outliers_ventas, outliers], ignore_index=True)
    # TODO: Registrar cantidad de valores
    num_data = data_ventas.shape[0]
    num_outliers = outliers_ventas.shape[0]
    hlp.log(f'Total Valid values: {num_data}')
    hlp.log(f'Total Outliers values: {num_outliers}')
    return data_ventas, outliers_ventas

