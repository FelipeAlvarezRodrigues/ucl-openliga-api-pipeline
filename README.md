# ⚠️ Project in Progress

> 🚧 This project is actively under development.  
> Currently, it fetches and processes match & table data from the **OpenLigaDB API** for the UEFA Champions League 2025/2026.  
> The next steps will include:

- Storing all processed data in a **SQL database**
- Using **Apache Airflow** for orchestration and scheduling
- Creating **Power BI dashboards** to analyze and visualize insights

---

# 🏆 UCL OpenLiga API Pipeline

This project — **`ucl-openliga-api-pipeline`** — connects to the [OpenLigaDB](https://api.openligadb.de/index.html) API to fetch, process, and analyze **UEFA Champions League 2025/2026** match data.

It demonstrates **data engineering & analytics skills** by:

- Interacting with external APIs
- Cleaning & structuring raw JSON data into **pandas DataFrames**
- Persisting results in CSV (SQL support coming soon)
- Logging all pipeline steps for transparency
- Preparing the data for further analysis and dashboarding

---

## ✨ Features

- 📡 Fetches **match results** and **league tables** directly from the API
- 🧹 Cleans & transforms raw JSON into structured **pandas DataFrames**
- 📊 Saves output as CSV (`all_matches.csv`, `league_table.csv`)
- 📝 Comprehensive logging of each pipeline step (`project.log`)
- 🔍 (Optional) Analyze logs via `analyze_logs.py`
- 🚀 Roadmap: Store data in **SQL**, orchestrate with **Airflow**, and visualize in **Power BI**

---

## 📂 Project Structure

OpenLiga/
├── main.py
├── openliga/
│ ├── api_handler.py
│ ├── data_processing.py
│ ├── utils.py
├── data/
│ ├── all_matches.csv
│ ├── league_table.csv
│ └── project.log
├── analyze_logs.py
├── requirements.txt
└── README.md

## How to Use

1.Install dependencies:
pip install -r requirements.txt

2.Run the main script:
python main.py

3.Check the output:
Processed match data: all_matches.csv
League table: league_table.csv
Logs: project.log

4.Analyze logs (optional):
python analyze_logs.py

## About OpenLigaDB

OpenLigaDB is a free API providing sports data, including football leagues and matches.
See OpenLigaDB documentation for more details.
url = "https://api.openligadb.de/index.html"

## License

This project is open source and free to use for educational and analytical purposes.
