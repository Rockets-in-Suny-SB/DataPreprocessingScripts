import geopandas as gp
import json

MAP = 'processed_data/Illinois_geo.json'

DEMOGRAPHIC_DATA = open('processed_data/IL_precincts_demographic.json','r')
load_json = json.load(DEMOGRAPHIC_DATA)['precincts']

neighbors = []
edges = {'edges':[]}
df = gp.read_file(MAP)
for index,row in df.iterrows():
    id = row['id']
    name = row['name']
    for precinct in load_json:
        if precinct['info'][name] == name:
            county = load_json['info']['county']
            population = float(load_json['demographic']['Total'])
        break
    neighbors = df[df.geometry.touches(row['geometry'])].name.tolist()
    for n in neighbors:
        edge = {}
        edge['self'] = id
        edge['adj'] = load_json[n]['info']['id']
        edge['sameCounty'] = (county == load_json[n]['info']['county'])
        edge_pop = float(load_json[n]['demographic']['Total'])
        edge['point'] = 1.0 - abs(edge_pop-population)/(edge_pop+population)
        edges['edges'].append(edge)
out = open('processed_data/IL_precicnts_edges.json','w')
json.dump(edges,out,indent=4)