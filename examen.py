## EXAMEN 1 _BRAULIO GONZÁLEZ ESQUIVEL_ ##

################################## Función_1: Carga de Datos a DF ##################################
def cargar_data(archivo):
    import pandas as pd
    import os
    #Función para cargar un archivo como DF
    extension = os.path.splitext(archivo)[1].lower()
#Cargar el archivo según la extensión
    if extension == ".csv":
        dataframe= pd.read_csv(archivo)
        return (dataframe)
    elif extension == ".xlsx":
        dataframe= pd.read_excel(archivo)
        return (dataframe)
    else:
        raise ValueError(f"Este formato no está soportado para esta función: {extension}")


################################## Función_2: Sustitución de Valores Nulos Pares, Impares y Str ##################################
def nulos_general(dataframe):
    import pandas as pd
    import numpy as np
    #Separo las columnas cuantitativas y cuali del DataFrame
    cuantitativas_con_nulos = dataframe.select_dtypes(include=["float64", "int64", "float", "int"])
    cualitativas_con_nulos = dataframe.select_dtypes(include=['object', 'datetime','category'])
    #Aquí solo voy a tomar en cuenta los valores numéricos y los clasificare en pares e impares...
    imparesGen= cuantitativas_con_nulos.iloc[ : , 1::2]
    paresGen= cuantitativas_con_nulos.iloc[ : , 0::2] #tomo en cuenta los valores de inicio a fin, y que los cuente en...
    #...1 o 2 empezando de 1 o 2 para par e impar

    #Quitar valores nulos...
    pares= paresGen.fillna(round(paresGen.mean(), 1))
    impares= imparesGen.fillna(99)
    cualitativas= cualitativas_con_nulos.fillna("Este_es_un_valor_nulo")
    #voy a unir todo...
    #Unimos el DataFrame cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos= pd.concat([cualitativas, pares, impares], axis=1)

    return(Datos_sin_nulos)


################################## Función_3: Identificación de Valores Nulos ##################################
def cuenta_nulos(dataframe):
    import pandas as pd
    import numpy as np
    pd.set_option('display.max_rows', None)
    #Valores nulos por columna
    valores_nulos_cols = dataframe.isnull().sum()
    #Valores nulos por dataframe
    valores_nulos_df = dataframe.isnull().sum().sum()
    
    return("Valores nulos por columna", valores_nulos_cols,
            "Valores nulos por dataframe", valores_nulos_df)


################################## Función_4: Sustituir las columnas numéricas por "rango intercuartilico" ##################################
def sus_intercuartilico(dataframe):
    import pandas as pd
    import numpy as np
    cuantitativas = dataframe.select_dtypes(include=["float64", "int64", "float", "int"])
    cualitativas= dataframe.select_dtypes(include=['object', 'datetime','category'])
    x=cuantitativas

    percentile25= x.quantile(0.25) #Q1
    percentile75= x.quantile(0.75) #Q3

    iqr= percentile75 - percentile25

    Limite_Superior_iqr= percentile75 + 1.5*iqr
    Limite_Inferior_iqr= percentile25 - 1.5*iqr

    data3_iqr= cuantitativas[(x<=Limite_Superior_iqr)&(x>=Limite_Inferior_iqr)]
    data3_iqr

    data4_iqr= data3_iqr.copy()
    data4_iqr= data4_iqr.fillna(round(data3_iqr.mean(),1))
    data4_iqr

    Datos_limpios_listings = pd.concat([cualitativas, data4_iqr], axis=1)
    return(Datos_limpios_listings)











######
#def nulos_prueba(dataframe):
 #   import pandas as pd
   # import numpy as np
 #   columnasMax= 0
 #   while columnasMax < len(dataframe.columns):
  #      columnas= dataframe.columns

   #     if columna

        #cualitativas_con_nulos = dataframe.select_dtypes(include=['object', 'datetime','category'])


   #def nulos_cuanti_prom(dataframe):
    #import pandas as pd
    #import numpy as np
   # cuantitativas = cuantitativas_con_nulos.fillna(round(cuantitativas_con_nulos.mean(), 1))
    #Unimos el DataFrame cuantitativo limpio con el dataframe cualitativo
  #  Datos_sin_nulos = pd.concat([cuantitativas, cualitativas_con_nulos], axis=1)

  #  return(Datos_sin_nulos)

  #def nulos_varios_gen(dataframe):
   # import pandas as pd
   # import numpy as np
   # columnasMax= 0
   # while columnasMax < len(dataframe.columns):
     #   columnas= dataframe.columnas
     #   if pd.api.types.is_string_dtype(dataframe[columnas]):
      #      dataframe[columnas]= dataframe[columnas].fillna("Este_es_un_valor_nulo")
     #   elif columnasMax % 2 == 0:ar
       #    
      #  else: 
      #      dataframe[columnas] = dataframe[columnas].fillna(99)
      #  columnasMax += 1

   # return dataframe