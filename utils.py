import pandas as pd
import numpy as np

def load_csv_data(path : str) -> pd.DataFrame :
    '''This Function is created to read csv files 
       Args: path(str): the path to csv file
       return: pd.DataFrame : a data frame that was read by function
    '''
    data=pd.read_csv(path)
    return data

def load_excel_data(path: str) -> pd.DataFrame :
    '''This Function is created to read excel files
       Args: path(str): an excel file path
       return: pd.DataFrame : a data frame that was read by function
    '''
    data=pd.read_excel(path)
    return data

def get_shape(data: pd.DataFrame) -> tuple :
    '''if you want to see the shape of data use this function
       Args: data(pd.DataFrame): a data frame that i want to know its shape
       Return: tuple: the shape of data
    '''
    return data.shape

def data_info(data: pd.DataFrame) -> None :
    
    '''it will give you an advantage to show info of your all columns'''

    number_cols=get_shape(data)[1]
    data.info(max_cols=number_cols,verbose=True)

def clip_dtype(data: pd.DataFrame) -> pd.DataFrame :

    '''if your data contains more than one type of data you can use it to displit data by type
       
       Args : data(pd.DataFrame) : Input dataframe

       Returns : tuple: (numeric dataframe, non-numeric dataframe)
    '''

    numeric_dtypes = ["int64", "int32", "float64", "float32", "boolean", "bool"]
    # non_numeric_dtypes = [
    #        "object", "string", "category",
    #        "datetime64[ns]", "datetime64[ns, tz]",
    #       "timedelta[ns]", "complex128", "complex64",
    #      "Sparse", "Interval"
    #   ]
    num_data=data.select_dtypes(include=numeric_dtypes)
    str_data=data.select_dtypes(exclude=numeric_dtypes)
    return num_data, str_data

def handel_null(data: pd.DataFrame) -> pd.DataFrame :
    
    '''this method check if your data has null or not
    then hanedl all cases either null or not
    using median to fill numerical columns 
    and mode to fill non numerical columns
    
    Args : data(pd.DataFrame) : Input dataframe

    Returns : pd.DataFrame : DataFrame without nulls
    '''

    number_of_nulls_series=data.isna().sum()
    number_of_nulls_scalar=data.isna().sum().sum()
    if(number_of_nulls_scalar==0):
        print("your data has not any nulls")
        return data
    else :
        print(f"number of null is : {number_of_nulls_scalar} ")
        num_data,str_data=clip_dtype(data)

        if not num_data.empty :
             median=num_data.median()

        if not str_data.empty :    
             mod=str_data.mode()[0]

        num_data=num_data.fillna(median)
        str_data=str_data.fillna(mod)  

        orig_data=pd.concat([num_data,str_data],axis=1).reindex(columns=data.columns)
        return orig_data 

def handel_duplicate(data : pd.DataFrame) -> pd.DataFrame :
   
   '''
    Remove duplicate rows from dataframe.

    Args:
        data (pd.DataFrame): Input dataframe.

    Returns:
        pd.DataFrame: Dataframe without duplicates.
    '''

   return data.drop_duplicates()             

def handel_outlier(data :pd.DataFrame ) -> pd.DataFrame :

    '''this function to replace  outlier with median value 
       usig inter quartile range
       
       Args:
         data (pd.DataFrame) : Input data frame
       return:
         pd.DataFrame: dataframe after replace outlier
    '''

    num_data , str_data = clip_dtype(data)
    Q1 = num_data.quantile(0.25)
    Q3 = num_data.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - (1.5*IQR)
    upper = Q3 + (1.5*IQR)
    median = num_data.median()
    mask = ( num_data < lower ) | ( num_data > upper )
    num_data = num_data.mask( mask , median , axis = 1 )
    cleand_data = pd.concat( [ num_data , str_data ] , axis = 1 ).reindex( columns = data.columns)
    return cleand_data