import json

inp = open('../processedData/districts_data.json','r')
loaded_json = json.load(inp)
state = {}
for s in loaded_json:
    state.setdefault(s,{})
    state[s].setdefault('demo',{})
    state[s].setdefault('vote',{})
    for p in loaded_json[s]:
        demographic = loaded_json[s][p]['demo']
        for group in demographic:
            state[s]['demo'].setdefault(group,0)
            state[s]['demo'][group] += int(demographic[group])
        vote = loaded_json[s][p]['vote']
        for party in vote:
            state[s]['vote'].setdefault(party,0)
            state[s]['vote'][party]+=int(vote[party]['Votes'])

out = open('../processedData/state_data.json','w')
json.dump(state,out,indent=4)