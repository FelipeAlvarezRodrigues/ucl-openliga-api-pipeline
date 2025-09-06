"""Script to fetch and process match data and table (Champions League 2025/2026) from the OpenLigaDB API."""

import pandas as pd
from openliga.api_handler import get_matches_data, get_match_data_by_id
from openliga.data_processing import extract_team_names, extract_match_day
from openliga.api_handler import get_league_table
from openliga.utils import setup_logging
import logging

# Call logging setup
setup_logging()

available_matches = get_matches_data("ucl", "2025")

matches_df = pd.DataFrame(available_matches)

# Basic info about the DataFrame
logging.info(f"Dtypes:\n {matches_df.dtypes}")
logging.info(f"Head:\n {matches_df.head()}")


# Process the DataFrame to extract team names and match days
matches_df = extract_team_names(matches_df)
matches_df = extract_match_day(matches_df)

matches_df = matches_df[
    [
        "matchID",
        "matchDay",
        "matchDateTime",
        "location",
        "leagueName",
        "team1_name",
        "team2_name",
        "goals",
        "matchResults",
        "numberOfViewers",
        "matchIsFinished",
    ]
]

matches_df.to_csv("data/all_matches.csv", index=False)
logging.info(f"All Matches DataFrame saved with shape: {matches_df.shape}")

# Get details for finished matches
for _, row in matches_df.iterrows():
    if row["matchIsFinished"]:  # If no match is finished, this block won't run
        logging.info(f"Getting data for match ID: {row['matchID']}")
        match_details = get_match_data_by_id(row["matchID"])
        logging.debug(f"Match details: {match_details}")  # See what is being returned
        if not match_details:
            logging.info("No data found.")
        else:
            match_df = pd.DataFrame([match_details])
            logging.info(f"Match DataFrame:\n {match_df}")
            match_df.to_csv(f"data/match_integrated{row['matchID']}.csv", index=False)
            logging.info(f"Match details for match ID {row['matchID']} saved.")


"""Filter matches for specific teams
teams = ["Real Madrid", "Bayern München"]
matches_df_filtered = matches_df[matches_df["team1_name"].isin(teams) | matches_df["team2_name"].isin(teams)]
"""

# get league table
table = get_league_table("ucl", "2025")
table_df = pd.DataFrame(table)

table_df.to_csv("data/league_table.csv", index=False)
logging.info(f"League Table DataFrame saved with shape: {table_df.shape}")
