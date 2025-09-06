import pandas as pd

# Reads the log file and loads it into a DataFrame.
# Each line in the log file is split into three columns: timestamp, level, and message.
log_df = pd.read_csv(
    "data/project.log",  # Path to the log file
    sep=" - ",  # Separator used in the log format
    header=None,  # No header row in the log file
    engine="python",  # Use the Python engine for flexible parsing
    names=["timestamp", "level", "message"],  # Names for the columns
)

# Displays the first five rows of the DataFrame to check the log content.
print(log_df.head())
print(log_df["level"].value_counts())  # Counts of each log level (INFO, WARNING, ERROR)
print(log_df["message"].value_counts().head(10))  # Top 10 most
