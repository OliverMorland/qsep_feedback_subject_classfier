import pandas as pd
from qsep_feedback_subject_classifier.utils.utils import xlsx_to_dataframe, dataframe_to_xlsx

SUBJECT_COLUMN = 'Subject'
COLUMN_TO_COLLAPSE = 'Categorized_Subject'

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

def sum_numerical_values(column_series):
    """
    Sum numerical values in a column series, treating NaN/None as 0.
    
    Args:
        column_series: A pandas Series containing numerical values to sum
        
    Returns:
        int: Sum of all numerical values in the series
    """
    # Fill NaN values with 0 and sum all values
    numeric_series = pd.to_numeric(column_series, errors='coerce')

    # Fill NaNs with 0 and sum
    filled_values = numeric_series.fillna(0)
    total_sum = filled_values.sum()
    
    # Convert to integer
    result = int(total_sum)
    return result


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
        if column_name != COLUMN_TO_COLLAPSE and column_name != SUBJECT_COLUMN:
            non_subject_columns.append(column_name)
    
    return non_subject_columns


def sum_column_values_by_subject(grouped_data, column_name: str) -> list:
    """
    Sum numerical values for a specific column across all subject groups.
    
    Args:
        grouped_data: Pandas GroupBy object grouped by 'Subject'
        column_name (str): Name of the column to process
        
    Returns:
        list: List of summed numerical values for each subject group
    """
    column_groups = grouped_data[column_name]
    summed_values = []
    
    for subject_name, column_series in column_groups:
        summed_value = sum_numerical_values(column_series)
        summed_values.append(summed_value)
    
    return summed_values


def build_aggregation_dictionary(grouped_data, non_subject_columns: list) -> dict:
    """
    Build a dictionary with summed values for all non-subject columns.
    
    Args:
        grouped_data: Pandas GroupBy object grouped by 'Subject'
        non_subject_columns (list): List of column names to process
        
    Returns:
        dict: Dictionary with column names as keys and summed values as values
    """
    aggregation_dict = {}
    
    for column_name in non_subject_columns:
        summed_values = sum_column_values_by_subject(grouped_data, column_name)
        aggregation_dict[column_name] = summed_values
    
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
    collapsed = collapsed.rename(columns={'index': f'{COLUMN_TO_COLLAPSE}'})

    return collapsed


def collapse_rows(input_dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Collapse rows in the input DataFrame by grouping by 'Subject' column and summing numbers in other columns.

    Args:
        input_dataframe (pd.DataFrame): The input DataFrame with a 'Subject' column.

    Returns:
        pd.DataFrame: A new DataFrame with collapsed rows and summed numerical values.
    """
    try:
        # Group by 'Subject'
        grouped_data = input_dataframe.groupby(COLUMN_TO_COLLAPSE)
        
        # Get all column names except 'Subject'
        non_subject_columns = get_non_subject_columns(input_dataframe)
        
        # Build dictionary with aggregated values for all columns
        aggregation_dict = build_aggregation_dictionary(grouped_data, non_subject_columns)
        
        # Get unique subject names to use as index
        unique_subjects = list(grouped_data.groups.keys())
        
        # Create the result DataFrame
        collapsed = create_collapsed_dataframe(aggregation_dict, unique_subjects)
        
        return collapsed
        
    except KeyError as key_error:
        print(f"DataFrame could not be created due to a missing column: {key_error}")
        return pd.DataFrame()
    
    except Exception as general_error:
        print(f"DataFrame could not be created due to an unexpected error: {general_error}")
        return pd.DataFrame()
