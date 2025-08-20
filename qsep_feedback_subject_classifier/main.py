from collections import defaultdict
import pandas as pd
import pyperclip
from pathlib import Path
from qsep_feedback_subject_classifier.utils.utils import xlsx_to_dataframes_dict, dataframes_dict_to_xlsx, normalize_excel_and_save, open_file, deduplicate_column, add_total_row_and_col
from qsep_feedback_subject_classifier.row_collapser import collapse_rows, SUBJECT_COLUMN, COLUMN_TO_COLLAPSE
from qsep_feedback_subject_classifier import categorize_label
from pdf_reader import convert_pdf_to_df

def get_input_file_from_clipboard():
    input_file = pyperclip.paste().strip().strip('"')
    Path(input_file).expanduser().resolve()
    if not Path(input_file).exists():
        raise FileNotFoundError(f"File not found: '{input_file}'. Please ensure you copied the correct file to your clipboard.")
    return input_file

def create_dataframes_dictionary(input_file):
    if input_file.endswith(".pdf"):
        input_sheets_dict = convert_pdf_to_df(input_file)
    else:
        normalize_excel_and_save(input_file, "temporary_cleaned.xlsx")
        
        # Read all sheets into a dictionary
        input_sheets_dict = xlsx_to_dataframes_dict("temporary_cleaned.xlsx")
    return input_sheets_dict

def get_output_file_path(input_file):
    input_path = Path(input_file)
    new_name = input_path.stem + "_Collapsed.xlsx"
    output_file = input_path.with_name(new_name)
    return output_file

def create_totals_summary_dataframe(categorized_sheets_dict):
    print("Creating Total sheet by combining all processed sheets")
    all_sheets_list = list(categorized_sheets_dict.values())
    combined_df = pd.concat(all_sheets_list, ignore_index=True)
    
    # Collapse rows in the combined data
    total_collapsed_df = collapse_rows(combined_df)
    return total_collapsed_df

def create_categorization_map_dataframe(category_map):
    category_df = pd.DataFrame.from_dict(category_map, orient='index').transpose()
    category_df = category_df.loc[:, category_df.columns.notna()]
    category_df = category_df.apply(deduplicate_column, axis=0)
    return category_df


def main():
    # Process all sheets from XLSM file
    input_file = get_input_file_from_clipboard()
    print(f"Processing file: '{input_file}'")
    output_file = get_output_file_path(input_file)

    input_sheets_dict = create_dataframes_dictionary(input_file)
    
    # Process each sheet
    category_map = defaultdict(list)
    categorized_sheets_dict = {}
    for sheet_name, sheet_df in input_sheets_dict.items():
        print(f"Processing sheet: {sheet_name}")
        
        # Add categorized subject column
        processed_df = sheet_df.copy()

        subject_col = next((col for col in processed_df.columns 
                            if col.lower() == SUBJECT_COLUMN.lower()), None)

        if subject_col is None:
            print(f"Warning: 'Subject' column not found in sheet '{sheet_name}'")
            continue

        processed_df.insert(1, COLUMN_TO_COLLAPSE, processed_df[subject_col].apply(categorize_label.categorize))
        for _, row in processed_df.iterrows():
            category_map[row[COLUMN_TO_COLLAPSE]].append(row[subject_col])

        # Collapse rows
        collapsed_df = collapse_rows(processed_df)
        collapsed_df = add_total_row_and_col(collapsed_df)
        
        # Store processed sheet
        categorized_sheets_dict[sheet_name] = collapsed_df
    
    # Combine all processed sheets into a 'Total' sheet
    total_collapsed_df = create_totals_summary_dataframe(categorized_sheets_dict)
    
    # Add to the dictionary
    categorized_sheets_dict['Total'] = total_collapsed_df

    category_df = create_categorization_map_dataframe(category_map)
    categorized_sheets_dict['Subject Category Mapping'] = category_df   
    
    # Write all processed sheets to output file
    dataframes_dict_to_xlsx(categorized_sheets_dict, output_file)
    print(f"Collapsed data from {len(categorized_sheets_dict)} sheets saved to {output_file}")
    open_file(output_file)
    if Path("temporary_cleaned.xlsx").exists():
        Path("temporary_cleaned.xlsx").unlink()
        

if __name__ == "__main__":
    main()