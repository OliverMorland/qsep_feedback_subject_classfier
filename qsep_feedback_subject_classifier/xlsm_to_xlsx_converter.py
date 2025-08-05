"""
Module for converting XLSM files to XLSX format while preserving data structure.
"""

import pandas as pd
from pathlib import Path
from typing import Dict, Any


def convert_xlsm_to_xlsx(input_path: str, output_path: str) -> bool:
    """
    Convert an XLSM file to XLSX format, preserving all data and structure.
    
    Args:
        input_path (str): Path to the input XLSM file
        output_path (str): Path for the output XLSX file
        
    Returns:
        bool: True if conversion successful, False otherwise
        
    Raises:
        FileNotFoundError: If input file doesn't exist
        Exception: For other conversion errors
    """
    try:
        # Check if input file exists
        if not Path(input_path).exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")
        
        # Create output directory if it doesn't exist
        output_dir = Path(output_path).parent
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Read all sheets from the XLSM file
        xl_file = pd.ExcelFile(input_path)
        sheet_data: Dict[str, Any] = {}
        
        # Read each sheet while preserving data types and formatting
        for sheet_name in xl_file.sheet_names:
            df = pd.read_excel(
                input_path, 
                sheet_name=sheet_name,
                keep_default_na=False,  # Preserve empty cells as empty strings
                na_values=[''],  # Only treat empty strings as NaN
            )
            
            # Add Categorized_Subject column as second column if Subject column exists
            if 'Subject' in df.columns:
                # Get column names as a list
                cols = df.columns.tolist()
                
                # Insert Categorized_Subject as second column (index 1)
                df.insert(1, 'Categorized_Subject', df['Subject'])
            
            sheet_data[sheet_name] = df
        
        # Write all sheets to the new XLSX file
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            for sheet_name, df in sheet_data.items():
                df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        print(f"Successfully converted {input_path} to {output_path}")
        return True
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"Error converting file: {e}")
        return False


def batch_convert_xlsm_to_xlsx(input_directory: str, output_directory: str) -> int:
    """
    Convert all XLSM files in a directory to XLSX format.
    
    Args:
        input_directory (str): Directory containing XLSM files
        output_directory (str): Directory to save XLSX files
        
    Returns:
        int: Number of files successfully converted
    """
    input_path = Path(input_directory)
    output_path = Path(output_directory)
    
    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    converted_count = 0
    xlsm_files = list(input_path.glob("*.xlsm"))
    
    if not xlsm_files:
        print(f"No XLSM files found in {input_directory}")
        return 0
    
    for xlsm_file in xlsm_files:
        # Generate output filename
        xlsx_filename = xlsm_file.stem + ".xlsx"
        output_file = output_path / xlsx_filename
        
        # Convert the file
        if convert_xlsm_to_xlsx(str(xlsm_file), str(output_file)):
            converted_count += 1
    
    print(f"Successfully converted {converted_count} out of {len(xlsm_files)} files")
    return converted_count


if __name__ == "__main__":
    # Example usage
    input_file = r"docs\input\Katie July 2025.xlsm"
    output_file = r"docs\output\Katie July 2025.xlsx"
    
    convert_xlsm_to_xlsx(input_file, output_file)