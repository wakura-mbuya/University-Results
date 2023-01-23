import pandas as pd

class LoadResults:
    """
    this class contains function results from an excell file to a pandas dataframe
   
    """
    
    def __init__(self):
        pass
    
    def load_results(self, excel_file):
        '''
        Load results from the raw excel files into pandas dataframe
        
        Params:
            excel_file: string 
            filename of the file containing the student results
        
        Returns: 
            Pandas.DataFrame
        '''
        df= pd.read_excel(excel_file,  skiprows=11)    
        df.drop(['S/N', 'NAME', 'RECOMMENDATIONS'], axis=1, inplace=True) #drop unwanted columns
        df.dropna(inplace=True) #get rid of rows with null values
        return df