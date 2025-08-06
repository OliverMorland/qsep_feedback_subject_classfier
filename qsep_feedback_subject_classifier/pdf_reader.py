import pdfplumber
import pandas as pd

def deduplicate_columns(cols):
    seen = {}
    new_cols = []
    for col in cols:
        if col not in seen:
            seen[col] = 0
            new_cols.append(col)
        else:
            seen[col] += 1
            new_cols.append(f"{col}.{seen[col]}")
    return new_cols


def convert_pdf_to_df(input_file_path):
    dataframes = []
    with pdfplumber.open(input_file_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                df = pd.DataFrame(table[1:], columns=table[0])
                header = df.iloc[0].fillna('') + df.iloc[1].fillna('')
                df.columns = header
                df = df.iloc[2:].reset_index(drop=True)
                dataframes.append(df)


    final_df = pd.concat(dataframes, ignore_index=True)

    new_header = "Count"

    headers = final_df.columns.tolist()
    for i, col in enumerate(headers):
        if not col or str(col).strip().startswith("Unnamed"):
            headers[i] = new_header
            break  
    final_df.columns = headers
    final_df.columns = deduplicate_columns(final_df.columns)

    dataframe_dict = {"Sheet 1": final_df}

    return dataframe_dict

    #final_df.to_excel("output_merged.xlsx", index=False)


# convert_pdf_to_df("docs\input\June-QSEP Cases Opened and Resolved Previous Month.pdf")