#utils ->, ['clip_dtype', 'data_info', 'get_shape', 'handel_duplicate',
#           'handel_null', 'handel_outlier', 'load_csv_data', 'load_excel_data']

import pandas as pd

from utils import load_csv_data , get_shape , data_info , handel_duplicate  , handel_null , handel_outlier
def do_preprocessing(path: str) -> pd.DataFrame:
    ''' this function do a preprocessing 

        Args:
            path (str): Path to CSV file

        Returns:
            pd.DataFrame: clean data
    '''
    #S1
    df=load_csv_data(path)
    #S2
    get_shape(df)
    #S3
    data_info(df)
    #S4
    df=handel_duplicate(df)
    #S5
    df = handel_null(df)
    #S6
    df=handel_outlier(df)

    return df
if __name__=="__main__":
    #Don't forget to chnge this path the data sent will be loaded at rposetory
    data=do_preprocessing('D:\\data sets\\D.S to ETL_practise\\Detailed NFL Play-by-Play Data 2009-2018\\NFL Play by Play 2009-2018 (v5).csv')