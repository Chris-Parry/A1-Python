import glob

import numpy as np
import pandas as pd

# Constants
Rt = 50  # Ohms
Rm = 4.7  # Ohms

# Get all files that match the pattern
filepath = glob.glob("data/Oscilloscope Data/scope_a1_pw2_*[0-9].csv")

for file in filepath:
    # Read the CSV file, skipping the first two rows
    df = pd.read_csv(file, skiprows=2, header=None)

    # Rename the columns
    df.columns = ["Time", "Voltage1", "Voltage2"]

    # Convert the voltage to current
    df["Current"] = (df["Voltage2"] * (Rm + Rt)) / (Rm * Rt)

    # Convert from mV to mA
    df["Current"] = df["Current"] / 1000

    # Calculate the power
    df["Power"] = df["Voltage1"] * df["Current"]

    # Since the voltage and current are sinusoidal, their phase difference
    # will affect the power
    # Assuming that the phase difference is zero for now, as it's not specified
    # in the question

    theta = np.radians(3.935)
    df["Power"] = df["Power"] * np.cos(theta)

    # Save the dataframe back to the CSV
    df.to_csv("data/Oscilloscope Data/new_" + file, index=False)
