import pandas as pd

def xlsx_to_dataframe(file_path: str) -> pd.DataFrame:
    """
    Read an XLSX file and return a DataFrame.

    Args:
        file_path (str): The path to the XLSX file.

    Returns:
        pd.DataFrame: The DataFrame containing the data from the XLSX file.
    """
    return pd.read_excel(file_path)

def dataframe_to_xlsx(dataframe: pd.DataFrame, output_file_path: str):
    """
    Write a DataFrame to an XLSX file.

    Args:
        dataframe (pd.DataFrame): The DataFrame to write.
        output_file_path (str): The path where the XLSX file will be saved.
    """
    dataframe.to_excel(output_file_path, index=False)