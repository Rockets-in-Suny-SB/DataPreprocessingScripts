import json

state = ['IL','OH','OR']
par = ['democratic','republican','others']
for s in state:
    geo = json.load(open('../processedData/'+s+'_state.json','r'))
    for state in geo['features']:
        properties = state['properties']
        for party in properties['vote_CONGRESSIONAL_2016'].keys():
            properties['vote_CONGRESSIONAL_2016'][party.capitalize()] = properties['vote_CONGRESSIONAL_2016'][party]
        for party in par:
            del properties['vote_CONGRESSIONAL_2016'][party]

        properties['vote_CONGRESSIONAL_2016']['winner'] = properties['vote_CONGRESSIONAL_2016']['winner'].capitalize()

        for party in properties['vote_PRESIDENTIAL_2016'].keys():
            properties['vote_PRESIDENTIAL_2016'][party.capitalize()] = properties['vote_PRESIDENTIAL_2016'][party]
        for party in par:
            del properties['vote_PRESIDENTIAL_2016'][party]
        properties['vote_PRESIDENTIAL_2016']['winner'] = properties['vote_PRESIDENTIAL_2016']['winner'].capitalize()

        for party in properties['vote_CONGRESSIONAL_2018'].keys():
            properties['vote_CONGRESSIONAL_2018'][party.capitalize()] = properties['vote_CONGRESSIONAL_2018'][party]
        for party in par:
            del properties['vote_CONGRESSIONAL_2018'][party]
        properties['vote_CONGRESSIONAL_2018']['winner'] = properties['vote_CONGRESSIONAL_2018']['winner'].capitalize()
    json.dump(geo,open('../processedData/'+s+'_state.json','w'))
