"""This script matches the old buurten names to the new buurten and creates a file with the corresponding nr of incidents and the coordinates"""

import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
# old_buurten = pd.read_csv('../data/oude_buurten.csv')
# new_buurten = pd.read_csv('../data/nieuwe_buurten.csv')
# buurten_information = pd.read_csv('../data/buurten_information.csv')
wijken = pd.read_csv('../data/wijken.csv')
def cleanIncidentData():
    incident_data = pd.read_csv('../data/brwaa_2010-2015.csv')
    # Clean the data:
    # Remove the rows that do not have a numeric value in the 'jaar' column
    incident_data['jaar'] = pd.to_numeric(incident_data['jaar'], errors="coerce")
    incident_data.dropna(how="any", inplace=True)
    # Only keep the 'Brand' meldingenr
    incident_data = incident_data[incident_data['landelijke_meldingsclassificatie_niveau1'].str.contains('Brand')]
    print(incident_data)
    incident_data.to_csv('../data/fire_incidents.csv', index=False)

fire_incidents = pd.read_csv('../data/fire_incidents.csv')
# incident_buurt = fire_incidents.buurt.unique()

df = fire_incidents.groupby(by=['buurt', 'prioriteit', 'dagdeel']).count()['uur'].reset_index()
df['buurt'] = df['buurt'].str.strip()
df['dagdeel'] = df['dagdeel'].str.strip()
df['code'] = np.nan
df['LAT'] = np.nan
df['LNG'] = np.nan
for buurt in df['buurt'].unique():
    if not buurt:
        continue
    buurt = buurt.replace('(', '\(')
    if sum(wijken['Wijknaam'].str.contains(buurt)):
        code = wijken[wijken['Wijknaam'].str.contains(buurt)]['Wijkcode']
        lat = wijken[wijken['Wijknaam'].str.contains(buurt)]['LAT']
        lng = wijken[wijken['Wijknaam'].str.contains(buurt)]['LNG']
        indexes = df['buurt'] == buurt
        df.loc[indexes, 'code'] = code.values[0]
        df.loc[indexes, 'LAT'] = lat.values[0]
        df.loc[indexes, 'LNG'] = lng.values[0]
print(df)
df.to_csv('../data/wijken_incidents.csv', index=False)
#
# print(f"{i} out of {len(incident_buurt)}")
exit(0)
