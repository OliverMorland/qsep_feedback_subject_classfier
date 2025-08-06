import pandas as pd
import pyperclip
from pathlib import Path
from qsep_feedback_subject_classifier.utils.utils import xlsx_to_dataframes_dict, dataframes_dict_to_xlsx, normalize_excel_and_save, open_file
from qsep_feedback_subject_classifier.row_collapser import collapse_rows
from qsep_feedback_subject_classifier import categorize_label



def main():
    # Process all sheets from XLSM file
    input_file = pyperclip.paste().strip().strip('"')
    Path(input_file).expanduser().resolve()
    if not Path(input_file).exists():
        raise FileNotFoundError(f"File not found: {input_file}")
    input_path = Path(input_file)
    new_name = input_path.stem + "_Collapsed.xlsx"
    output_file = input_path.with_name(new_name)

    normalize_excel_and_save(input_file, "temporary_cleaned.xlsx")
    
    # Read all sheets into a dictionary
    input_sheets_dict = xlsx_to_dataframes_dict("temporary_cleaned.xlsx")
    
    # Process each sheet
    categorized_sheets_dict = {}
    for sheet_name, sheet_df in input_sheets_dict.items():
        print(f"Processing sheet: {sheet_name}")
        
        # Add categorized subject column
        processed_df = sheet_df.copy()
        processed_df.insert(1, 'Categorized_Subject', processed_df['Subject'].apply(categorize_label.categorize))
        
        # Collapse rows
        collapsed_df = collapse_rows(processed_df)
        
        # Store processed sheet
        categorized_sheets_dict[sheet_name] = collapsed_df
    
    # Combine all processed sheets into a 'Total' sheet
    print("Creating Total sheet by combining all processed sheets")
    all_sheets_list = list(categorized_sheets_dict.values())
    combined_df = pd.concat(all_sheets_list, ignore_index=True)
    
    # Collapse rows in the combined data
    total_collapsed_df = collapse_rows(combined_df)
    
    # Add to the dictionary
    categorized_sheets_dict['Total'] = total_collapsed_df
    
    # Write all processed sheets to output file
    dataframes_dict_to_xlsx(categorized_sheets_dict, output_file)
    print(f"Collapsed data from {len(categorized_sheets_dict)} sheets saved to {output_file}")
    open_file(output_file)

if __name__ == "__main__":
    main()