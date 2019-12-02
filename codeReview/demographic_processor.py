import csv
import pandas as pd

STATE = 'Illinois'
RAWDATA = 'nhgis0007_ds171_2010_votedist_codebook.csv'
PROCESSED_DATA = '../processedData/IL_precincts_demographic.csv'

with open(RAWDATA, 'r') as input, open(PROCESSED_DATA, 'w') as out:
    reader = csv.reader(input)
    header = next(reader, None)
    state_index = header.index('STATE')
    writer = csv.writer(out)
    writer.writerow(header)
    # Get data of target states
    for row in reader:
        if row[state_index] == STATE:
            writer.writerow(row)
    print('Get data of target states done')
# Read processed csv using pandas
df = pd.read_csv(PROCESSED_DATA)
# Rename some columns to be readable according to the codebook
df.rename(columns={
    'AIUXE001': 'Total',
    'AIUXE002': 'White',
    'AIUXE003': 'Black or African American',
    'AIUXE004': 'American Indian and Alaska Native',
    'AIUXE005': 'Asian',
    'AIUXE006': 'Native Hawaiian and Other Pacific Islander',
    'AIUXE007': 'Some Other Race',
    'AIUXE008': 'Two or more races',
    'H7Q001': 'Total',
    'H7Q003': 'White',
    'H7Q004': 'Black or African American',
    'H7Q005': 'American Indian and Alaska Native',
    'H7Q006': 'Asian',
    'H7Q007': 'Native Hawaiian and Other Pacific Islander',
    'H7Q008': 'Some Other Race',
    'H7Q009': 'Two or more races'
}, inplace=True)
# Keep wanted columns of data
keep_col = ['STATE', 'STATEA','COUNTY','COUNTYA','NAME', 'Total', 'White', 'Black or African American',
            'American Indian and Alaska Native', 'Asian', 'Native Hawaiian and Other Pacific Islander',
            'Some Other Race', 'Two or more races']
# Save to file
new_f = df[keep_col]
new_f.to_csv(PROCESSED_DATA, index=False)
print('Get wanted columns Done')

