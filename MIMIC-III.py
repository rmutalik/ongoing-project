# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data
base_path = "C:\\Users\\rmutalik\\Desktop\\mimic-iii-clinical-database-1.4\\"

df_admissions = pd.read_csv(base_path + "ADMISSIONS.csv")
df_callout = pd.read_csv(base_path + "CALLOUT.csv")
df_caregivers = pd.read_csv(base_path + "CAREGIVERS.csv")
df_cptevents = pd.read_csv(base_path + "CPTEVENTS.csv")
