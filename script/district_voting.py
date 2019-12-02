import csv
import json

districts = {}
inp = open('../processedData/congressional_districts_demographic.csv', 'r')
demo = csv.reader(inp)
inp = open('../processedData/congressional_districts_voting_processed.csv', 'r')
vote = csv.reader(inp)

header = next(demo, None)
for row in demo:
    districts.setdefault(row[0], {})
    districts[row[0]].setdefault(row[2], {})
    districts[row[0]][row[2]]['demo'] = {
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
    districts[row[0]][row[1]].setdefault('vote', {})
    districts[row[0]][row[1]]['vote'][row[2]] = {
        "Votes": row[3],
        "Candidate": row[4]
    }

out = open('../processedData/districts_data.json', 'w')
json.dump(districts, out, indent=4)
