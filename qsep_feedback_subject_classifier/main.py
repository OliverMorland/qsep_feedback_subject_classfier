import phrase_classifier
import pandas as pd
from qsep_feedback_subject_classifier.utils.utils import xlsx_to_dataframe, dataframe_to_xlsx, xlsx_to_dataframes_dict, dataframes_dict_to_xlsx
from qsep_feedback_subject_classifier.row_collapser import collapse_rows
from qsep_feedback_subject_classifier import categorize_label


def categorize_subjects(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Replace strings in the 'Subject' column with only the first word.
    
    Args:
        dataframe (pd.DataFrame): Input DataFrame with a 'Subject' column
        
    Returns:
        pd.DataFrame: DataFrame with modified 'Subject' column containing only first words
    """
    try:
        # Check if 'Subject' column exists
        if 'Subject' not in dataframe.columns:
            print("Warning: 'Subject' column not found in DataFrame")
            return dataframe
        
        # Create a copy to avoid modifying the original DataFrame
        modified_df = dataframe.copy()
        
        # Extract first word from each Subject entry
        subject_values = modified_df['Subject']
        first_words = []
        
        for subject_value in subject_values:
            # Convert to string and handle NaN/None values
            subject_string = str(subject_value)
            
            # Split by spaces and take the first word
            words = subject_string.split()
            if len(words) > 0:
                first_word = words[0]
            else:
                first_word = subject_string  # Keep original if no spaces found
            
            first_words.append(first_word)
        
        # Replace the Subject column with first words
        modified_df['Subject'] = first_words
        
        return modified_df
        
    except Exception as error:
        print(f"Error extracting first words from Subject column: {error}")
        return dataframe


def main():
    # Process all sheets from XLSM file
    input_file = r"docs\input\Katie_July_simple_titles_all_sheets.xlsm"
    output_file = r"docs\output\Katie_July_Collapsed_all_sheets.xlsx"
    
    # Read all sheets into a dictionary
    input_sheets_dict = xlsx_to_dataframes_dict(input_file)
    
    # Process each sheet
    processed_sheets_dict = {}
    for sheet_name, sheet_df in input_sheets_dict.items():
        print(f"Processing sheet: {sheet_name}")
        
        # Add categorized subject column
        processed_df = sheet_df.copy()
        processed_df.insert(1, 'Categorized_Subject', processed_df['Subject'].apply(categorize_label.categorize))
        
        # Collapse rows
        collapsed_df = collapse_rows(processed_df)
        
        # Store processed sheet
        processed_sheets_dict[sheet_name] = collapsed_df
    
    # Write all processed sheets to output file
    dataframes_dict_to_xlsx(processed_sheets_dict, output_file)
    print(f"Collapsed data from {len(processed_sheets_dict)} sheets saved to {output_file}")

if __name__ == "__main__":
    main()