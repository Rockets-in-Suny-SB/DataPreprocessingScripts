import json
# inp = open('../processedData/districts_data.json','r')
# distrcts = json.load(inp)
# for state in ['Illinois','Ohio','Oregon']:
#     rawFile = '../data/'+state+'_congressional_geo.json'
#     inp = open(rawFile,'r')
#     geojson = json.load(inp)
#     for district in geojson['features']:
#         id = district['properties']['CD116FP']
#         if id != 'ZZ':
#             id = int(id)
#             district['properties']['id'] = id
#             district['properties']['demographic'] = distrcts[state][str(id)]['demo']
#             district['properties']['vote'] = distrcts[state][str(id)]['vote']
#             if distrcts[state][str(id)]['vote']['democratic']['Votes']>distrcts[state][str(id)]['vote']['republican']['Votes']:
#                 district['properties']['vote']['color'] = 'red'
#             else:
#                 district['properties']['vote']['color'] = 'blue'
#     outFile = '../processedData/'+state+'_congressional_geo_processed.json'
#     out = open(outFile,'w')
#     json.dump(geojson,out,indent=4)
inp = open('../processedData/state_data.json','r')
states = json.load(inp)
state_dic = {'IL':'Illinois','OH':'Ohio','OR':'Oregon'}
for state in ['IL','OH','OR']:
    rawFile = '../data/'+ state +'_state.json'
    inp = open(rawFile,'r')
    geojson = json.load(inp)
    for s in geojson['features']:
        s['properties']['demographic'] = states[state_dic[state]]['demo']
        s['properties']['vote'] = states[state_dic[state]]['vote']
    outFile = '../processedData/'+state+'_state.json'
    out = open(outFile,'w')
    json.dump(geojson,out,indent=4)