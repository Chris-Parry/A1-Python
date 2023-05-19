import glob
import re

import pandas as pd
import plotly.graph_objects as go


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


def plotly_plot_csvs(sample_name_prefix) -> None:
    csv_files = glob.glob(
        f"data/Attension Data/csg524 {sample_name_prefix} Measurement *.csv"
    )
    csv_files.sort()

    fig = go.Figure()
    regex_measurement_number = r"Measurement (\d+)"
    for file in csv_files:
        # Read the CSV data
        data = pd.read_csv(file)

        if match := re.search(regex_measurement_number, file):
            fig.add_trace(
                go.Scatter(
                    x=data["Time [s]"],
                    y=data["CA mean [°]"],
                    mode="lines",
                    name=f"Data from M {match[1]}",
                )
            )
    fig.update_layout(
        height=600,
        width=1600,
        title_text=f"Data from {sample_name_prefix} Measurements",
    )
    fig.show()


plotly_plot_csvs("Sample 1")
plotly_plot_csvs("Sample 2")
plotly_plot_csvs("Sample 3")
plotly_plot_csvs("Sample 4")
plotly_plot_csvs("Sample 5")
plotly_plot_csvs("Treated Sample 1")

# TODO Fix the fact that plotting multiple times seems to overwrite the previous plot
