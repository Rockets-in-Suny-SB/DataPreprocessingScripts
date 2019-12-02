import csv
import pandas as pd

def getStates(inputFile,outputFile,state):
    with open(inputFile,'r') as input, open(outputFile,'w') as out:
        writer = csv.writer(out)
        reader = csv.reader(input)
        header = next(reader,None)
        writer.writerow(header)
        #Get data of target states
        for row in reader:
            if row[1] in state:
                row[7] = row[7].replace('District ','')
                writer.writerow(row)
        print('Get data of target states done')
        return

def columnFilter(inputFile,outputFile):
    df=pd.read_csv(inputFile)
    df.rename(columns={
        'county': 'county_name'
    },inplace=True)
    #Keep wanted columns of data
    keep_col = ['state','district','party','candidatevotes','candidate']
    new_f = df[keep_col]
    #Save to the processed file
    new_f.to_csv(outputFile, index=False)
    print('Filt columns done')
    return

def votesCombination(inputFile,outputFile,state):
    other_party_dic = {}
    for s in state:
        other_party_dic[s] = {}
    with open(inputFile,'r') as inp, open(outputFile,'w') as out:
        writer = csv.writer(out)
        reader = csv.reader(inp)
        header = next(reader,None)
        writer.writerow(header)
        for row in reader:
            if row[2] not in ['democrat','republican']:
                other_party_dic[row[0]].setdefault(row[1],0)
                other_party_dic[row[0]][row[1]] += int(row[3])
            else:
                if row[2] == 'democrat':
                    row[2] = 'democratic'
                writer.writerow(row)
        for state in other_party_dic.keys():
            for dist in other_party_dic[state].keys():
                writer.writerow([state,dist,'others',str(other_party_dic[state][dist]),''])
    print('Remove other parties done')
    return

RAWDATA = '../data/district_overall_2018.csv'
STATEDATA = '../data/congressional_districts_voting.csv'
STATE = ['Oregon','Ohio','Illinois']
PROCESSEDDATA = '../processedData/congressional_districts_voting_processed.csv'

getStates(RAWDATA,STATEDATA,STATE)
columnFilter(STATEDATA,STATEDATA)
votesCombination(STATEDATA,PROCESSEDDATA,STATE)

print('Processed Done')