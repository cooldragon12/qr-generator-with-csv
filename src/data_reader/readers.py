from genericpath import exists
import pandas as pd

from log import getLogger

logger = getLogger('readers.py')

def get_data_csv(file_path, *args, **kwargs):
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
        
    if not file_path:
        logger.error(f"Please specify lo path of file")
        raise 
    # This start getting the csv to the path specified
    logger.info(f"Getting the Data From CSV {file_path}", exc_info=1)
    
    
    # Checks the file if exist
    if not exists(file_path):
        raise FileNotFoundError("File specified not exist "+ file_path)

    # This read the csv
    data = pd.read_csv(file_path, delimiter)

    logger.info("Data has been gathered")

    # Getting the specific column we want to return
    series = data[to_add]

    # Removing all Null Values
    series = series.dropna()

    # The array return is the column that turned into a series.
    # To make it usable 
    return series

