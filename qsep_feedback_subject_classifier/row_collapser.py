import pandas as pd

def generate_xlsx_with_collapsed_rows(input_file: str, output_file: str):
    """
    Read an XLSX file, collapse rows based on the 'Subject' column, and write the result to a new XLSX file.

    Args:
        input_file (str): The path to the input XLSX file.
        output_file (str): The path where the output XLSX file will be saved.
    """
    # Read the input XLSX file
    df = xlsx_to_dataframe(input_file)
    
    # Collapse rows
    collapsed_df = collapse_rows(df)
    
    # Write the collapsed DataFrame to an output XLSX file
    dataframe_to_xlsx(collapsed_df, output_file)

def combine_text_values(column_series):
    """
    Combine text values in a column series by joining them with spaces.
    
    Args:
        column_series: A pandas Series containing values to combine
        
    Returns:
        str: Combined text values separated by spaces
    """
    # Remove NaN values, convert to string, and join with spaces
    non_null_values = column_series.dropna()
    string_values = non_null_values.astype(str)
    combined_text = ' '.join(string_values)
    return combined_text


def get_non_subject_columns(dataframe: pd.DataFrame) -> list:
    """
    Get all column names from the DataFrame except 'Subject'.
    
    Args:
        dataframe (pd.DataFrame): Input DataFrame
        
    Returns:
        list: List of column names excluding 'Subject'
    """
    all_columns = dataframe.columns
    non_subject_columns = []
    
    for column_name in all_columns:
        if column_name != 'Subject':
            non_subject_columns.append(column_name)
    
    return non_subject_columns


def combine_column_values_by_subject(grouped_data, column_name: str) -> list:
    """
    Combine text values for a specific column across all subject groups.
    
    Args:
        grouped_data: Pandas GroupBy object grouped by 'Subject'
        column_name (str): Name of the column to process
        
    Returns:
        list: List of combined text values for each subject group
    """
    column_groups = grouped_data[column_name]
    combined_values = []
    
    for subject_name, column_series in column_groups:
        combined_text = combine_text_values(column_series)
        combined_values.append(combined_text)
    
    return combined_values


def build_aggregation_dictionary(grouped_data, non_subject_columns: list) -> dict:
    """
    Build a dictionary with combined values for all non-subject columns.
    
    Args:
        grouped_data: Pandas GroupBy object grouped by 'Subject'
        non_subject_columns (list): List of column names to process
        
    Returns:
        dict: Dictionary with column names as keys and combined values as values
    """
    aggregation_dict = {}
    
    for column_name in non_subject_columns:
        combined_values = combine_column_values_by_subject(grouped_data, column_name)
        aggregation_dict[column_name] = combined_values
    
    return aggregation_dict


def create_collapsed_dataframe(aggregation_dict: dict, unique_subjects: list) -> pd.DataFrame:
    """
    Create a DataFrame from the aggregation dictionary and add Subject column.
    
    Args:
        aggregation_dict (dict): Dictionary with combined column values
        unique_subjects (list): List of unique subject names
        
    Returns:
        pd.DataFrame: DataFrame with collapsed rows and Subject column
    """
    collapsed = pd.DataFrame(aggregation_dict, index=unique_subjects)
    
    # Reset index to make 'Subject' a regular column again
    collapsed = collapsed.reset_index()
    collapsed = collapsed.rename(columns={'index': 'Subject'})
    
    return collapsed


def collapse_rows(input_dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Collapse rows in the input DataFrame by combining text in the 'Subject' column and add numbers in other columns.

    Args:
        input_dataframe (pd.DataFrame): The input DataFrame with a 'Subject' column.

    Returns:
        pd.DataFrame: A new DataFrame with collapsed rows.
    """
    # Group by 'Subject'
    grouped_data = input_dataframe.groupby('Subject')
    
    # Get all column names except 'Subject'
    non_subject_columns = get_non_subject_columns(input_dataframe)
    
    # Build dictionary with aggregated values for all columns
    aggregation_dict = build_aggregation_dictionary(grouped_data, non_subject_columns)
    
    # Get unique subject names to use as index
    unique_subjects = list(grouped_data.groups.keys())
    
    # Create the result DataFrame
    collapsed = create_collapsed_dataframe(aggregation_dict, unique_subjects)
    
    return collapsed

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
