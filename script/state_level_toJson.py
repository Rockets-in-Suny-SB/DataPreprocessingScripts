import json

inp = open('../processedData/districts_data.json','r')
loaded_json = json.load(inp)
state = {}
for s in loaded_json:
    state.setdefault(s,{})
    state[s].setdefault('demographic',{})
    state[s].setdefault('vote2016', {})
    state[s].setdefault('vote2018', {})
    for p in loaded_json[s]:
        demographic = loaded_json[s][p]['demographic']
        for group in demographic:
            state[s]['demographic'].setdefault(group,0)
            state[s]['demographic'][group] += int(demographic[group])
        vote = loaded_json[s][p]['vote2016']
        for party in vote:
            state[s]['vote2016'].setdefault(party,0)
            state[s]['vote2016'][party.capitalize()]+=int(vote[party]['Votes'])
        vote = loaded_json[s][p]['vote2018']
        for party in vote:
            state[s]['vote2018'].setdefault(party,0)
            state[s]['vote2018'][party]+=int(vote[party]['Votes'])

out = open('../processedData/state_data.json','w')
json.dump(state,out,indent =4)

party_dic = {0:'Democratic',1:'Republican',2:'Others'}

loaded_json = json.load(open('../processedData/state_data.json','r'))
for s in loaded_json.keys():
    vote = loaded_json[s]['vote2016']
    list = [vote['democratic'],vote['republican'],vote['others']]
    vote['winner'] = party_dic[list.index(max(list))]
    vote = loaded_json[s]['votep2016']
    list = [vote['democratic'], vote['republican'], vote['others']]
    vote['winner'] = party_dic[list.index(max(list))]
    vote = loaded_json[s]['vote2018']
    list = [vote['democratic'], vote['republican'], vote['others']]
    vote['winner'] = party_dic[list.index(max(list))]

out = open('../processedData/state_data.json','w')
json.dump(loaded_json,out,indent=4)