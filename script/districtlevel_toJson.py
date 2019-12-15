import csv
import json

DATA = '../processedData/2016_congressional_districts_voting_processed.csv'
OUTPUT = '../processedData/district_summary_2016.json'
inp = open(DATA,'r')
reader = csv.reader(inp)
row = next(reader,None)
dic = {}
total = {}
state_counter = {}
for row in reader:
    state = row[0]
    district = row[1]
    party = row[2]
    number = row[3]
    name = row[4]
    total.setdefault(state, {})
    total[state].setdefault(district,{})
    total[state][district].setdefault('party','')
    total[state][district].setdefault('vote', 0)
    total[state].setdefault('dvote', 0)
    total[state].setdefault('rvote', 0)
    total[state].setdefault('total', 0)
    if party == 'democratic':
        if int(number) > int(total[state][district]['vote']):
            total[state][district]['party'] = 'Democratic'
            total[state][district]['name'] = name
            total[state][district]['vote'] = number
            total[state]['dvote'] += int(number)
            total[state]['total'] += int(number)
    elif party == 'republican':
        if int(number) > int(total[state][district]['vote']):
            total[state][district]['party'] = 'Republican'
            total[state][district]['name'] = name
            total[state][district]['vote'] = number
            total[state]['rvote'] += int(number)
            total[state]['total'] += int(number)
for state in total.keys():
    dic.setdefault(state,[])
    state_counter.setdefault(state,{})
    for district in total[state].keys():
        if district in ['dvote','rvote','total']:
            continue
        dic[state].append({
            'id': district,
            'name': total[state][district]['name'],
            'party': total[state][district]['party']
        })
        state_counter[state].setdefault(total[state][district]['party'],0)
        state_counter[state].setdefault('total', 0)
        state_counter[state][total[state][district]['party']] +=1
        state_counter[state]['total']+=1
dic['Illinois_Summary'] = 'Republican Congressional Representatives: '+str(state_counter['Illinois']['Republican'])+'<br/>'
dic['Illinois_Summary'] += 'Republican Representatives Percentage: '+str(int(float(state_counter['Illinois']['Republican'])/float(state_counter['Illinois']['total'])*100))+'%<br/>'
dic['Illinois_Summary'] += 'Rebpulican Voting Percentage: '+str(int(float(total['Illinois']['rvote'])/float(total['Illinois']['total'])*100))+'%<br/>'
dic['Illinois_Summary'] += 'Democratic Congressional Representatives: '+str(state_counter['Illinois']['Democratic'])+'<br/>'
dic['Illinois_Summary'] += 'Democratic Representatives Percentage: '+str(int(float(state_counter['Illinois']['Democratic'])/float(state_counter['Illinois']['total'])*100))+'%<br/>'
dic['Illinois_Summary'] += 'Democratic Voting Percentage: '+str(int(float(total['Illinois']['dvote'])/float(total['Illinois']['total'])*100))+'%<br/>'

dic['Ohio_Summary'] = 'Republican Congressional Representatives: '+str(state_counter['Ohio']['Republican'])+'<br/>'
dic['Ohio_Summary'] += 'Republican Representatives Percentage: '+str(int(float(state_counter['Ohio']['Republican'])/float(state_counter['Ohio']['total'])*100))+'%<br/>'
dic['Ohio_Summary'] += 'Rebpulican Voting Percentage: '+str(int(float(total['Ohio']['rvote'])/float(total['Ohio']['total'])*100))+'%<br/>'
dic['Ohio_Summary'] += 'Democratic Congressional Representatives: '+str(state_counter['Ohio']['Democratic'])+'<br/>'
dic['Ohio_Summary'] += 'Democratic Representatives Percentage: '+str(int(float(state_counter['Ohio']['Democratic'])/float(state_counter['Ohio']['total'])*100))+'%<br/>'
dic['Ohio_Summary'] += 'Democratic Voting Percentage: '+str(int(float(total['Ohio']['dvote'])/float(total['Ohio']['total'])*100))+'%<br/>'

dic['Oregon_Summary'] = 'Republican Congressional Representatives: '+str(state_counter['Oregon']['Republican'])+'<br/>'
dic['Oregon_Summary'] += 'Republican Representatives Percentage: '+str(int(float(state_counter['Oregon']['Republican'])/float(state_counter['Oregon']['total'])*100))+'%<br/>'
dic['Oregon_Summary'] += 'Rebpulican Voting Percentage: '+str(int(float(total['Oregon']['rvote'])/float(total['Oregon']['total'])*100))+'%<br/>'
dic['Oregon_Summary'] += 'Democratic Congressional Representatives: '+str(state_counter['Oregon']['Democratic'])+'<br/>'
dic['Oregon_Summary'] += 'Democratic Representatives Percentage: '+str(int(float(state_counter['Oregon']['Democratic'])/float(state_counter['Oregon']['total'])*100))+'%<br/>'
dic['Oregon_Summary'] += 'Democratic Voting Percentage: '+str(int(float(total['Oregon']['dvote'])/float(total['Oregon']['total'])*100))+'%<br/>'
json.dump(dic,open(OUTPUT,'w'),indent=4)
