#Demographic data processer

import csv
import pandas as pd

def getState(input,output):
    with open(input,'rb') as inp, open(output,'wb') as out:
        writer = csv.writer(out)
        #Get data of target state
        for row in csv.reader(inp):
            if row[4] == 'STATE' or row[4] == 'Illinois' or row[4] == 'Ohio' or row[4] == 'Oregon':
                writer.writerow(row)
        print('Get data of target state done')
        return

def processData(file):
    #Read processed file using pandas
    df=pd.read_csv(file)
    #Rename some columns to be readable according to the codebook
    df.rename(columns={
        'AIUXE001':    'Total',
        'AIUXE002':    'White',
        'AIUXE003':    'Black or African American',
        'AIUXE004':    'American Indian and Alaska Native',
        'AIUXE005':    'Asian',
        'AIUXE006':    'Native Hawaiian and Other Pacific Islander',
        'AIUXE007':    'Some Other Race',
        'AIUXE008':    'Two or more races',
        'H7Q001':      'Total',
        'H7Q003':      'White',
        'H7Q004':      'Black or African American',
        'H7Q005':      'American Indian and Alaska Native',
        'H7Q006':      'Asian',
        'H7Q007':      'Native Hawaiian and Other Pacific Islander',
        'H7Q008':      'Some Other Race',
        'H7Q009':      'Two or more races'
    },inplace=True)
    #Keep wanted columns of data
    keep_col = ['STATE','STATEA','CDCURRA','Total','White','Black or African American','American Indian and Alaska Native','Asian','Native Hawaiian and Other Pacific Islander','Some Other Race','Two or more races']
    new_f = df[keep_col]
    #Save to the processed file
    new_f.to_csv(file, index=False)
    return

RAWDATA = '../data/nhgis0009_ds238_2018_cd116th.csv'
PROCESSEDDATA = '../processed_data/congressional_districts_demographic.csv'
getState(RAWDATA,PROCESSEDDATA)
processData(PROCESSEDDATA)

print('Processed Done')