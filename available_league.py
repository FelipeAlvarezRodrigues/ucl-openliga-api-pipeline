import pandas as pd
from openliga.api_handler import get_available_leagues

available_leagues = get_available_leagues()

leagues_df = pd.DataFrame(available_leagues)

# The column 'sport' contains nested dictionaries. To filter by sportId, we can use a lambda function.
# print(leagues_df.head())


# When we get data from API (specially JSON), the data type are treated as strings.
# We need to convert the 'leagueSeason' column to integer for proper comparison.
leagues_df["leagueSeason"] = leagues_df["leagueSeason"].astype(int)


# Filter for sportId == 1 (e.g., Fußball) and season >= 2025
filtered_df = leagues_df[
    leagues_df["sport"].apply(lambda x: x["sportId"] == 1)
    & (leagues_df["leagueSeason"] >= 2025)
]

# Display leagues that contain "Champions League" in their name
print(filtered_df[filtered_df["leagueName"].str.contains("Champions League")])
