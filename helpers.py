# Importación de librerias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime as dt

sns.set()

def actual(strategy='log'):
    if strategy == 'log':
        actual = str(dt.now())[:19]
    if strategy == 'archive':
        actual = str(dt.now())[:19].replace(' ', '_').replace(':', '-')
        return actual
    return actual

def log(message):
    now = actual()
    with open("logs.txt", "a") as f:
        f.write(now + ' - ' + message + '\n')
        print('['+ now + ']' + ' - ' + message)

def IQROutliers(df, column):
    Q1 = df[column].quantile(q=0.25)
    Q3 = df[column].quantile(q=0.75)
    IQR = Q3 - Q1
    minlim = Q1 - (1.5 * IQR)
    maxlim = Q1 + (1.5 * IQR)
    mask1 = df[column] >= minlim
    df_iqr = df[mask1]
    mask2 = df[column] < minlim
    iqr_outliers = df[mask2]
    mask3 = df_iqr[column] <= maxlim
    df_iqr = df_iqr[mask3]   
    mask4 = df[column] > maxlim
    iqr_outliers = df[mask4]
    return df_iqr, iqr_outliers, minlim, maxlim

def SigmaOutliers(df, column):
    # Calculo de maximos y minimos
    minlim = df[column].mean() - 3 * df[column].std()
    maxlim = df[column].mean() + 3 * df[column].std()
    mask1 = df[column] >= minlim
    df_sigma = df[mask1]
    mask2 = df[column] < minlim
    sigma_outliers = df[mask2]
    mask3 = df_sigma[column] <= maxlim
    df_sigma = df_sigma[mask3]   
    mask4 = df[column] > maxlim
    sigma_outliers = df[mask4]
    return df_sigma, sigma_outliers, minlim, maxlim

def OutliersVisualizer(df, column, strategy='sigma'):
    if strategy == 'iqr':
        df_without, df_outliers, minlim, maxlim = IQROutliers(df, column)
    else:
        df_without, df_outliers, minlim, maxlim = SigmaOutliers(df, column)
    # Histograma con outliers
    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    fig.set_size_inches(10, 2.5)
    ax1.hist(df[column],  bins=10, color='cornflowerblue')
    ax1.set_title('Con Outliers')
    # Histograma sin outliers
    ax2.hist(df_without[column],  bins=10, color='lightsalmon')
    ax2.set_title('Sin Outliers')  
    plt.show()
    # Boxplot con outliers
    fig, axes = plt.subplots(1, 2, figsize=(10, 2.5), sharey=True)
    sns.boxplot(data=df, x=column, ax=axes[0], color='cornflowerblue')
    axes[0].set_title('Con Outliers')
    # Boxplot sin outliers
    sns.boxplot(data=df_without, x=column, ax=axes[1], color='lightsalmon')
    axes[1].set_title('Sin Outliers')
    plt.show()
    
def VisualEvaluation(df, df_outliers=pd.DataFrame()):
    count_missing = df.isna().sum().values
    count_columns = df.count().values
    count_outliers = 0
    if df_outliers.shape[0] > 1:
        count_outliers = df_outliers.count().values
    columns_names = df.columns.values

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    fig.suptitle('Proporción de valores nulos y outliers respecto del total')

    # Grafico de Barras
    axes[0].barh(columns_names, count_columns, color='lightsalmon', label='Válidos')
    axes[0].barh(columns_names, count_outliers, color='cornflowerblue', label='Outliers')
    axes[0].barh(columns_names, count_missing, color='mediumaquamarine', label='Nulo')

    # Grafico de Pastel
    nulls = df.isnull().sum(axis=1)
    if df_outliers.shape[0] > 1:
        count_outliers = df_outliers.shape[0]
    count_missing = df[nulls > 0].shape[0]
    total_values = df.count().sum()
    values_pie = [count_missing, total_values, count_outliers]
    colors =  sns.color_palette('Set2')
    axes[1].pie(values_pie, colors=colors, autopct='%0.2f%%')
    plt.legend(labels=['Nulos', 'Válidos', 'Outliers'] )
    plt.show()