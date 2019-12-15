import csv
import json

districts = {}
inp = open('../processedData/congressional_districts_demographic.csv', 'r')
demo = csv.reader(inp)
vote = csv.reader(open('../processedData/congressional_districts_voting_processed.csv', 'r'))
vote2016 = csv.reader(open('../processedData/2016_congressional_districts_voting_processed.csv', 'r'))

header = next(demo, None)
for row in demo:
    districts.setdefault(row[0], {})
    districts[row[0]].setdefault(row[2], {})
    districts[row[0]][row[2]]['demographic'] = {
        "Total": row[3],
        "White": row[4],
        "Black or African American": row[5],
        "Asian": row[7],
        "Native Hawaiian and Other Pacific Islander": row[8],
        "Two or more races": row[10],
        "American Indian and Alaska Native": row[6],
        "Some Other Race": row[9],
    }

header = next(vote, None)
for row in vote:
    print(row)
    districts[row[0]][row[1]].setdefault('vote2018', {})
    districts[row[0]][row[1]]['vote2018'][row[2].capitalize()] = {
        "Votes": row[3],
        "Candidate": row[4]
    }
header = next(vote2016, None)
for row in vote2016:
    districts[row[0]][row[1]].setdefault('vote2016', {})
    districts[row[0]][row[1]]['vote2016'][row[2].capitalize()] = {
        "Votes": row[3],
        "Candidate": row[4]
    }

out = open('../processedData/districts_data.json', 'w')
json.dump(districts, out, indent=4)
