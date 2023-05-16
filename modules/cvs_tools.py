import glob

import pandas as pd


def convert_xls_to_csv() -> None:
    xls = pd.ExcelFile("data/Attension Data/Sample 1 Treated.xls")

    for sheet_name in xls.sheet_names:
        df = xls.parse(sheet_name)
        headers = df.columns.tolist()
        df.to_csv(f"data/Attension Data/{sheet_name}.csv", index=False, header=headers)


def drop_empty_csv_rows() -> None:
    directory_files = glob.glob("data/Attension Data/*.csv")

    for csv in directory_files:
        df = pd.read_csv(csv)

        df = df.dropna()
        headers = df.columns.tolist()

        df.to_csv(csv, index=False, header=headers)
