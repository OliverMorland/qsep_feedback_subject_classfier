import phrase_classifier
from qsep_feedback_subject_classifier.utils.utils import xlsx_to_dataframe, dataframe_to_xlsx
from qsep_feedback_subject_classifier.row_collapser import collapse_rows

def main():
    # Convert XLSM file to XLSX
    input_file = r"docs\input\Katie_July_simple_titles.xlsm"
    output_file = r"docs\output\Katie_July_Collapsed.xlsx"
    
    input_df = xlsx_to_dataframe(input_file)
    collapsed_df = collapse_rows(input_df)
    output_df = dataframe_to_xlsx(collapsed_df, output_file)
    print(f"Collapsed data saved to {output_file}")

if __name__ == "__main__":
    main()