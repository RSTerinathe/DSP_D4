"""This script matches the old buurten names to the new buurten and creates a file with the corresponding nr of incidents and the coordinates"""

import pandas as pd
pd.set_option("display.max_columns", None)
old_buurten = pd.read_csv('../data/oude_buurten.csv')
# new_buurten = pd.read_csv('../data/nieuwe_buurten.csv')
# buurten_information = pd.read_csv('../data/buurten_information.csv')

def cleanIncidentData():
    incident_data = pd.read_csv('../data/incident_data.csv')
    # Clean the data:
    # Remove the rows that do not have a numeric value in the 'jaar' column
    incident_data['jaar'] = pd.to_numeric(incident_data['jaar'], errors="coerce")
    incident_data.dropna(how="any", inplace=True)
    # Only keep the 'Brand' meldingen
    incident_data = incident_data[incident_data['landelijke_meldingsclassificatie_niveau1'].str.contains('Brand')]
    print(incident_data)
    incident_data.to_csv('../data/fire_incidents.csv', index=False)

fire_incidents = pd.read_csv('../data/fire_incidents.csv')
incident_buurt = fire_incidents.buurt.unique()
i = 0
for buurt in incident_buurt:
    buurt = buurt.strip()
    if not buurt:
        continue
    print(buurt)
    buurt = buurt.replace('(', '\(')
    if sum(old_buurten['oude_naam'].str.contains(buurt)):
        i+= 1
        print('Found')


print(f"{i} out of {len(incident_buurt)}")
exit(0)
