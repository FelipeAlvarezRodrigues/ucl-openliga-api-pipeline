# Get data from the OpenLigaDB API

import requests

"""Fetches data from the given API URL and returns it as JSON."""


# Helper function to get data from a URL
def get_available(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


# Function to get available sports
def get_available_sports():
    url = f"https://api.openligadb.de/getavailablesports"
    return get_available(url)


# Function to get available leagues
def get_available_leagues():
    url = f"https://api.openligadb.de/getavailableleagues"
    return get_available(url)


# Function to get match data for a specific league and season
def get_matches_data(leagueShortcut, season):
    url = f"https://api.openligadb.de/getmatchdata/{leagueShortcut}/{season}"
    return get_available(url)


# Function to get match data by match ID
def get_match_data_by_id(matchID):
    url = f"https://api.openligadb.de/getmatchdata/{matchID}"
    return get_available(url)


# Function to get league table for a specific league and season
def get_league_table(leagueShortcut, season):
    url = f"https://api.openligadb.de/getbltable/{leagueShortcut}/{season}"
    return get_available(url)
