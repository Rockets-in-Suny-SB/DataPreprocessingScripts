import csv
import pandas as pd

def getStates(inputFile,outputFile,state):
    with open(inputFile,'rb') as input, open(outputFile,'wb') as out:
        writer = csv.writer(out)
        reader = csv.reader(input)
        header = next(reader,None)
        writer.writerow(header)
        #Get data of target states
        for row in reader:
            if row[1] == state:
                writer.writerow(row)
        print('Get data of target states done')
        return

def columnFilter(inputFile,outputFile):
    df=pd.read_csv(inputFile)
    df.rename(columns={
        'county': 'county_name'
    },inplace=True)
    #Keep wanted columns of data
    keep_col = ['state','district','party','candidatevotes']
    new_f = df[keep_col]
    #Save to the processed file
    new_f.to_csv(outputFile, index=False)
    print('Filt columns done')
    return

def votesCombination(inputFile,outputFile,state):
    other_party_dic = {}
    other_party_dic['Oregon'] = {}
    with open(inputFile,'rb') as inp, open(outputFile,'wb') as out:
        writer = csv.writer(out)
        reader = csv.reader(inp)
        header = next(reader,None)
        writer.writerow(header)
        for row in reader:
            if row[2] not in ['democrat','republican']:
                other_party_dic[row[0]].setdefault(row[1],0)
                other_party_dic[row[0]][row[1]] += int(row[3])
            else:
                writer.writerow(row)
        for state in other_party_dic.keys():
            for dist in other_party_dic[state].keys():
                writer.writerow([state,dist,'others',str(other_party_dic[state][dist])])
    print('Remove other parties done')
    return

rawData = 'data/district_overall_2018.csv'
stateData = 'data/congressional_districts_voting.csv'
state = 'Oregon'
processedData = 'processed_data/congressional_districts_voting_processed.csv'

getStates(rawData,stateData,state)
columnFilter(stateData,stateData)
votesCombination(stateData,processedData,state)

print('Processed Done')