import pandas as pd

from classes.Demand.DemandCalculator import DemandCalculator

wijken = pd.read_csv('../data/wijken.csv')
incident_data = pd.read_csv('../data/wijken_incidents_updated.csv')

calculator = DemandCalculator(incident_data, wijken)

# df = calculator.getTotalDemand()
# df.to_csv('../data/demand_for_wijken.csv', index= False)
df = calculator.getDemandForTimeOfDay('Ochtend')
df.to_csv('../data/demand_for_wijken_ochtend.csv', index= False)
df = calculator.getDemandForTimeOfDay('Middag')
df.to_csv('../data/demand_for_wijken_middag.csv', index= False)
df = calculator.getDemandForTimeOfDay('Avond')
df.to_csv('../data/demand_for_wijken_avond.csv', index= False)
df = calculator.getDemandForTimeOfDay('Nacht')
df.to_csv('../data/demand_for_wijken_nacht.csv', index= False)
