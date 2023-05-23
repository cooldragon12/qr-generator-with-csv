from genericpath import exists
import pandas as pd

from ..exceptions import DirectoryNotFoundError
def get_data_csv(file_path, *args, **kwargs) -> pd.DataFrame:
    """
        ```Returns``` 
        List of data


        ABOUT:
        This works using the pandas library to make an array of item to use.
    """
    to_add = ""
    delimiter = ","
    if kwargs is not None:
        if kwargs['to_get'] is not None: 
            to_add = kwargs['to_get']
        # if kwargs['delimiter'] is not None:
        #     delimiter = kwargs['delimiter']
        
    # Checks the file if exist
    if not exists(file_path):
        raise FileNotFoundError("File specified not exist "+ file_path)

    # This read the csv
    data = pd.read_csv(file_path, delimiter)


    # Getting the specific column we want to return
    series = data[to_add]

    # Removing all Null Values
    series = series.dropna()

    # The array return is the column that turned into a series.
    # To make it usable 
    return series

def queueItWithRawText():
    raw = input("Enter the content to add. Separate with `,`: \n")

    lists = raw.split(',')
    
    names = [email.split('.')[0].strip() for email in lists]
    
    return names
    


def queueItWithCSV(file_path):
    # After Getting the Raw data from a csv , More Specifically at email column
    # NOTE: This can be change
    data = get_data_csv(file_path=file_path, to_get="GE Email")

    # We will remove any extensions at the email, only to get the name
    # By using splitting
    data = data.str.split('.', expand=True)

    # then we will slect only the names which is index zero
    names = data[0].tolist()
    
    # After that we will use Queue package to manage multiple requests
    return names