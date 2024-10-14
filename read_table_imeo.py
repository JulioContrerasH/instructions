import pandas as pd
import pathlib

# Read the table from the URL
dir = pathlib.Path(r"C:\Users\contr\Downloads\unep_methanedata_detected_plumes.csv")
df = pd.read_csv(dir)

df_prisma = df[df["satellite"] == "PRISMA - ASI"]
df_emit = df[df["satellite"] == "EMIT - NASA"]
df_enmap = df[df["satellite"] == "EnMAP - DLR"]
df_enmap.keys()
df_enmap["emission_auto"]
# Group by lat and lon
df_enmap.groupby(["lat", "lon"]).size().reset_index(name="count")


# read json
import json

# Cargar el JSON desde un archivo o string
with open(r"C:\Users\contr\Downloads\sources_2024-09-12T11_54_29.397Z.json", 'r') as f:
    content = json.load(f)

features = content["features"]
rows = []
for feature in features:
    properties = feature['properties']
    row = {
        "cluster_id": properties['cluster_id'],
        "gas": properties['gas'],
        "sector": properties['sector'],
        "plume_count": properties['plume_count'],
        "plume_ids": properties['plume_ids'],
        "lat": feature["geometry"]["coordinates"][1].,
        "lon": feature["geometry"]["coordinates"][0],
        "observation_scenes_names": properties['observation_scenes_names'],
        "emission_auto": properties['emission_auto'],
        "emission_uncertainty_auto": properties['emission_uncertainty_auto'],
        "published_at_max": properties['published_at_max'],
        "published_at_min": properties['published_at_min'],
        "timestamp_max": properties['timestamp_max'],
        "timestamp_min": properties['timestamp_min'],
        "detection_date_count": properties['detection_date_count'],
        "observation_date_count": properties['observation_date_count'],
        "persistence": properties['persistence'],
        "source_name": properties['source_name'],
        "date_count": properties['date_count']
    }
    rows.append(row)


df = pd.DataFrame(rows)

# save to csv
# df.to_csv(r"C:\Users\contr\Downloads\carbon_map.csv", index=False)

df = df[df["gas"] == "CH4"]

# Group by lat and lon
df.groupby(["lat", "lon"]).size().reset_index(name="count")


# sum plume count df["plume_count"]
df["plume_count"].sum()
df["plume_count"].sum()

