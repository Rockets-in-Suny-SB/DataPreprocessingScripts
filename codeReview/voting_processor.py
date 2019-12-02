import csv
import pandas as pd

STATE = 'Illinois'
RAWDATA = '2016-precinct-state.csv'
PROCESSED_DATA = '../processedData/IL_precincts_voting_2016c.csv'
JSON_DATA = '../processedData/IL_precincts_voting_2016c.json'

with open(RAWDATA, 'r') as input, open(PROCESSED_DATA, 'w') as out:
    reader = csv.reader(input)
    header = next(reader, None)
    state_index = header.index('state')
    party_index = header.index('party')
    writer = csv.writer(out)
    writer.writerow(header)
    # Get data of target states
    for row in reader:
        if row[state_index] == STATE:
            # Formatting the party name
            if row[party_index] == 'democrat':
                row[party_index] = 'democratic'
            writer.writerow(row)
    print('Get data of target states done')
# Read processed file using pandas
df = pd.read_csv(PROCESSED_DATA)
# Rename some columns
df.rename(columns={
    'state': 'STATE',
    'state_fips': 'STATEA',
    'county_name': 'COUNTY',
    'county_fips': 'COUNTYA',
    'precinct': 'NAME',
}, inplace=True)
# Keep wanted columns of data
keep_col = ['STATE', 'STATEA', 'COUNTY', 'COUNTYA', 'NAME', 'party', 'votes']
# Save to file
new_f = df[keep_col]
new_f.to_csv(PROCESSED_DATA, index=False)
print('Get wanted columns Done')
