import pandas as pd

functiekaart = pd.read_csv('../data/functiekaart.csv', sep=';')
buurtcentra = functiekaart[functiekaart['Functie'] == 'wijk- / buurtcentrum']
buurtcentra = buurtcentra.drop(['Footprint','Oppervlakte_gecorrigeerd','WKT_LNG_LAT','WKT_LAT_LNG'], axis=1)
buurtcentra.to_csv('../data/simulated_incidents2.csv', index=False)
print(functiekaart.columns)
