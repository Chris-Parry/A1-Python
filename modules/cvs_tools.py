import glob

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


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


def plotly_plot_csvs() -> None:
    csv_files = glob.glob("data/Attension Data/*.csv")

    # Create subplot with as many rows as files
    fig = make_subplots(rows=len(csv_files), cols=1)

    for i, file in enumerate(csv_files):
        data = pd.read_csv(file)

        fig.add_trace(
            go.Scatter(
                x=data["Time [s]"],
                y=data["CA mean [°]"],
                mode="lines",
                name=f"Data from {file}",
            ),
            row=i + 1,
            col=1,
        )

    fig.update_layout(
        height=400 * len(csv_files),
        width=800,
        title_text="Subplots from multiple CSV files",
    )
    fig.show()


plotly_plot_csvs()
