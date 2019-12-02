import csv
import json

STATE = 'Illinois'
DEMOGRAPHIC_DATA = '../processedData/IL_precincts_demographic.csv'
DEMOGRAPHIC_JSON = '../processedData/IL_precincts_demographic.json'
VOTING_DATA = '../processedData/IL_precincts_voting_2016c.csv'
VOTING_JSON = '../processedData/IL_precincts_voting_2016c.json'

#csv to json file
demographic_dic = {}
demographic_dic['precincts'] = {}
with open(DEMOGRAPHIC_DATA, 'r') as input:
    reader = csv.reader(input)
    header = next(reader, None)
    id = 1700000 # initial id for Illinois
    for row in reader:
        preicinct_dic = {}
        preicinct_dic['info'] = {
            'name': row[4],
            'id': id,
            'county': row[2],
            'countyid': row[3]
        }
        id += 1
        preicinct_dic['demographic'] = {
            'Total': row[5],
            'White': row[6],
            'Black or African American': row[7],
            'American Indian and Alaska Native': row[8],
            'Asian': row[9],
            'Native Hawaiian and Other Pacific Islander': row[10],
            'Some Other Race': row[11],
            'Two or more races': row[12]
        }
        demographic_dic['precincts'][row[4]] = preicinct_dic # Precinct name as the key
    json.dump(demographic_dic,open(DEMOGRAPHIC_JSON,'w'),indent=4)

voting_dic = {}
voting_dic['precincts'] = {}
with open(VOTING_DATA, 'r') as input:
    reader = csv.reader(input)
    header = next(reader, None)
    vote_2016 = {}
    vote_2016['precincts'] = {}
    for row in reader:
        county = row[2]
        name = row[4]
        party = row[5]
        vote = row[6]
        vote_2016['precincts'].setdefault(name,{})
        if party in ['democratic','republican']:
            vote_2016['precincts'][name][party] = vote
        else:
            vote_2016['precincts'][name].setdefualt('others',0)
            vote_2016['precincts'][name]['others'] += int(vote)
    for precinct in vote_2016['precincts'].keys():
        precinct_dic = {}
        precinct_dic['vote2016c'][precinct] = vote_2016['precincts'][precinct]
        for p in demographic_dic['precincts']:
            if p['name'] == name and p['county'] == county:
                preicinct_dic['info'] = p['info']
        voting_dic['precincts'][precinct] = preicinct_dic # Precinct name as the key
    json.dump(voting_dic, open(VOTING_JSON,'w'), indent=4)

