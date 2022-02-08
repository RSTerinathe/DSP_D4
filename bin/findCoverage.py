import pandas as pd
import numpy as np

TIME_THRESHOLD = 240
tt_firestations = pd.read_csv('../data/travelling_times_firestations2.csv')
tt_parkingspots = pd.read_csv('../data/travelling_times.csv')


# Count all neighbourhoods and count neighbourhoods that are within X time of a firestation
nr_demandpoints = len(tt_firestations['wijknaam'].unique())
covered = (tt_firestations[tt_firestations['travel_time'] <= TIME_THRESHOLD])['wijknaam'].unique()
nr_covered = len(covered)
print(f"Previous within {TIME_THRESHOLD} seconds range: {nr_covered}/{nr_demandpoints}")

optimized_spots = pd.read_csv('../data/optimized_spots.csv')
# Find wijken that have not been covered
non_covered = tt_firestations.loc[~tt_firestations['wijknaam'].isin(covered)]['wijknaam'].unique()
# Filter travelling times that are within threshold and only for the wijken that are not covered yet
traveltimes_non_covered = tt_parkingspots.loc[tt_parkingspots['wijknaam'].isin(non_covered)]
traveltimes_non_covered = traveltimes_non_covered[traveltimes_non_covered['travel_time'] <= TIME_THRESHOLD]

for nr_firetrucks in range(2,6):
    for part_of_day in ['Morning', 'Afternoon', 'Evening', 'Night']:
        non_covered_new = non_covered
        df = (optimized_spots[np.bitwise_and(optimized_spots['Placed fire trucks'] == nr_firetrucks, optimized_spots['Minute range'] == TIME_THRESHOLD // 60)])
        df = df[df['Part of day'] == part_of_day]
        for row in df.iterrows():
            coordinates = f"{row[1]['Latitude']}_{row[1]['Longitude']}"
            found = traveltimes_non_covered[traveltimes_non_covered['origin_coords'] == coordinates]
            if not found.empty:
                for row2 in found.iterrows():
                    non_covered_new = non_covered_new[non_covered_new != (row2[1]['wijknaam'])]
        print(f"Nr_trucks={nr_firetrucks}, part_of_day={part_of_day}: {nr_demandpoints - len(non_covered_new)}/{nr_demandpoints}")

# Check if there are any coordinates of the parked vehicles in the set
