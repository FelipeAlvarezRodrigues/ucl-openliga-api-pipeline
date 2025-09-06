import pandas as pd


# Functions to extract team names from nested dictionaries
def extract_team_names(df):
    df["team1_name"] = df["team1"].apply(lambda x: x["teamName"])
    df["team2_name"] = df["team2"].apply(lambda x: x["teamName"])
    return df


# Function to extract match day from nested dictionaries
def extract_match_day(df):
    df["matchDay"] = df["group"].apply(
        lambda x: (
            x["groupName"].split(".")[0]
            if isinstance(x, dict) and "groupName" in x
            else None
        )
    )
    return df


# Goals !!!
