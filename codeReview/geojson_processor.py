import json

MAP = '../processed_data/Illinois_geo.json'
DEMOGRAPHIC_JSON = '../processedData/IL_precincts_demographic.json'

load_json = json.load(MAP)
demographic_dic = json.load(DEMOGRAPHIC_JSON)['precincts']
# Assign precinct id in the geo json file
for precicnt in load_json['features']:
    name = precicnt['properties']['NAME']
    for p in demographic_dic:
        if demographic_dic[p]['info']['name'] == name:
            precicnt['properties']['id'] = demographic_dic[p]['info']['id']

json.dump(load_json,open('MAP','w'),indent=4)