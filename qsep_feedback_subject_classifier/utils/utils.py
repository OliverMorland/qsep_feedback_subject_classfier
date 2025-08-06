import pandas as pd
from openpyxl import load_workbook
from openpyxl.worksheet.worksheet import Worksheet



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


def unmerge_cells_and_fill(ws: Worksheet):
   
    for merged_range in list(ws.merged_cells.ranges):
        top_left = ws.cell(row=merged_range.min_row, column=merged_range.min_col)
        value = top_left.value
        ws.unmerge_cells(str(merged_range))
        for row in ws.iter_rows(
            min_row=merged_range.min_row,
            max_row=merged_range.max_row,
            min_col=merged_range.min_col,
            max_col=merged_range.max_col,
        ):
            for cell in row:
                cell.value = value


def trim_rows_until_subject(ws: Worksheet, keyword="Subject"):

    header_row_idx = None
    for row in ws.iter_rows(min_row=1, max_row=ws.max_row):
        for cell in row:
            if cell.value and str(cell.value).strip().lower() == keyword.lower():
                header_row_idx = cell.row
                break
        if header_row_idx:
            break

    if header_row_idx is None:
        raise ValueError(f"Could not find a row with '{keyword}'")

    if header_row_idx > 1:
        ws.delete_rows(1, header_row_idx - 1)

def delete_columns_with_no_header(ws: Worksheet):
   
    for col_idx in range(ws.max_column, 0, -1):
        header_cell = ws.cell(row=1, column=col_idx)
        if not header_cell.value or str(header_cell.value).strip() == "":
            ws.delete_cols(col_idx)
