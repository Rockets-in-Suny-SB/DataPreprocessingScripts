import json
import csv
state = {}

DEMOGRAPHICDATA = '../processed_data/congressional_districts_demographic.csv'
VOTINGDATA = '../processed_data/congressional_districts_voting_processed.csv'
GEOJSON = '../processed_data/Oregon_congressional_geo.json'
PROCESSEDDATA = '../processed_data/Oregon_congressional_geo_processed.json'
STATE = 'Oregon'

with open(DEMOGRAPHICDATA,'rb') as inp:
    reader = csv.reader(inp)
    title = next(reader, None)
    for row in reader:
        state.setdefault(row[0],{})
        state[row[0]].setdefault('District '+row[2],{})
        state[row[0]]['District '+row[2]].setdefault('demographic',{})
        for index in range(3, len(row)):
            state[row[0]]['District '+row[2]]['demographic'][title[index]] = row[index]

with open(VOTINGDATA,'rb') as inp:
    reader = csv.reader(inp)
    title = next(reader, None)
    for row in reader:
        state[row[0]][row[1]].setdefault('voting', {})
        state[row[0]][row[1]]['voting'][row[2]] = row[3]

COLOR = {'democrat':'red','republican':'blue','others':'yellow'}

for s in state.keys():
    for dist in state[s].keys():
        winner = ''
        votes = 0
        for party in state[s][dist]['voting'].keys():
            if state[s][dist]['voting'][party]>votes:
                votes = state[s][dist]['voting'][party]
                winner = party
        state[s][dist]['voting']['winner'] = winner
        state[s][dist]['voting']['color'] = COLOR[winner]

with open(GEOJSON,'r') as inp, open(PROCESSEDDATA,'w') as out:
    loaded_json = json.load(inp)
    for dist in loaded_json['features']:
        distname = dist['properties']['NAMELSAD'][14:]
        dist['properties']['demographic'] = state[STATE][distname]['demographic']
        dist['properties']['votes'] = state['Oregon'][distname]['voting']
    json.dump(loaded_json,out)

print('Processed')