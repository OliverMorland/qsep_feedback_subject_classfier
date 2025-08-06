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

def xlsx_to_dataframes_dict(file_path: str) -> dict[str, pd.DataFrame]:
    """
    Read all sheets from an XLSX file and return a dictionary of DataFrames.

    Args:
        file_path (str): The path to the XLSX file.

    Returns:
        dict[str, pd.DataFrame]: Dictionary with sheet names as keys and DataFrames as values.
    """
    excel_file = pd.ExcelFile(file_path)
    sheet_names = excel_file.sheet_names
    
    dataframes_dict = {}
    for sheet_name in sheet_names:
        sheet_dataframe = pd.read_excel(file_path, sheet_name=sheet_name)
        dataframes_dict[sheet_name] = sheet_dataframe
    
    return dataframes_dict

def dataframe_to_xlsx(dataframe: pd.DataFrame, output_file_path: str):
    """
    Write a DataFrame to an XLSX file.

    Args:
        dataframe (pd.DataFrame): The DataFrame to write.
        output_file_path (str): The path where the XLSX file will be saved.
    """
    dataframe.to_excel(output_file_path, index=False)

def dataframes_dict_to_xlsx(dataframes_dict: dict[str, pd.DataFrame], output_file_path: str):
    """
    Write multiple DataFrames to separate sheets in an XLSX file.

    Args:
        dataframes_dict (dict[str, pd.DataFrame]): Dictionary with sheet names as keys and DataFrames as values.
        output_file_path (str): The path where the XLSX file will be saved.
    """
    excel_writer = pd.ExcelWriter(output_file_path, engine='openpyxl')
    
    for sheet_name, dataframe in dataframes_dict.items():
        dataframe.to_excel(excel_writer, sheet_name=sheet_name, index=False)
    
    excel_writer.close()