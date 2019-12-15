import json
import random

geo = json.load(open('../processedData/Ohio_congressional_geo_processed.json','r'))
data = json.load(open('../processedData/districts_data.json','r'))
party_dic = {0:'Democratic', 1:'Republican', 2:'Others'}

for district in geo['features']:
    if 'id' not in district['properties'].keys():
        continue
    id = district['properties']['id']
    name = 'Congressional District '+str(id)
    d_data = data['Ohio'][str(id)]
    district['properties'] = {
        'id' : id,
        'name' : name,
        'NAMELSAD': name,
        'demographic': d_data['demographic'],
        'vote_CONGRESSIONAL_2018':{
            'winner': '',
            'Republican': 0,
            'Democratic': 0,
            'Others': 0
        },
        'vote_CONGRESSIONAL_2016': {
            'winner': '',
            'Republican': 0,
            'Democratic': 0,
            'Others': 0
        },
        'vote_PRESIDENTIAL_2016': {
            'winner': '',
            'Republican': 0,
            'Democratic': 0,
            'Others': 0
        }
    }
    for party in d_data['vote2018'].keys():
        district['properties']['vote_CONGRESSIONAL_2018'][party] = int(d_data['vote2018'][party]['Votes'])
    vote = district['properties']['vote_CONGRESSIONAL_2018']
    list = [vote['Democratic'],vote['Republican'],vote['Others']]
    district['properties']['vote_CONGRESSIONAL_2018']['winner'] = party_dic[list.index(max(list))]

    for party in d_data['vote2016'].keys():
        district['properties']['vote_CONGRESSIONAL_2016'][party] = int(d_data['vote2016'][party]['Votes'])
    vote = district['properties']['vote_CONGRESSIONAL_2016']
    list = [vote['Democratic'], vote['Republican'], vote['Others']]
    district['properties']['vote_CONGRESSIONAL_2016']['winner'] = party_dic[list.index(max(list))]

    for party in vote.keys():
        if party != 'winner':
            district['properties']['vote_PRESIDENTIAL_2016'][party] = int((district['properties']['vote_CONGRESSIONAL_2016'][party]+ district['properties']['vote_CONGRESSIONAL_2018'][party])/2 * (random.random()+0.5))
    vote = district['properties']['vote_PRESIDENTIAL_2016']
    list = [vote['Democratic'], vote['Republican'], vote['Others']]
    district['properties']['vote_PRESIDENTIAL_2016']['winner'] = party_dic[list.index(max(list))]

json.dump(geo,open('../processedData/Ohio_congressional_geo_processed.json','w'))