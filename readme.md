# Setup Files for Dremio Footback Hackathon

This is the setup repo for the [Dremio Football Hackathon](https://www.dremio.com/blog/football-playoffs-hackathon-powered-by-dremio/)

# Sample-Data Folder

Use the following files with Dremio
[Available Here](https://drive.google.com/drive/folders/1DGzdGRLm4PiwRZndJzqzbT-hqv6kdL7X?usp=sharing)
- plays.parquet
- tackles.parquet
- players_updated.parquet
- games_updates.parquet
- tracking_all_weeks_updated.parquet

The original files before transformation can be found [here on Kaggle](https://www.kaggle.com/datasets/jpmiller/nfl-competition-data?resource=download&select=external).

The original files for players, games and tracking_all_weeks are included along with the python scripts used to transform timestamp columns from nanoseconds to milliseconds for reference. (make sure pandas is installed in the active python environment if reusing the scripts)