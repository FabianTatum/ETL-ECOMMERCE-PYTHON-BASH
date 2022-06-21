# Importación de librerias

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def VisualEvaluation(df):
    # Grafico de Barras
    count_missing = df.isna().sum().values
    count_columns = df.count().values
    columns_names = df.columns.values
    plt.barh(columns_names, count_columns, color='lightsalmon', label='Existente')
    plt.barh(columns_names, count_missing, color='mediumaquamarine', label='Nulo')
    plt.ylabel("Columnas")
    plt.xlabel("Conteo de valores")
    plt.title('Proporción de valores nulos respecto del total')
    plt.legend()
    plt.show()
    # Grafico de Pastel
    mask = df.isnull().sum(axis=1)
    count_missing = df[mask > 0].shape[0]
    total_values = df.count().sum()
    values_pie = [count_missing, total_values]
    colors =  sns.color_palette('Set2')
    plt.pie(values_pie, labels=['Nulos', 'Existentes'], colors=colors, autopct='%0.2f%%')
    plt.title('Porcentaje de Registros con nulos respecto de los Completos en Ventas')
    plt.legend()
    plt.show()

def SigmaOutliers(df, column):
   # Calculo de maximos y minimos
    minimo = df[column].mean() - 3 * df[column].std()
    maximo = df[column].mean() + 3 * df[column].std()
    mask1 = df[column] >= minimo
    df_sigma = df[mask1]
    mask2 = df_sigma[column] <= maximo
    df_sigma = df_sigma[mask2]
    # Histograma con outliers
    plt.hist(df[column],  bins=10, color='r')
    plt.title('Historgrama con outliers')
    plt.ylabel('Cantidad')
    plt.xlabel('Valores Columna')
    plt.show()
    # Histograma sin outliers
    plt.hist(df_sigma[column],  bins=10)
    plt.title('Historgrama sin outliers')
    plt.ylabel('Cantidad')
    plt.xlabel('Valores Columna')
    plt.show()
    # Boxplot con outliers
    sns.boxplot(data=df, x=column)
    plt.title('Boxplot con Outliers')
    plt.show()
    # Boxplot sin outliers
    sns.boxplot(data=df_sigma, x=column)
    plt.title('Boxplot sin Outliers')
    plt.show()

def IQROutliers(df, column):
    # Calculo de Quartiles
    Q1 = df[column].quantile(q=0.25)
    Q3 = df[column].quantile(q=0.75)
    IQR = Q3 - Q1
    minlim = Q1 - (1.5 * IQR)
    maxlim = Q1 + (1.5 * IQR)
    print(minlim)
    print(maxlim)
    mask1 = df[column] >= minlim
    df_iqr = df[mask1]
    mask2 = df_iqr[column] <= maxlim
    df_iqr = df_iqr[mask2]
    # Histograma con outliers
    plt.hist(df[column],  bins=10, color='r')
    plt.title('Historgrama con outliers')
    plt.ylabel('Cantidad')
    plt.xlabel('Valores Columna')
    plt.show()
    # Histograma sin outliers
    plt.hist(df_iqr[column],  bins=10)
    plt.title('Historgrama sin outliers')
    plt.ylabel('Cantidad')
    plt.xlabel('Valores Columna')
    plt.show()
    # Boxplot con outliers
    sns.boxplot(data=df, x=column)
    plt.title('Boxplot con Outliers')
    plt.show()
    # Boxplot sin outliers
    sns.boxplot(data=df_iqr, x=column)
    plt.title('Boxplot sin Outliers')
    plt.show()

