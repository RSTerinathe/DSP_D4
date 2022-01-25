import pandas as pd

from classes.Demand.DemandCalculator import DemandCalculator

wijken = pd.read_csv('../data/wijken.csv')
incident_data = pd.read_csv('../data/wijken_incidents_updated.csv')

calculator = DemandCalculator(incident_data, wijken)
df = calculator.getTotalDemand()
df.to_csv('../data/demand_for_wijken.csv', index= False)
