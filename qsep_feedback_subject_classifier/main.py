import phrase_classifier
from qsep_feedback_subject_classifier.xlsm_to_xlsx_converter import convert_xlsm_to_xlsx

def main():
    # Convert XLSM file to XLSX
    input_file = r"docs\input\Katie_July_simple_titles.xlsm"
    output_file = r"docs\output\Katie_July_simple_titles.xlsx"
    
    print("Converting XLSM to XLSX...")
    if convert_xlsm_to_xlsx(input_file, output_file):
        print(f"Successfully converted {input_file} to {output_file}")
    else:
        print("Conversion failed")
    
    # Original classification example
    # phrase_classifier.create_dataset(samples_per_category=500)
    # feed_back_classifier = phrase_classifier.Classifier()
    # ans = feed_back_classifier.classify_text("they hung up on me!")
    # print(f"Classification result: {ans}")

if __name__ == "__main__":
    main()